(() => {
    "use strict";

    // Define the base path for the icons
    const iconSet = "material_symbols";

    // Cache for storing icon lists
    const iconListCache = {};

    // Cache for storing individual icons
    const iconCache = {};

    // Integration ready check
    let integrationReady = false;
    let readyCheckPromise = null;

    // Function to check if the integration is ready
    async function checkIntegrationReady(retries = 5, delay = 1000) {
        if (integrationReady) {
            return true;
        }

        if (readyCheckPromise) {
            return readyCheckPromise;
        }

        readyCheckPromise = (async () => {
            for (let i = 0; i < retries; i++) {
                try {
                    const testUrl = `/${iconSet}/m3o/icons.json`;
                    const response = await fetch(testUrl, { 
                        cache: 'no-cache',
                        headers: { 'Cache-Control': 'no-cache' }
                    });
                    if (response.ok) {
                        integrationReady = true;
                        console.debug(`Material Symbols integration ready after ${i + 1} attempt(s)`);
                        return true;
                    }
                } catch (error) {
                    console.debug(`Integration ready check attempt ${i + 1} failed:`, error.message);
                }
                
                if (i < retries - 1) {
                    await new Promise(resolve => setTimeout(resolve, delay * Math.pow(1.5, i)));
                }
            }
            console.warn(`Material Symbols integration not ready after ${retries} attempts`);
            return false;
        })();

        return readyCheckPromise;
    }

    // Function to fetch the list of icons for a given set with retry logic
    async function fetchIconList(set) {
        console.debug(`Fetching icon list for set: ${set}`);
        
        // Check cache first
        if (iconListCache[set]) {
            console.debug(`Icon list for set ${set} found in cache`);
            return iconListCache[set];
        }

        // Wait for integration to be ready
        const ready = await checkIntegrationReady();
        if (!ready) {
            console.error(`Integration not ready, cannot fetch icon list for ${set}`);
            return [];
        }

        const url = `/${iconSet}/${set}/icons.json`;
        let lastError = null;

        // Retry logic
        for (let attempt = 1; attempt <= 3; attempt++) {
            try {
                console.debug(`Fetching icon list for ${set}, attempt ${attempt}`);
                const response = await fetch(url, {
                    cache: 'no-cache',
                    headers: { 'Cache-Control': 'no-cache' }
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
                const data = await response.json();
                if (!Array.isArray(data)) {
                    throw new Error(`Unexpected data format for ${set}: expected array`);
                }
                
                const iconNames = data.map(icon => icon.name).filter(Boolean);
                if (iconNames.length === 0) {
                    throw new Error(`No valid icons found in ${set}`);
                }
                
                iconListCache[set] = iconNames;
                console.debug(`Fetched and cached icon list for set ${set}: ${iconNames.length} icons`);
                return iconNames;
            } catch (error) {
                lastError = error;
                console.warn(`Error fetching icon list for ${set} (attempt ${attempt}):`, error.message);
                
                if (attempt < 3) {
                    await new Promise(resolve => setTimeout(resolve, 500 * attempt));
                }
            }
        }
        
        console.error(`Failed to fetch icon list for ${set} after 3 attempts:`, lastError);
        return [];
    }

    // List of icon sets to load
    const iconSets = ["m3o", "m3of", "m3s", "m3sf", "m3r", "m3rf"];

    // Initialise the icon system
    (async () => {
        try {
            console.debug("Material Symbols: Starting initialisation");
            
            // Wait for integration to be ready
            const ready = await checkIntegrationReady();
            if (!ready) {
                console.error("Material Symbols: Integration not ready, initialisation failed");
                return;
            }

            // Fetch all icon lists concurrently with proper error handling
            const fetchPromises = iconSets.map(async (set) => {
                try {
                    await fetchIconList(set);
                    return { set, success: true };
                } catch (error) {
                    console.error(`Error fetching icon list for ${set}:`, error);
                    return { set, success: false, error };
                }
            });
            
            const results = await Promise.allSettled(fetchPromises);
            const successful = results.filter(result => 
                result.status === 'fulfilled' && result.value.success
            ).length;
            
            console.debug(`Material Symbols: Fetched ${successful}/${iconSets.length} icon lists successfully`);

            // Define the custom icons for each set
            iconSets.forEach(set => {
                window.customIcons = window.customIcons || {};
                window.customIcons[set] = {
                    getIcon: async (iconName) => {
                        const key = `${set}:${iconName}`;
                        
                        // Check cache first
                        if (iconCache[key]) {
                            console.debug(`Icon ${iconName} from set ${set} found in cache`);
                            return iconCache[key];
                        }

                        // Ensure integration is ready
                        const ready = await checkIntegrationReady();
                        if (!ready) {
                            console.error(`Integration not ready, cannot fetch icon ${iconName} from ${set}`);
                            return null;
                        }

                        const iconUrl = `/${iconSet}/${set}/${iconName}.svg`;
                        let lastError = null;

                        // Retry logic for individual icons
                        for (let attempt = 1; attempt <= 2; attempt++) {
                            try {
                                console.debug(`Fetching icon ${iconName} from ${set}, attempt ${attempt}`);
                                const response = await fetch(iconUrl, {
                                    cache: 'no-cache',
                                    headers: { 'Cache-Control': 'no-cache' }
                                });
                                
                                if (!response.ok) {
                                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                                }
                                
                                const svgText = await response.text();
                                if (!svgText || !svgText.trim()) {
                                    throw new Error(`Empty SVG response for ${iconName} in ${set}`);
                                }
                                
                                const parser = new DOMParser();
                                const svgDoc = parser.parseFromString(svgText, "image/svg+xml");
                                
                                // Check for parsing errors
                                const parseError = svgDoc.querySelector("parsererror");
                                if (parseError) {
                                    throw new Error(`SVG parsing error for ${iconName} in ${set}`);
                                }
                                
                                const svgElement = svgDoc.querySelector("svg");
                                if (!svgElement) {
                                    throw new Error(`No SVG element found for ${iconName} in ${set}`);
                                }

                                const paths = Array.from(svgElement.querySelectorAll("path"))
                                    .map(path => path.getAttribute("d"))
                                    .filter(Boolean);
                                    
                                if (paths.length === 0) {
                                    throw new Error(`No valid paths found in SVG for ${iconName} in ${set}`);
                                }

                                const iconData = {
                                    viewBox: svgElement.getAttribute("viewBox") || "0 0 24 24",
                                    path: paths.join(" ")
                                };
                                
                                iconCache[key] = iconData;
                                console.debug(`Fetched and cached icon ${iconName} from set ${set}`);
                                return iconData;
                            } catch (error) {
                                lastError = error;
                                console.warn(`Error fetching icon ${iconName} from ${set} (attempt ${attempt}):`, error.message);
                                
                                if (attempt < 2) {
                                    await new Promise(resolve => setTimeout(resolve, 200));
                                }
                            }
                        }
                        
                        console.error(`Failed to fetch icon ${iconName} from ${set}:`, lastError);
                        return null;
                    },
                    getIconList: async () => {
                        try {
                            const iconNames = await fetchIconList(set);
                            return iconNames.map(name => ({ name }));
                        } catch (error) {
                            console.error(`Error getting icon list for ${set}:`, error);
                            return [];
                        }
                    }
                };
            });
            
            console.debug(`Material Symbols: Custom icons defined for all sets`);
        } catch (error) {
            console.error("Material Symbols: Initialisation failed:", error);
        }
    })();

    // Log a styled message to the console
    console.info(
        "%c MATERIAL SYMBOLS                    %c %c 2025.11.15  ",
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#1FBEF2;color:#FFFFFF;padding:3px 43px 2px 8px;border-radius:999vh;border:5px solid #1FBEF2;font-family:"Roboto", sans-serif;margin-top:18px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 8px 2px 0;border-radius:999vh 0 0 999vh;border:0;font-family:"Roboto", sans-serif;margin-left:-94px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 9px 2px 0;border-radius:0 999vh 999vh 0;border:0;font-family:"Roboto", sans-serif;margin-left:-1px;margin-bottom:18px'
    );
})();

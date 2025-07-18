(() => {
    "use strict";

    // Define the base path for the icons
    const iconSet = "material_symbols";

    // Cache for storing icon lists
    const iconListCache = {};

    // Cache for storing individual icons
    const iconCache = {};

    // Function to fetch the list of icons for a given set
    async function fetchIconList(set) {
        console.debug(`Fetching icon list for set: ${set}`);
        if (iconListCache[set]) {
            console.debug(`Icon list for set ${set} found in cache`);
            return iconListCache[set];
        }

        const url = `/${iconSet}/${set}/icons.json`;
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Failed to fetch icons.json for ${set}: ${response.statusText}`);
            }
            const data = await response.json();
            if (!Array.isArray(data)) {
                throw new Error(`Unexpected data format for ${set}`);
            }
            const iconNames = data.map(icon => icon.name).filter(Boolean);
            iconListCache[set] = iconNames;
            console.debug(`Fetched and cached icon list for set ${set}`);
            return iconNames;
        } catch (error) {
            console.error(`Error fetching icon list for ${set}:`, error);
            return [];
        }
    }

    // List of icon sets to load
    const iconSets = ["m3o", "m3of", "m3s", "m3sf", "m3r", "m3rf"];

    (async () => {
        // Fetch all icon lists concurrently
        await (async (sets) => {
            const fetchPromises = sets.map(async (set) => {
                try {
                    await fetchIconList(set);
                } catch (error) {
                    console.error(`Error fetching icon list for ${set}:`, error);
                }
            });
            await Promise.all(fetchPromises);
            console.debug(`All icon lists fetched`);
        })(iconSets);

        // Define the custom icons for each set
        iconSets.forEach(set => {
            window.customIcons = window.customIcons || {};
            window.customIcons[set] = {
                getIcon: async (iconName) => {
                    const key = `${set}:${iconName}`;
                    if (iconCache[key]) {
                        console.debug(`Icon ${iconName} from set ${set} found in cache`);
                        return iconCache[key];
                    }

                    const iconUrl = `/${iconSet}/${set}/${iconName}.svg`;
                    try {
                        const response = await fetch(iconUrl);
                        if (!response.ok) {
                            throw new Error(`Failed to fetch icon ${iconName} from ${set}: ${response.statusText}`);
                        }
                        const svgText = await response.text();
                        const parser = new DOMParser();
                        const svgDoc = parser.parseFromString(svgText, "image/svg+xml");
                        const svgElement = svgDoc.querySelector("svg");
                        if (!svgElement) {
                            throw new Error(`Invalid SVG format for ${iconName} in ${set}`);
                        }

                        const iconData = {
                            viewBox: svgElement.getAttribute("viewBox") || "0 0 24 24",
                            path: Array.from(svgElement.querySelectorAll("path"))
                                .map(path => path.getAttribute("d"))
                                .filter(Boolean)
                                .join(" ")
                        };
                        iconCache[key] = iconData;
                        console.debug(`Fetched and cached icon ${iconName} from set ${set}`);
                        return iconData;
                    } catch (error) {
                        console.error(`Error fetching icon ${iconName} from ${set}:`, error);
                        return null;
                    }
                },
                getIconList: async () => {
                    const iconNames = await fetchIconList(set);
                    return iconNames.map(name => ({ name }));
                }
            };
        });
        console.debug(`Custom icons defined for all sets`);
    })();

    // Log a styled message to the console
    console.info(
        "%c MATERIAL SYMBOLS                    %c %c 2025.07.18  ",
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#1FBEF2;color:#FFFFFF;padding:3px 43px 2px 8px;border-radius:999vh;border:5px solid #1FBEF2;font-family:"Roboto", sans-serif;margin-top:18px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 8px 2px 0;border-radius:999vh 0 0 999vh;border:0;font-family:"Roboto", sans-serif;margin-left:-94px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 9px 2px 0;border-radius:0 999vh 999vh 0;border:0;font-family:"Roboto", sans-serif;margin-left:-1px;margin-bottom:18px'
    );
})();

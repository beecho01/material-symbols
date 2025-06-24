(() => {
    "use strict";

    // Define the base path for the icons
    let iconSet = "material_symbols";

    // Cache for storing icon lists
    let iconListCache = {};

    // Cache for storing individual icons
    let iconCache = {};

    // Function to fetch the list of icons for a given set
    async function fetchIconList(set) {
        if (iconListCache[set]) {
            return iconListCache[set];
        }

        let url = `/${iconSet}/${set}/icons.json`;
        try {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Failed to fetch icons.json for ${set}`);
            }
            let data = await response.json();
            let iconNames = data.map(icon => icon.name);
            iconListCache[set] = iconNames;
            return iconNames;
        } catch (error) {
            console.error(`Error fetching icon list for ${set}:`, error);
            return [];
        }
    }

    // List of icon sets to load
    let iconSets = ["m3o", "m3of", "m3s", "m3sf", "m3r", "m3rf"];

    (async () => {
        // Fetch all icon lists concurrently
        await (async (sets) => {
            let fetchPromises = sets.map(async (set) => {
                try {
                    await fetchIconList(set);
                } catch (error) {
                    console.error(`Error fetching icon list for ${set}:`, error);
                }
            });
            await Promise.all(fetchPromises);
        })(iconSets);

        // Define the custom icons for each set
        iconSets.forEach(set => {
            window.customIcons[set] = {
                getIcon: async (iconName) => {
                    let key = `${set}:${iconName}`;
                    if (iconCache[key]) {
                        return iconCache[key];
                    }

                    let iconUrl = `/${iconSet}/${set}/${iconName}.svg`;
                    try {
                        let response = await fetch(iconUrl);
                        if (!response.ok) {
                            throw new Error(`Failed to fetch icon ${iconName} from ${set}`);
                        }
                        let svgText = await response.text();
                        let parser = new DOMParser();
                        let svgDoc = parser.parseFromString(svgText, "image/svg+xml");
                        let svgElement = svgDoc.querySelector("svg");
                        if (!svgElement) {
                            return null;
                        }

                        let iconData = {
                            viewBox: svgElement.getAttribute("viewBox") || "0 0 24 24",
                            path: Array.from(svgElement.querySelectorAll("path"))
                                .map(path => path.getAttribute("d"))
                                .join(" ")
                        };
                        iconCache[key] = iconData;
                        return iconData;
                    } catch (error) {
                        console.error(`Error fetching icon ${iconName} from ${set}:`, error);
                        return null;
                    }
                },
                getIconList: async () => {
                    let iconNames = await fetchIconList(set);
                    return iconNames.map(name => ({ name }));
                }
            };
        });
    })();

    // Log a styled message to the console
    console.info(
        "%c MATERIAL SYMBOLS                    %c %c 2025.06.24  ",
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#1FBEF2;color:#FFFFFF;padding:3px 43px 2px 8px;border-radius:999vh;border:5px solid #1FBEF2;font-family:"Roboto", sans-serif;margin-top:18px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 8px 2px 0;border-radius:999vh 0 0 999vh;border:0;font-family:"Roboto", sans-serif;margin-left:-94px',
        '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 9px 2px 0;border-radius:0 999vh 999vh 0;border:0;font-family:"Roboto", sans-serif;margin-left:-1px;margin-bottom:18px'
    );
})();

(() => {
  "use strict";

  // Base path 
  const a = "material_symbols";

  // Cache for loaded icons.json files
  const iconCache = {};

  // Cache for individual icon SVGs
  const iconSvgCache = {};

  // Load icons.json for a given icon set if not already cached
  const loadIconSet = async (iconsetPrefix) => {
    if (!iconCache[iconsetPrefix]) {

      try {

        // Fetch icons.json
        const response = await fetch(`/${a}/${iconsetPrefix}/icons.json`);
        if (!response.ok) throw new Error(`Failed to fetch icons.json for ${iconsetPrefix}`);
        
        // Read as array and map to icon names
        const icons = await response.json();
        iconCache[iconsetPrefix] = icons.map(icon => icon.name);
        // console.log(`Loaded icons for ${iconsetPrefix}:`, iconCache[iconsetPrefix]);

      } catch (error) {
        
        // Failed to load icons.json
        // console.error(`Error loading icon set ${iconsetPrefix}:`, error);
        iconCache[iconsetPrefix] = [];
      }
    }
    // Return icon list
    return iconCache[iconsetPrefix];
  };

  // Fetch the SVG for an individual icon
  const getIcon = async (iconsetPrefix, iconName) => {
    const cacheKey = `${iconsetPrefix}:${iconName}`;
    if (iconSvgCache[cacheKey]) return iconSvgCache[cacheKey];

    // Ensure icons.json is loaded
    await loadIconSet(iconsetPrefix); 

    // Warn if icon not found in icon set
    if (!iconCache[iconsetPrefix].includes(iconName)) {
      console.warn(`Icon "${iconName}" not found in icon set "${iconsetPrefix}".`);
      return '';
    }

    try {

      // Fetch SVG
      const response = await fetch(`/${a}/${iconsetPrefix}/${iconName}.svg`);
      if (!response.ok) {
        console.error(`Failed to fetch icon "${iconName}" from icon set "${iconsetPrefix}".`);
        return '';
      }

      // Parse SVG
      const svgText = await response.text();
      const doc = new DOMParser().parseFromString(svgText, "text/html");
      const svgElement = doc.querySelector("svg");
      if (!svgElement) return '';

      // Extract path and viewBox
      const viewBox = svgElement.getAttribute("viewBox") || "0 0 24 24";
      const path = svgElement.querySelector("path")?.getAttribute("d");

      // Cache SVG
      const iconObject = { path, viewBox };
      iconSvgCache[cacheKey] = iconObject;
      return iconObject;

    } catch (error) {

      // Console error if failed to load SVG
      console.error("Error fetching icon:", error);
      return '';
    }
  };

  // Get icon list for a specified prefix
  const getIconList = async (iconsetPrefix) => {
    await loadIconSet(iconsetPrefix);
    return iconCache[iconsetPrefix].map(name => ({ name }));
  };

  window.customIconsets = window.customIconsets || {};
  window.customIcons = window.customIcons || {};

  // Register icon sets for each prefix 
  ["m3o", "m3of", "m3r", "m3rf", "m3s", "m3sf"].forEach((prefix) => {

    // Register the icon set with Home Assistant's custom icon API
    window.customIconsets[prefix] = (iconName) => getIcon(prefix, iconName);

    // Register with `window.customIcons` to provide both `getIcon` and `getIconList`
    window.customIcons[prefix] = {
      getIcon: (iconName) => getIcon(prefix, iconName),
      getIconList: () => getIconList(prefix),
    };

    // console.log(`Registered icon set: ${prefix}`);

  });

  console.info(
    "%c MATERIAL SYMBOLS                    %c %c 2024.10.27  ",
    '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#1FBEF2;color:#FFFFFF;padding:3px 43px 2px 8px;border-radius:999vh;border:5px solid #1FBEF2;font-family:"Roboto", sans-serif;margin-top:18px',
    '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 8px 2px 0;border-radius:999vh 0 0 999vh;border:0;font-family:"Roboto", sans-serif;margin-left:-94px',
    '@import url("https://fonts.googleapis.com/css2?family=Roboto");background-color:#FFFFFF;color:#1FBEF2;padding:3px 9px 2px 0;border-radius:0 999vh 999vh 0;border:0;font-family:"Roboto", sans-serif;margin-left:-1px;margin-bottom:18px'
  );
})();
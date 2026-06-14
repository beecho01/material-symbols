import logging
import json
from os import path
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.helpers.http import HomeAssistantView

LOGGER = logging.getLogger(__name__)

NAME = "Material Symbols"
DOMAIN = "material_symbols"
VERSION = "2026.06.14"

ICONS_URL = f"/{DOMAIN}"
LOADER_URL = f"/{DOMAIN}/material_symbols.js"
ICONS_PATH = f"custom_components/{DOMAIN}/data"
LOADER_PATH = f"custom_components/{DOMAIN}/material_symbols.js"


class ListingView(HomeAssistantView):
    requires_auth = False

    def __init__(self, url, iconset_path, hass, iconset_prefix):
        self.url = url
        self.name = f"api:{DOMAIN}:{iconset_prefix}"
        self.iconset_path = iconset_path
        self.hass = hass
        self._cache = None
        LOGGER.debug(f"ListingView initialised with URL: {self.url}, "
                     f"iconset_path: {self.iconset_path}, "
                     f"iconset_prefix: {iconset_prefix}")

    async def get(self, request):
        if self._cache is not None:
            LOGGER.debug(f"Serving cached icons list for {self.iconset_path}")
            return self.json(self._cache)

        try:
            icons_list = await self.hass.async_add_executor_job(
                self.get_icons_list, self.iconset_path
            )
            self._cache = icons_list
            LOGGER.debug(f"Icons list loaded and cached: {len(icons_list)} icons")
            return self.json(icons_list)
        except Exception as e:
            LOGGER.error(f"Error fetching icons list for {self.iconset_path}: {e}")
            return self.json([])

    def get_icons_list(self, iconset_path):
        icons_json_path = path.join(iconset_path, "icons.json")
        try:
            if not path.exists(icons_json_path):
                LOGGER.warning(f"icons.json not found at: {icons_json_path}")
                return []
            with open(icons_json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            LOGGER.error(f"Error reading icons.json for {iconset_path}: {e}")
            return []


async def async_setup(hass: HomeAssistant, config):
    LOGGER.info(f"Setting up Material Symbols with version {VERSION}")
    
    try:
        # Register the JavaScript loader first
        await hass.http.async_register_static_paths(
            [StaticPathConfig(LOADER_URL, hass.config.path(LOADER_PATH), True)]
        )
        LOGGER.debug(f"Static JS path registered: {LOADER_URL}")
        add_extra_js_url(hass, LOADER_URL)

        iconset_prefixes = ["m3o", "m3of", "m3r", "m3rf", "m3s", "m3sf"]
        registered_count = 0
        
        for iconset_prefix in iconset_prefixes:
            icons_url = f"{ICONS_URL}/{iconset_prefix}"
            icons_path = hass.config.path(f"{ICONS_PATH}/{iconset_prefix}")
            icons_list_url = f"{icons_url}/icons.json"

            # Check if the path exists before registering
            if not path.exists(icons_path):
                LOGGER.warning(f"Icon path does not exist, skipping: {icons_path}")
                continue

            LOGGER.debug(f"Registering static path: {icons_url} -> {icons_path}")
            await hass.http.async_register_static_paths(
                [StaticPathConfig(icons_url, icons_path, True)]
            )
            
            LOGGER.debug(f"Registering API view: {icons_list_url}")
            hass.http.register_view(
                ListingView(icons_list_url, icons_path, hass, iconset_prefix)
            )
            registered_count += 1
            
        if registered_count == 0:
            LOGGER.error("No icon sets were registered - check if icon data exists")
            return False
            
        LOGGER.info(f"Material Symbols setup complete. Registered {registered_count}/{len(iconset_prefixes)} icon sets.")
        return True
        
    except Exception as e:
        LOGGER.error(f"Error during Material Symbols setup: {e}")
        return False


async def async_setup_entry(hass, entry):
    LOGGER.info(f"Setting up entry for Material Symbols: {entry}")
    return True


async def async_remove_entry(hass, entry):
    LOGGER.info(f"Removing entry for Material Symbols: {entry}")
    return True


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate from old entry."""
    if entry.version == 1:
        entry.version = 2
        hass.config_entries.async_update_entry(
            entry,
            title="Material Symbols"
        )
        LOGGER.info("Migrated Material Symbols config entry to version 2.")
    return True
import logging
import json
from os import path, walk
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.components.http.view import HomeAssistantView

LOGGER = logging.getLogger(__name__)

NAME = "Material Symbols"
DOMAIN = "material_symbols"
VERSION = "2025.05.18"

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
        LOGGER.debug(f"ListingView initialised with URL: {self.url}, "
                     f"iconset_path: {self.iconset_path}, "
                     f"iconset_prefix: {iconset_prefix}")

    async def get(self, request):
        # Fetch the icons list
        icons_list = await self.hass.async_add_executor_job(
            self.get_icons_list, self.iconset_path
        )
        LOGGER.debug(f"Icons list served: {icons_list}")
        return self.json(icons_list)

    def get_icons_list(self, iconset_path):
        icons = []
        for dirpath, dirnames, filenames in walk(iconset_path):
            LOGGER.debug(f"Walking directory: {dirpath}")
            for fn in filenames:
                if fn.endswith(".svg"):
                    # Remove potential './' or subdirectory paths
                    icon_name = fn[:-4]
                    LOGGER.debug(f"Found icon: {icon_name}")
                    icons.append({"name": icon_name})
        LOGGER.debug(f"Final icons list: {icons}")
        return icons


async def async_setup(hass: HomeAssistant, config):
    LOGGER.debug(f"Setting up Material Symbols with version {VERSION}")
    await hass.http.async_register_static_paths(
        [StaticPathConfig(LOADER_URL, hass.config.path(LOADER_PATH), True)]
    )
    LOGGER.debug(f"Static JS path registered: {LOADER_URL}")
    add_extra_js_url(hass, LOADER_URL)

    iconset_prefixes = ["m3o", "m3of", "m3r", "m3rf", "m3s", "m3sf"]
    for iconset_prefix in iconset_prefixes:
        icons_url = f"{ICONS_URL}/{iconset_prefix}"
        icons_path = hass.config.path(f"{ICONS_PATH}/{iconset_prefix}")
        icons_list_url = f"{icons_url}/icons.json"

        LOGGER.debug(f"Registering static path: {icons_url} -> {icons_path}")
        await hass.http.async_register_static_paths(
            [StaticPathConfig(icons_url, icons_path, True)]
        )
        LOGGER.debug(f"Registering API view: {icons_list_url}")
        hass.http.register_view(
            ListingView(icons_list_url, icons_path, hass, iconset_prefix)
        )
    LOGGER.info("Material Symbols setup complete.")
    return True


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
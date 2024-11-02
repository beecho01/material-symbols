import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig

LOGGER = logging.getLogger(__name__)

DOMAIN = "material_symbols"
VERSION = "2024.11.02"

DATA_EXTRA_MODULE_URL = "frontend_extra_module_url"
LOADER_URL = f"/{DOMAIN}/material_symbols.js"
LOADER_PATH = f"custom_components/{DOMAIN}/material_symbols.js"
ICONS_URL = f"/{DOMAIN}"
ICONS_PATH = f"custom_components/{DOMAIN}/data"

async def async_setup(hass: HomeAssistant, config):
    # Register the JS loader file
    await hass.http.async_register_static_paths(
        [StaticPathConfig(LOADER_URL, hass.config.path(LOADER_PATH), True)]
    )
    add_extra_js_url(hass, LOADER_URL)

    # Define icon set folders and register their static paths
    iconset_prefixes = ["m3o", "m3of", "m3r", "m3rf", "m3s", "m3sf"]
    for iconset_prefix in iconset_prefixes:
        await hass.http.async_register_static_paths(
            [
                StaticPathConfig(
                    f"{ICONS_URL}/{iconset_prefix}",
                    hass.config.path(f"{ICONS_PATH}/{iconset_prefix}"),
                    True,
                )
            ]
        )

    return True

async def async_setup_entry(hass, entry):
    return True

async def async_remove_entry(hass, entry):
    return True

async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate from old entry."""
    if entry.version == 1:
        entry.version = 2
        hass.config_entries.async_update_entry(
            entry,
            title="Material Symbols"
        )
        LOGGER.info("Migrating Material Symbols config entry.")
    return True
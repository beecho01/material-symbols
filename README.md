# HomeAssistant Material Symbols
![Home Assistant](https://img.shields.io/badge/home%20assistant-%2341BDF5.svg?style=for-the-badge&logo=home-assistant&logoColor=white)

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/beecho01/material-symbols)](https://github.com/beecho01/material-symbols/releases)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
![GitHub file size in bytes](https://img.shields.io/github/size/beecho01/material-symbols/dist/material-symbols.js?label=plugin%20size)
![GitHub last commit](https://img.shields.io/github/last-commit/beecho01/material-symbols)
[![GitHub closed issues by-label](https://img.shields.io/github/issues-closed/beecho01/material-symbols/icon%20request?label=community%20requests)](https://github.com/beecho01/material-symbols/issues?q=is%3Aclosed+label%3A"icon+request")

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg


Additional vector icons for Home Assistant, to better represent Philips Hue bulbs and fixtures.
Inspired by the Hue icons in the iOS app, and for personal use only, this repo also features custom vectors created specifically by the author for Hue
fixtures and groups that aren't represented by the 'official' icon set.

## <a name="installation"></a>Installation

material-symbols has been accepted into the [Home Assistant Community Store (HACS)](https://hacs.xyz).

### HACS (Recommended):
This is the recommended way to install material-symbols. material-symbols is a default repository for HACS. To install:

- Open HACS (installation instructions are [here](https://hacs.xyz/docs/installation/installation/)).
- Go to "Frontend" section
- Click button with "+" icon
- Search for "Material Symbols" and install it.
- Add the following to your configuration.yaml, save and restart HA.
```
frontend:
  extra_module_url:
    - /hacsfiles/material-symbols/material-symbols.js
```

### Manual:
- Copy `dist/material-symbols.js` into your `config/www` folder.
- Go to Configuration -> Lovelace Dashboards -> Resources -> Add Resource
- set url as `/local/material-symbols.js` and Resource Type as `Javascript Module`.
- Add the following to your configuration.yaml, save and restart HA.
```
frontend:
  extra_module_url:
    - /local/material-symbols.js
```

- Save, restart Home Assistant.


## Usage
- In your entity editor, specify an icon as `m3s:<icon-name>-<style>`
- If you set `state_color: true` in your card, you'll see the icons get colorised based upon the current RGB setting.

### Example:

```
title: Smart Plug
state_color: true
type: entities
entities:
  - entity: switch.tv_smart_plug
    name: My TV
    icon: m3s:switches-outlined
```

## Icons

### Material Symbols

Material Symbols includes ?? icons modelled upon the Google Webfont Material Symbols for personal use

[//]: # (Start Material Symbols)

| Icon | Name | Icon | Name 
| :--- | :--- | :--- | :--- |

[//]: # (End Material Symbols)

### Icon Requests?
Your light not there? Let me know what's missing by raising a [Custom Icon Request](https://github.com/beecho01/material-symbols/issues/new?assignees=arallsopp&labels=icon+request&template=custom-icon-request.md&title=Icon%20Request%20%5Bname%20of%20fixture%5D).

### Sample Dash
With view icons and state color applied. Play bars are offline.

### Finding Icons
Hass Hue Icons uses the new 'keywords' functionality to help you find specific fixtures. Try searching in the Home Assistant iconpicker for 'pendant' or 'switch'.

Material Symbols also offers a [standalone preview tool](https://beecho01.github.io/material-symbols/docs/build/tester/iconfinder.html). Take a look.

### Discussion:
There's a thread over at the [home assistant forums](https://community.home-assistant.io/) that tracks this repo.

## Troubleshooting:

### Can't ever see the icons?
If you cannot see the new icons, or you get an empty box where you're expecting an icon, flush your network cache.

### Icons don't show on first load of the dash?
Did you add the frontend extra_module_url in your configuration.yaml? See the [installation section](#installation) for details.

## OpenHASP user?
I periodically update a ttf font file in a zip at [font/material-symbols-ttf.zip](font/material-symbols-ttf.zip). Thanks to @nagyrobi for the suggestion.

## Thanks and Props
- @hulkhaugen and @thomasloven for the technique.
- @ludeeus for the installation guidance.
- @HunterX86 for providing 4 sample icons in [#191](https://github.com/beecho01/material-symbols/issues/191)
- Everyone who has helped make this repo so broad by raising an [Icon Request](https://github.com/beecho01/material-symbols/issues/new?assignees=arallsopp&labels=icon+request&template=custom-icon-request.md&title=Icon%20Request%20%5Bname%20of%20fixture%5D).

### Stargazers
[![Stargazers repo roster for @arallsopp/material-symbols](https://reporoster.com/stars/arallsopp/material-symbols)](https://github.com/beecho01/material-symbols/stargazers)

---

## Want to use these icons on your physical wall switches and push buttons?
www.unikkontakt.dk has been given rights to use the custom hass-hue icons in their icon database, allowing you to create unique, beautiful and functional overprinted switches that reflect your smart home.

Ønsker du at bruge disse ikoner på dine fysiske kontakter og trykknapper?
www.unikkontakt.dk er blevet tildelt rettigheder til at bruge custom hass-hue ikonerne i deres ikon-database, som gør det muligt for dig at designe unikke, flotte og funktionelle kontakter med printede ikoner, som matcher dit smart home.

### License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
I do this for fun, without charge, and to give back to the community. You may remix, tweak, and build upon this work non-commercially, as long as you credit the original author, provide a link to the license, and indicate if any changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use unless agreed. If you remix, transform or build upon the material, you must distribute your contributions under the same or compatible license as the original. 


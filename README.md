# HomeAssistant Material Symbols
<div align="left">
  <br>
  <img src="docs/badges/built-for-homeassistant.svg"> &nbsp
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://forthebadge.com/images/badges/cc-nc-sa.svg"></a> &nbsp
  <br>
  <br>
  <img src="https://img.shields.io/github/v/release/beecho01/material-symbols?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/size/beecho01/material-symbols/dist%2Fmaterial-symbols.js?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/last-commit/beecho01/material-symbols?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/issues-closed/beecho01/material-symbols/icon%20request?label=community%20requests&style=for-the-badge">
  <br>
  <br>
  <br>
</div>

<!-- [![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration) -->

Material Symbols includes 18620 SVG icon files modelled upon the Google Material Symbols and is for personal use only.

Material Symbols uses the new 'keywords' functionality to help you find specific fixtures. Try searching in the Home Assistant iconpicker for 'pendant' or 'switch'. Material Symbols also offers a [standalone preview tool](https://beecho01.github.io/material-symbols/docs/build/tester/iconfinder.html).

---

## Table of contents

- [Installation](#installation)
- [Usage](#Usage)
- [FAQ](#FAQ)
- [Troubleshooting](#Troubleshooting)
- [Community](#community)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)

---

## <a name="installation"></a>Installation

Unfortunately Material Symbols has not yet been accepted into the [Home Assistant Community Store (HACS)](https://hacs.xyz).

### HACS (Recommended):
This is the recommended way to install Material Symbols. Material Symbols is a default repository for HACS. To install:

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

---

## <a name="Usage"></a>Usage
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

---

## <a name="FAQ"></a>FAQ

### Icon Requests?
Your light not there? Let me know what's missing by raising a [Custom Icon Request](https://github.com/beecho01/material-symbols/issues/new?assignees=beecho01&labels=icon+request&template=custom-icon-request.md&title=Icon%20Request%20%5Bname%20of%20fixture%5D).

### Sample Dash
With view icons and state color applied. Play bars are offline.

## <a name="Troubleshooting"></a>Troubleshooting

### Can't ever see the icons?
If you cannot see the new icons, or you get an empty box where you're expecting an icon, flush your network cache.

### Icons don't show on first load of the dash?
Did you add the frontend extra_module_url in your configuration.yaml? See the [installation section](#installation) for details.

---

### <a name="community"></a>Community
There's a thread over at the [home assistant forums](https://community.home-assistant.io/) that tracks this repo.

---

## <a name="thanks"></a>Thanks
- Big thanks to @arallsopp for his repository and work he's undertaken, I have used it as a basis of this repository
- @hulkhaugen and @thomasloven for the technique.
- @ludeeus for the installation guidance.
- @HunterX86 for providing 4 sample icons in [#191](https://github.com/beecho01/material-symbols/issues/191)
- Everyone who has helped make this repo so broad by raising an [Icon Request](https://github.com/beecho01/material-symbols/issues/new?assignees=beecho01&labels=icon+request&template=custom-icon-request.md&title=Icon%20Request%20%5Bname%20of%20fixture%5D).

### Stargazers
[![Stargazers repo roster for @beecho01/material-symbols](https://reporoster.com/stars/beecho01/material-symbols)](https://github.com/beecho01/material-symbols/stargazers)

---

### <a name="copyright-and-license"></a>Copyright and license

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
I do this for fun, without charge, and to give back to the community. You may remix, tweak, and build upon this work non-commercially, as long as you credit the original author, provide a link to the license, and indicate if any changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use unless agreed. If you remix, transform or build upon the material, you must distribute your contributions under the same or compatible license as the original. 


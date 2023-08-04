<div align="center">
    <img src="https://github.com/beecho01/material-symbols/blob/main/docs/build/tester/images/Screenshot%202023-08-04%20202906.png">
     <h1 align="center">Material Symbols for Home Assistant</h1>
</div>

---

Material Symbols for Home Assistant is collection of 18620 Google Material Symbols files for use within Home Assistant.

This repository has a [Preview Tool](https://beecho01.github.io/material-symbols/docs/build/tester/iconfinder.html) that can be used to assist in picking the correct the icon. This preview tool uses keywords to help you find icons matching your need for use for YAML configuration or UI interface. Simply type in what you are looking for and copy the icon string, starting "m3s:" for use.

Please be aware that this tool has a couple of issues I am working on to resolve:
- Slow seaching due to large number of icons
- A number of icons appear blank due to an SVG "viewbox" issue

---

<div align="left">
  <br>
  <img src="https://img.shields.io/badge/built_for-Home_Assistant-47BFF5?style=for-the-badge"> &nbsp
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/license-CC--BY--NC--SA--4.0-lightgrey?style=for-the-badge"></a> &nbsp
  <img src="https://img.shields.io/github/downloads/beecho01/material-symbols/total?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/v/release/beecho01/material-symbols?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/size/beecho01/material-symbols/dist%2Fmaterial-symbols.js?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/last-commit/beecho01/material-symbols?style=for-the-badge"> &nbsp
  <img src="https://img.shields.io/github/issues-closed/beecho01/material-symbols/icon%20request?label=community%20requests&style=for-the-badge">
  <br>
  <br>
</div>

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


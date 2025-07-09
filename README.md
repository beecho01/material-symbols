<div align="center">
    <img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/custom_components/material_symbols/images/Banner_Image.png">
     <h1 align="center">Material Symbols for Home Assistant</h1>
</div>

**Material Symbols for Home Assistant** is a collection of 14,404 Google Material Symbols for use within Home Assistant. It uses the icon-set produced and maintained by [iconify](https://github.com/iconify/icon-sets).

There is a [Icon Finder Tool](https://beecho01.github.io/material-symbols-iconfinder/) to help you select the correct icon. Simply type in what you're looking for, click the icon of choice, and the icon entry for home assistant will be copied to your clipboard (e.g., `m3o:light`). The copied text can be pasted for use in your YAML configuration or into you UI frontend interface.

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">


<div align="left">
  <br>
  <img src="https://img.shields.io/badge/built_for-Home_Assistant-47BFF5?style=for-the-badge"> &nbsp;
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/license-CC--BY--NC--SA--4.0-lightgrey?style=for-the-badge"></a> &nbsp;
  <img src="https://img.shields.io/github/downloads/beecho01/material-symbols/total?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/v/release/beecho01/material-symbols?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/repo-size/beecho01/material-symbols?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/last-commit/beecho01/material-symbols?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/issues-closed/beecho01/material-symbols/icon%20request?label=community%20requests&style=for-the-badge">
  <br>
  <br>
</div>

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/warning.svg">
> </picture>
>
> To see how to complete the migration from repository (v1.X.X) to an "Integration" repository (202X.X.X+), please visit the [Migration documentation](https://github.com/beecho01/material-symbols/blob/main/docs/Migration.md).

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="table-of-contents"></a>Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
    - [HACS Installation (Recommended)](#hacs-installation-recommended)
    - [Manual Installation](#manual-installation)
- [Usage](#usage)
    - [Example](#example)
- [Community](#community)
- [Troubleshooting](#troubleshooting)
    - [Icons Not Showing?](#icons-not-showing)
- [Feedback and Contributions](#feedback-and-contributions)
- [Thanks](#thanks)
  - [Stargazers](#stargazers)
- [Copyright and License](#copyright-and-license)
    - [License Summary](#license-summary)

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="installation"></a>Installation

#### <a name="hacs-installation-recommended"></a>HACS Installation (Recommended)

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/info.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/info.svg">
> </picture><br>
>
> **Note**: Material Symbols is now installable via [HACS](https://hacs.xyz) as a **Default Integration** 🥳.


1. First, tap on the integration repository quick-link below and install:

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=beecho01&repository=material-symbols)

2. Then the next setup quick-link below to complete the setup configuration:

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=material_symbols)

3. After the installation completes, restart Home Assistant to load the new integration.
    - You're browser cache may need to be deleted to show the icons as desired.

<br>

---

#### <a name="manual-installation"></a>Manual Installation

If you prefer to install the integration manually:

1. **Download the Integration:**

   - Download the `material_symbols` folder from the `custom_components` directory of this repository.

2. **Copy to Home Assistant:**

   - Place the `material_symbols` folder into your Home Assistant `config/custom_components/` directory. The final path should be `config/custom_components/material_symbols/`.

3. **Restart Home Assistant:**

   - Restart Home Assistant to load the new integration.
  
4. **Add Integration to Devices & Services:**

   - In the Home Assistant Settings menu, select **Devices & Services**.
   - Tap the **+ Add Integration** button.
   - Search for **Material Symbols** and select it.
   - This should now show as successfully configured.
   - Tap **Finish**.
  
5. **Restart Home Assistant:**

   - Restart Home Assistant to complete the setup.

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="usage"></a>Usage

Once installed, you can use the Material Symbols icons in your Lovelace UI.

  The icons come in six distinct styles, each with its own prefix:
- Outlined: `m3o`
- Outlined and filled: `m3of`
- Rounded: `m3r`
- Rounded and filled: `m3rf`
- Sharp: `m3s`
- Sharp and filled: `m3sf`

**Using an Icon:**

  In your entity configuration, specify the icon using the appropriate prefix and icon name:

  ```yaml
  icon: 'prefix:icon_name'
  ```

  Replace `prefix` with one of the prefixes above and `icon_name` with the desired icon. There is a [Icon Finder Tool](https://beecho01.github.io/material-symbols-iconfinder/) to help you select the correct icon for your needs.

#### <a name="example"></a>Example
  ```yaml
  type: entities
  title: Lights
  entities:
    - entity: light.living_room
      name: Living Room Light
      icon: 'm3o:light'
    - entity: light.kitchen
      name: Kitchen Light
      icon: 'm3of:light'
    - entity: light.bedroom
      name: Bedroom Light
      icon: 'm3r:light'
    - entity: light.garage
      name: Garage Light
      icon: 'm3rf:light'
    - entity: light.porch
      name: Porch Light
      icon: 'm3s:light'
    - entity: light.garden
      name: Garden Light
      icon: 'm3sf:light'
  ```

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="community"></a>Community
Join the discussion on the [Home Assistant Community Forum](https://community.home-assistant.io/t/material-symbols-for-home-assistant/599573).

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="troubleshooting"></a>Troubleshooting
### <a name="icons-not-showing"></a>Icons Not Showing?

#### <ins>If you're seeing this issue in the desktop browser:</ins>
- **Try clearing browser cache using developer tools** - With developer tools open (`F12`/`CTRL` + `SHIFT` + `I`/`CMD` `SHIFT` `I`), right click on the browser reload button and click `Empty Cache and Hard Reload`. If this option isn't available, you can also try `SHIFT` clicking on the reload button, `CTRL` + `F5`, or `CTRL` + `SHIFT` + `R`.
- **Try clearing browser cache using browser history** - This can vary by browser but [this page](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0025251) has good instructions for various browsers. Generally speaking, you have to navigate to your browser history , click `Delete browsing data`, and then clear `Cached images and files` (Do not clear cookies and other site data, it will log you out of everything).

#### <ins>If you're seeing this issue in the Android companion app:</ins>
As of [2025.4.3](https://github.com/home-assistant/android/releases/tag/2025.4.3), the Home Assistant Android companion app has a new internal option to clear app cache. 

Within the app navigate to `Settings`, `Companion app`, scroll all the way down to the `Need help?` section near the bottom, click `Troubleshooting`, and then click `Reset frontend cache`. Then stop the app, optionally clear app cache via Android settings, and then re-open the app.

#### <ins>If you're seeing this issue in the iPhone companion app:</ins>
Within the app navigate to `Settings`, `Companion app`, `Debugging`, and then click `Reset frontend cache`. Then stop and re-open the app.

#### <ins>If you're seeing this issue in the Fully Kiosk Browser app:</ins>
Within the app swipe from the left edge to open the Fully Kiosk Browser sidebar menu, click `Privacy Check`, toggle on `Cache`, click `Delete`, and then click `Goto Start URL`.

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="feedback-and-contributions"></a>Feedback and Contributions
If you encounter issues or have suggestions, please open an issue on GitHub.
Contributions are welcome! Feel free to submit pull requests.

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="thanks"></a>Thanks
- Big thanks to [@vigonotion](https://github.com/vigonotion) and his repository [hass-simpleicons](https://github.com/vigonotion/hass-simpleicons) and [@thomasloven](https://github.com/thomasloven) for his repository [hass-fontawesome](https://github.com/thomasloven/hass-fontawesome), of which this integration and github repository is based.
- Thanks to OpenAI and ChatGPT their LLM `01-preview` for assistance in resolving issues during development.
- Thanks to [@Nerwyn](https://github.com/Nerwyn) for his inclusion of this repository in his repository, giving this project exposure. Furthermore, I have based the [Troubleshooting](#troubleshooting) cache clearing section based on his work in [Common Stuck Update Issues #12](https://github.com/Nerwyn/material-you-utilities/discussions/12).

### Stargazers
<div align="left">
    <a href="https://star-history.com/#beecho01/material-symbols&Date">
     <picture>
       <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=beecho01/material-symbols&type=Date&theme=dark" />
       <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=beecho01/material-symbols&type=Date" />
       <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=beecho01/material-symbols&type=Date" />
     </picture>
    </a>
</div>

[![Stargazers repo roster for @beecho01/material-symbols](https://reporoster.com/stars/beecho01/material-symbols)](https://github.com/beecho01/material-symbols/stargazers)

<img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/docs/assets/images/Line.svg" alt="line break" width="100%" height="3px">

## <a name="copyright-and-license"></a>Copyright and License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

#### <a name="license-summary"></a>License Summary
 - **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
 - **NonCommercial**: You may not use the material for commercial purposes.
 - **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

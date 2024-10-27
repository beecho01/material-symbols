<div align="center">
    <img src="https://raw.githubusercontent.com/beecho01/material-symbols/refs/heads/main/custom_components/material_symbols/images/Banner_Image.png">
     <h1 align="center">Material Symbols for Home Assistant</h1>
</div>

**Material Symbols for Home Assistant** is a collection of 13460 Google Material Symbols for use within Home Assistant. It uses the icon-set produced and maintained by [iconify](https://github.com/iconify/icon-sets).

There is a [Icon Finder Tool](https://beecho01.github.io/material-symbols-iconfinder/) to help you select the correct icon. Simply type in what you're looking for, click the icon of choice, and the icon entry for home assistant will be copied to your clipboard (e.g., `m3o:light`). The copied text can be pasted for use in your YAML configuration or into you UI frontend interface.

---

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/warning.svg">
> </picture>
>
> ### Breaking Changes
> - **Repository Structure**: The repository and installation have transitioned from a "Lovelace" repository (v1.X.X) to an "Integration" repository (202X.X.X+). Users should reinstall from the new integration repository to avoid compatibility issues.
> - **Icon Prefix Migration**: The icon prefix has transitioned from m3s, which previously contained all icon styles, to individual prefixes based on style. Each style now has its unique prefix (e.g., m3o for outlined, m3r for rounded). Refer to the documentation for the complete list of prefixes.
> - **Reduction in Available Icons**: The number of available icons has been reduced from ~18,600 to 13,460.

---

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

## <a name="table-of-contents"></a>Table of Contents

- [Table of Contents](#table-of-contents)
- [Migrating from v1.X.X to 202X.X.X](#migrating-from-v1xx-to-202xxx)
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

---


## <a name="Migrating from v1.X.X to 202X.X.X"></a>Migrating from v1.X.X to 202X.X.X

My recommendation here is to fully uninstall the existing v1.X.X repository and remove all traces of it from the system. Please do the following to complete this:

**If you originally installed the icons via HACS:**
1.  Go to `HACS` and in the search bar search `Material Symbols`.
2.  Find the repository in the list and click on it.
3.  Click the `Menu Icon` (3 vertical dots) for the repository
4.  Click `Remove`
5.  On the Remove pop-up/modal, select `Remove`
6.  Wait for this to complete
7.  Go to your dashboard of choice and via the `Menu Icon` (3 vertical dots), select the `Resources` option.
8.  Identify if a javascript module ending `material-symbols.js` is present. If so remove it.
9.  After removing the resource and references, restart Home Assistant to apply the changes.
10. Once Home Assistant restarts, clear your browser’s cache to ensure it no longer tries to load the removed icon pack resources.
11. Continue to the [Installation](#installation) steps to install the 202X.X.X integration.

**If you originally installed the icons via configuration.yaml:**

If your resources are managed by configuration.yaml:
1. Remove the `material-symbols.js` from

    ```
    frontend:
      extra_module_url:
        - /local/community/material-symbols/material-symbols.js
    ```
    or the location you placed it.

If your resources are managed in the resources section of the dashboard UI:

1.  Go to your dashboard of choice and via the `Menu Icon` (3 vertical dots), select the `Resources` option.
2.  Identify if a javascript module ending `material-symbols.js` is present. If so remove it.

Make sure to delete the files from the location you placed it.

1.  After removing the resource and files, restart Home Assistant to apply the changes.
2.  Once Home Assistant restarts, clear your browser’s cache to ensure it no longer tries to load the removed icon pack resources.
3.  Continue to the [Installation](#installation) steps to install the 202X.X.X integration.

---

## <a name="installation"></a>Installation

#### <a name="hacs-installation-recommended"></a>HACS Installation (Recommended)

**Note**: Material Symbols is now installable via [HACS](https://hacs.xyz) as a custom **Integration**.

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/info.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/info.svg">
> </picture><br>
>
> There are 2 methods to install via HACS below. First is by the my.home-assistant.io quick links and the second, by typing the custom repository.


##### HACS Method 1

1. First, tap on the integration repository quick-link below and install:

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=beecho01&repository=material-symbols)

2. Then the next setup quick-link below to complete the setup configuration:

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=material_symbols)

3. After the installation completes, restart Home Assistant to load the new integration.
    - You're browser cache may need to be deleted to show the icons as desired.

##### HACS Method 2

1. **Add the Custom Repository to HACS manually:**

   - Open Home Assistant and navigate to **HACS**.
   - Click on **Integrations**.
   - Click on the three dots in the top-right corner and select **Custom repositories**.
   - In the dialog that appears:
     - **Repository URL**: `https://github.com/beecho01/material-symbols`
     - **Category**: **Integration**
   - Click **Add**.
   - You should see a confirmation that the repository was added successfully.

2. **Install the Integration:**

   - In HACS, go back to **Integrations**.
   - Click on the **Explore & Add Repositories** button.
   - Search for **Material Symbols**.
   - Click on the **Material Symbols** integration.
   - Click **Download** in the bottom right corner.
   - Confirm the installation by clicking **Download** again.
  
3. ** Add Integration to Devices & Services:**

   - In the Home Assistant Settings menu, select **Devices & Services**.
   - Tap the **+ Add Integration** button.
   - Search for **Material Symbols** and select it.
   - This should now show as succesfully configured.
   - Tap **Finish**.

4. **Restart Home Assistant:**

   - After the installation completes, restart Home Assistant to load the new integration.
   - You're browser cache may need to be deleted to show the icons as desired.
<br>

#### <a name="manual-installation"></a>Manual Installation

If you prefer to install the integration manually:

1. **Download the Integration:**

   - Download the `material_symbols` folder from the `custom_components` directory of this repository.

2. **Copy to Home Assistant:**

   - Place the `material_symbols` folder into your Home Assistant `config/custom_components/` directory. The final path should be `config/custom_components/material_symbols/`.

3. **Restart Home Assistant:**

   - Restart Home Assistant to load the new integration.
  
4. ** Add Integration to Devices & Services:**

   - In the Home Assistant Settings menu, select **Devices & Services**.
   - Tap the **+ Add Integration** button.
   - Search for **Material Symbols** and select it.
   - This should now show as succesfully configured.
   - Tap **Finish**.
  
5. **Restart Home Assistant:**

   - Restart Home Assistant to complete the setup.

---

## <a name="usage"></a>Usage

Once installed, you can use the Material Symbols icons in your Lovelace UI.

**Icon Prefixes and Styles:**

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

---

## <a name="community"></a>Community
Join the discussion on the [home assistant community forum](https://community.home-assistant.io/t/material-symbols-for-home-assistant/599573).

---

## <a name="troubleshooting"></a>Troubleshooting
#### <a name="icons-not-showing"></a>Icons Not Showing?
 - **Clear Browser Cache**: If icons are not displaying, clear your browser cache and reload the Home Assistant interface.
 - **Restart Home Assistant**: Ensure you've restarted Home Assistant after installing the integration.
 - **Check Installation**: Verify that the integration is installed correctly and that the icons are in the right directories.
 - **Mobile Application**: Unfortunately, clearing the application cache isnt a sure-fire way to remove the existing cached icons. It has been suggested on the Community Forum thread [here](https://community.home-assistant.io/t/icons-doesnt-display-on-app/251852/15), that uninstalling the application and re-installing is the most likely way to get them to show correctly.  

---

## <a name="feedback-and-contributions"></a>Feedback and Contributions
If you encounter issues or have suggestions, please open an issue on GitHub.
Contributions are welcome! Feel free to submit pull requests.

---

## <a name="thanks"></a>Thanks
- Big thanks to [@vigonotion](https://github.com/vigonotion) and his repository [hass-simpleicons](https://github.com/vigonotion/hass-simpleicons) and [@thomasloven](https://github.com/thomasloven) for his repository [hass-fontawesome](https://github.com/thomasloven/hass-fontawesome), of which this integration and github repository is based.
- Thanks to OpenAI and ChatGPT their LLM `01-preview` for assistance in resolving issues during development.

### Stargazers
[![Stargazers repo roster for @beecho01/material-symbols](https://reporoster.com/stars/beecho01/material-symbols)](https://github.com/beecho01/material-symbols/stargazers)

---

## <a name="copyright-and-license"></a>Copyright and License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

#### <a name="license-summary"></a>License Summary
 - **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
 - **NonCommercial**: You may not use the material for commercial purposes.
 - **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

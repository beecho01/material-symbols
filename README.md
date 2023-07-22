# HomeAssistant Material Symbols
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/beecho01/material-symbols)](https://github.com/beecho01/material-symbols/releases)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
![GitHub file size in bytes](https://img.shields.io/github/size/beecho01/material-symbols/dist/material-symbols.js?label=plugin%20size)
![GitHub last commit](https://img.shields.io/github/last-commit/beecho01/material-symbols)
[![GitHub closed issues by-label](https://img.shields.io/github/issues-closed/beecho01/material-symbols/icon%20request?label=community%20requests)](https://github.com/beecho01/material-symbols/issues?q=is%3Aclosed+label%3A"icon+request")
[![Man Hours](https://img.shields.io/endpoint?url=https%3A%2F%2Fmh.jessemillar.com%2Fhours%3Frepo%3Dhttps%3A%2F%2Fgithub.com%2Farallsopp%2Fmaterial-symbols.git)](https://jessemillar.com/r/man-hours)

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

### Hue Icons

material-symbols includes ?? Naterial Symbols modelled upon the Google Webfont Material Symbols webpage for personal use

[//]: # (Start Material Symbols)

| Icon | Name | Icon | Name 
| :--- | :--- | :--- | :--- |
| ![hue:bloom](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bloom.svg)| hue:bloom | ![hue:bollard](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bollard.svg)| hue:bollard |
| ![hue:bridge-v1](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bridge-v1.svg)| hue:bridge-v1 | ![hue:bridge-v2](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bridge-v2.svg)| hue:bridge-v2 |
| ![hue:bulb-candle](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-candle.svg)| hue:bulb-candle | ![hue:bulb-classic](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-classic.svg)| hue:bulb-classic |
| ![hue:bulb-filament](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-filament.svg)| hue:bulb-filament | ![hue:bulb-flood](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-flood.svg)| hue:bulb-flood |
| ![hue:bulb-group](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-group.svg)| hue:bulb-group | ![hue:bulb-spot](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-spot.svg)| hue:bulb-spot |
| ![hue:bulb-sultan](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/bulb-sultan.svg)| hue:bulb-sultan | ![hue:ceiling-round](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/ceiling-round.svg)| hue:ceiling-round |
| ![hue:ceiling-square](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/ceiling-square.svg)| hue:ceiling-square | ![hue:desk-lamp](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/desk-lamp.svg)| hue:desk-lamp |
| ![hue:dimmer-switch](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/dimmer-switch.svg)| hue:dimmer-switch | ![hue:double-spot](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/double-spot.svg)| hue:double-spot |
| ![hue:downstairs](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/downstairs.svg)| hue:downstairs | ![hue:floor-lantern](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/floor-lantern.svg)| hue:floor-lantern |
| ![hue:floor-shade](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/floor-shade.svg)| hue:floor-shade | ![hue:floor-spot](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/floor-spot.svg)| hue:floor-spot |
| ![hue:go](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/go.svg)| hue:go | ![hue:home](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/home.svg)| hue:home |
| ![hue:iris](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/iris.svg)| hue:iris | ![hue:lightstrip](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/lightstrip.svg)| hue:lightstrip |
| ![hue:motion-sensor](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/motion-sensor.svg)| hue:motion-sensor | ![hue:outdoor-motion-sensor](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/outdoor-motion-sensor.svg)| hue:outdoor-motion-sensor |
| ![hue:pendant-long](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/pendant-long.svg)| hue:pendant-long | ![hue:pendant-round](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/pendant-round.svg)| hue:pendant-round |
| ![hue:play-bar](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/play-bar.svg)| hue:play-bar | ![hue:plug](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/plug.svg)| hue:plug |
| ![hue:recessed-ceiling](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/recessed-ceiling.svg)| hue:recessed-ceiling | ![hue:recessed-floor](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/recessed-floor.svg)| hue:recessed-floor |
| ![hue:room-attic](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-attic.svg)| hue:room-attic | ![hue:room-balcony](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-balcony.svg)| hue:room-balcony |
| ![hue:room-bathroom](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-bathroom.svg)| hue:room-bathroom | ![hue:room-bbq](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-bbq.svg)| hue:room-bbq |
| ![hue:room-bedroom](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-bedroom.svg)| hue:room-bedroom | ![hue:room-carport](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-carport.svg)| hue:room-carport |
| ![hue:room-closet](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-closet.svg)| hue:room-closet | ![hue:room-computer](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-computer.svg)| hue:room-computer |
| ![hue:room-dining](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-dining.svg)| hue:room-dining | ![hue:room-driveway](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-driveway.svg)| hue:room-driveway |
| ![hue:room-front-door](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-front-door.svg)| hue:room-front-door | ![hue:room-games](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-games.svg)| hue:room-games |
| ![hue:room-garage](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-garage.svg)| hue:room-garage | ![hue:room-guestroom](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-guestroom.svg)| hue:room-guestroom |
| ![hue:room-gym](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-gym.svg)| hue:room-gym | ![hue:room-hallway](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-hallway.svg)| hue:room-hallway |
| ![hue:room-kids](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-kids.svg)| hue:room-kids | ![hue:room-kitchen](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-kitchen.svg)| hue:room-kitchen |
| ![hue:room-laundry](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-laundry.svg)| hue:room-laundry | ![hue:room-living](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-living.svg)| hue:room-living |
| ![hue:room-lounge](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-lounge.svg)| hue:room-lounge | ![hue:room-nursery](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-nursery.svg)| hue:room-nursery |
| ![hue:room-office](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-office.svg)| hue:room-office | ![hue:room-other](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-other.svg)| hue:room-other |
| ![hue:room-outdoors](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-outdoors.svg)| hue:room-outdoors | ![hue:room-pool](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-pool.svg)| hue:room-pool |
| ![hue:room-porch](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-porch.svg)| hue:room-porch | ![hue:room-recreation](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-recreation.svg)| hue:room-recreation |
| ![hue:room-stairs](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-stairs.svg)| hue:room-stairs | ![hue:room-storage](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-storage.svg)| hue:room-storage |
| ![hue:room-studio](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-studio.svg)| hue:room-studio | ![hue:room-terrace](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-terrace.svg)| hue:room-terrace |
| ![hue:room-toilet](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/room-toilet.svg)| hue:room-toilet | ![hue:single-spot](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/single-spot.svg)| hue:single-spot |
| ![hue:table-shade](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/table-shade.svg)| hue:table-shade | ![hue:table-wash](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/table-wash.svg)| hue:table-wash |
| ![hue:upstairs](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/upstairs.svg)| hue:upstairs | ![hue:wall-lantern](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/wall-lantern.svg)| hue:wall-lantern |
| ![hue:wall-shade](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/wall-shade.svg)| hue:wall-shade | ![hue:wall-spot](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/svgs/wall-spot.svg)| hue:wall-spot |

[//]: # (End Material Symbols)

### Icon Requests?
Your light not there? Let me know what's missing by raising a [Custom Icon Request](https://github.com/beecho01/material-symbols/issues/new?assignees=arallsopp&labels=icon+request&template=custom-icon-request.md&title=Icon%20Request%20%5Bname%20of%20fixture%5D).

### Sample Dash
With view icons and state color applied. Play bars are offline.
![lovelace_example](https://raw.githubusercontent.com/beecho01/material-symbols/main/docs/examples/lovelace_example.png)

### Finding Icons
Hass Hue Icons uses the new 'keywords' functionality to help you find specific fixtures. Try searching in the Home Assistant iconpicker for 'pendant' or 'switch'.

**NEW:** Hass Hue Icons also offers a [standalone preview tool](https://arallsopp.github.io/material-symbols/docs/build/tester/iconfinder.html). Take a look.

### Discussion:
There's a thread over at the [home assistant forums](https://community.home-assistant.io/t/created-custom-colorizable-hue-icons-as-a-lovelace-resource) that tracks this repo.

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


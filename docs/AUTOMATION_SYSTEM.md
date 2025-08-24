# 🤖 Material S### Core Automation Files
- **`.github/workflows/auto-update-icons.yml`** - Main GitHub Action workflow
- **`.github/iconify-hash.txt`** - Stores the last processed iconify commit hash
- **`scripts/test_update_detection.py`** - Test script for update detection logics Auto-Update System

This document explains the comprehensive automation system for keeping your Material Symbols icons up-to-date automatically.

## 🎯 Overview

The automation system monitors the [iconify Material Symbols repository](https://github.com/iconify/icon-sets) for updates and automatically:
1. **Detects changes** to the Material Symbols icon set
2. **Regenerates all SVG files** with the latest icons
3. **Updates the README** with the current icon count
4. **Bumps the JavaScript version** to the current date (YYYY.MM.DD format)
5. **Commits and pushes** all changes automatically

## 📁 Files Overview

### Core Automation Files
- **`.github/workflows/auto-update-icons.yml`** - Main GitHub Action workflow
- **`.github/iconify-hash.txt`** - Stores the last processed iconify commit hash
- **`scripts/update_versions.py`** - Unified version updater for both JS and manifest
- **`scripts/test_update_detection.py`** - Test script for update detection logic

### Enhanced Scripts
- **`custom_components/material_symbols/data/generate_svgs.py`** - Complete icon processing: generation, counting, README updates, and version management

## 🚀 How It Works

### 1. Trigger Mechanisms
- **Daily Schedule**: Runs every day at 2 AM UTC
- **Manual Trigger**: Can be manually triggered via GitHub Actions UI
- **API Monitoring**: Checks iconify repository for changes to `material-symbols.json`

### 2. Update Detection Process
```bash
# Gets the latest commit hash for material-symbols.json
curl -s "https://api.github.com/repos/iconify/icon-sets/commits?path=json/material-symbols.json&per_page=1"

# Compares with stored hash in .github/iconify-hash.txt
# If different → UPDATE NEEDED
# If same → No action required
```

### 3. Update Process Flow
When updates are detected:

1. **🎨 Icon Generation & Processing**
   ```bash
   cd custom_components/material_symbols/data
   python generate_svgs.py
   ```
   - Downloads latest Material Symbols JSON from iconify
   - Generates fresh SVG files for all 6 style variants (15,556 total icons)
   - Creates icons.json files for each variant
   - Updates README.md with current icon count
   - Automatically updates JavaScript and manifest versions to current date

3. **📝 Version Management**
   - Updates `material_symbols.js` version to `YYYY.MM.DD` format
   - Updates `manifest.json` version to match
   - Handled automatically during icon generation
   - Today's version: `2025.08.23`

4. **🚀 Git Operations**
   ```bash
   git add .
   git commit -m "🤖 Auto-update Material Symbols icons (v2025.08.23)"
   git push
   ```

## 🛠️ Manual Usage

### Full Icon Regeneration (includes everything)
```bash
cd custom_components/material_symbols/data
python generate_svgs.py
```
This single command:
- Downloads latest icons from iconify
- Generates all SVG files (15,556 total)
- Creates icons.json files for each variant
- Updates README.md with current count
- Updates JavaScript and manifest versions

### Test Update Detection
```bash
python scripts/test_update_detection.py
```

### Manual Icon Counting (if needed for debugging)
```bash
# Count existing icons - currently returns 15,556 total
cd custom_components/material_symbols/data
python -c "
import os
folders = ['m3o', 'm3of', 'm3r', 'm3rf', 'm3s', 'm3sf']
total = sum(len([f for f in os.listdir(folder) if f.endswith('.svg')]) for folder in folders if os.path.exists(folder))
print(f'Total icons: {total}')
"
```

## 📊 Current Status

- **Total Icons**: 15,556 SVG files across 6 style variants
- **Current Version**: 2025.08.23 (Auto-updated) - Both JavaScript and manifest.json
- **Last Iconify Commit**: 0e73a77b (2025-08-22)
- **Icon Variants**:
  - `m3o`: 2,538 (Material 3 Outlined)
  - `m3of`: 3,854 (Material 3 Outlined Filled)
  - `m3r`: 2,228 (Material 3 Rounded)
  - `m3rf`: 3,342 (Material 3 Rounded Filled)
  - `m3s`: 1,590 (Material 3 Sharp)
  - `m3sf`: 2,004 (Material 3 Sharp Filled)

## 🔧 Configuration

### GitHub Action Settings
The workflow runs with these settings:
- **Python Version**: 3.11
- **Timezone**: UTC
- **Dependencies**: `requests` library for API calls
- **Permissions**: Standard repository read/write access

### Version Format
JavaScript versions follow `YYYY.MM.DD` format:
- `2025.08.23` = August 23rd, 2025
- Easy to understand and sort chronologically
- Automatically updated on each icon refresh

## 🎉 Benefits

1. **⏰ Always Up-to-Date**: Never miss new Material Symbols icons
2. **🔄 Zero Maintenance**: Fully automated, no manual intervention needed  
3. **📈 Accurate Counts**: README always shows correct icon count
4. **🏷️ Version Tracking**: Clear versioning tied to update dates
5. **🤖 Professional Commits**: Clean, informative commit messages
6. **🚀 Home Assistant Ready**: Icons immediately available in your integration

## 🐛 Troubleshooting

If the automation isn't working:

1. **Check GitHub Actions Tab**: Look for workflow run errors
2. **Verify Permissions**: Ensure the repository has Actions enabled
3. **API Rate Limits**: GitHub API has rate limits (shouldn't be an issue with daily runs)
4. **Manual Test**: Run `python scripts/test_update_detection.py` locally

## 🚀 What's Next?

The automation is fully set up and ready! It will:
- Monitor iconify daily for new Material Symbols
- Automatically update your repository when changes are detected
- Keep your Home Assistant integration fresh with the latest icons
- Maintain accurate documentation automatically

Your users will always have access to the newest Google Material Symbols icons! 🎨✨

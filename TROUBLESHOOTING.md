# Material Symbols Troubleshooting Guide

## Common Issues and Solutions

### 1. Icons Not Loading After Page Refresh

**Symptoms:**
- Icons display correctly when editing dashboard
- Icons disappear after refreshing the page
- Icons work inconsistently between desktop and mobile

**Causes:**
- Race condition between Home Assistant frontend loading and Material Symbols integration
- Browser caching issues
- Integration not being ready when frontend tries to load icons

**Solutions:**

#### For Users:
1. **Clear browser cache completely** (Ctrl+Shift+R on most browsers)
2. **Hard refresh multiple times** - Sometimes it takes 2-3 refreshes
3. **Navigate to another dashboard and back** - This often triggers a reload
4. **Edit and exit dashboard mode** - This forces a refresh of resources
5. **Restart Home Assistant** if the issue persists

#### For Developers:
The latest version (2025.08.23+) includes:
- Integration readiness checking before loading icons
- Retry mechanisms for failed requests
- Better error handling and logging
- Cache invalidation improvements

### 2. Icons Not Showing on Mobile App

**Symptoms:**
- Icons work fine on desktop browser
- Mobile companion app shows no icons or blank spaces

**Known Issue:**
This is a known issue with the Home Assistant companion apps. A bug report has been filed: [home-assistant/android#4834](https://github.com/home-assistant/android/issues/4834)

**Workarounds:**
1. Force close and reopen the companion app
2. Log out and log back into the app
3. Clear app cache/data (Android) or reinstall app
4. Use the mobile browser instead of the app temporarily

### 3. Console Errors in Browser

If you see console errors, enable debug logging to get more information:

1. Open browser developer tools (F12)
2. Go to Console tab
3. Look for messages starting with "Material Symbols:"
4. Report any errors with full error messages

### 4. Performance Issues

If icons are loading slowly:

1. Check your Home Assistant server resources
2. Ensure you're using the latest version of the integration
3. Check network connectivity between your device and Home Assistant
4. Consider restarting Home Assistant to clear any memory issues

## Debug Information

### Checking Integration Status

1. Go to **Settings** → **Devices & Services**
2. Find "Material Symbols" in the list
3. Verify it shows as "Configured" status

### Browser Console Debugging

Open browser console (F12) and look for these messages:
- `Material Symbols: Starting initialisation` - Integration is starting
- `Material Symbols: Integration ready` - Integration is working
- `Material Symbols: Fetched X/6 icon lists successfully` - Icon loading status
- `Material Symbols: Custom icons defined for all sets` - Setup complete

### Checking Files

Verify these files exist in your installation:
```
custom_components/material_symbols/
├── __init__.py
├── config_flow.py
├── manifest.json
├── material_symbols.js
└── data/
    ├── m3o/
    │   ├── icons.json
    │   └── [thousands of .svg files]
    ├── m3of/
    │   ├── icons.json
    │   └── [thousands of .svg files]
    ├── m3r/
    │   ├── icons.json
    │   └── [thousands of .svg files]
    ├── m3rf/
    │   ├── icons.json
    │   └── [thousands of .svg files]
    ├── m3s/
    │   ├── icons.json
    │   └── [thousands of .svg files]
    └── m3sf/
        ├── icons.json
        └── [thousands of .svg files]
```

## Getting Help

If none of these solutions work:

1. **Check the GitHub Issues**: [beecho01/material-symbols/issues](https://github.com/beecho01/material-symbols/issues)
2. **Create a new issue** with:
   - Your Home Assistant version
   - Browser/device information
   - Console error messages (if any)
   - Steps to reproduce the problem
3. **Include debug logs** from both browser console and Home Assistant logs
# How to Monitor Your Material Symbols Automation

## 1. Local Testing
```bash
# Complete icon processing (includes count, README update, version management)
cd custom_components/material_symbols/data
python generate_svgs.py

# Test update detection
python scripts/test_update_detection.py
```

## 2. GitHub Actions Monitoring

### Check Workflow Status
1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. Look for "Auto-update Material Symbols Icons" workflow
4. Check recent runs for success/failure

### Manual Trigger
You can manually trigger the workflow:
1. Go to **Actions** tab
2. Select "Update Icon Count in README"
3. Click **Run workflow** → **Run workflow**

## 3. Verification Methods

### A) Check Git History
```bash
git log --oneline -n 5
# Look for commits like "🤖 Auto-update icon count in README"
```

### B) Compare Before/After
```bash
# Before making changes, note the current count
grep "collection of" README.md

# After running automation, check if it changed
grep "collection of" README.md
```

### C) Check Workflow Logs
- In GitHub Actions, click on any workflow run
- Check the logs for messages like:
  - "✓ Updated README.md with icon count: X,XXX"
  - "ℹ No changes needed in README.md"

## 4. Current Status

- **Current Icon Count**: 15,556 total icons (across 6 style variants)
- **Unique Icon Names**: 3,911 (each available in multiple styles)
- **Style Breakdown**:
  - m3o (Outlined): 2,538 icons
  - m3of (Outlined Filled): 3,854 icons
  - m3r (Rounded): 2,228 icons
  - m3rf (Rounded Filled): 3,342 icons
  - m3s (Sharp): 1,590 icons
  - m3sf (Sharp Filled): 2,004 icons
- **README Status**: ✅ Up to date with total count

## 5. Troubleshooting

### If the count seems wrong:
```bash
# Debug the count manually
ls custom_components/material_symbols/data/m3o/*.svg | wc -l
```

### If GitHub Actions fails:
- Check the workflow file syntax
- Verify file permissions
- Check if the repository has Actions enabled

### If README doesn't update:
- Verify the regex pattern matches your README format
- Check file encoding (should be UTF-8)
- Ensure the script has write permissions

## 6. Expected Outputs

### Successful Count Script:
```
Counting Material Symbols icons...

m3o: 2538 SVG files
m3of: 3854 SVG files
m3r: 2228 SVG files
m3rf: 3342 SVG files
m3s: 1590 SVG files
m3sf: 2004 SVG files

Total SVG files: 15556
✓ Updated README.md with icon count: 15,556
```

### Successful GitHub Action:
- Commit message: "🤖 Auto-update icon count in README"
- Green checkmark in Actions tab
- Updated timestamp on README.md

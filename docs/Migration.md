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
11. Continue to the [Installation](https://github.com/beecho01/material-symbols/blob/main/README.md#installation) steps to install the 202X.X.X integration.

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
3.  Continue to the [Installation](https://github.com/beecho01/material-symbols/blob/main/README.md#installation) steps to install the 202X.X.X integration.
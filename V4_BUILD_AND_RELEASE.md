# Build and install V4
Same GitHub steps as V3. App ID is unchanged, so the APK installs over V3 and keeps your history (the plan is replaced on first start; the old plan is archived inside the app data).
1. Upload to your repository (replace existing files): `www` (now includes `plan_v4.js`), `android-overrides`, `package.json`, `capacitor.config.json`, `patch_manifest.py`, `BUILD-WORKFLOW.yml`, and the `V4_*` documents.
2. Replace `.github/workflows/build-apk.yml` with the text of the new `BUILD-WORKFLOW.yml` (it also sets versionName 4.0.0).
3. Actions tab: wait for the green tick, download `My-Workouts-V4-APK`, unzip, install `app-debug.apk` over V3.
4. First start: check the version label shows "Version 4" and the dashboard says the programme starts Mon 2 Nov 2026.
5. If something looks wrong, Backup in V3 first (More > Backup) so data can be restored.

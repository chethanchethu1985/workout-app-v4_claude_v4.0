# Workout App V4 - implementation report
Status: source package complete; Android APK NOT built or installed yet (build runs in your GitHub workflow). Everything below marked "tested" was tested in a desktop browser only.

## Features retained (V3 code kept, regression-tested in a browser)
Today screen and day strip, calendar, plan editor, Yoga and Cardio sessions, Workout Library (add/edit/remove, search), structured plan builder and saved templates, Excel template/import/export (optional columns), GIF/video tiles and YouTube/GIF search links, pre/post-workout and breathing hands-free sessions with transitions and next-exercise preview, manual main-workout player with set logging and rest timer, history/progress, local storage, Backup/Restore, Health Tracker, folder-sync card (Android plugin), settings. Not present in V3 and therefore not preserved: Health Connect, Google Fit and Fastrack integrations (never built; Progress showed "Not Connected" panels, removed in V3 final).

## Features enhanced
- Programme data: the old plan is replaced by the 8-week PDF plan, starting Monday 2 Nov 2026 (week/day mapping rewritten).
- Workout player: supersets, tri-sets and drop sets run round by round with the PDF rests; per-exercise "rest after"; per-side items rest 0 between Left and Right inside rounds; per-item breathing timings (in/hold/out/hold) with voice cues; instruction panel (primary/secondary muscles, difficulty, how-to, breathing, alternative, block note) on exercise screens; "arm"/"hand" per-side exercises split Left/Right.
- Calendar: week chips W1-W8 with completion, weekly summary table, Completed/Pending/Skipped status, month follows the selected week.
- Black theme, compact spacing, no horizontal overflow at 360, 412 and 768 px widths.

## New features
Dashboard (programme, week/day, today, next session, weekly and overall completion, cardio minutes, recovery day, latest health readings, day details), Programme guide in More (PDF overview text), V3-to-V4 data migration.

## Workout data imported
56 days, 2,720 items after Left/Right splitting (494 main exercises in 261 blocks, 240 warm-ups, 580 stretch holds from 288 stretches, 112 breathing, 24 cardio, 66 yoga). Details: V4_PDF_RECONCILIATION.md.

## Database changes
Same storage key as V3 (`myWorkouts.v3`) so V4 upgrades in place. On first start V4 sets `S.v4=1`, moves the old plan and dated overrides to `S.v3arch` (kept for recovery), loads the new plan, and keeps logs/history, custom library workouts, templates, settings and media links. Restoring an old V3 backup also triggers the migration. New plan fields: `blk`, `restAfter`, `tm`, `x` (reference to instruction data), `bn`, `tg`, `bth`, `when`, `how`, `cue`.

## Technical changes
`www/plan_v4.js` (plan + instruction data + guide text); `index.html` (theme, dashboard, calendar, engine patches, migration); `capacitor.config.json` appName "My Workouts V4" (app ID unchanged, so it installs over V3); `package.json` 4.0.0; workflow sets versionName 4.0.0 / versionCode 4 and artifact My-Workouts-V4-APK; V3 documents moved to docs/v3.

## Bugs found and fixed during V4 work
Start-up crash when the Health shell rendered before its settings existed; superset rest was applied between Left and Right sides; box-breathing timing text and a "max s" entry were mis-parsed; small-screen horizontal overflow on Library, More, Progress and Health tabs.

## Known limitations
No APK built yet; folder plugin not compiled against the real Android libraries; real Excel (.xlsx) import untested (library arrives in the build); Health Connect/Google Fit/Fastrack not available; no media (GIF/video) is bundled, you attach or sync your own; see the confirmation list in V4_PDF_RECONCILIATION.md.

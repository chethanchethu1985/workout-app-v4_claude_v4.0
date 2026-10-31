# V4 test report
Statuses: PASS / FAIL / BLOCKED / NOT TESTED. "PASS (browser)" = verified in headless Chromium on desktop, not on a phone.

| Area | Status | Evidence |
|---|---|---|
| All 8 weeks imported (56 days) | PASS (browser) | 56 days, 7 per week |
| Exercises match the PDF | PASS (automatic checks) | counts, word check and 86 prescription checks, see reconciliation |
| Programme dates | PASS (browser) | 30 Oct none; Mon 2 Nov = W1D1; Sun 8 Nov = W1D7 recovery; Mon 9 Nov = W2D1; Sun 27 Dec = W8D7; 28 Dec none |
| Old active plan removed | PASS (browser) | old plan and overrides absent after migration |
| History / custom workouts kept | PASS (browser) | simulated V3 data migrated, logs and library kept, old plan archived |
| Superset / tri-set rest timing | PASS (browser) | A no rest, B then 60 s; Left/Right no rest inside a round |
| Dashboard, calendar, weekly summary | PASS (browser) | rendered, screenshots reviewed |
| Black theme, no overflow | PASS (browser) | 360x640, 412x915, 768x1024: no sideways scroll |
| Earlier V3 features (library, plan builder, Excel optional columns with stubbed library, health tracker, history, folder card with mock plugin) | PASS (browser) | regression scripts re-run on V4 |
| Real-time timers over a full workout, voice cues | NOT TESTED | needs a phone |
| GIF/video playback, folder sync | NOT TESTED | needs a phone, plugin not built |
| Real .xlsx upload | NOT TESTED | library comes from the GitHub build |
| Android build, install, startup | NOT TESTED | run the GitHub workflow |
| Health Connect / Google Fit / Fastrack | NOT IMPLEMENTED | not in V3 |

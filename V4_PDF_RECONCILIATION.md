# V4 - PDF vs imported plan reconciliation
Source: 8_Week_Muscle_Gain_Programme.pdf, daily plans on pages 7-133 (56 days). Programme start Monday 2 November 2026; Day 56 = Sunday 27 December 2026.

## Automatic checks (all run, results real)
| Check | PDF | Imported | Result |
|---|---|---|---|
| Daily plans | 56 | 56 | match |
| Workout blocks (straight sets, supersets, tri-sets, drop sets) | 261 | 261 | match |
| Main exercises ("Primary:" entries) | 494 | 494 | match |
| Warm-up rows | 240 | 240 | match |
| Stretching rows | 288 | 288 rows (580 timed holds, because each "hold x N reps" becomes N holds) | match |
| Breathing rows | 112 | 112 | match |
| Cardio rows | 24 | 24 | match |
| Yoga rows | 66 | 66 | match |
| Exercise names: every word found on the exercise's own PDF day pages | - | 0 missing | match |
| Straight-set prescriptions ("N sets x reps" and "Rest between sets: X s") found verbatim in the PDF | 86 | 86 | 0 mismatches |
| Breathing: cycles x cycle length equals the stated minutes | 112 | 112 | match |

Parsing issues raised by the importer: 0 (two rule fixes were needed during development: box-breathing timing text and one "max s" entry).

## Not imported as schedule data
PDF Parts 4-6 (exercise variation matrix, muscle coverage matrix, tracking sheets, assessment sheet) and the duplicate-workout validation pages are reference/tracking material. Page 1-6 overview text and the page-134 progression summary are in the app under More > Programme guide.

## Items for your confirmation (not assumed silently)
1. The PDF cover says "Status: DRAFT FOR REVIEW. The Excel file ... will only be prepared after you approve this PDF." You described it as approved: please confirm this is the final version.
2. Week 6 Tuesday, Stage 3 Wall Sit shows the repetition value "max s". It is shown as "max hold (seconds)" with no countdown.
3. Stretches say "30 s hold x 2 reps (each side where applicable)". Imported as two holds per stretch (this matches the PDF's 8-minute estimate). Each-side repeats are not added automatically; the wording stays in the instructions.
4. Supersets, tri-sets and drop sets run round by round as the PDF describes (A, B, rest, repeat). Per-side exercises inside them do Left then Right with no rest, then the stated rest.
5. Straight-set exercises done per side run all Left sets, then all Right sets (the app's existing Left-then-Right flow).
6. The PDF gives rest between sets and rest after supersets, but not between separate blocks. The app default (More > rest between exercises, 90 s) is used there.
7. Rep ranges such as 10-12 are shown as written; the logging box starts at the top of the range.
8. Wednesday/Friday text says "15-20 min easy cardio" while the cardio table lists one duration (for example 15 min). The table value is used as the timer; the text is in Day details.

## Per-day counts (items as imported before left/right splitting)
| Day | Week | Weekday | Session | Warm-up | Main exercises | Stretch holds | Breathing | Cardio/Yoga |
|---|---|---|---|---|---|---|---|---|
| 1 | W1 | Monday | Chest and Back Foundation + Biceps + Upper Abs | 5 | 9 | 12 | 2 | 0 |
| 2 | W1 | Tuesday | Quadriceps, Adductors, Calves + Lower Abs | 5 | 7 | 12 | 2 | 0 |
| 3 | W1 | Wednesday | Shoulders and Arms + Obliques | 5 | 7 | 12 | 2 | 1 |
| 4 | W1 | Thursday | Hamstrings, Glutes, Calves + Deep Core | 5 | 6 | 13 | 2 | 0 |
| 5 | W1 | Friday | Back, Chest Support and Forearms + Biceps + De | 5 | 8 | 13 | 2 | 1 |
| 6 | W1 | Saturday | Arms, Legs, Chest-Lat Pump + Step-Board Cardio | 5 | 5 | 13 | 2 | 0 |
| 7 | W1 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 10 |
| 8 | W2 | Monday | Chest and Back (Upper Chest, Lat Focus) + Bice | 5 | 8 | 12 | 2 | 0 |
| 9 | W2 | Tuesday | Quadriceps Emphasis, Hips, Calves + Lower Abs | 5 | 7 | 12 | 2 | 0 |
| 10 | W2 | Wednesday | Shoulder Variations and Arms + Obliques | 5 | 7 | 13 | 2 | 1 |
| 11 | W2 | Thursday | Hamstrings and Glutes (Unilateral) + Deep Core | 5 | 6 | 12 | 2 | 0 |
| 12 | W2 | Friday | Back Thickness, Push-Up Strength and Forearms  | 5 | 9 | 12 | 2 | 1 |
| 13 | W2 | Saturday | Arms, Unilateral Legs, Shoulders + Step-Board  | 5 | 5 | 12 | 2 | 0 |
| 14 | W2 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 11 |
| 15 | W3 | Monday | Chest-Back Supersets + Biceps + Upper Abs | 5 | 12 | 12 | 2 | 0 |
| 16 | W3 | Tuesday | Quadriceps-Hamstring Supersets, Calves + Lower | 5 | 9 | 12 | 2 | 0 |
| 17 | W3 | Wednesday | Shoulder and Arm Supersets + Obliques | 5 | 10 | 12 | 2 | 1 |
| 18 | W3 | Thursday | Hamstring-Quad Supersets, Glutes, Calves + Dee | 5 | 9 | 11 | 2 | 0 |
| 19 | W3 | Friday | Back-Chest Supersets, Forearms + Biceps + Deep | 5 | 12 | 11 | 2 | 1 |
| 20 | W3 | Saturday | Arm Supersets, Legs, Press Variations + Step-B | 5 | 8 | 12 | 2 | 0 |
| 21 | W3 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 11 |
| 22 | W4 | Monday | Chest-Back Supersets (4 s Negatives) + Biceps  | 5 | 10 | 12 | 2 | 0 |
| 23 | W4 | Tuesday | Quadriceps Volume, Hamstring Supersets + Lower | 5 | 10 | 12 | 2 | 0 |
| 24 | W4 | Wednesday | Shoulders and Arms (Slow Eccentrics) + Oblique | 5 | 10 | 12 | 2 | 1 |
| 25 | W4 | Thursday | Hamstrings and Glutes (Slow Eccentrics) + Deep | 5 | 10 | 12 | 2 | 0 |
| 26 | W4 | Friday | Back-Chest Supersets, Forearms + Biceps + Deep | 5 | 12 | 12 | 2 | 1 |
| 27 | W4 | Saturday | Arm Supersets, Legs, Shoulders + Step-Board Ca | 5 | 8 | 12 | 2 | 0 |
| 28 | W4 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 9 |
| 29 | W5 | Monday | Intensity target: 1-2 RIR (last set of isolati | 5 | 14 | 12 | 2 | 0 |
| 30 | W5 | Tuesday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 0 |
| 31 | W5 | Wednesday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 1 |
| 32 | W5 | Thursday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 0 |
| 33 | W5 | Friday | Intensity target: 1-2 RIR (last set of isolati | 5 | 12 | 12 | 2 | 1 |
| 34 | W5 | Saturday | Intensity target: 1-2 RIR (last set of isolati | 5 | 10 | 12 | 2 | 0 |
| 35 | W5 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 9 |
| 36 | W6 | Monday | Intensity target: 1-2 RIR (last set of isolati | 5 | 14 | 11 | 2 | 0 |
| 37 | W6 | Tuesday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 0 |
| 38 | W6 | Wednesday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 1 |
| 39 | W6 | Thursday | Intensity target: 1-2 RIR (last set of isolati | 5 | 11 | 12 | 2 | 0 |
| 40 | W6 | Friday | Intensity target: 1-2 RIR (last set of isolati | 5 | 12 | 12 | 2 | 1 |
| 41 | W6 | Saturday | Intensity target: 1-2 RIR (last set of isolati | 5 | 10 | 12 | 2 | 0 |
| 42 | W6 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 8 |
| 43 | W7 | Monday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 16 | 12 | 2 | 0 |
| 44 | W7 | Tuesday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 12 | 2 | 0 |
| 45 | W7 | Wednesday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 12 | 12 | 2 | 1 |
| 46 | W7 | Thursday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 12 | 2 | 0 |
| 47 | W7 | Friday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 15 | 12 | 2 | 1 |
| 48 | W7 | Saturday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 13 | 2 | 0 |
| 49 | W7 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 9 |
| 50 | W8 | Monday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 16 | 13 | 2 | 0 |
| 51 | W8 | Tuesday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 12 | 2 | 0 |
| 52 | W8 | Wednesday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 12 | 13 | 2 | 1 |
| 53 | W8 | Thursday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 12 | 2 | 0 |
| 54 | W8 | Friday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 15 | 12 | 2 | 1 |
| 55 | W8 | Saturday | Intensity target: 1-2 RIR (Week 8: 2 RIR, volu | 5 | 11 | 12 | 2 | 0 |
| 56 | W8 | Sunday | Active Recovery: Cardio, Full-Body Yoga and Br | 0 | 0 | 0 | 2 | 7 |

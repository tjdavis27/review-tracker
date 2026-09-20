# Escape Room Review Tracker v2.2.2 - Rating Fix

## What changed

`Add Review` now asks for the star rating.

- 5 stars: Florence Google total +1 and selected employees receive +1 weekly/payroll/overall 5-star credit.
- 4, 3, 2, or 1 star: Florence Google total +1 and no employee 5-star credit is added.

The change history records the actual rating.

## Existing data is preserved

This build intentionally keeps the exact same browser storage key:

`escapeRoomReviewTracker.v213`

It also keeps the same Supabase configuration, table, tracker key, and state structure.
No totals, employees, location data, archives, or history are reset or converted.

For extra protection, the first load creates a separate one-time local safety snapshot at:

`escapeRoomReviewTracker.preRatingFixBackup.v222`

The safety snapshot is never used as the active tracker and does not overwrite existing data.

## Clarified labels

Employee totals are now explicitly described as 5-star review credit.
Florence and location Google totals still represent all actual Google reviews regardless of rating.

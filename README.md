# Escape Room Review Tracker v2.2.4

## Correct review-counting rule

The tracker now separates the actual Google review total from 5-star competition
credit.

### Any Google review (1-5 stars)
- Florence Total Reviews +1

### 5-star review only
- Florence 5-Star Reviews This Week +1
- Selected employee Weekly +1
- Selected employee Payroll +1
- Selected employee Overall +1
- Selected employee competition credit +1

### 4-star or lower
- Florence Total Reviews +1
- Florence 5-Star Reviews This Week does NOT change
- Employee Weekly does NOT change
- Employee Payroll does NOT change
- Employee Overall does NOT change
- Employee credit does NOT change

## Labels

`Florence Total Reviews` means ALL Google reviews.

Weekly/payroll/overall employee counts remain 5-star competition counts.

## Existing data is preserved

This version keeps the exact same:
- localStorage key: `escapeRoomReviewTracker.v213`
- Supabase tracker key: `florence-review-tracker`
- employee, location, history, archive, and total structures

A new optional `fiveStarWeek` field is added non-destructively to the existing
Florence state so lower-rated reviews can increase the overall total without
increasing the weekly 5-star count.

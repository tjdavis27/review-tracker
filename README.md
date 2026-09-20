# Escape Room Review Tracker v2.2.5

## Fixed: lower-rated reviews increasing the weekly 5-star count

The weekly 5-star number is now a completely separate counter.

### Any Google review
- Florence Total Reviews +1

### 5-star review
- Florence Total Reviews +1
- Florence 5-Star Reviews This Week +1
- Selected employee Weekly +1
- Selected employee Payroll +1
- Selected employee Overall +1

### 1-4 star review
- Florence Total Reviews +1
- Florence 5-Star Reviews This Week does NOT change
- Employee Weekly does NOT change
- Employee Payroll does NOT change
- Employee Overall does NOT change

## Existing data is preserved and current week is repaired

The app keeps the exact same localStorage and Supabase keys.

On first load of v2.2.5, it performs a non-destructive one-time repair:
- Starts with the existing all-review gain for the current week.
- Finds lower-rated reviews already logged during the current week.
- Subtracts only those lower-rated reviews from the new 5-star weekly counter.

It does not reset the Florence total, employee totals, locations, history,
archives, payroll counts, or overall counts.

## Weekly reset

Start New Week now archives:
- Florence 5-star reviews gained
- Florence total reviews gained

Then only the 5-star weekly counter is reset to zero. The overall Google total
continues normally.

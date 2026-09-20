# Escape Room Review Tracker v2.2.3

## Five-star-only competition fix

Only 5-star reviews count toward tracker totals.

### 5-star review
- Florence 5-Star Total +1
- Florence 5-Star Reviews This Week +1
- Selected employees: Weekly +1
- Selected employees: Payroll +1
- Selected employees: Overall +1

### 4-star or lower
- Florence total does not change
- Reviews This Week does not change
- Employee Weekly does not change
- Employee Payroll does not change
- Employee Overall does not change
- Competition progress does not change

A lower-rated review is only written to History as `Not Counted` so it can be
noted without affecting any numbers.

## Existing data is preserved

This release intentionally keeps the exact same:
- localStorage data key: `escapeRoomReviewTracker.v213`
- Supabase tracker key: `florence-review-tracker`
- state/data schema

No totals, employees, history, archives, locations, or existing records are
cleared or migrated.

If a lower-rated review was already added in v2.2.2, v2.2.3 will not silently
alter your existing totals. Use Undo (if still available) or subtract that one
review manually from Florence once.

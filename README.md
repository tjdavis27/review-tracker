# Escape Room Review Tracker v2.2.1

## Fix in this version

The browser reserves `location` as a global name (`window.location`).

v2.2.0 also declared a helper named `location()`, which caused:

`Uncaught SyntaxError: Identifier 'location' has already been declared`

v2.2.1 renames that helper to `getLocation()` everywhere.

## Test

1. Close old tracker test windows.
2. Extract the ZIP.
3. Double-click `TEST-LOCAL.bat`.
4. It opens on:
   `http://127.0.0.1:8878/?v=221`

The page should show:

`JavaScript is running. Buttons are active.`

If a browser error still occurs, the red error box will show the exact message.

## GitHub

Once confirmed working, upload `index.html`.
Your Supabase URL and publishable key remain embedded.

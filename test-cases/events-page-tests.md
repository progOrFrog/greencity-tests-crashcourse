# Test Cases for GreenCity Events Page

---

## TC-01: Switching event display mode (Grid/List view)
**Description:** Verifies that a user can successfully toggle the layout of the events list between grid view and list view.

**Priority:** Medium

**Prerequisites:** - The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
- The event list is fully loaded and contains at least two events.

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click on the `List view` icon (the button with three horizontal lines) located in the top right corner above the event cards. | - | The layout changes. Events are displayed sequentially in a vertical list format. |
| 2 | Click on the `Grid view` icon (the button with four small squares) located next to the list view icon. | - | The layout reverts. Events are displayed in a grid format with multiple cards per row. |

---

## TC-02: Viewing detailed information about an event
**Description:** Verifies that a user can navigate to the event details page to view comprehensive information about a specific event.

**Priority:** High

**Prerequisites:** - The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
- At least one event card is displayed on the page.

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Locate any event card (e.g., "Some Event") and click the `More` button at the bottom of the card. | - | The system redirects the user to the event details page. Full information (description, location, time, organizer) is successfully displayed. |

---

## TC-03: Filtering events by status
**Description:** Verifies that the filter functionality correctly updates the event list to show only events matching the selected status.

**Priority:** High

**Prerequisites:** - The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
- The event list contains events with different statuses (e.g., Open, Closed).

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | In the `Filter` section, click on the `Status` dropdown menu to expand it. | - | A dropdown list with available statuses is displayed. |
| 2 | Select the checkbox next to the `Open` status. | - | The page dynamically reloads the event list. Only events with the `Open` status badge are displayed in the results. |

---

## TC-04 (Negative): Attempting to create an event as an unauthorized user
**Description:** Verifies that an unauthenticated user is restricted from accessing the event creation functionality.

**Priority:** High

**Prerequisites:** - The user is **NOT** logged into the system (guest state).
- The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click the `Create event` button located in the top right area of the page. | - | The user is not redirected to the event creation form. A modal window appears prompting the user to sign in or sign up to proceed. |

---

## TC-05 (Negative): Filtering events with no matching results
**Description:** Verifies that the system correctly handles and displays an appropriate message when the applied filter criteria result in zero matching events.

**Priority:** Medium

**Prerequisites:** - The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
- The event list is loaded.

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | In the `Filter` section, click on the `Date range` filter to expand it. | - | A calendar or date selection tool is displayed. |
| 2 | Select a specific narrow date range in the past (or far future) where no events are scheduled. | - | The event list is cleared. The system displays a user-friendly message indicating that no events were found (e.g., "0 items found" or "No events matching your search criteria"). |

---

## TC-06: Applying multiple filters and using the "Reset all" function
**Description:** Verifies that a user can apply multiple filters simultaneously to narrow down the search and then successfully clear all applied filters using the "Reset all" button.
**Priority:** Medium
**Prerequisites:** - The user is on the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
- The event list is fully loaded and displays the total number of items (e.g., "25 items found").

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | In the `Filter` section, click on the `Type` dropdown and select a specific category. | - | The event list updates to display only events categorized as "Social". |
| 2 | Click on the `Status` dropdown and select a specific status. | - | The event list updates further. It now displays only events that are BOTH "Social" AND "Open". |
| 3 | Click the `Reset all` button located to the right of the filter options. | - | All applied filters are cleared. The event list resets to its default state, displaying all available events again. |

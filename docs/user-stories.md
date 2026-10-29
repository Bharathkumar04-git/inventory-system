# User Stories

## v1 - Add Stock
**US1:** As a shop owner, I want to add a new item with its name, quantity and price, so that I can keep my stock records.
- Acceptance: item appears in the stock table after submitting
- Acceptance: empty name or negative quantity is rejected

## v2 - Update Stock
**US2:** As a shop owner, I want to change the quantity of an existing item, so that my stock stays correct after sales or purchases.
- Acceptance: new quantity is shown in the table
- Acceptance: quantity cannot be negative

## v3 - Low Stock Alert
**US3:** As a shop owner, I want to see an alert for items with low stock, so that I can reorder them in time.
- Acceptance: items with quantity below 10 are shown in the alert list
- Acceptance: items with enough stock are not shown in the alert list
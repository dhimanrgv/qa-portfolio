# Test Cases -- SauceDemo Application
Author: dhimanrgv | Version: 1.0 | Date: 2021-06-24

## Login Module
| TC ID | Scenario | Expected Result | Priority | Status |
|---|---|---|---|---|
| TC-LGN-001 | Valid login | Redirect to /inventory.html | P1 | PASS |
| TC-LGN-002 | Locked out user | Error message displayed | P1 | PASS |
| TC-LGN-003 | Empty username | Username required error | P2 | PASS |
| TC-LGN-004 | Empty password | Password required error | P2 | PASS |
| TC-LGN-005 | Wrong password | Error message displayed | P2 | PASS |
| TC-LGN-006 | Dismiss error | Banner disappears | P3 | PASS |

## Inventory Module
| TC ID | Scenario | Expected Result | Priority | Status |
|---|---|---|---|---|
| TC-INV-001 | Product count | Exactly 6 products | P1 | PASS |
| TC-INV-002 | All prices positive | Price > $0 for all | P1 | PASS |
| TC-INV-003 | Sort A to Z | Ascending alphabetical | P2 | PASS |
| TC-INV-004 | Sort Z to A | Descending alphabetical | P2 | PASS |

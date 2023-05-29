# Requirement Traceability Matrix (RTM)
Project: SauceDemo | Author: dhimanrgv | Version: 2.0 | Updated: 2023-05-29

| Req ID | Requirement | Priority | Test Cases | Status | Defect |
|---|---|---|---|---|---|
| REQ-001 | Valid login redirects to inventory | P1 | TC-LGN-001 | PASS | -- |
| REQ-002 | Locked-out user sees error | P1 | TC-LGN-002 | PASS | -- |
| REQ-003 | Empty username validation | P2 | TC-LGN-003 | PASS | -- |
| REQ-004 | Empty password validation | P2 | TC-LGN-004 | PASS | -- |
| REQ-005 | Wrong password shows error | P2 | TC-LGN-005 | PASS | -- |
| REQ-006 | Error banner dismissible | P3 | TC-LGN-006 | PASS | -- |
| REQ-007 | Products page shows 6 items | P1 | TC-INV-001 | PASS | -- |
| REQ-008 | All products have valid prices | P1 | TC-INV-002 | PASS | -- |
| REQ-009 | Sort A to Z works correctly | P2 | TC-INV-003 | PASS | -- |
| REQ-010 | Sort Z to A works correctly | P2 | TC-INV-004 | PASS | -- |
| REQ-011 | Sort price low to high | P2 | TC-INV-005 | PASS | -- |
| REQ-012 | Sort price high to low | P2 | TC-INV-006 | PASS | -- |
| REQ-013 | Add to cart updates badge | P1 | TC-INV-007 | PASS | -- |
| REQ-014 | Cart persists items | P1 | TC-CRT-001 | PASS | BUG-002 |
| REQ-015 | Remove item from cart | P1 | TC-CRT-002 | PASS | -- |
| REQ-016 | Checkout form validates fields | P1 | TC-CHK-001,002,003 | PASS | -- |
| REQ-017 | Zip code format validation | P2 | TC-CHK-004 | FAIL | BUG-004 |
| REQ-018 | Order summary shows correct total | P1 | TC-CHK-005 | PASS | -- |
| REQ-019 | Order confirmation on success | P1 | TC-CHK-006 | PASS | -- |
| REQ-020 | Problem user sees correct images | P2 | TC-INV-008 | FAIL | BUG-001 |

## Coverage Summary
| Status | Count | % |
|---|---|---|
| PASS | 18 | 90% |
| FAIL | 2 | 10% |
| **Total** | **20** | |

## Sign-off
| Role | Name | Date |
|---|---|---|
| QA Lead | dhimanrgv | 2023-05-29 |

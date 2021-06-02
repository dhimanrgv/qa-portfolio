# Test Plan: Login Module
Version: 1.0 | Author: dhimanrgv | Date: 2021-06-02

## Scope
- Valid login for all user roles
- Invalid credential handling
- Empty field validation

## Test Cases
| TC ID | Description | Priority |
|---|---|---|
| TC-LGN-001 | Valid login - standard_user | P1 |
| TC-LGN-002 | Locked out user error | P1 |
| TC-LGN-003 | Empty username error | P2 |
| TC-LGN-004 | Empty password error | P2 |
| TC-LGN-005 | Wrong password error | P2 |
| TC-LGN-006 | Error banner dismissal | P3 |

## Entry Criteria
Application deployed to staging, test data seeded.
## Exit Criteria
All P1/P2 cases pass, no open Critical/High bugs.

# Bug Report Log
Project: SauceDemo QA | Tester: dhimanrgv

## BUG-001: Problem user images fail to load
Severity: Medium | Priority: P2 | Status: Open | Found: 2021-07-07
Steps: Login as problem_user, view inventory. Expected: images load. Actual: broken.

## BUG-002: Cart badge not cleared after order completion
| Field | Detail |
|---|---|
| Severity | High | Priority | P1 |
| Status | Fixed v2.1 | Found | 2021-08-10 |

**Steps:**
1. Add 3 items, complete full checkout, click Back Home
2. Observe cart icon badge

**Expected:** Badge shows 0.
**Actual:** Badge still shows 3.
**Root Cause:** Cart state not cleared from localStorage on ORDER_COMPLETE.
**Fix:** Cleared on order completion dispatch. Verified in v2.1.

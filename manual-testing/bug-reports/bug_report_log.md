# Bug Report Log
Project: SauceDemo & API QA | Tester: dhimanrgv | Updated: 2023-02-20

## BUG-001 | problem_user images broken      | Medium | P2 | Open
## BUG-002 | cart badge after order           | High   | P1 | Fixed v2.1
## BUG-003 | sort reset on refresh            | Low    | P3 | Won't Fix
## BUG-004 | zip accepts special chars        | Medium | P2 | Open
## BUG-005 | performance glitch blank screen  | Medium | P2 | Known/By Design

## BUG-006: DELETE /booking returns HTTP 201 instead of 200/204
Severity: Low | Priority: P3 | Status: Open | Found: 2023-01-10
Module: API / Booking endpoint

Summary: DELETE /booking/{id} returns 201 (Created) on success.
Expected: 200 (OK) or 204 (No Content) per REST standards.
Actual: 201 returned -- semantically incorrect.
Impact: Clients checking for 200/204 will incorrectly treat deletion as failed.

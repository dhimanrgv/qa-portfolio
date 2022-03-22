# Bug Report Log
Project: SauceDemo QA | Tester: dhimanrgv

## BUG-001: Problem user images fail to load
Severity: Medium | Priority: P2 | Status: Open | Found: 2021-07-07

## BUG-002: Cart badge not cleared after order completion
Severity: High | Priority: P1 | Status: Fixed v2.1 | Found: 2021-08-10
Root Cause: Cart state not cleared from localStorage on ORDER_COMPLETE.

## BUG-003: Sort dropdown resets on page refresh
Severity: Low | Priority: P3 | Status: Won't Fix | Found: 2022-01-11
Sort is intentionally session-only per product spec.

## BUG-004: Checkout zip code accepts special characters
Severity: Medium | Priority: P2 | Status: Open | Found: 2022-03-22
Steps: Checkout with Zip=!@#$% -- no validation error, proceeds to step 2.
Risk: Could cause downstream payment/shipping API failures.

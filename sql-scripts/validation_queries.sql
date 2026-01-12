-- =================================================================
-- sql-scripts/validation_queries.sql  v2.0
-- Backend data validation queries for QA testing.
-- Updated 2026-01-12 with session and RTM queries.
-- =================================================================

-- 1. Retrieve all active users
SELECT user_id, username, email, status, created_at
FROM users WHERE status = 'active' ORDER BY created_at DESC;

-- 2. Verify newly registered user exists
SELECT COUNT(*) AS user_count
FROM users WHERE email = 'testuser@example.com' AND status = 'active';

-- 3. Validate order with JOIN
SELECT o.order_id, o.total_amount, o.status, u.username
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
WHERE o.order_id = 1001 AND o.status = 'completed';

-- 4. Cart items with product details
SELECT ci.product_id, p.product_name, ci.quantity,
       ci.unit_price, (ci.quantity * ci.unit_price) AS line_total
FROM cart_items ci
INNER JOIN products p ON ci.product_id = p.product_id
WHERE ci.cart_id = 555;

-- 5. Orders per user (GROUP BY)
SELECT u.username, COUNT(o.order_id) AS orders, SUM(o.total_amount) AS total_spent
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.username
HAVING COUNT(o.order_id) > 0
ORDER BY total_spent DESC;

-- 6. Orders missing payment records (defect check)
SELECT o.order_id, o.user_id, o.total_amount
FROM orders o
LEFT JOIN payments p ON o.order_id = p.order_id
WHERE p.payment_id IS NULL AND o.status != 'cancelled';

-- 7. Session validation
SELECT s.session_id, u.username, s.created_at, s.expires_at
FROM sessions s
INNER JOIN users u ON s.user_id = u.user_id
WHERE s.created_at >= NOW() - INTERVAL '1 hour' AND s.is_active = TRUE;

-- 8. RTM test results linked to requirements
SELECT r.requirement_id, r.requirement_name, t.test_name, t.status
FROM requirements r
INNER JOIN test_cases t ON r.requirement_id = t.requirement_id
WHERE t.status IN ('FAIL', 'BLOCKED')
ORDER BY r.requirement_id;

-- 9. Cleanup stale test data (TEST ENV ONLY)
DELETE FROM test_users
WHERE created_at < NOW() - INTERVAL '7 days' AND username LIKE 'test_%';

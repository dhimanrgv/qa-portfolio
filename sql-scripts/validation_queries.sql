-- =================================================================
-- sql-scripts/validation_queries.sql
-- Backend data validation queries for QA testing.
-- Demonstrates: SELECT, WHERE, ORDER BY, GROUP BY, JOIN, subqueries.
-- =================================================================

-- 1. Retrieve all active users
SELECT user_id, username, email, status, created_at
FROM users
WHERE status = 'active'
ORDER BY created_at DESC;

-- 2. Verify newly registered user exists
SELECT COUNT(*) AS user_count
FROM users
WHERE email = 'testuser@example.com' AND status = 'active';

-- 3. Validate order with correct total (INNER JOIN)
SELECT o.order_id, o.user_id, o.total_amount, o.status, u.username
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
WHERE o.order_id = 1001 AND o.status = 'completed';

-- 4. Check cart items match expected products
SELECT ci.product_id, p.product_name, ci.quantity,
       ci.unit_price, (ci.quantity * ci.unit_price) AS line_total
FROM cart_items ci
INNER JOIN products p ON ci.product_id = p.product_id
WHERE ci.cart_id = 555;

-- 5. Count orders per user (GROUP BY + HAVING)
SELECT u.username,
       COUNT(o.order_id)   AS total_orders,
       SUM(o.total_amount) AS total_spent,
       AVG(o.total_amount) AS avg_order_value
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.username
HAVING COUNT(o.order_id) > 0
ORDER BY total_spent DESC;

-- 6. Find orders missing payment records (defect validation)
SELECT o.order_id, o.user_id, o.total_amount, o.created_at
FROM orders o
LEFT JOIN payments p ON o.order_id = p.order_id
WHERE p.payment_id IS NULL AND o.status != 'cancelled';

-- 7. Price integrity check
SELECT product_id, product_name, price
FROM products WHERE price <= 0;

-- 8. Cleanup stale test data (TEST ENV ONLY -- never run in production)
DELETE FROM test_users
WHERE created_at < NOW() - INTERVAL '7 days' AND username LIKE 'test_%';

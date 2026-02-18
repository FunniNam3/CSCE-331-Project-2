
/* Query 1: Total orders by week */
SELECT COUNT(*) AS total_orders FROM receipt WHERE EXTRACT(WEEK FROM purchase_date) = 1;

/* Query 2: Top 10 sales */
SELECT 
    r.purchase_date,
    SUM(d.price) + COALESCE(SUM(f.price), 0) AS total_sales
FROM receipt r
LEFT JOIN drink_to_receipt dtr ON r.id = dtr.receipt_id
LEFT JOIN drink d ON dtr.drink_id = d.id
LEFT JOIN food_to_receipt ftr ON r.id = ftr.receipt_id
LEFT JOIN food f ON ftr.food_id = f.id
GROUP BY r.purchase_date
ORDER BY total_sales DESC
LIMIT 10;

/* Query 3: sales by hour */
SELECT 
    EXTRACT(HOUR FROM r.purchase_date) AS hour_of_day,
    COUNT(DISTINCT r.id) AS total_orders,
    SUM(d.price) + COALESCE(SUM(f.price), 0) AS total_sales
FROM receipt r
LEFT JOIN drink_to_receipt dtr ON r.id = dtr.receipt_id
LEFT JOIN drink d ON dtr.drink_id = d.id
LEFT JOIN food_to_receipt ftr ON r.id = ftr.receipt_id
LEFT JOIN food f ON ftr.food_id = f.id
GROUP BY hour_of_day
ORDER BY hour_of_day;

/* Query 4 */
SELECT * FROM menu_usage_summary;
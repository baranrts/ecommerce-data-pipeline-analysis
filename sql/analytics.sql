-- 1. En Çok Ciro Yapan İlk 10 Ürün Kategorisi
SELECT 
    p.product_category_name AS kategori,
    COUNT(oi.order_id) AS toplam_siparis_adeti,
    ROUND(SUM(oi.price)::numeric, 2) AS toplam_ciro
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE p.product_category_name IS NOT NULL
GROUP BY p.product_category_name
ORDER BY toplam_ciro DESC
LIMIT 10;

-- 2. En Çok Harcama Yapan İlk 10 Eyalet (Coğrafi Analiz)
SELECT 
    c.customer_state AS eyalet,
    COUNT(DISTINCT o.order_id) AS toplam_siparis,
    ROUND(SUM(op.payment_value)::numeric, 2) AS toplam_harcama
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_payments op ON o.order_id = op.order_id
GROUP BY c.customer_state
ORDER BY toplam_harcama DESC
LIMIT 10;

-- 3. Müşterilerin Tercih Ettiği Ödeme Yöntemleri
SELECT 
    payment_type AS odeme_tipi,
    COUNT(*) AS islem_sayisi,
    ROUND(SUM(payment_value)::numeric, 2) AS toplam_tutar,
    ROUND(AVG(payment_installments), 1) AS ortalama_taksit
FROM order_payments
GROUP BY payment_type
ORDER BY islem_sayisi DESC;
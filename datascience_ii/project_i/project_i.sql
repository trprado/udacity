-- 1.
SELECT
    BillingCountry,
    COUNT(*) AS Invoices
FROM Invoice
GROUP BY 1
ORDER BY 2 DESC;

-- 2.
SELECT
    BillingCity,
    SUM(Total) AS city_total
FROM Invoice
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- 3.
SELECT
    cus.CustomerId,
    cus.FirstName || ' ' || cus.LastName AS full_name,
    SUM(inv.Total) AS total_usd
FROM Customer AS cus
JOIN Invoice as inv
ON inv.CustomerId == cus.CustomerId
GROUP BY 2
ORDER BY 3 DESC
LIMIT 1;

-- 4.
SELECT
    cus.Email,
    cus.FirstName,
    cus.LastName,
    gen.Name AS genre_music
FROM Customer AS cus
JOIN Invoice AS inv
ON inv.CustomerId = cus.CustomerId
JOIN InvoiceLine AS inl
ON inl.InvoiceId = inv.InvoiceId
JOIN Track AS tr
ON tr.TrackId == inl.TrackId
JOIN Genre AS gen
ON tr.GenreId = gen.GenreId
WHERE gen.Name = 'Rock'
GROUP BY 1
ORDER BY 1;

-- 5.
SELECT
    art.ArtistId,
    art.Name,
    COUNT(*) AS Songs
FROM Artist AS art
JOIN Album AS alb
ON alb.ArtistId = art.ArtistID
JOIN Track as tr
ON tr.AlbumId = alb.AlbumId
JOIN Genre AS gen
ON tr.GenreId = gen.GenreId
WHERE gen.Name = 'Rock'
GROUP BY art.Name
ORDER BY 3 DESC;

-- 6.
-- Part 1
SELECT
    art.Name,
    SUM(inl.Quantity * inl.UnitPrice) AS AmountSpent
FROM Artist AS art
JOIN Album AS alb
ON alb.ArtistId = art.ArtistId
JOIN Track AS tr
ON tr.AlbumId = alb.AlbumId
JOIN InvoiceLine AS inl
ON inl.TrackId = tr.TrackId
GROUP BY 1
ORDER BY 2 DESC;

-- Part 2
SELECT
    art.Name,
    SUM(inl.Quantity * inl.UnitPrice) AS AmountSpent,
    cus.CustomerId,
    cus.FirstName,
    cus.LastName
FROM Artist AS art
JOIN Album AS alb
ON alb.ArtistId = art.ArtistId
JOIN Track AS tr
ON tr.AlbumId = alb.AlbumId
JOIN InvoiceLine AS inl
ON inl.TrackId = tr.TrackId
JOIN Invoice AS inv
ON inl.InvoiceId = inv.InvoiceId
JOIN Customer AS cus
ON inv.CustomerId = cus.CustomerId
WHERE art.Name = 'Iron Maiden'
GROUP BY 3
ORDER BY 2 DESC;

-- 7.
WITH purchases AS (
    SELECT
        COUNT(*) AS Purchases,
        cus.Country,
        gen.Name,
        gen.GenreId
    FROM Customer AS cus
    JOIN Invoice AS inv
    ON inv.CustomerId = cus.CustomerId
    JOIN InvoiceLine AS inl
    ON inl.InvoiceId = inv.InvoiceId
    JOIN Track AS trk
    ON trk.TrackId = inl.TrackId
    JOIN Genre AS gen
    ON gen.GenreId = trk.GenreID
    GROUP BY 2, 3
    ORDER BY 1 DESC
), max_pur AS (
    SELECT
        MAX(pur.Purchases) as max_pur,
        pur.Country
    FROM purchases AS pur
    GROUP BY pur.Country
)

SELECT
    pur.Purchases,
    pur.Country,
    pur.Name,
    pur.GenreId
FROM purchases AS pur
JOIN max_pur AS mpur
ON mpur.Country = pur.Country
AND mpur.max_pur = pur.Purchases
ORDER BY pur.Country

-- 8.
WITH music_avg_time AS (
    SELECT
        AVG(Milliseconds) as avg_time
    FROM Track
)

SELECT
    Name,
    Milliseconds
FROM Track
JOIN music_avg_time
WHERE Milliseconds > avg_time
ORDER BY 2 DESC

-- 9.
WITH total_spend AS (
    SELECT
        cus.Country,
        SUM(inv.Total) AS TotalSpend,
        cus.FirstName,
        cus.LastName,
        cus.CustomerId
    FROM Customer AS cus
    LEFT JOIN Invoice AS inv
    ON inv.CustomerId = cus.CustomerId
    GROUP BY 5
), max_spend AS (
    SELECT
        MAX(ts.TotalSpend) as max_spend,
        ts.Country
    FROM total_spend AS ts
    GROUP BY 2
)

SELECT
    ts.Country,
    ts.TotalSpend,
    ts.FirstName,
    ts.LastName,
    ts.CustomerId
FROM total_spend AS ts
JOIN max_spend AS ms
ON ts.Country = ms.Country
AND ts.TotalSpend = ms.max_spend
ORDER BY 1
# Write your MySQL query statement below
SELECT DISTINCT
    NULLIF(email, null) AS Email
FROM (
    SELECT
        email,
        COUNT(email) OVER (PARTITION BY email) checke
    FROM Person
)t  WHERE checke > 1

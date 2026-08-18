# Write your MySQL query statement below
DELETE p1
FROM Person p1
INNER JOIN Person p2 
ON p1.email = p2.email   -- Match rows with duplicate emails
AND p1.id > p2.id;        -- Keep the smaller ID, delete the larger ID



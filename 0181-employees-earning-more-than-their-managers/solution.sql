# Write your MySQL query statement below
SELECT
E.name AS Employee
FROM Employee AS E
INNER JOIN Employee AS A
ON E.managerID = A.id
WHERE E.salary > A.salary


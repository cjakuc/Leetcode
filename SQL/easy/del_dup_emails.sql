-- Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id is the primary key column for this table.

-- For example, after running your query, the above Person table should have the following rows:

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+

-- Note:

-- Your output is the whole Person table after executing your sql. Use delete statement.

-- Write your MySQL query statement below

WITH min_id_tbl AS (
SELECT
    p.Email,
    MIN(p.Id) AS min_id
FROM Person AS p
GROUP BY
    p.Email
)

DELETE p
FROM Person AS p
INNER JOIN min_id_tbl AS mit ON mit.Email = p.Email
WHERE
    mit.min_id != p.Id
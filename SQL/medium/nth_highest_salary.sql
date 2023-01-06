-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.      
      WITH ranked_salaries AS(
          SELECT
            e.Salary,
            RANK() OVER (
                ORDER BY e.Salary DESC
            ) AS sal_rank
          FROM Employee AS e
          GROUP BY
            e.Salary
      )
      SELECT
        rs.Salary
      FROM ranked_salaries AS rs
      WHERE rs.sal_rank = N
  );
END
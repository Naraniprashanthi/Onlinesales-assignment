
----imported excel to server----

select top 3 
d.NAME as DEPT_NAME,
AVG(s.[AMT (USD)]) as AVG_MONTHLY_SALARY
from Employees$ e 
join Departments$ d on e.[DEPT ID] = d.ID
join Salaries$ s on e.ID = s. EMP_ID
GROUP BY d.NAME
ORDER BY AVG_MONTHLY_SALARY DESC
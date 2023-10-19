import pandas as pd

departments = pd.read_csv('Departments.csv', sep='\t')
departments = departments.reset_index(drop=True)
employees = pd.read_csv('Employees.csv', sep='\t')
salaries = pd.read_csv('Salaries.csv', sep='\t')

employeeSalary = employees.merge(salaries, left_on='ID', right_on='EMP_ID')

departmentSalary = employeeSalary.merge(departments, left_on='DEPT ID', right_on='ID')
avgeSalary_by_dept = departmentSalary.groupby('NAME_x')['AMT (USD)'].mean().reset_index()
avgeSalary_by_dept.rename(columns={'NAME_x': 'DEPT_NAME', 'AMT (USD)': 'AVG_MONTHLY_SALARY (USD)'}, inplace=True)

top_3_dep = avgeSalary_by_dept.sort_values(by='AVG_MONTHLY_SALARY (USD)', ascending=False).head(3)

print(top_3_dep)


use hr;
# выведите номера отделов и количество сотрудников в каждом отделе, где сотрудников больше 10

SELECT  
department_id, count(*) as amount
FROM employees
group by department_id
having amount > 10
;

SELECT t1.department_name, t2.amount
FROM departments t1
JOIN (
SELECT  department_id, count(*) as amount
FROM employees
group by department_id
having amount > 10
) t2
ON t1.department_id = t2.department_id
;

# найти максимальную зарплату в каждом департаменте. Вывести department_id и max_salary.
SELECT department_id, max(salary) as max_salary
from employees
group by department_id
having max_salary > 10000
;

# Найти сотрудников, у которых наибольшая зарплата в их департаменте

select t1.first_name, t1.last_name, t2.max_salary
from employees t1
join(
SELECT department_id, max(salary) as max_salary
from employees
group by department_id
) t2
on t1.department_id = t2.department_id
and t1.salary = t2.max_salary
;
select department_name
from departments t1
join
(select department_id, count(*) as count_ 
from employees
group by department_id
order by count_ desc
limit 1) t2
on t1.department_id = t2.department_id
;
# Tatubalin
select department_name, count(*) as count_
from employees
join departments
on departments.department_id = employees.department_id
group by department_name
order by count_ desc
limit 1
;
# Tatubalin
select department_name, count(*) as count_
from employees
join departments
on departments.department_id = employees.department_id
group by department_name
having count_ > 10; 

/*Найти департаменты, в которых больше 10 сотрудников*/
select t1.department_name, t2.department_id, count_
from departments t1
join 
(select department_id, count(*) as count_
from employees
group by department_id
having count_ > 10) t2
on t2.department_id = t1.department_id
;


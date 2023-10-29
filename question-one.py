use dummydb;
select *
from employees;

select *
from jobs;

select employees.first_name, jobs.job_title
from employees, jobs
where employees.job_id=jobs.job_id;
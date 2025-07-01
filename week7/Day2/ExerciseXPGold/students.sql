-- Continuation of the Exercise XP +

-- Select
-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

-- Fetch the first four students. You have to order the four students alphabetically by last_name.
select first_name, last_name, birth_date
from students
order by last_name ASC
limit 4

-- Fetch the details of the youngest student.
select *
from students
order by birth_date desc 
limit 1

-- Fetch three students skipping the first two students.
select * 
from students 
limit 3 offset 2
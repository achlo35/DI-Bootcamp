-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

create table actors(
  actor_id varchar(50) primary key,
  first_name varchar(50) not null,
  last_name varchar(100),
  age date,
  number_oscars smallint
);

insert into actors
values
('1', 'Matt', 'Damon', '1970-08-10', 5),
('2', 'George', 'Clooney', '1961-06-05', 2),
('3', 'Angelina', 'Jolie', '1975-06-04', 1),
('4', 'Jennifer', 'Aniston', '1969-02-11', 0);

SELECT COUNT(*) as total_actors
FROM actors;

insert into actors 
values
('5', 'Leonardo', 'DiCaprio', '1974-11-11', 1),
('6', 'Denzel', 'Washington', null, 2);
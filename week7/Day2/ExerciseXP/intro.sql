-- Create a database called public.
-- Add two tables:
-- items
create table items(
  id varchar(50) primary key,
  name varchar(50) not null,
  price float
);

-- customers.
create table customers(
  id varchar(50) primary key,
  first_name varchar(50) not null,
  last_name varchar(50) not null
);



-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80
insert into items
values('1', 'Small Desk', 100),
('2', 'Large Desk', 300),
('3', 'Fan', 80);

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson
insert into customers
values('1', 'Greg', 'Jones'),
('2', 'Sandra', 'Jones'),
('3', 'Scott', 'Scott'),
('4', 'Trevor', 'Green'),
('5', 'Melanie', 'Johnson');

-- Use SQL to fetch the following data from the database:
-- All the items.
select *
from items

-- All the items with a price above 80 (80 not included).
select *
from items
where price > 80

-- All the items with a price below 300. (300 included)
select *
from items
where price < 300

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
select *
from customers
where last_name = 'Smith'

-- All customers whose last name is ‘Jones’.
select *
from customers
where last_name = 'Jones'

-- All customers whose firstname is not ‘Scott’.
select *
from customers
where last_name != 'Scott'
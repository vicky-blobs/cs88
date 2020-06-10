create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-- Comment out the unfinished questions while you
-- are working so as to avoid errors in the tests.

-- All short dogs
create table short_dogs as
-- REPLACE THIS LINE
select dogs.name as name, dogs.fur as fur, dogs.height as size from dogs where dogs.height < 40;

-- The size of each dog
create table size_of_dogs as
-- REPLACE THIS LINE
select dogs.name, sizes.size from dogs, sizes where dogs.height <= sizes.max and dogs.height > sizes.min;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
-- REPLACE THIS LINE
select parents.child from parents, dogs where dogs.name = parents.child and parents.child = dogs.name 
order by dogs.height desc;


-- Height and name of every dog that shares height 10's digit  
-- with at least one other dog and has the highest 1's digit of all dogs 
-- that have the same 10's digit
create table tallest as
-- REPLACE THIS LINE
select dogs.height, dogs.name from dogs where dogs.height / (select dogs.height from dogs order by dogs.height desc) != 1;


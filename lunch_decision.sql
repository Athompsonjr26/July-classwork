CREATE TABLE restaurant (
  id serial PRIMARY KEY,
  name varchar
);

CREATE TABLE student (
  id serial PRIMARY KEY,
  name varchar
);

CREATE TABLE preference (
  restaurant_id integer REFERENCES restaurant (id),
  student_id integer REFERENCES student (id)
);

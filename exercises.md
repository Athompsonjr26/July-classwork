# Projects DB Exercises

## Setup

Create a new database called projects_db or whatever you want. Restore the database from the projects.sql file via the command:

psql projects_db < projects.sql

## Problems

* Do a cartesian join between the project table and the tech table
* Perform a left outer join between the project table and the project_uses_tech tables
* Perform a left outer join between the tech table and the project_uses_tech table
* Perform a left outer join from the project table to the project_users_tech table and then left outer join again to the tech table.
* Start from the answer on the previous problem and get the count of how many different tech each project uses
* For each tech, get the count of how many projects use it
* Rank each project by how many tech it uses
* Rank each tech by how many projects use it
* What is the average number of techs used by a project?

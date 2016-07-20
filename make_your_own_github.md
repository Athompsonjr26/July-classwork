# Make Your Own Github

You will make your own GitHub-like database.

This project has three sections:

* building the schema
* inserting the data
* writing the queries

## Building the Schema

Here are *some* of the domain objects in *your* GitHub:

* project
* pull request
* user
* commit
* star (for projects)
* tech (represents either a language, library, or a framework). The project table will have a many-to-many association with the tech table.

Design your schema (screen-less activity):

* list the columns you would want to have for each domain object in the list above. Read ahead to the "Questions" section below to make sure you have the columns you need to answer those questions.
* identify the one-to-many and many-to-many associations, do this on the board or on paper by diagraming

Author the schema:

Write your schema in a .sql file, say my_github.sql. Load in that schema by doing `psql my_github_db < my_github.sql`. To ease fast development, I suggest putting a `DROP TABLE IF EXISTS my_table` statement before each `CREATE TABLE my_table` statement - otherwise you will get a "relation already exists" error.

Ask me to check off on the schema before moving on to the next step.

## Entering Data

You will now painstakingly enter data into this database. You should enter data for all projects you have on the real GitHub and for each partner. I suggest using Postico to enter data, it will be less painful than writing individual insert statements.

For commits, entering every individual commit would be too tedious, so I suggest just entering 3 or 4 mock commits for each project.

Add some stars to each project.

## Questions

You will answer the following questions using SQL queries:

* How popular is this project (based on number of stars)?
* How many projects does this user have?
* List this user's projects.
* What are this user's top 3 projects based on number of stars?
* What are the top 3 projects overall based on the number of tech used?
* Are there more than one project with the same name?
* How many contributors does each project have (include even projects that have no contributors)?
* How many projects does each user have (include even users that have no projects)?
* What is the average number of commits on a project?
* What is the average number of contributors on a project?
* What is the average number of stars on a project?
* Who are the contributors to this project?
* Who made the most PRs (pull requests) to this project?
* What is this user's PR acceptence rate (ratio of PRs merged vs PRs unmerged)?
* What tech does this project use?
* What tech does this user know - based on the tech used in his projects?
* Who are the top 3 contributors to this project based on number of commits?
* What are this user's top 3 projects based on number of commits?
* Write a query to enable plotting a project's commit activity by date.
* Write a query to enable plotting a user's number of commits by date.

## Bonus

Think of other questions you would like to answer, and write queries for them. If you need to build more schema in order to answer those questions, do that.

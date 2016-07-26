# Todo List

As a warm up exercise to building the Twitter app with the Python/Flask stack, you are going to first build a todo list app. You will implement the app in 3 stages:

1. Create the database schema and enter some sample tasks
2. Make a Flask app to display the tasks on a web page
3. Allow the ability to add a new task
4. Allow the ability to complete a task
5. Allow the ability to delete a task

The app will only have one page, which displays the tasks and contains forms to submit actions to the back end.

## Create a Database Schema

Create a database in PostgreSQL and a table within it to store tasks. A task needs to have a name, and a flag marking whether it is complete.

Create same sample tasks in the database with Postico or psql.

## Display the List

Make a Flask app with one page displaying the list of tasks from the database.

In your Flask app, before doing

app.run(debug=True)

MAKE SURE you do

app.debug = True

This will give you better error messages when things go wrong.

## Styling

Style the todo list so it looks good. You'll put your stylesheet in the static subdirectory of your project, and link to it.

## Adding tasks

To add the ability to add tasks, you will need to create a form with a text input on the page. You will also need to create a route handler in Flask to handle the form submission and create the task in the database using the PyGreSQL driver's db.insert() method.

## Completing tasks

Add the ability to check off tasks. This is how it will work from the user perspective:

1. There is a checkbox to the left of each task in the list, and a "Mark complete" button at the button of the list.
2. The user will check each task he wants to complete.
3. The user will click to "Mark complete" button to mark complete each task he has checked.

To do this, you will create a second form that wraps around/contains the list of tasks, as well as the "Mark complete" button. That way, the checkbox inputs will be submitted as part of the form submission. To communicate to the backend which tasks you want to mark as completed, I suggest setting the "name" attribute of each checkbox to the database ID of each task. For example, suppose you had 3 tasks in the database:

todo=# select * from task;
 id | name  | complete
----+-------+----------
  2 | Eat   | f
  5 | Code  | f
  6 | Sleep | f
(3 rows)

You would render the todo list as such:

<form action="/edit_tasks">
  <ul>  
    <li>
      <input type="checkbox" name="2">
      Eat
    </li>
    <li>
      <input type="checkbox" name="5">
      Code
    </li>
    <li>
      <input type="checkbox" name="6">
      Sleep
    </li>
  </ul>
  <button type="submit" name="complete">Mark Complete</button>
</form>

You will create another route handler to handle the form submission. The route handler will loop through each task ID that was submitted from the form and issue an update to that task to change its completion status.

Bonus: try to update all selected tasks with just one SQL statement instead of looping through each one.

## Deleting Tasks

The scheme for deleting tasks is similar to marking them complete. The user will

1. Check each task he wants to delete.
2. Click the "Delete" button.

To implement this we need to piggy back on the same submit URL we used for marking tasks complete because we can only have one form that contains the task list. But, there has to be a way to distinguish between a submission for marking tasks complete vs deleting them. To do this, you will add name attributes to the buttons:

<button type="submit" name="complete">Mark Complete</button>
<button type="submit" name="delete">Delete</button>

This way, when the "Mark Complete" button is clicked, a "complete" parameter will be posted to the backend. Vice versa, when the "Delete" button is clicked, a "delete" parameter will be posted. Your route handler can then use this parameter to distinguish between what action to perform. Try

print request.form

to determine what the submitted data looks like.

## Bonus

1. Ability to mark a complete task as undone.
2. Display the count of the number of undone tasks that remain in a corner.
3. Allow multiple users, each user "signs in" to use his own list.

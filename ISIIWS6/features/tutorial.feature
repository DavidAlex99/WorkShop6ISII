Feature: Add a task to the to-do list
  Scenario: Adding a task
    Given the To-Do list is empty
        When the user adds a task "Buy groceries"
            Then the to-do list should contain "Buy groceries"

  Scenario: List all the task
    Given the To-Do list contains:
      | task              |
      | Buy Groceries     |
      | Make the dishes   |
      | Wash the clothes  |
      When the user list all tasks by name
        Then the output should contain
          | task              |
          | Buy Groceries     |
          | Make the dishes   |
          | Wash the clothes  |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
      When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
      When the user clears the to-do list
        Then the to-do list should be empty

  Scenario: Edit a task's details
    Given the to-do list contains the task "Buy groceries" with description "Milk, Bread"
      When the user edits the task "Buy groceries" changing description to "Milk, Bread, Eggs"
        Then the to-do list should show the task "Buy groceries" with description "Milk, Bread, Eggs"

  Scenario: Filter completed tasks
    Given the to-do list contains tasks with various statuses
      | Task           | Status   |
      | Buy groceries  | Completed|
      | Pay bills      | Pending  |
      When the user filters tasks by the status "Completed"
        Then the output should only show tasks with status "Completed"
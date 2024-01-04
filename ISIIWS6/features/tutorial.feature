Feature: showing off behave

  Scenario: Adding a task
    Given the To-Do list is empty
        When the user adds a task "Buy groceries"
            Then the to-do list should contain "Buy groceries"

  Scenario: List all the task
    Given the To-Do list contains:
    | Buy Groceries     |
    | Make the dishes   |
    | Wash the clothes  |
        When the user list all tasks by name
            Then the output should contain
            | Buy Groceries     |
            | Make the dishes   |
            | Wash the clothes  |

  Scenario: Clear the entire to-do list
    Given : Given the to-do list contains tasks:
    | Buy Groceries     |
    | Make the dishes   |
    | Wash the clothes  |
      When : When the user clears the to-do list
        Then : the to-do list should be empty

  Scenario : Mark a task as completed
    Given : Given the to-do list contains tasks:
    | TASK              |  STATUS
    | Buy Groceries     |  PENDING
    | Make the dishes   |  PENDING
    | Wash the clothes  |  PENDING
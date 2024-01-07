# FIRST METHOD: Adding a task Given the To - Do list is empty

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = []

# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.append(task)

# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'

# SECOND METHOD:
# Step 1: the To-Do list contains:
@given('the To-Do list contains')
def step_impl(context):
    global to_do_list
    to_do_list = [row['task'] for row in context.table]

# Step 2: the user list all tasks by name
@when('the user list all tasks by name')
def step_impl(context):
    global to_do_list
    context.output = to_do_list

# Step 3: the output should contain
@then('the output should contain')
def step_impl(context):
    expected_tasks = [row['task'] for row in context.table]
    for task in expected_tasks:
        assert task in context.output, f"Task '{task}' not found in output"

    # THIRD METHOD:
    # Step 1: the to-do list contains tasks:
    @given('the to-do list contains tasks')
    def step_impl(context):
        global to_do_list
        to_do_list = [{row['Task']: row['Status']} for row in context.table]

    # Step 2: the user marks task "Buy groceries" as completed
    @when('the user marks task "{task_name}" as completed')
    def step_impl(context, task_name):
        global to_do_list
        for task in to_do_list:
            if task_name in task:
                task[task_name] = 'Completed'

    # Step 3: the to-do list should show task "Buy groceries" as completed
    @then('the to-do list should show task "{task_name}" as completed')
    def step_impl(context, task_name):
        global to_do_list
        for task in to_do_list:
            if task_name in task:
                assert task[task_name] == 'Completed', f'Task {task_name} is not marked as completed'

    # FOURTH METHOD:
    # Step 1: the to-do list contains tasks:
    @given('the to-do list contains tasks')
    def step_impl(context):
        global to_do_list
        to_do_list = [row['Task'] for row in context.table]

    # Step 2: the user clears the to-do list
    @when('the user clears the to-do list')
    def step_impl(context):
        global to_do_list
        to_do_list.clear()

    # Step 3: the to-do list should be empty
    @then('the to-do list should be empty')
    def step_impl(context):
        global to_do_list
        assert len(to_do_list) == 0, 'The to-do list is not empty'

# ToDo App – Python CLI

A command-line based ToDo application built with Python.

The project started as a simple task-management application and was gradually enhanced with task persistence, priorities, categories, due dates, task IDs, pagination, bulk operations, activity logging, configuration management, import/export, and automated testing.

---

## 🚀 Features

### Task Management

- Add tasks
- View tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- Search tasks

### Task Organization

- Task ID
- Priority
  - Low
  - Medium
  - High
- Category
  - Work
  - Learning
  - Personal
  - Other
- Due dates
- Overdue task identification
- Due today identification
- Upcoming tasks

### Filtering and Sorting

- Filter by completion status
- Filter by priority
- Filter by category
- Filter by due date
- Sort by priority
- Sort by due date
- Sort alphabetically

### Advanced Features

- Task pagination
- Bulk task deletion
- Bulk task completion
- JSON persistence
- Import tasks
- Export tasks
- Activity logging
- Centralized application configuration

### Validation

- Empty task validation
- Maximum task-name length validation
- Priority validation
- Category validation
- Due-date validation
- Invalid task-number handling
- Invalid input handling

---

## 🛠️ Technologies

- Python
- JSON
- Pytest
- Git
- GitHub

---

## 📁 Project Structure

```text
ToDo-App-V3/
│
├── main.py
├── menu.py
├── task_manager.py
├── storage.py
├── logger.py
├── config.py
│
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py
│
├── tasks.json
├── .gitignore
└── README.md

File Responsibilities
main.py

Application entry point.

Handles the main menu and coordinates the different task-management operations.

menu.py

Contains menu-related functionality and terminal formatting.

task_manager.py

Contains the main task-management logic, including:

Adding tasks
Editing tasks
Deleting tasks
Completing tasks
Searching
Filtering
Sorting
Pagination
Bulk operations
Task ID generation
Task summary
storage.py

Handles task persistence and JSON operations.

Responsible for:

Saving tasks
Loading tasks
Task data migration
Importing tasks
Exporting tasks
logger.py

Handles activity logging.

Application activities are recorded with timestamps.

config.py

Contains centralized application configuration:

TASK_ID_START = 1000
PAGE_SIZE = 5
MAX_TASK_NAME_LENGTH = 100
LOG_FILE = "activity.log"
⚙️ Requirements
Python 3.x
Pytest

Install Pytest:

pip install pytest
▶️ Running the Application

Clone the repository:

git clone git@github.com:shariefimran/ToDo-App-Version3.git

Navigate to the project directory:

cd ToDo-App-V3

Run the application:

python main.py
🧪 Running Tests

Run all automated tests:

pytest

Current test result:

11 passed in 0.01s
🆔 Task IDs

Each task receives a unique Task ID.

The default starting ID is:

1000

The starting value can be configured in config.py:

TASK_ID_START = 1000

Task IDs are used for identifying tasks and performing bulk operations.

⚙️ Configuration

Application configuration is centralized in:

config.py

Current configuration:

TASK_ID_START = 1000
PAGE_SIZE = 5
MAX_TASK_NAME_LENGTH = 100
LOG_FILE = "activity.log"
Configuration Details
Configuration	Default	Purpose
TASK_ID_START	1000	Starting value for Task IDs
PAGE_SIZE	5	Number of tasks displayed per page
MAX_TASK_NAME_LENGTH	100	Maximum allowed task-name length
LOG_FILE	activity.log	Activity log filename

Centralizing these values allows application settings to be changed without modifying the core task-management logic.

💾 Data Storage

Tasks are stored locally in:

tasks.json

The application automatically saves task changes to the JSON file.

Task Data Example
{
    "name": "Learn Python",
    "completed": false,
    "priority": "High",
    "category": "Learning",
    "due_date": "2026-12-12",
    "task_id": 1000
}
📥 Import and Export

The application supports exporting tasks to a separate JSON file and importing them back into the application.

Export file:

tasks_export.json

These runtime files are excluded from Git tracking through .gitignore.

📝 Activity Logging

The application records important task activities with timestamps.

Example:

2026-09-19 11:44:45 - Added task : validating the task ids (ID: 1014)
2026-09-19 11:47:52 - Deleted task : validating the due date (ID: 1009)
2026-09-19 11:51:49 - Edited task : validating the logger activity to validating the edit task logging (ID: 1015)

Runtime activity logs are stored locally in:

activity.log

The log file is excluded from Git tracking through .gitignore.

📄 Pagination

Tasks are displayed using pagination.

The default page size is:

PAGE_SIZE = 5

Navigation options include:

[N] Next
[P] Previous
[B] Back

The page size can be changed through config.py.

🗑️ Bulk Operations

The application supports bulk operations using Task IDs.

Bulk Delete

Multiple Task IDs can be entered using comma-separated values:

1001,1002,1005
Bulk Complete

Multiple pending tasks can be marked as completed using their Task IDs.

🔍 Filtering

Tasks can be filtered using different criteria:

Completion status
Priority
Category
Due date

Due-date filtering includes:

Overdue
Due Today
Upcoming
🔃 Sorting

Tasks can be sorted by:

Priority
Due date
Alphabetical order
📊 Task Summary

The application provides a task summary containing information about the current task collection, including completion and due-date information.

🛡️ Input Validation

The application validates user input for:

Empty task names
Maximum task-name length
Priority selection
Category selection
Due dates
Invalid task numbers
Invalid menu choices
Invalid numeric input

Invalid input is handled without terminating the application.

🧪 Test Coverage

The project currently contains 11 automated tests covering:

Task search
Search with no matching task
Empty task search
Task deletion
Invalid deletion input
Invalid task number
Task completion
Already completed task
Invalid completion input
Invalid completion task number
Empty task completion

Current test result:

11 passed in 0.01s
🔄 Development History

The application was developed incrementally through multiple versions.

V3

Core task-management functionality and JSON persistence.

Implemented:

Add task
View task
Edit task
Delete task
Mark task completed
Search task
Task summary
JSON persistence
Input validation
Unit testing
V4

Added:

Priority
Category
Due dates
Filtering
Sorting
Improved summaries
Validation improvements
JSON data migration
Unit testing
V5

Added:

Improved CLI formatting
Better terminal output
Pagination
Import/export
Task IDs
Bulk operations
Activity logging
Centralized configuration
Project cleanup
Final testing and polish
🧹 Project Cleanup

Runtime-generated files are excluded from Git tracking.

The .gitignore file contains:

__pycache__/
*.pyc

activity.log
tasks_export.json

.DS_Store

This keeps generated logs, exported data, Python cache files, and macOS metadata out of the Git repository.

🔮 Future Enhancements

Possible future improvements include:

Database storage
User authentication
REST API
Web interface
Advanced reporting
Cloud synchronization
More comprehensive automated testing
👨‍💻 Author

Imran Sharief

Senior Performance Engineer

📄 License

This project is currently intended for learning and personal development.



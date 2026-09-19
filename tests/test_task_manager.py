from task_manager import search_task, delete_task, mark_task_completed


def test_search_task(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Python")
    result = search_task(tasks)

    assert result is True


def test_search_task_not_found(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Java")
    result = search_task(tasks)

    assert result is False


def test_search_task_empty(monkeypatch):
    tasks = []

    result = search_task(tasks)

    assert result is False


def test_delete_task(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        },
        {
            "name": "Practice pytest",
            "completed": False,
            "priority": "Medium",
            "category": "Learning",
            "due_date": None,
            "task_id": 1001
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = delete_task(tasks)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Practice pytest"


def test_delete_invalid_input(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "abc")
    result = delete_task(tasks)

    assert result is False
    assert len(tasks) == 1


def test_delete_invalid_task_number(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "999")
    result = delete_task(tasks)

    assert result is False
    assert len(tasks) == 1


def test_mark_task_completed(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = mark_task_completed(tasks)

    assert result is True
    assert tasks[0]["completed"] is True


def test_mark_task_already_completed(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": True,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = mark_task_completed(tasks)

    assert result is False
    assert tasks[0]["completed"] is True


def test_mark_task_invalid_input(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "abc")
    result = mark_task_completed(tasks)

    assert result is False
    assert tasks[0]["completed"] is False


def test_mark_task_invalid_number(monkeypatch):
    tasks = [
        {
            "name": "Learn Python",
            "completed": False,
            "priority": "High",
            "category": "Learning",
            "due_date": None,
            "task_id": 1000
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "999")
    result = mark_task_completed(tasks)

    assert result is False
    assert tasks[0]["completed"] is False


def test_mark_task_empty():
    tasks = []

    result = mark_task_completed(tasks)

    assert result is False

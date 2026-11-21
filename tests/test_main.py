
import pytest
from app.main import TaskManager


def test_add_task():
    manager = TaskManager()
    manager.add_task("Learn DevOps")

    assert len(manager.list_tasks()) == 1
    assert manager.list_tasks()[0]["task"] == "Learn DevOps"


def test_list_tasks():
    manager = TaskManager()
    manager.add_task("Build DevOptiX")
    manager.add_task("Learn Docker")

    assert len(manager.list_tasks()) == 2


def test_complete_task():
    manager = TaskManager()
    manager.add_task("Complete project")

    manager.complete_task(0)

    assert manager.list_tasks()[0]["completed"] is True


def test_empty_task():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_invalid_task_index():
    manager = TaskManager()

    with pytest.raises(IndexError):
        manager.complete_task(0)

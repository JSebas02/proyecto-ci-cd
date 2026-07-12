import pytest

from src.services import (
    clear_tasks,
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
)


@pytest.fixture(autouse=True)
def reset_tasks():
    clear_tasks()


def test_get_all_tasks_starts_empty():
    assert get_all_tasks() == []


def test_create_task_returns_task():
    task = create_task("Estudiar")

    assert task["id"] == 1
    assert task["title"] == "Estudiar"
    assert task["completed"] is False


def test_create_task_adds_task_to_list():
    create_task("Estudiar")

    assert len(get_all_tasks()) == 1


def test_create_multiple_tasks_assigns_consecutive_ids():
    first_task = create_task("Primera")
    second_task = create_task("Segunda")

    assert first_task["id"] == 1
    assert second_task["id"] == 2


def test_create_task_removes_external_spaces():
    task = create_task("  Estudiar Python  ")

    assert task["title"] == "Estudiar Python"


def test_create_task_rejects_empty_title():
    with pytest.raises(ValueError, match="El título es obligatorio"):
        create_task("")


def test_create_task_rejects_spaces_only():
    with pytest.raises(ValueError, match="El título es obligatorio"):
        create_task("   ")


def test_create_task_rejects_non_string_title():
    with pytest.raises(ValueError, match="El título debe ser texto"):
        create_task(None)


def test_get_task_by_id_returns_existing_task():
    created_task = create_task("Estudiar")

    found_task = get_task_by_id(created_task["id"])

    assert found_task == created_task


def test_get_task_by_id_returns_none_when_not_found():
    assert get_task_by_id(99) is None


def test_delete_task_removes_existing_task():
    task = create_task("Eliminar")

    result = delete_task(task["id"])

    assert result is True
    assert get_all_tasks() == []


def test_delete_task_returns_false_when_not_found():
    result = delete_task(99)

    assert result is False
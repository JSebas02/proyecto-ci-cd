import pytest

from src.app import create_app
from src.services import clear_tasks


@pytest.fixture()
def client():
    clear_tasks()

    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client

    clear_tasks()


def test_get_tasks_returns_empty_list(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == []


def test_post_task_creates_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Estudiar pruebas"},
    )

    data = response.get_json()

    assert response.status_code == 201
    assert data["id"] == 1
    assert data["title"] == "Estudiar pruebas"
    assert data["completed"] is False


def test_post_task_without_title_returns_400(client):
    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "El título debe ser texto"
    }


def test_delete_existing_task_returns_204(client):
    created_response = client.post(
        "/tasks",
        json={"title": "Eliminar tarea"},
    )

    task_id = created_response.get_json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")

    assert delete_response.status_code == 204


def test_delete_non_existing_task_returns_404(client):
    response = client.delete("/tasks/99")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "Tarea no encontrada"
    }


def test_get_tasks_returns_created_tasks(client):
    client.post("/tasks", json={"title": "Primera"})
    client.post("/tasks", json={"title": "Segunda"})

    response = client.get("/tasks")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["title"] == "Primera"
    assert data[1]["title"] == "Segunda"
from flask import Flask, jsonify, request

from src.services import (
    create_task,
    delete_task,
    get_all_tasks,
)


def create_app():
    app = Flask(__name__)

    @app.get("/tasks")
    def list_tasks():
        return jsonify(get_all_tasks()), 200

    @app.post("/tasks")
    def add_task():
        data = request.get_json(silent=True) or {}

        try:
            task = create_task(data.get("title"))
            return jsonify(task), 201
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @app.delete("/tasks/<int:task_id>")
    def remove_task(task_id):
        if not delete_task(task_id):
            return jsonify({"error": "Tarea no encontrada"}), 404

        return "", 204

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
tasks = []
next_id = 1


def get_all_tasks():
    return tasks


def get_task_by_id(task_id):
    return next(
        (task for task in tasks if task["id"] == task_id),
        None
    )


def create_task(title):
    global next_id

    if not isinstance(title, str):
        raise ValueError("El título debe ser texto")

    title = title.strip()

    if not title:
        raise ValueError("El título es obligatorio")

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    return task


def delete_task(task_id):
    task = get_task_by_id(task_id)

    if task is None:
        return False

    tasks.remove(task)
    return True


def clear_tasks():
    global next_id

    tasks.clear()
    next_id = 1
    
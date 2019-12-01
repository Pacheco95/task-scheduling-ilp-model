from entities import Task, ResourceConstraints, Machine


def load_tasks(file_path: str) -> [Task]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    tasks = []

    for line in lines[1:]:
        split = map(float, line.split(','))
        arguments = tuple(map(ResourceConstraints, split))
        tasks.append(Task(*arguments))

    return tasks


def load_machines(file_path: str) -> [Task]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    machines = []

    for line in lines[1:]:
        arguments = tuple(map(float, line.split(',')))
        machines.append(Machine(*arguments))

    return machines

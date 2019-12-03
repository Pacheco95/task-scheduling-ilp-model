from entities import Task, ResourceConstraints, Machine


def str2bool(v: str) -> bool:
    return v.lower() in ("yes", "true", "t", "1")


def load_tasks(file_path: str) -> [Task]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    tasks = []

    constructor_parameter_types = ((ResourceConstraints,) * 3 + (str2bool,))

    for line in lines[1:]:
        line = line.strip()
        split = list(zip(constructor_parameter_types, tuple(line.split(','))))
        split = list(map(lambda t: t[0](t[1]), split))
        tasks.append(Task(*split))

    return tasks


def load_machines(file_path: str) -> [Task]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    machines = []

    constructor_parameter_types = ((float,) * 4 + (str2bool,))

    for line in lines[1:]:
        line = line.strip()
        arguments = list(zip(constructor_parameter_types, tuple(line.split(','))))
        arguments = list(map(lambda t: t[0](t[1]), arguments))
        machines.append(Machine(*arguments))

    return machines

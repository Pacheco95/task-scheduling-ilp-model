from mip import *

from entities import Task, Machine


def schedule(tasks: List[Task], machines: List[Machine]) -> List[Tuple[int, int]]:
    tasks_it = range(len(tasks))
    machines_it = range(len(machines))

    scheduling_model = Model('Task Scheduling', sense=MAXIMIZE)

    """
    List of Xij variables.
    1 if task i was scheduled to machine j, 0 otherwise
    """
    x = dict()

    for i in tasks_it:
        for j in machines_it:
            var_name = 'x_%02d_%02d' % (i + 1, j + 1)
            x[i, j] = scheduling_model.add_var(var_type=BINARY, name=var_name)

    """
    Objective function
    """
    for i, task in enumerate(tasks):
        for j, machine in enumerate(machines):
            scheduling_model += x[i, j] * (1 - task.time_constr.maximum)

    """
    Ensure that one task will be scheduled to 1 machine at maximum
    """
    for i in tasks_it:
        scheduling_model += xsum(x[i, j] for j in machines_it) <= 1

    """
    Ensure that all tasks scheduled to a machine m does not overflow RAM capacity
    """
    for j, m in enumerate(machines):
        scheduling_model += xsum(x[i, j] * tasks[i].ram_constr.maximum for i in tasks_it) <= m.ram_capacity

    scheduling_model.optimize()

    if scheduling_model.status != OptimizationStatus.OPTIMAL:
        raise Exception('Unfeasible problem')

    scheduled_tasks = dict(filter(lambda elem: elem[1].x == 1, x.items()))

    return list(map(lambda elem: (elem[0] + 1, elem[1] + 1), scheduled_tasks.keys()))

from mip import *

from input_loader import load_machines, load_tasks

tasks = load_tasks('input/tasks.csv')
machines = load_machines('input/machines.csv')

# Used to iterate elements of tasks
tasks_it = range(len(tasks))
# Used to iterate elements of machines
machines_it = range(len(machines))

master = Model('Master', MAXIMIZE)

# list of patterns by machine
K: Dict[int, List[int]] = {}

# 1, if machine j will execute pattern k. 0, otherwise.
Yjk: Dict[Tuple, Var] = {}

# 1, if task i will be executed by machine j using pattern k. 0, otherwise.
Yijk: Dict[Tuple, Var] = {}

# Objective function
# Maximize the number of scheduled tasks
master += xsum(Yijk[i, j, k] for i in machines_it for j in tasks_it for k in K[j])

# Ensure that a machine will execute at most one pattern
for j in machines_it:
    master += xsum(Yjk[j, k] for k in K[j]) <= 1

# Ensure that a task will be executed by at most one machine
for i in tasks_it:
    master += xsum(Yijk[i, j, k] for j in machines_it for k in K[j]) <= 1

import itertools
import random

import scheduler
from entities import Machine, Task, ResourceConstraints


def generate_random_task():
    cpu_constr = ResourceConstraints(random.randrange(200, 16000))
    ram_constr = ResourceConstraints(random.randrange(200, 16000))
    time_constr = ResourceConstraints(random.randrange(0, 3600))
    has_vcard = random.random() < 0.1
    return Task(cpu_constr, ram_constr, time_constr, has_vcard)


machine_models = [
    {
        'ram': 1000,
        'cores': 1000,
        'vcard': False
    }, {
        'ram': 2000,
        'cores': 2000,
        'vcard': False
    }, {
        'ram': 8000,
        'cores': 6000,
        'vcard': True
    }, {
        'ram': 16000,
        'cores': 16000,
        'vcard': True
    }
]

machines = [Machine(model['ram'], 0, model['cores'], 0, model['vcard']) for model in machine_models]
machines_it = range(len(machine_models))

tasks = [generate_random_task() for i in range(100)]

test_case_1 = [[(n, t)] for n in [1, 5, 20, 100] for t in machines_it]
# print(len(test_case_1))
# print(test_case_1)

test_case_2 = [[(i, j) for j in machines_it] for i in [1, 5, 20, 100]]
# print(len(test_case_2))
# print(test_case_2)

test_cases = test_case_1 + test_case_2

for case in test_cases:
    current_machines = list(itertools.chain.from_iterable([n * [machines[m]] for n, m in case]))
    scheduler.schedule(tasks, current_machines)
    print(case)
    print(current_machines)

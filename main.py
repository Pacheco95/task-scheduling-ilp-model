from input_loader import load_tasks, load_machines
from scheduler import schedule

if __name__ == '__main__':
    tasks = load_tasks('input/tasks.csv')
    machines = load_machines('input/machines.csv')

    print('Tasks:')
    for task in tasks:
        print('\t', task)

    print('Machines:')
    for machine in machines:
        print('\t', machine)

    s = schedule(tasks, machines)
    print('Escalonamento (Tarefa, Máquina):', s)

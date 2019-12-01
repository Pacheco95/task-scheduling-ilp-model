from input_loader import load_tasks, load_machines
from scheduler import schedule

if __name__ == '__main__':
    s = schedule(load_tasks('input/tasks.csv'), load_machines('input/machines.csv'))
    print('Escalonamento (Tarefa, Máquina):', s)

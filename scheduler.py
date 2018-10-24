from tasks import task, Tasks
from BatteryModel import Battery

def EDF(task_set):
    pass



if __name__ == "__main__":
    t1 = task(7, 18, 650)
    t2 = task(5, 10, 800)
    t3 = task(8, 26, 400)
    t4 = task(10, 38, 380)

    tasks = Tasks()
    tasks.add_task(t1)
    tasks.add_task(t2)
    tasks.add_task(t3)
    tasks.add_task(t4)

    tasks.calculate_runtime()

    battery = Battery()
    consumption = battery.tasks_consumption(38, tasks)

    print(consumption)
from tasks import task, Tasks
from BatteryModel import Battery

def EDF(task_set):
    temp = {}
    new_order = []
    for task in task_set.task_lists:
        temp[task] = task.deadline

    for key, value in sorted(temp.items(), key=lambda x: x[1]):
        new_order.append(key)
    task_set.task_lists = new_order
    task_set.calculate_runtime()


def DVS_A1(task_set):
    pass


def plot_consumption():
    observation_time = []
    consumption = []
    observation_time.append(38)
    consumption.append(battery.tasks_consumption(38, tasks))
    consumption.append(battery.tasks_consumption(380, tasks))
    tasks.plot(observation_time, consumption)


if __name__ == "__main__":
    t1 = task('1', 7, 18, 650)
    t2 = task('2', 5, 10, 800)
    t3 = task('3', 8, 26, 400)
    t4 = task('4', 10, 38, 380)

    tasks = Tasks()
    tasks.add_task(t1)
    tasks.add_task(t2)
    tasks.add_task(t3)
    tasks.add_task(t4)

    battery = Battery()

    ### Phase 1
    # Prescheduling using EDF
    EDF(tasks)

    plot_consumption()

    # Check ensure tasks in non-increasing order of loads. In case failure, scale down the voltage.
    task_list = []
    for task in tasks.task_lists:
        task_list.append(task)

    for index in range(1, len(task_list)):
        # Downscale the failing task by minimum amount.
        while task_list[index].current > task_list[index -1].current:
            task_list[index].ScaleDown1()


    ### Phase 2
    # Repeadtedly use the available slack time by scaling down speeds of tasks.


    tasks.calculate_runtime()

from tasks import task, Tasks
from BatteryModel import Battery
import operator

def EDF(task_set):
    temp = {}
    new_order = []
    for task in task_set.task_lists:
        temp[task] = task.deadline

    for key, value in sorted(temp.items(), key=lambda x: x[1]):
        new_order.append(key)
    task_set.task_lists = new_order
    task_set.calculate_runtime()

    for t in task_set.task_lists:
        if not t.scheduable():
            return False

    return True

def plot_consumption(battery, tasks):
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
    scheduable = EDF(tasks)

    if not scheduable:
        raise Exception('Task not scheduable.')


    # plot_consumption(battery, tasks)

    # Check ensure tasks in non-increasing order of loads. In case failure, scale down the voltage.
    task_list = []
    for task in tasks.task_lists:
        task_list.append(task)

    for index in range(1, len(task_list)):
        # Downscale the failing task by minimum amount.
        while task_list[index].current > task_list[index -1].current:
            task_list[index].ScaleDown1()


    consumption = battery.tasks_consumption(38, tasks)

    print(battery.battery_failed)

    while battery.battery_failed:
        failed_task = battery.failed_task
        failed_task.ScaleDown()
        tasks.calculate_runtime()
        consumption = battery.tasks_consumption(38, tasks)

    plot_consumption(battery, tasks)
    ### Phase 2
    # Overall planning strategy to scale down based on maximum slack time
    slack_times = {}
    for task in task_list:
        if task.slack > 0:
            slack_times[task] = task.slack
        print(f'Task {task} with slack time {task.slack}')

    while slack_times:
        max_slack_task = max(slack_times.items(), key=operator.itemgetter(1))[0]
        print(f'Task {max_slack_task} with slack time {slack_times[max_slack_task]}')
        max_slack_task.ScaleDown1()
        tasks.calculate_runtime()
        if not tasks.check_scheduable():
            print(f'Task {max_slack_task} not scheduable, deleting from task list.')
            max_slack_task.ScaleUp1()
            tasks.calculate_runtime()
            del slack_times[max_slack_task]

    plot_consumption(battery, tasks)

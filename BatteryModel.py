import math


class Battery:
    """
    High level analytical model of Rakhmatov and Vrudhula's charge sensitive model.
    Battery model parameters:
        alpha     - Battery's theoretical capacity.
        beta      - Recovery rate.
        i(t)      - Load on battery
        L         - Battery life time
    """

    def __init__(self):
        self.capacity = 40375
        self.recovery_rate = 0.273
        self.m = 10
        self.total_consumption = 0

    def tasks_consumption(self, observation: int, tasks: object):
        consumption = 0
        for task in tasks.task_lists:
            start_time, duration, current = task.get_property()
            consumption += self.task_cost(observation, \
                                                     start_time, \
                                                     duration, \
                                                     current)
        self.total_consumption += consumption
        assert self.total_consumption <= self.capacity
        return consumption

    def task_cost(self, observation, tk, duration, current):
        """

        :param observation: Task observation time
        :param tk: Task start time
        :param duration: Duration of the task until finish
        :param current: Current for the task
        :return:
        """
        finish_time = tk + duration
        temp = []
        for m in range(1, self.m + 1):
            term1 = math.pow(self.recovery_rate, 2) * math.pow(m, 2)
            term2 = (math.exp(-term1 * (observation - finish_time)) - math.exp(-term1 * (observation - tk))) / term1
            temp.append(term2)

        consumption = current * duration + current * 2 * math.fsum(temp)
        return consumption
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

    def task_cost(self, B, tk, duration, current):
        """

        :param B: Task observation time
        :param tk: Task start time
        :param duration: Duration of the task until finish
        :param current: Current for the task
        :return:
        """
        finish_time = tk + duration
        temp = []
        for m in range(1, self.m + 1):
            term1 = math.pow(self.recovery_rate, 2) * math.pow(self.m, 2)
            term2 = (math.exp(-term1 * (B - finish_time)) - math.exp(-term1 * (B - tk))) / term1
            temp.append(term2)

        return current * duration + current * 2 * math.fsum(temp)

    def k_tasks(self, observation_time: int, tasks: dict, tasks_order: list):
        for task in tasks_order:
            self.total_consumption += self.task_cost(observation_time, \
                                                     tasks[task]["start_time"], \
                                                     tasks[task]["duration"], \
                                                     tasks[task]["current"])
        return self.total_consumption
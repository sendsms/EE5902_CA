import math


class Tasks:
    def __init__(self):
        self.task_lists = []
        self.position = 0

    def add_task(self, task):
        self.task_lists.append(task)

    def calculate_runtime(self):
        current_time = 0
        for t in self.task_lists:
            t.update_starttime(current_time)
            current_time = t.finishtime

    def __repr__(self):
        return f'Tasks({self.task_lists})'


class task:
    def __init__(self, duration, deadline, current):
        self.duration = duration
        self.deadline = deadline
        self.current = current
        self.starttime = 0
        self.finishtime = self.starttime + self.duration

    def update_starttime(self, starttime):
        self.starttime = starttime
        self.finishtime = self.starttime + self.duration

    def CalDuration(self, Vdd, Vdd_new):
        voltage_sets = set([3.3, 3.0, 2.7, 2.5, 2.0])

        assert Vdd in voltage_sets
        assert Vdd_new in voltage_sets

        Vth = 0.4
        s = Vdd / Vdd_new
        I_new = self.current / math.pow(s, 3)
        Duration_new = self.duration * s * (1 + 2 * (s - 1) * Vth / (Vdd - Vth))

        return I_new, Duration_new

    def ScaleVoltage(self, voltage_old, voltage_new):
        self.current, self.duration = self.CalDuration(voltage_old, voltage_new)
        self.finishtime = self.starttime + self.duration

    def get_property(self):
        return self.starttime, self.duration, self.current
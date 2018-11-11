import math
import matplotlib.pyplot as plt

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

    def check_scheduable(self):
        scheduable = True
        for t in self.task_lists:
            if not t.scheduable():
                scheduable = False
        return scheduable

    def __repr__(self):
        return f'Tasks({self.task_lists})'

    def plot(self, time=[], consumption=[]):
        x1 = []
        x2 = []
        y = []
        task_name = []
        slack = []
        plt.figure(1)
        for t in self.task_lists:
            x1.append(t.starttime)
            x2.append(t.duration)
            y.append(t.current)
            task_name.append(t.name)
            slack.append(t.slack)
            plt.text(t.starttime + t.duration/2, t.current/2, t.name)
        plt.subplot(2, 1, 1)
        plt.bar(x1, y, x2, align='edge', color='w', edgecolor='k')
        plt.xlabel('t (min)')
        plt.ylabel('I (mA)')
        plt.title(r'$\mu_{%d} = %d mA.min,\ \mu_\infty = %d mA.min$' % (time[0], consumption[0], consumption[1]))

        plt.subplot(2, 1, 2)
        plt.plot(task_name, slack, 'o')
        plt.xlabel('tasks')
        plt.ylabel('t (min)')
        plt.title('Task slack time')

        plt.tight_layout()
        plt.show()



class task:
    def __init__(self, name, duration, deadline, current):
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.current = current
        self.starttime = 0
        self.finishtime = self.starttime + self.duration
        self.slack = self.deadline - self.finishtime
        self.voltage_sets = {5: 3.3, 4: 3.0, 3: 2.7, 2: 2.5, 1: 2.0}
        self.voltage_level = 5
        self.voltage = self.voltage_sets[self.voltage_level]

    def scheduable(self):
        return self.deadline >= self.finishtime

    def update_starttime(self, starttime):
        self.starttime = starttime
        self.finishtime = self.starttime + self.duration
        self.slack = self.deadline - self.finishtime

    def CalDuration(self, Vdd, Vdd_new):
        Vth = 0.4
        s = Vdd / Vdd_new
        I_new = self.current / math.pow(s, 3)
        Duration_new = self.duration * s * (1 + 2 * (s - 1) * Vth / (Vdd - Vth))

        return I_new, Duration_new

    def ScaleVoltage(self, voltage_new):
        self.current, self.duration = self.CalDuration(self.voltage, voltage_new)
        self.finishtime = self.starttime + self.duration
        self.slack = self.deadline - self.finishtime
        self.voltage = voltage_new

    def ScaleDown1(self):
        self.voltage_level -= 1
        new_voltage = self.voltage_sets[self.voltage_level]
        self.ScaleVoltage(new_voltage)
        self.voltage = new_voltage

    def ScaleUp1(self):
        self.voltage_level += 1
        new_voltage = self.voltage_sets[self.voltage_level]
        self.ScaleVoltage(new_voltage)
        self.voltage = new_voltage


    def get_property(self):
        return self.starttime, self.duration, self.current

    def __repr__(self):
        return f'Task({self.name})'
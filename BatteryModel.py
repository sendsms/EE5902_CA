import math

# Total there will be n tasks.
# Current of task k is Ik
# Start time of task k is tk
# Duration of task k is Delta k

class Battery:
    """
    High level analytical model of Rakhmatov and Vrudhula's charge sensitive model.
    Battery model parameters:
        alpha     - Battery's theoretical capacity.
        beta      - Recovery rate.
        i(t)      - Load on battery
        L         - Battery life time
    """
    def __init__(self, current, observation_time, start_time, finish_time, recovery_rate):
        self.capacity = 40375
        self.observation_time = observation_time
        self.current = current
        self.start_time = start_time
        self.finish_time = finish_time
        self.recovery_rate = 0.273
        self.m = 10

    def consume(self, current):
        self.current = current
        temp = []
        for m in range(1, self.m + 1):
            term1 = math.pow(self.recovery_rate, 2) * math.pow(self.m, 2)
            term2 = (math.exp(-term1 * (self.observation_time - self.finish_time)) - math.exp(-term1 * (self.observation_time - self.start_time))) / term1
            temp.append(term2)

        return self.current * self.duration + self.current * 2 * math.fsum(temp)

    def run_tasks(self, tasks):
        


tasks = {1: [7, 18, 650],
         2: [5, 10, 800],
         3: [8, 26, 400],
         4: [10, 38, 380]}
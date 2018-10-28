# EE5902_CA
#### EE5902_CA Battery Aware Scheduling

TODOs:
- [x] Create task object. Task object should contain start time, current, duration
  - Task object having update_starttime method used for schedule runtime
  - Task object having calculate duration method to obtain new current, new duration after voltage scaling
- [x] Create task sets object. An object to hold list of tasks. 
  * Method add_task used to add task into the list 
  * Method calculate runtime used to rearrange start/finish time for each task
- [x] Battery object used to simulate battery model. 
  * Method tasks_consumption - Given tasks and observation time to calculate total battery consumed in mA.min
- [ ] Scheduler object. Scheduler should operate on tasks object. Schedule tasks based on algorithm before pass to battery for calculating cost. 





Battery model is using Rakhmatov and Vrudhula's charge sensitive model. Cost function is based on the model equation. In order to calculate the total current consumption, we need to know the *observation time*, *task start time*, *task duration*, and *task current*. 

These parameters need to be calculated by scheduler. Based on scheduling, the task start time t~k~ is equal to the previous task finish time t~k-1~ + Delta~k-1~. 

Only duration is given for each task, so the scheduler have to assign start time, finish time (start time + duration) to the task. Then the whole tasks can be passed to battery model for calculation of consumption. 

Equation is given to calculate the duration and current after voltage been scaled. When CPU voltage scale down by factor s, the battery current scales by s^3^ . The task execution time also scale based on equation. 



##### Task Sets:

| Task # | Duration (min) | Deadline (min) | Current (mA) |
| ------ | -------------- | -------------- | ------------ |
| 1      | 7              | 18             | 650          |
| 2      | 5              | 10             | 800          |
| 3      | 8              | 26             | 400          |
| 4      | 10             | 38             | 380          |



Evaluation matrices:

1. Charge used
2. Task size
3. Slack time



Algorithm 1 - SNOPS:

Slack-nibbling overall planning strategy (SNOPS) algorithm iteratively nibbles slacks for appropriate tasks selected by an overall planning dynamic priority function to perform DVS until the slack is exhausted and an optimum voltage setting is obtained. 

In battery aware task scheduling (BTS), it is carried out by two consecutive steps: pre-scheduling (task sorting), and DVS.  

Step 1: Prescheduling. All tasks in the initial set are sorted by an original scheduling algorithm which attempts to figure out a feasible schedule with plenty of slacks. 

- [x] EDF algorithm

- [x] Trying to generate a nonincreasing order of loads (greedy approach).

- [x] Ensure no failure. In case failure downscale the voltage of the failing task by the minimum amount. 

Step 2: Voltage scaling. Selected tasks in the schedule are submitted to DVS module for evaluation of distributable slacks; approved ones earn the opportunity for scaling by turns until slack depletion; an optimum BTS voltage setting is therefore obtained. Repeatedly use the available slack time by scaling down speeds of tasks to achieve the most effective decrease of the cost with respect to the discrete voltage downscaling effectiveness measure. 



Slack utilization strategy. 

The candidate pool accommodates tasks with available slack; the task selection scheme includes a DVS decision algorithm and a task selection algorithm, determining scaling direction and applicable target. 


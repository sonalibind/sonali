from collections import deque

def round_robin_with_gantt(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_bt = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    t = 0  # current time
    queue = deque()
    gantt_chart = []

    # Initially, add all processes to queue in order
    for i in range(n):
        queue.append(i)

    while queue:
        i = queue.popleft()

        if remaining_bt[i] > 0:
            start_time = t
            if remaining_bt[i] > time_quantum:
                t += time_quantum
                remaining_bt[i] -= time_quantum
                queue.append(i)
            else:
                t += remaining_bt[i]
                waiting_time[i] = t - burst_time[i]
                remaining_bt[i] = 0

            end_time = t
            gantt_chart.append((f"P{i+1}", start_time, end_time))

    # Calculate Turnaround Time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Print Gantt Chart
    print("Gantt Chart:")
    for entry in gantt_chart:
        print(f"{entry[0]} ({entry[1]} - {entry[2]})", end=" | ")
    print("\n")

    # Calculate averages
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example input from image
processes = [0, 1, 2]                # P1, P2, P3
burst_time = [5, 4, 7]              # burst times
time_quantum = 2

round_robin_with_gantt(processes, burst_time, time_quantum)








# Algorithm:

# 1. Initialize:

# Current time = 0

# Remaining burst time for each process = burst time

# Waiting time for all processes = 0

# A queue with all process indices

# An empty Gantt chart list

# 2. Loop until the queue is empty:

#  * Dequeue the first process from the queue

#  *If the remaining burst time is more than 0:

# Record the start time (current time)

# If remaining burst time > time quantum:

# Add time quantum to current time

# Subtract time quantum from remaining burst time

# Re-enqueue the process (since it’s not yet complete)

#  * Else (remaining burst time ≤ time quantum):

# Add remaining burst time to current time

# Calculate waiting time = current time - original burst time

# Set remaining burst time to 0 (process completed)

# Record the (Process ID, Start Time, End Time) in the Gantt chart

# 3. After all processes finish:

# Calculate turnaround time = burst time + waiting time for each process

# Print Gantt chart and compute average waiting & turnaround time


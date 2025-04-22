def sjf_scheduling(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    gantt_chart = []

    time = 0
    completed_processes = 0

    # Process by shortest burst time
    while completed_processes < n:
        shortest = -1
        min_bt = float('inf')

        for i in range(n):
            if not completed[i] and burst_time[i] < min_bt:
                min_bt = burst_time[i]
                shortest = i

        if shortest != -1:
            start_time = time
            time += burst_time[shortest]
            end_time = time
            waiting_time[shortest] = start_time
            turnaround_time[shortest] = end_time
            completed[shortest] = True
            completed_processes += 1
            gantt_chart.append((f"P{shortest+1}", start_time, end_time))
        else:
            time += 1  # if no process is ready, move time forward

    # Calculate averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Print Gantt Chart
    print("Gantt Chart:")
    for entry in gantt_chart:
        print(f"{entry[0]} ({entry[1]} - {entry[2]})", end=" | ")
    print("\n")

    print(f"Average Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")

# Example input
processes = [0, 1, 2]              # P1, P2, P3
burst_time = [5, 4, 7]            # same as earlier

sjf_scheduling(processes, burst_time)


















# Algorithm:

# 1. Initialize:

# Current time = 0

# Waiting time and turnaround time arrays = 0 for all

# An array to track if a process is completed

# An empty Gantt chart list

# 2. Loop until all processes are completed:

# * Among the processes not yet completed, find the one with the smallest burst time

# * If such a process exists:

# Record its start time = current time

# Add burst time to current time (process runs to completion)

# Set waiting time = start time

# Set turnaround time = current time (end time)

# Mark the process as completed

# Add (Process ID, Start Time, End Time) to the Gantt chart

# * Else:

# If no process is found, increment current time (CPU idle)

# 3. After all processes complete:

# Print the Gantt chart

# Compute average waiting and turnaround times
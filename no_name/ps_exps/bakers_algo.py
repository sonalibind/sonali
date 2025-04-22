def is_safe_state(processes, available, max_demand, allocation):
    n = len(processes)
    m = len(available)

    # Calculate Need matrix: Need[i][j] = Max[i][j] - Allocation[i][j]
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    print("\n Need Matrix:")
    for i in range(n):
        print(f"P{i}:", need[i])

    finish = [False] * n
    safe_sequence = []
    work = available[:]

    print("\n Process Execution Steps:")
    while len(safe_sequence) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                print(f"\n P{i} is executing...")
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(f"P{i}")
                print(f"Resources available after P{i}: {work}")
                allocated = True
                break
        if not allocated:
            return False, [], need

    return True, safe_sequence, need

# ------------------------------
# 🌟 MAIN PROGRAM STARTS HERE
# ------------------------------
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter available resources (space-separated):")
available = list(map(int, input().split()))

print("\nEnter Max demand matrix row by row (space-separated):")
max_demand = []
for i in range(n):
    row = list(map(int, input(f"Max for P{i}: ").split()))
    max_demand.append(row)

print("\nEnter Allocation matrix row by row (space-separated):")
allocation = []
for i in range(n):
    row = list(map(int, input(f"Allocation for P{i}: ").split()))
    allocation.append(row)

processes = [f"P{i}" for i in range(n)]

# Run Banker's Algorithm
is_safe, sequence, need = is_safe_state(processes, available, max_demand, allocation)

# Output result
print("\n------------------------------")
if is_safe:
    print(" System is in a SAFE state.")
    print(" Safe sequence:", " -> ".join(sequence))
else:
    print(" System is in an UNSAFE state (deadlock possible).")











# 1. Input n, m, available[], max_demand[], allocation[]
# 2. Calculate Need[][] = Max[][] - Allocation[][]
# 3. Initialize finish[] = False, work[] = available[]
# 4. While there are unfinished processes:
#     a. For each process i:
#         - If Need[i] <= work[], mark as finished, update work[], and add to safe sequence.
#     b. If no process can proceed, return unsafe state.
# 5. Output the safe sequence if found, else unsafe state.

def look_disk_scheduling():
    print("LOOK Disk Scheduling Algorithm")
    
    # Get input
    current_head = int(input("Enter current position of disk head: "))
    direction = input("Enter direction (left/right): ").lower()
    
    n = int(input("Enter number of requests: "))
    requests = list(map(int, input("Enter the request sequence: ").strip().split()))
    
    # Sort the requests
    sorted_requests = sorted(requests)
    
    # Initialize variables
    seek_sequence = [current_head]  # Start with current head position
    total_seek_distance = 0
    
    # LOOK algorithm implementation
    if direction == "right":
        # Handle all requests greater than current head position
        right_requests = [track for track in sorted_requests if track > current_head]
        for track in right_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
        
        # Then handle requests less than current head position (in reverse)
        left_requests = [track for track in sorted_requests if track < current_head]
        left_requests.reverse()  # Process in descending order
        for track in left_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
    
    else:  # direction is left
        # Handle all requests less than current head position
        left_requests = [track for track in sorted_requests if track < current_head]
        left_requests.reverse()  # Process in descending order
        for track in left_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
        
        # Then handle requests greater than current head position
        right_requests = [track for track in sorted_requests if track > current_head]
        for track in right_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
    
    # Output
    print("\nOutput:")
    print(f"Total number of seek operations = {total_seek_distance}")
    # Remove the starting position (current_head) from sequence for final display
    final_sequence = seek_sequence[1:]
    print(f"Seek Sequence is: {final_sequence}")

if __name__ == "__main__":
    look_disk_scheduling()




#     Algorithm Steps

# 1. Input Collection:

# Get current head position (starting point)
# Get direction of initial movement (left/right)
# Get list of track requests to be serviced


#2. Processing:

# Sort all the requests in ascending order
# Split the requests into two groups:

# Requests greater than the current head position
# Requests less than the current head position




#3. Scheduling:

# If direction is "right":

# Service all requests greater than current head position in ascending order
# After reaching the highest requested track, reverse direction
# Service all requests less than current head position in descending order


# If direction is "left":

# Service all requests less than current head position in descending order
# After reaching the lowest requested track, reverse direction
# Service all requests greater than current head position in ascending order




#4. Calculation:

# Calculate total seek distance by summing the absolute differences between consecutive tracks in the sequence
# Record the seek sequence (order in which tracks are visited)


#5. Output:

# Display total seek operations (head movement distance)
# Display the seek sequence
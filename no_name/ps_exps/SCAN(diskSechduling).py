def scan_disk_scheduling():
    print("SCAN Disk Scheduling Algorithm")
    
    # Get input
    current_head = int(input("Enter current position of disk head: "))
    total_tracks = int(input("Enter total number of tracks on disk: "))
    direction = input("Enter direction (left/right): ").lower()
    
    n = int(input("Enter number of requests: "))
    requests = list(map(int, input("Enter the request sequence: ").strip().split()))
    
    # Sort the requests
    sorted_requests = sorted(requests)
    
    # Initialize variables
    seek_sequence = [current_head]  # Start with current head position
    total_seek_distance = 0
    
    # SCAN algorithm implementation
    if direction == "right":
        # Handle all requests greater than current head position
        for track in sorted_requests:
            if track > current_head:
                seek_sequence.append(track)
                total_seek_distance += abs(track - seek_sequence[-2])
        
        # Add the rightmost track if not already included
        if total_tracks - 1 not in seek_sequence and total_tracks - 1 > current_head:
            seek_sequence.append(total_tracks - 1)
            total_seek_distance += abs(total_tracks - 1 - seek_sequence[-2])
        
        # Then move left - reversed order
        reverse_requests = sorted(x for x in sorted_requests if x < current_head)[::-1]
        for track in reverse_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
    
    else:  # direction is left
        # Handle all requests less than current head position
        reverse_requests = sorted(x for x in sorted_requests if x < current_head)[::-1]
        for track in reverse_requests:
            seek_sequence.append(track)
            total_seek_distance += abs(track - seek_sequence[-2])
        
        # Add the leftmost track (0) if not already included
        if 0 not in seek_sequence and 0 < current_head:
            seek_sequence.append(0)
            total_seek_distance += abs(0 - seek_sequence[-2])
        
        # Then move right
        for track in sorted_requests:
            if track > current_head:
                seek_sequence.append(track)
                total_seek_distance += abs(track - seek_sequence[-2])
    
    # Output
    print("\nOutput:")
    print(f"Total number of seek operations = {total_seek_distance}")
    # Remove the starting position (current_head) if needed for final sequence display
    final_sequence = seek_sequence[1:]
    print(f"Seek Sequence is: {final_sequence}")

if __name__ == "__main__":
    scan_disk_scheduling()












# Algorithm Steps

#1. Input Collection:

# Get current head position (starting point)
# Get total number of tracks on the disk
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
# Move to the highest track on disk (if not already there)
# Reverse direction and service all requests less than current head position in descending order


# If direction is "left":

# Service all requests less than current head position in descending order
# Move to the lowest track on disk (track 0, if not already there)
# Reverse direction and service all requests greater than current head position in ascending order




#4. Calculation:

# Calculate total seek distance by summing the absolute differences between consecutive tracks in the sequence
# Record the seek sequence (order in which tracks are visited)


#5. Output:

# Display total seek operations (head movement distance)
# Display the seek sequence
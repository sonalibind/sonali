def fifo_page_replacement():
    print("FIFO Page Replacement Algorithm")
    
    # Get input from user
    n = int(input("Enter the number of pages in the reference string: "))
    reference_string = list(map(int, input("Enter the page reference string: ").strip().split()))
    
    frame_count = int(input("Enter the number of frames (memory size): "))
    frames = []  # List to hold current pages in memory
    page_faults = 0
    
    print("Page Reference\tFrames")
    
    # Process each page reference
    for i, page in enumerate(reference_string):
        # Check if page is already in a frame
        if page not in frames:
            # Page fault occurs
            page_faults += 1
            
            # If frames are available, add the page
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # If frames are full, replace using FIFO
                frames.pop(0)  # Remove the oldest page
                frames.append(page)  # Add the new page
        
        # Print current state
        print(f"{page}\t\t{' '.join(map(str, frames))}")
    
    print(f"\nTotal Page Faults: {page_faults}")
    print("FIFO Algorithm Finished.")

if __name__ == "__main__":
    fifo_page_replacement()


# algo
#1. Input: Page reference string, Number of frames
#2. Initialize: Empty frames list, page_faults = 0
#3. For each page in reference string:

# If page not in frames:

# Increment page_faults
# If frames list is full:

# Remove oldest page (first element)


# Add new page to end of frames


# Print current state of frames


#4. Output: Total page faults
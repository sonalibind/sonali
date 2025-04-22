def lru_page_replacement():
    print("LRU Page Replacement Algorithm")
    
    # Get input from user
    n = int(input("Enter the number of pages in the reference string: "))
    reference_string = list(map(int, input("Enter the page reference string: ").strip().split()))
    
    frame_count = int(input("Enter the number of frames (memory size): "))
    frames = []  # List to hold current pages in memory
    page_faults = 0
    page_usage = {}  # Dictionary to track when each page was last used
    
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
                # If frames are full, replace using LRU
                # Find the least recently used page
                lru_page = min(page_usage, key=lambda k: page_usage[k] if k in frames else float('inf'))
                frames.remove(lru_page)
                frames.append(page)
        
        # Update the usage time for this page
        page_usage[page] = i
        
        # Print current state
        print(f"{page}\t\t{' '.join(map(str, frames))}")
    
    print(f"\nTotal Page Faults: {page_faults}")
    print("LRU Algorithm Finished.")
    print("=== Code Execution Successful ===")

if __name__ == "__main__":
    lru_page_replacement()



# algp
# 1. Input: Page reference string, Number of frames

# 2. Initialize: Empty frames list, page_faults = 0, usage_time dictionary

# 3. For each page in reference string:

# If page not in frames:

# Increment page_faults
# If frames list is full:

# Find page with oldest usage time
# Replace that page with new page


# Else: Add page to frames


# Update usage time for current page
# Print current state of frames


# 4. Output: Total page faults
import sys

# FCFS (First Come First Serve) disk scheduling algorithm
def process_fcfs(request_queue, start_track):
    total_movements = 0
    current_track = start_track
    for request in request_queue:
        total_movements += abs(request - current_track)
        current_track = request
    return total_movements

# SCAN disk scheduling algorithm
def process_scan(request_queue, start_track, num_tracks):
    sorted_requests = sorted(request_queue)
    total_movements = 0
    current_track = start_track
    direction = -1  # Initially moving towards lower tracks
    while sorted_requests:
        if current_track in sorted_requests:
            sorted_requests.remove(current_track)
        if current_track == 0 or current_track == num_tracks - 1:
            direction *= -1  # Change direction
        current_track += direction
        total_movements += 1
    return total_movements

# C-SCAN (Circular SCAN) disk scheduling algorithm
def process_cscan(request_queue, start_track, num_tracks):
    sorted_requests = sorted(request_queue)
    total_movements = 0
    current_track = start_track
    while sorted_requests:
        if current_track in sorted_requests:
            sorted_requests.remove(current_track)
        if current_track == num_tracks - 1:
            current_track = 0  # Move to the beginning after reaching the end
        else:
            current_track += 1  # Move to the next track
        total_movements += 1
    return total_movements

def run_disk_scheduling(start_pos, requests_file):
    try:
        with open(requests_file, 'r') as file:
            request_queue = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Error: File not found.")
        return

    num_tracks = 5000  # Total number of tracks

    # Task 1: Calculate head movements for the original requests
    print("Task 1:")
    print("FCFS Head Movements:", process_fcfs(request_queue.copy(), start_pos))
    print("SCAN Head Movements:", process_scan(request_queue.copy(), start_pos, num_tracks))
    print("C-SCAN Head Movements:", process_cscan(request_queue.copy(), start_pos, num_tracks))

    # Task 2: Calculate head movements for unique requests
    unique_requests = sorted(set(request_queue))
    print("\nTask 2:")
    print("FCFS Head Movements:", process_fcfs(unique_requests, start_pos))
    print("SCAN Head Movements:", process_scan(unique_requests, start_pos, num_tracks))
    print("C-SCAN Head Movements:", process_cscan(unique_requests, start_pos, num_tracks))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py [start_position] [requests_file]")
    else:
        start_pos = int(sys.argv[1])
        requests_file = sys.argv[2]
        run_disk_scheduling(start_pos, requests_file)
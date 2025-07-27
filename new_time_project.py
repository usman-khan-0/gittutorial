import time
import sys
import threading

def display_time():
    while not stop_event.is_set():
        sys.stdout.write("\rProgram starting at: " + time.strftime("%H:%M:%S"))
        sys.stdout.flush()
        time.sleep(1)  # Update every second

def perform_delays():
    print()  # Move to next line after starting time
    for seconds in [0, 20]:
        print(f"Starting {seconds}-second delay...")
        time.sleep(seconds)
        print(f"Finished {seconds}-second delay")
    stop_event.set()  # Signal to stop time display
    print("Program done")

# Global stop event for thread control
stop_event = threading.Event()

# Start time display in a separate thread
time_thread = threading.Thread(target=display_time)
time_thread.start()

# Perform delays in the main thread
perform_delays()

# Wait for the time thread to finish
time_thread.join()
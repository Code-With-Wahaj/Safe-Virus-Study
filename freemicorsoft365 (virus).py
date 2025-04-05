import os
import shutil
import sys

# Automatically determine the Desktop path and safe_virus_study folder
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
WORKING_DIR = os.path.join(DESKTOP_PATH, "safe_virus_study")

# Ensure the directory exists
os.makedirs(WORKING_DIR, exist_ok=True)

# Get the path of the current script, handling PyInstaller executables
def get_script_path():
    if getattr(sys, 'frozen', False):  # Check if running as a PyInstaller executable
        return sys.executable  # Path to the executable
    else:
        return __file__  # Path to the script when running as a .py file

# Self-replication function to create executable replicas
def replicate(script_path):
    # Ensure that we don't replicate the replica over itself
    if os.path.basename(script_path) in ['replica_1.py', 'replica_2.py', 'replica_3.py']:
        print(f"Skipping replication for {script_path} as it's a replica.")
        return

    for i in range(1, 4):  # Create 3 copies
        replica_name = f"replica_{i}.py"
        replica_path = os.path.join(WORKING_DIR, replica_name)

        # Copy the original executable to the new replica path
        shutil.copy(script_path, replica_path)

        print(f"Replicated: {replica_path}")

        # Add logic for each replica to replicate itself when run
        # (Ensure the replica doesn't overwrite itself)
        if not os.path.exists(replica_path + ".replicated"):  # Check if the replica has already replicated
            with open(replica_path + ".replicated", 'w') as f:
                f.write("This replica has already executed replication.")

            # Instruct the replica to replicate more
            replicate(replica_path)  # Call the replicate function recursively for each replica

# File modification simulation
def modify_files():
    for file_name in os.listdir(WORKING_DIR):
        file_path = os.path.join(WORKING_DIR, file_name)
        if file_name.endswith(".txt"):
            with open(file_path, "a") as file:
                file.write("\nThis file has been safely modified by a benign script.\n")
            print(f"Modified: {file_path}")

# Main function
if __name__ == "__main__":
    script_path = get_script_path()  # Get the current script path
    replicate(script_path)  # Replicate the script as executables
    modify_files()  # Modify dummy files

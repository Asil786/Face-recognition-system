import os

def main():
    # Open a file for writing
    file_name = "example.txt"
    with open(file_name, 'w') as f:
        f.write("Hello, this is a sample text.")

    # Read from the file
    with open(file_name, 'r') as f:
        content = f.read()
        print("Content of the file:", content)

    # Close the file

    # Get process ID (PID)
    pid = os.getpid()
    print("Process ID:", pid)

    # Set the process group ID (PGID) - Not supported in Windows
    if os.name != 'nt':
        os.setpgid(pid, 0)
        print("Process group ID:", os.getpgid(pid))

    # Get user ID (UID)
    # uid = os.getuid()
    # print("User ID:", uid)

    # Get group ID (GID)
    gid = os.getgid()
    print("Group ID:", gid)

    # Get effective group ID (EGID)
    egid = os.getegid()
    print("Effective Group ID:", egid)

    # Get effective user ID (EUID)
    euid = os.geteuid()
    print("Effective User ID:", euid)

    # Remove the file
    os.remove(file_name)

if __name__ == "__main__":
    main()

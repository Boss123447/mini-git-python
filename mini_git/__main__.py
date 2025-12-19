import sys
from . import commands

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m mini_git <command> [args...]")
        print("Commands: init, add, commit, log")
        return
    
    cmd = sys.argv[1]

    if cmd == 'init':
        commands.cmd_init()
    
    elif cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: python - m mini_git add <file>")
            return
        commands.cmd_add(sys.argv[2])

    elif cmd == "commit":
        if len(sys.argv) < 3:
            print('Usage: python -m mini_git commit "<message>"')
            return
        message = " ".join(sys.argv[2:])
        commands.cmd_commit(message)

    elif cmd == "log":
        commands.cmd_log()

    else:
        print(f"Unknown command: {cmd}")
        print("Commands: init, add, commit, log")
        
if __name__ == "__main__":
    main()
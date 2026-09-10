import argparse 

def add_task(args):
    # This function should accept 'args' and print: ✅ Task added: <description>
    print(f"✅ Task added: {args.description}")

def list_tasks(args):
    print("📋 Listing all tasks...")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    subparsers = parser.add_subparsers()

    # - For "add", require a "description" argument and set its handler
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.set_defaults(func=add_task)

    # - For "list", just set the handler to list_tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_tasks)

    # - Parse the arguments and call the appropriate handler (if exists)'''
    args = parser.parse_args()

    if hasattr (args, "func"):
        args.func(args)         # call function dynamically
    else:
        parser.print_help()
#!/usr/bin/env python3
"""todo-cli-python — a simple command-line todo app with JSON storage.

Usage:
    python todo.py add "Buy milk"
    python todo.py list
    python todo.py done 1
    python todo.py delete 2
    python todo.py clear

Tasks are stored in todos.json next to this script. Standard library only.
"""

import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        print("Warning: todos.json is corrupt, starting fresh.", file=sys.stderr)
        return []


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def cmd_add(args):
    tasks = load_tasks()
    tasks.append({"task": args.text, "done": False})
    save_tasks(tasks)
    print(f'Added #{len(tasks)}: {args.text}')


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python todo.py add \"Your task\"")
        return
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['task']}")


def _pick(tasks, number):
    if number < 1 or number > len(tasks):
        print(f"Error: no task #{number}.", file=sys.stderr)
        sys.exit(1)
    return tasks[number - 1]


def cmd_done(args):
    tasks = load_tasks()
    task = _pick(tasks, args.number)
    task["done"] = True
    save_tasks(tasks)
    print(f"Done #{args.number}: {task['task']}")


def cmd_delete(args):
    tasks = load_tasks()
    task = _pick(tasks, args.number)
    del tasks[args.number - 1]
    save_tasks(tasks)
    print(f"Deleted #{args.number}: {task['task']}")


def cmd_clear(args):
    tasks = [t for t in load_tasks() if not t["done"]]
    save_tasks(tasks)
    print("Cleared all completed tasks.")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI todo app.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("text", help="Task description")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="List all tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("number", type=int, help="Task number from list")
    p_done.set_defaults(func=cmd_done)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("number", type=int, help="Task number from list")
    p_del.set_defaults(func=cmd_delete)

    p_clear = sub.add_parser("clear", help="Remove all completed tasks")
    p_clear.set_defaults(func=cmd_clear)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

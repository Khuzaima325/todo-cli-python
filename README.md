# Todo CLI (Python)

A simple command-line todo app written in Python using only the standard library. Add tasks, list them, mark them done, and delete them — everything is saved to a local `todos.json` file so your list survives between runs.

## Features

- Add, list, complete, and delete tasks
- Clear all completed tasks in one command
- Tasks persist in `todos.json` (plain JSON, easy to back up or edit)
- No dependencies — works with any Python 3.8+ install

## How to run

```bash
python todo.py add "Buy milk"
python todo.py list
python todo.py done 1
python todo.py delete 2
python todo.py clear
```

## Commands

| Command | What it does |
| --- | --- |
| `add "text"` | Add a new task |
| `list` | Show all tasks with their status |
| `done N` | Mark task number N as done |
| `delete N` | Delete task number N |
| `clear` | Remove all completed tasks |

## License

MIT — see [LICENSE](LICENSE).

Built by @khuzaima.tech

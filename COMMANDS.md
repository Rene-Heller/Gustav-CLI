# CLI Command Documentation

This repository defines a Click-based command-line interface in `src/cli/main.py`.
The primary package entry point is `Gustav`, which exposes a grouped CLI with several commands.
Additional scripts are also registered as standalone Click commands.

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

- On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- On Windows (cmd):

```cmd
.venv\Scripts\activate.bat
```

- On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install the package from the project root:

```bash
pip install .
```

## Command Summary

| Command | Description |
|---|---|
| `Gustav hello` | Print a friendly greeting. |
| `Gustav status` | Show system status; use `--verbose` for detailed health checks. |
| `Gustav greet <name>` | Greet a user by name. |
| `Gustav repeat <message>` | Repeat a message multiple times with optional `--times`. |
| `Gustav sum <a> <b>` | Add two integers and print the result. |
| `Gustav subcommand` | Print a message about Gustav's subcommands. |
| `form_answer` | Read stdin and echo the input prefixed with `The result is:`. |
| `command` | Print a demonstration message for a generic command. |
| `flag` | Print an explanation of how CLI flags work. |
| `option` | Print an explanation of how CLI options work. |
| `pipe` | Print an explanation of pipe usage. |

## `Gustav` Group Commands

These commands are registered to the `Gustav` command group in `main.py`.

### `Gustav hello`

Prints a friendly greeting message.

Example:

```bash
Gustav hello
```

Output:

```
Hello dear Master Kevin!
```

### `Gustav status`

Prints a service status summary.

Options:

- `--verbose`, `-v`
  - Prints detailed status lines for CPU, memory, and disk.

Examples:

```bash
Gustav status
```

```bash
Gustav status --verbose
```

### `Gustav greet <name>`

Prints a personalized greeting for the provided `name`.

Arguments:

- `name` — the name to greet.

Example:

```bash
Gustav greet Alice
```

Output:

```
Hello Alice! Nice to have you here :)
```

### `Gustav repeat <message>`

Prints the given message multiple times.

Arguments:

- `message` — the text to repeat.

Options:

- `--times`, `-t` — number of repetitions (default: `2`).

Example:

```bash
Gustav repeat "Hello world" --times 3
```

Output:

```
1: Hello world
2: Hello world
3: Hello world
```

### `Gustav sum <a> <b>`

Adds two integer arguments and prints the result.

Arguments:

- `a` — first integer.
- `b` — second integer.

Example:

```bash
Gustav sum 3 8
```

Output:

```
11
```

### `Gustav subcommand`

Prints a short message about nested commands and the command group's identity.

Example:

```bash
Gustav subcommand
```

Output:

```
My commands behave like any other commands. But they are part of me: Gustav!
```

## Standalone Commands

These commands are also available as separate entry points from `pyproject.toml`.

### `form_answer`

Reads text from stdin and prints it prefixed with `The result is:`.

Example:

```bash
echo "42" | form_answer
```

Output:

```
The result is: 42
```

### `command`

Prints a demonstration message for a generic command.

Example:

```bash
command
```

### `flag`

Prints an explanation of how CLI flags work.

Example:

```bash
flag
```

### `option`

Prints an explanation of how CLI options work.

Example:

```bash
option
```

### `pipe`

Prints an explanation of pipe usage and how it can feed values between commands.

Example:

```bash
pipe
```

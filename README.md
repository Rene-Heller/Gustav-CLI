# Gustav-CLI
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
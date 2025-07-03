# The Breakup Project: Terminal-Based Breakup Journal

A terminal-based journaling and emotional progress tracker, built to help you process through code. lol.

No fancy UI. No cloud sync. Just your thoughts in a text file, and a graph that shows you're getting better even when it doesn't feel like it. Dont forget your own journal.txt file

## Features

- Simple CLI for daily journaling
- Timestamped entries saved to `journal.txt`
- Emotion tracking and analysis (future feature)
- Data visualization (future feature)

## Prerequisites

- Python 3.7 or higher installed on your system

## Installation

### Windows (PowerShell/Command Prompt)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rush1120/thebreakupproject.git
   cd thebreakupproject
   ```
2. **Install dependencies and build the package:**
   ```bash
   py -m pip install .
   ```

### Linux/macOS (Terminal)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rush1120/thebreakupproject.git
   cd thebreakupproject
   ```
2. **Install dependencies and build the package:**
   ```bash
   pip install .
   ```

## Usage

### Option 1: Using the installed command (recommended)

After installation, start a new journal entry by running:

**Windows:**

```bash
breakup-journal
```

**Linux/macOS:**

```bash
breakup-journal
```

### Option 2: Running directly

If the installed command doesn't work, you can run the script directly:

**Windows:**

```bash
py breakup_journal/main.py
```

**Linux/macOS:**

```bash
python3 breakup_journal/main.py
```

Follow the prompts to write your entry. Entries are saved in `journal.txt` with a timestamp.

## Tips

- **For development with virtual environment:**

  **Windows:**

  ```bash
  # Create virtual environment
  py -m venv venv

  # Activate virtual environment
  venv\Scripts\activate

  # Install project
  py -m pip install .

  # Deactivate when done
  deactivate
  ```

  **Linux/macOS:**

  ```bash
  # Create virtual environment
  python3 -m venv venv

  # Activate virtual environment
  source venv/bin/activate

  # Install project
  pip install .

  # Deactivate when done
  deactivate
  ```

## Development

- Main code: `breakup_journal/main.py`
- Package config: `setup.py`
- Journal file: `journal.txt`

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

## Privacy

Your entries are stored **locally** in `journal.txt`. Nothing is uploaded or shared.

## License

MIT

# The Breakup Project: Terminal-Based Breakup Journal

A terminal-based journaling and emotional progress tracker, built to help you process through code. lol.

No fancy UI. No cloud sync. Just your thoughts in a text file, and a graph that shows you're getting better even when it doesn't feel like it.
Dont forget your own journal.txt file

## Features
- Simple CLI for daily journaling
- Timestamped entries saved to `journal.txt`
- Emotion tracking and analysis (future feature)
- Data visualization (future feature)

## Installation

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

To start a new journal entry, run:

```bash
breakup-journal
```

Follow the prompts to write your entry. Entries are saved in `journal.txt` with a timestamp.

## Tips
- Always activate your virtual environment before running scripts:
  ```bash
  source venv/bin/activate
  ```
- To exit the virtual environment:
  ```bash
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

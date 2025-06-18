# breakup-journal

A terminal-based journaling and emotional progress tracker, built to help you process through code. lol.

No fancy UI. No cloud sync. Just your thoughts in a text file, and a graph that shows you're getting better  even when it doesn't feel like it.
Dont forget to add your own journal.txt file
---

## Requirements

- Python 3.8+
- pip
- virtualenv (recommended)

---

##  Setup

Clone the repo and set up your virtual environment:

```bash
git clone https://github.com/Rush1120/thebreakupproject
cd breakup-journal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install dependencies manually:

```bash
pip3 install vaderSentiment matplotlib pandas
```

---

##  Writing a Journal Entry

Run the following command and follow the prompt:

```bash
python main.py
```

- Type your entry.  
- Press Enter twice to save.

Your entries are saved in `journal.txt`.

---

##  Analyzing Your Progress

To visualize your emotional healing over time:

```bash
python analyzer.py
```

A graph will pop up, showing your sentiment scores for each entry

---

## File Structure

- `main.py` — Write new journal entries.
- `analyzer.py` — Analyze and plot your emotional progress.
- `journal.txt` — Your private journal entries.

---

## Tips

- Always activate your virtual environment before running scripts okay:
  ```bash
  source venv/bin/activate
  ```
- To exit the virtual environment:
  ```bash
  deactivate
  ```

---

## Privacy

Your entries are stored **locally** in `journal.txt`. Nothing is uploaded or shared.

---

##  Contributing

Pull requests and issues are welcome fr

---

## License

MIT

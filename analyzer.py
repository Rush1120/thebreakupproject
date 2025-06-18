from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
import re
from datetime import datetime

def extract_entries(file_path="journal.txt"):
    with open(file_path, "r") as f:
        content = f.read()
        
        entries = re.findall(r"\[(.*?)\]\n(.*?)(?=\n\[|$)", content, re.DOTALL)
        data = []
        for timestamp, text in entries:
            try:
                dt = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
            except:
                continue
            data.append((dt, text.strip()))
        return data

def analyze_and_plot(entries):
    analyzer = SentimentIntensityAnalyzer()
    results = []

    for dt, text in entries:
        score = analyzer.polarity_scores(text)["compound"]
        results.append({"date": dt, "sentiment": score})

    df = pd.DataFrame(results)
    df.sort_values("date", inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["sentiment"], marker='o', linestyle='-', color='teal')
    plt.title("📈 Your Emotional Healing Over Time", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score (-1 to +1)")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    entries = extract_entries()
    print(f"DEBUG: Extracted entries: {entries}")  # Add this line
    if not entries:
        print("No journal entries found. Go cry in `main.py` first.")
    else:
        analyze_and_plot(entries)

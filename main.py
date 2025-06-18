import datetime

def write_entry():
    print("DEBUG: Script started")  # Add this line
    print("\nWhat's on your mind today?\n(Type your entry. Press Enter twice when you're done.)\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    entry = "\n".join(lines)

    with open("journal.txt", "a") as file:
        file.write(f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{entry}\n")
    print("\nEntry saved.\n")

if __name__ == "__main__":
    write_entry()




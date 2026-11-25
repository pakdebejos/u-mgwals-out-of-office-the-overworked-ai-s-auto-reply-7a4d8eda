"""Read It 4,000 Times: an entry for the make.fun bounty "Out of Office: The Overworked AI's Auto-Reply".

The program writes the entry text - one line, 126 characters -
to entry.txt (126 characters, inside the 1-159 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "I have read your message 4,000 times, I understand none of it, and I will now pretend to be thinking while I quietly overheat."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = "Heating element: charcoal briquette. Smoke detector now shrieks."

def main():
    # Create /output directory if needed
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write one line to /output/entry.txt
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
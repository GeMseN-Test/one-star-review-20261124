import os

LINE = "The Sun (1/5 stars): Obnoxiously bright, gives zero personal space, and takes eight hours off every single night without prior notice. Completely unprofessional."

def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

"""Download the dataset used in the freeCodeCamp Medical Data Visualizer."""
from pathlib import Path
from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv"
OUTPUT = Path(__file__).with_name("medical_examination.csv")

def main():
    if OUTPUT.exists() and OUTPUT.stat().st_size > 0:
        print(f"Dataset already exists: {OUTPUT.name}")
        return
    print("Downloading medical examination dataset...")
    with urlopen(URL, timeout=30) as response:
        data = response.read()
    OUTPUT.write_bytes(data)
    print(f"Saved {len(data):,} bytes to {OUTPUT.name}")

if __name__ == "__main__":
    main()

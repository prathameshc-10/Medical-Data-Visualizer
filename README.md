# Medical Data Visualizer

This project uses Pandas, Matplotlib, Seaborn, and NumPy to visualize medical examination data.

## Included files

- `medical_data_visualizer.py` — builds the categorical plot and correlation heat map.
- `main.py` — runs both plots.
- `test_module.py` — basic tests that check figure generation.
- `download_dataset.py` — downloads `medical_examination.csv`.
- `requirements.txt` — Python dependencies.

## Setup

Use Python 3.9 or newer. Open a terminal in this folder and run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install the dependencies and download the dataset:

```bash
python -m pip install -r requirements.txt
python download_dataset.py
```

## Run the charts

```bash
python main.py
```

The program saves `catplot.png` and `heatmap.png` in the project folder.

## Run tests

```bash
python -m unittest test_module.py
```

## Notes for freeCodeCamp

The analyzer uses `medical_examination.csv` from the freeCodeCamp boilerplate repository. If you are using the official freeCodeCamp starter code, keep its provided `test_module.py` and run those tests as well; the tests in this package are basic smoke tests.

## Interpretation

The charts describe associations in this dataset. They do not establish that any factor causes cardiovascular disease.

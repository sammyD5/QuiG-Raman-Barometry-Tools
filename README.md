#  Quartz-in-Garnet Raman Spectral Analysis

## Key Features
* **Baseline Correction:** Automated baseline subtraction using the Asymmetric Least Squares (ALS) algorithm.
* **Temperature Correction:** Integrated Bose-Einstein temperature correction for high-quality spectral analysis.
* **Peak Fitting:** Robust Pseudo-Voigt fitting (Levenberg-Marquardt) for accurate determination of peak centers and FWHM.
* **High-Resolution Output:** Automatic generation of publication-ready plots (900 DPI).
* **Reproducibility:** Saves full analysis results in JSON format for easy reloading and batch processing.

---

## Installation

### Prerequisites
* **Python 3.12.10** (The core analysis module is pre-compiled for Python 3.12.10).
* Required libraries: `numpy`, `scipy`, `matplotlib`.

### Setup
1. Clone this repository or download the ZIP file.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

 ## Usage
 1. Place your Raman data (`.txt` files) in your working directory. Data should be in two columns: `Wavenumber` and `Intensity`.
 2. Open `run_QuiG_Raman_Spectral_Analysis.py` and update the **USER CONFIGURATION** section:
    ```bash
    # Example Configuration
    QUARTZ_INCLUSION_FILE = r'path/to/your/data.txt'
    FILE_PREFIX = 'Sample_01'  # Prefix for output filenames
    OUTPUT_DIRECTORY = 'Results'
 3. Run the script:
    ```bash
    python run_QuiG_Raman_Spectral_Analysis.py


 ## Output Files
 The tool generates several diagnostic and result files in your specified output directory:
 * `[Prefix]_corrected_spectrum.png` : processed spectrum after baseline and temperature corrections.
 * `[Prefix]_spectrum_with_peaks.png` : overview of identified peaks with markers.
 * `[Prefix]_pseudo_voigt_fits.png` : detailed view of individual peak fits and residuals.
 * `[Prefix]_analysis_summary.txt` : text summary of peak positions and FWHM.
 * `[Prefix]_analysis_results.json` : full data structure for programmatic use or reloading.

---

# Quartz-in-Garnet Correlation and Anisotropy Check

## Key Features
* **Raman Shift Correlation:**  Calculates Δω = ω(standard) - ω(sample) for 464, 207, and 128 peaks of quartz
* **Residual Pressure Caclulation:** Hydrostatic appreoach to calculate an initial pressure estimate
* **Published Pressure Calibration:** 3 sets of published calibrations from - Schmidt & Ziemann (2000), Enami et al. (2007), and Ashley et al. (2014)

  ---

  ## Installation
  
  ### Prerequisites
* **Python 3.12.10** (The core analysis module is pre-compiled for Python 3.12.10).
* Ensure Python 3.7+ is installed with required packages - `numpy`, `scipy`, `matplotlib`, `pandas`

### Setup
1. Clone this repository or download the ZIP file.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Prepare your input data: Ensure your data file follows the format described in the [example_QuiG_data.txt](#input-data-format).
2. Open the runner script: Open `run_QuiG_Correlation_Anisotropy.py` in a text editor (e.g., VS Code, Notepad++, or Spyder).
3. Update the configuration: Set the `INPUT_DATA_FILE` path to point to your data and define your `OUTPUT_DIRECTORY`.
4. Customize plot appearance (Optional): You can modify the `CORRELATION_PLOT` dictionary to change how your results look:
    ```python
    CORRELATION_PLOT = {
        'marker': 'o',      # Shape: 'o', 's', '^', 'D', '*'
        'color': '#2E86AB', # Color (hex code or name)
        'size': 120,        # Size of markers
        'dpi': 900          # Resolution (900 is publication quality)
    }
    ```
5. Run the analysis: Open your terminal or command prompt and execute:
    ```bash
    python run_QuiG_Correlation_Anisotropy.py
    ```
6. View Results: Once complete, all plots and data tables will be saved in your specified `OUTPUT_DIRECTORY`.


 ## Output Files
 The tool generates several diagnostic and result files in your specified output directory:
 * `correlation_diagram_delta.png` : correlation between different Raman shift measurement (Δω₁ vs Δω₂).
 * `pressure_comparison_P1_vs_P2.png` : diagnostic plot for pressure consistency.
 * `QuiG_analysis_summary.txt` : includes all sample results and statistics.
 * `QuiG_analysis_results.csv` : results in spreadsheet format
 * `QuiG_analysis_results.json` : full data structure for reloading.

---

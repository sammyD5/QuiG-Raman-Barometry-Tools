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
* **Python 3.12** (The core analysis module is pre-compiled for Python 3.12).
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
 * `[Prefix]_corrected_spectrum.png` : The processed spectrum after baseline and temperature corrections.
 * `[Prefix]_spectrum_with_peaks.png` : Overview of identified peaks with markers.
 * `[Prefix]_pseudo_voigt_fits.png` : Detailed view of individual peak fits and residuals.
 * `[Prefix]_analysis_summary.txt` : A human-readable text summary of peak positions and FWHM.
 * `[Prefix]_analysis_results.json` : Full data structure for programmatic use or reloading.


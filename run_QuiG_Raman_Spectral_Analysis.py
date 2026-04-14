"""
Raman Spectroscopy Analysis - User Script
==========================================
This script provides a simple interface to run Raman analysis.
Users only need to modify the configuration section below.

Author: Samaroha Das (Sammy)
Contact: samaroha.das@postgrad.curtin.edu.au
Date: 2026-04-14
"""

# Import the core analysis module
from QuiG_Raman_Spectral_Analysis_Core import analyze_raman_spectra, load_results_from_file
import os

# ===============================
# USER CONFIGURATION
# ===============================

# Path to your quartz inclusion Raman spectrum file
QUARTZ_INCLUSION_FILE = r'C:\Users\21910478\OneDrive - Curtin\Curtin_PhD\Data\Southern India\Raman Barometry\IO6-79E_2026-04-13\IO6-79E_Qtz_2_008.txt'

# Specify a prefix for your output files (e.g., 'Inclusion_1', 'Sample_A')
FILE_PREFIX = 'IO6-79E_Qtz_2' # If left as None or '', it will automatically use the name of the input file.

# Output directory for results and plots
OUTPUT_DIRECTORY = 'Raman_Analysis_Output'

# Analysis parameters
LASER_WAVELENGTH = 532  # Laser wavelength in nm (common: 532, 633, 785)
TEMPERATURE = 298       # Temperature in Kelvin (25°C = 298 K)

# Plot parameters
PLOT_XLIM = 1000        # X-axis limit for all plots in cm⁻¹
SAVE_DPI = 900          # Resolution for saved plots (higher = better quality)

# Processing options
APPLY_BOSE_EINSTEIN = True  # Apply Bose-Einstein temperature correction

# ===============================
# RUN ANALYSIS
# ===============================

if __name__ == "__main__":
    
    print("\n" + "="*80)
    print("RAMAN SPECTROSCOPY ANALYSIS TOOL")
    print("="*80)
    print("\nThis tool performs comprehensive Raman spectroscopy analysis including:")
    print("  • Baseline correction (ALS algorithm)")
    print("  • Bose-Einstein temperature correction")
    print("  • Pseudo-Voigt peak fitting (Levenberg-Marquardt)")
    print("  • FWHM calculation")
    print("  • High-resolution plot saving (900 DPI)")
    print("  • Results saving and reloading capability")
    print("\n" + "="*80 + "\n")
    
    # Check if file exists
    if not os.path.exists(QUARTZ_INCLUSION_FILE):
        print(f"⚠ ERROR: File not found!")
        print(f"   {QUARTZ_INCLUSION_FILE}")
        print("\nPlease update QUARTZ_INCLUSION_FILE in this script to point to your data file.")
        input("\nPress Enter to exit...")
    else:
        # Determine naming prefix
        base_filename = os.path.splitext(os.path.basename(QUARTZ_INCLUSION_FILE))[0]
        final_prefix = FILE_PREFIX if FILE_PREFIX else base_filename

        print(f"✓ File found: {os.path.basename(QUARTZ_INCLUSION_FILE)}")
        print(f"✓ Output Prefix: {final_prefix}")
        print(f"✓ Output directory: {OUTPUT_DIRECTORY}")
        print(f"✓ Laser wavelength: {LASER_WAVELENGTH} nm")
        print(f"✓ Temperature: {TEMPERATURE} K")
        print(f"✓ Plot resolution: {SAVE_DPI} DPI")
        print("\nStarting analysis...\n")
        
        try:
            # Run the analysis
            results = analyze_raman_spectra(
                quartz_file=QUARTZ_INCLUSION_FILE,
                output_dir=OUTPUT_DIRECTORY,
                apply_bose_einstein=APPLY_BOSE_EINSTEIN,
                laser_wavelength=LASER_WAVELENGTH,
                temperature=TEMPERATURE,
                plot_xlim=PLOT_XLIM,
                save_dpi=SAVE_DPI,
                prefix=final_prefix  # Pass the prefix to the core
            )
            
            print("\n" + "="*80)
            print("✓ ANALYSIS COMPLETE!")
            print("="*80)
            print(f"\nTotal peaks fitted: {len(results['fit_results'])}")
            print(f"\nAll plots saved at {SAVE_DPI} DPI with prefix '{final_prefix}_'")
            print(f"Location: {OUTPUT_DIRECTORY}/")
            
            print("\nResults stored in 'results' dictionary with keys:")
            print("  • 'wavenumber': Raman shift values")
            print("  • 'raw_intensity': Original intensity data")
            print("  • 'corrected_intensity': Processed intensity")
            print("  • 'baseline': Calculated baseline")
            print("  • 'fit_results': Peak fitting parameters and statistics")
            
            print("\n" + "="*80)
            print("OUTPUT FILES:")
            print("="*80)
            # Dynamic names in the print-out summary
            print(f"  • {OUTPUT_DIRECTORY}/{final_prefix}_corrected_spectrum.png")
            print(f"  • {OUTPUT_DIRECTORY}/{final_prefix}_spectrum_with_peaks.png")
            print(f"  • {OUTPUT_DIRECTORY}/{final_prefix}_pseudo_voigt_fits.png")
            print(f"  • {OUTPUT_DIRECTORY}/{final_prefix}_analysis_results.json")
            print(f"  • {OUTPUT_DIRECTORY}/{final_prefix}_analysis_summary.txt")
            
            print("\n" + "="*80)
            print("TO RELOAD RESULTS LATER:")
            print("="*80)
            print(f"  from QuiG_Raman_Spectral_Analysis_Core import load_results_from_file")
            print(f"  results = load_results_from_file('{OUTPUT_DIRECTORY}/{final_prefix}_analysis_results.json')")
            
            print("\n" + "="*80)
            print("PEAK SUMMARY:")
            print("="*80)
            for peak_name, result in sorted(results['fit_results'].items(), key=lambda x: float(x[0])):
                print(f"  Peak {peak_name}: {result['center']:.2f} cm⁻¹ (FWHM: {result['fwhm']:.2f} cm⁻¹)")
            
            print("\n✓ Analysis completed successfully!")
            print("="*80 + "\n")
            
        except Exception as e:
            print("\n" + "="*80)
            print("⚠ ERROR DURING ANALYSIS")
            print("="*80)
            print(f"\nError message: {str(e)}")
            print("\nPlease check:")
            print("  1. File path is correct")
            print("  2. Output directory permissions")
            print("  3. Your core module is compiled correctly")
            print("\n" + "="*80 + "\n")
            import traceback
            traceback.print_exc()
        
        input("\nPress Enter to exit...")


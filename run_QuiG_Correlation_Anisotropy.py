"""
QuiG Correlation and Anisotropy Analysis - User Script
=======================================================
This script provides a simple interface to run QuiG barometry analysis.
Users only need to modify the configuration section below.

Author: Samaroha Das (Sammy)
Contact: samaroha.das@postgrad.curtin.edu.au
Date: 2026-04-16
"""

# Import the core analysis module
from QuiG_Correlation_Anisotropy_Core import (
    load_peak_data,
    calculate_raman_shifts,
    calculate_residual_pressures,
    plot_correlation_diagram,
    plot_pressure_comparison,
    save_analysis_results,
    create_output_directory,
    RAMAN_DERIVATIVES,
    STANDARD_QUARTZ_PEAKS
)

# ===============================
# USER CONFIGURATION
# ===============================

# Path to your input data file
# Format: Tab or comma-delimited with 4 columns
# Column 1: Sample Label
# Column 2: 128 cm⁻¹ peak position
# Column 3: 207 cm⁻¹ peak position
# Column 4: 464 cm⁻¹ peak position
INPUT_DATA_FILE = r'C:\path\to\your\quartz_peak_data.txt'

# Output directory for results and plots
OUTPUT_DIRECTORY = 'QuiG_Analysis_Output'

# ===============================
# PLOT CUSTOMIZATION
# ===============================

# Correlation Diagram (Δω1 vs Δω2)
CORRELATION_PLOT = {
    'marker': 'o',           # Marker style: 'o', 's', '^', 'D', '*', etc.
    'color': '#2E86AB',      # Marker color (hex or name)
    'size': 120,             # Marker size
    'figsize': (10, 8),      # Figure size (width, height) in inches
    'dpi': 900              # Resolution for saved plot
}

# Pressure Comparison Diagram (P1 vs P2)
PRESSURE_PLOT = {
    'marker': 's',           # Marker style
    'color': '#A23B72',      # Marker color
    'size': 120,             # Marker size
    'figsize': (10, 10),     # Figure size (width, height) in inches
    'dpi': 900              # Resolution for saved plot
}

# ===============================
# ANALYSIS PARAMETERS
# ===============================

# Delimiter in input file ('auto', 'tab', or 'comma')
DATA_DELIMITER = 'auto'

# Derivative set to use for pressure calculations
# Options: 'Schmidt_Ziemann_2000', 'Enami_2007', 'Ashley_2014'
DERIVATIVE_SET = 'Enami_2007'

# Standard (unstressed) quartz peak positions (cm⁻¹)
# Modify only if you have better calibrated reference values
STANDARD_PEAKS = {
    '128': 128.0,
    '207': 207.0,
    '464': 464.0
}

# ===============================
# RUN ANALYSIS
# ===============================

if __name__ == "__main__":
    
    import os
    
    print("\n" + "="*80)
    print("QuiG BAROMETRY ANALYSIS TOOL")
    print("Quartz-in-Garnet Correlation and Anisotropy Analysis")
    print("="*80)
    print("\nThis tool performs:")
    print("  • Raman shift correlation analysis (Δω₁ vs Δω₂)")
    print("  • Residual pressure calculations (hydrostatic approach)")
    print("  • High-resolution publication-quality plots")
    print("  • Comprehensive results export (JSON, CSV, TXT)")
    print("\n" + "="*80 + "\n")
    
    # Check if input file exists
    if not os.path.exists(INPUT_DATA_FILE):
        print(f"⚠ ERROR: Input file not found!")
        print(f"   {INPUT_DATA_FILE}")
        print("\nPlease update INPUT_DATA_FILE in this script.")
        print("\nExpected file format (tab or comma-delimited):")
        print("  Label    Peak_128    Peak_207    Peak_464")
        print("  Sample1  127.5       206.8       463.2")
        print("  Sample2  128.2       207.3       464.5")
        print("  ...")
        input("\nPress Enter to exit...")
    else:
        print(f"✓ Input file found: {os.path.basename(INPUT_DATA_FILE)}")
        print(f"✓ Output directory: {OUTPUT_DIRECTORY}")
        print(f"✓ Derivative set: {DERIVATIVE_SET}")
        print(f"✓ Plot resolution: {CORRELATION_PLOT['dpi']} DPI")
        print("\nStarting analysis...\n")
        
        try:
            # Create output directory
            output_dir = create_output_directory(OUTPUT_DIRECTORY)
            
            # Step 1: Load peak data
            print("="*80)
            print("STEP 1: Loading Peak Data")
            print("="*80)
            data = load_peak_data(INPUT_DATA_FILE, delimiter=DATA_DELIMITER)
            print()
            
            # Step 2: Calculate Raman shifts (Δω1 and Δω2)
            print("="*80)
            print("STEP 2: Calculating Raman Shifts")
            print("="*80)
            shift_results = calculate_raman_shifts(data, standard_peaks=STANDARD_PEAKS)
            print()
            
            # Step 3: Plot correlation diagram
            print("="*80)
            print("STEP 3: Generating Correlation Diagram (Δω₁ vs Δω₂)")
            print("="*80)
            plot_correlation_diagram(
                shift_results,
                output_dir=output_dir,
                marker=CORRELATION_PLOT['marker'],
                color=CORRELATION_PLOT['color'],
                size=CORRELATION_PLOT['size'],
                save_dpi=CORRELATION_PLOT['dpi'],
                figsize=CORRELATION_PLOT['figsize']
            )
            print()
            
            # Step 4: Calculate residual pressures
            print("="*80)
            print("STEP 4: Calculating Residual Pressures")
            print("="*80)
            pressure_results = calculate_residual_pressures(
                shift_results['data'],
                derivative_set=DERIVATIVE_SET,
                standard_peaks=STANDARD_PEAKS
            )
            print()
            
            # Step 5: Plot pressure comparison
            print("="*80)
            print("STEP 5: Generating Pressure Comparison Diagram (P₁ vs P₂)")
            print("="*80)
            plot_pressure_comparison(
                pressure_results,
                output_dir=output_dir,
                marker=PRESSURE_PLOT['marker'],
                color=PRESSURE_PLOT['color'],
                size=PRESSURE_PLOT['size'],
                save_dpi=PRESSURE_PLOT['dpi'],
                figsize=PRESSURE_PLOT['figsize']
            )
            print()
            
            # Step 6: Save results
            print("="*80)
            print("STEP 6: Saving Analysis Results")
            print("="*80)
            json_file, csv_file, summary_file = save_analysis_results(
                shift_results,
                pressure_results,
                output_dir
            )
            print()
            
            # Display summary
            print("\n" + "="*80)
            print("✓ ANALYSIS COMPLETE!")
            print("="*80)
            
            data_with_results = pressure_results['data']
            
            print(f"\nAnalyzed {len(data_with_results)} samples")
            print(f"\nAll outputs saved in: {OUTPUT_DIRECTORY}/")
            
            print("\n" + "="*80)
            print("OUTPUT FILES:")
            print("="*80)
            print(f"  • correlation_diagram_Delta_omega.png")
            print(f"  • pressure_comparison_P1_vs_P2.png")
            print(f"  • QuiG_analysis_results.json (complete data)")
            print(f"  • QuiG_analysis_results.csv (spreadsheet format)")
            print(f"  • QuiG_analysis_summary.txt (human-readable report)")
            
            print("\n" + "="*80)
            print("QUICK SUMMARY:")
            print("="*80)
            print("\nRaman Shift Statistics:")
            print(f"  Δω₁: {data_with_results['Delta_omega1'].mean():.3f} ± {data_with_results['Delta_omega1'].std():.3f} cm⁻¹")
            print(f"  Δω₂: {data_with_results['Delta_omega2'].mean():.3f} ± {data_with_results['Delta_omega2'].std():.3f} cm⁻¹")
            
            print("\nResidual Pressure Statistics:")
            print(f"  P₁:  {data_with_results['P1_kbar'].mean():.3f} ± {data_with_results['P1_kbar'].std():.3f} kbar")
            print(f"       ({data_with_results['P1_GPa'].mean():.3f} ± {data_with_results['P1_GPa'].std():.3f} GPa)")
            print(f"  P₂:  {data_with_results['P2_kbar'].mean():.3f} ± {data_with_results['P2_kbar'].std():.3f} kbar")
            print(f"       ({data_with_results['P2_GPa'].mean():.3f} ± {data_with_results['P2_GPa'].std():.3f} GPa)")
            
            delta_P = data_with_results['P1_kbar'] - data_with_results['P2_kbar']
            print(f"  ΔP:  {delta_P.mean():.3f} ± {delta_P.std():.3f} kbar")
            
            print("\nSample Results:")
            print("-" * 80)
            print(f"{'Label':<15} {'P₁ (kbar)':<12} {'P₂ (kbar)':<12} {'ΔP (kbar)':<12}")
            print("-" * 80)
            for idx, row in data_with_results.iterrows():
                delta_p = row['P1_kbar'] - row['P2_kbar']
                print(f"{row['Label']:<15} {row['P1_kbar']:>11.3f} {row['P2_kbar']:>11.3f} {delta_p:>11.3f}")
            
            print("\n" + "="*80)
            print("AVAILABLE DERIVATIVE SETS:")
            print("="*80)
            for name, info in RAMAN_DERIVATIVES.items():
                print(f"\n{name}:")
                print(f"  Reference: {info['reference']}")
                print(f"  d(128)/dP = {info['128']} cm⁻¹/kbar")
                print(f"  d(207)/dP = {info['207']} cm⁻¹/kbar")
                print(f"  d(464)/dP = {info['464']} cm⁻¹/kbar")
            
            print("\n✓ Analysis completed successfully!")
            print("="*80 + "\n")
            
        except Exception as e:
            print("\n" + "="*80)
            print("⚠ ERROR DURING ANALYSIS")
            print("="*80)
            print(f"\nError message: {str(e)}")
            print("\nPlease check:")
            print("  1. Input file format is correct (4 columns: Label, Peak_128, Peak_207, Peak_464)")
            print("  2. File path is correct")
            print("  3. Peak values are numeric")
            print("  4. Delimiter is correct (tab or comma)")
            print("\n" + "="*80 + "\n")
            import traceback
            traceback.print_exc()
        
        input("\nPress Enter to exit...")


# ===============================
# ADDITIONAL USER FUNCTIONS
# ===============================

def show_derivative_info():
    """Display information about available derivative sets"""
    print("\n" + "="*80)
    print("AVAILABLE RAMAN SHIFT DERIVATIVE SETS")
    print("="*80 + "\n")
    
    for name, info in RAMAN_DERIVATIVES.items():
        print(f"{name}:")
        print(f"  Reference: {info['reference']}")
        print(f"  Note: {info.get('note', 'N/A')}")
        print(f"  Derivatives (cm⁻¹/kbar):")
        print(f"    d(128)/dP = {info['128']}")
        print(f"    d(207)/dP = {info['207']}")
        print(f"    d(464)/dP = {info['464']}")
        print()


def create_example_input_file(filepath='example_quartz_peaks.txt'):
    """
    Create an example input file showing the correct format
    
    Parameters:
    -----------
    filepath : str
        Path where to create the example file
    """
    example_data = """Label	Peak_128	Peak_207	Peak_464
Sample1	127.5	206.8	463.2
Sample2	128.2	207.3	464.5
Sample3	127.8	206.9	463.8
Sample4	128.1	207.1	464.2
Sample5	127.6	206.7	463.5
"""
    
    with open(filepath, 'w') as f:
        f.write(example_data)
    
    print(f"Example input file created: {filepath}")
    print("\nFile format:")
    print("  - Tab-delimited (can also use comma)")
    print("  - 4 columns: Label, Peak_128, Peak_207, Peak_464")
    print("  - Header row (will be skipped during analysis)")
    print("  - Peak positions in cm⁻¹")


# Uncomment to create an example input file
# create_example_input_file()

# Uncomment to view derivative information
# show_derivative_info()
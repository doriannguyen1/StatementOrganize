# StatementOrganize

A Python utility that normalizes and organizes bank statement CSV files from multiple financial institutions into a consistent format.

## Overview

StatementOrganize processes CSV export files from various banks and credit card providers, standardizing their format by:
- Removing unnecessary columns
- Reorganizing column order for consistency
- Adjusting amount signs to match a standard convention
- Handling bank-specific formatting quirks

## Supported Banks/Cards

- **Chase** - Credit cards and checking accounts
- **Capital One (C1)** - Transaction downloads
- **Bilt** - Credit card statements
- **American Express (Amex)** - Activity reports

## How to Use

1. **Place input files** in the `input/` folder
   - Files should be CSV exports from supported banks
   - File names should contain the bank identifier (e.g., "Chase", "C1", "Bilt", "Amex", or "Activity" for Amex)

2. **Run the application**
   ```
   python Main.py
   ```

3. **Retrieve output** from the `output/` folder
   - Cleaned and normalized CSV files will be generated with the same filename

## Project Structure

- **Main.py** - Entry point that scans the input folder and processes all CSV files
- **Reader.py** - Core file processing logic that handles different bank formats
- **Helper.py** - Cleaning functions for each supported bank format
- **input/** - Place your bank statement CSV files here
- **output/** - Cleaned files are written here

## File Processing

The application automatically detects the bank format based on the filename and applies the appropriate cleaning function:
- Filenames containing "chase" → Uses Chase cleaning rules
- Filenames containing "c1" or "transaction_download" → Uses Capital One cleaning rules
- Filenames containing "bilt" → Uses Bilt cleaning rules
- Filenames containing "amex" or "activity" → Uses Amex cleaning rules

## Notes

- Original input files are not modified
- Output files maintain the same filename as input files
- Processing handles various CSV edge cases and skips malformed rows gracefully
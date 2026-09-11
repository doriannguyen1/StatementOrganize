# StatementOrganize

A Python utility that normalizes and organizes bank statement CSV files from multiple financial institutions into a consistent format.

## Overview

StatementOrganize processes CSV export files from different banks and credit card providers, standardizing them by:
- cleaning and normalizing transaction rows
- applying bank-specific parsing rules
- categorizing expenses and income where needed
- writing the result to the output folder in a consistent structure

## Supported Banks/Cards

- **Chase**
- **Capital One (C1)**
- **Bilt**
- **American Express (Amex)**
- **Ally**

## How to Use

1. Place raw CSV files in the `input/` folder.
2. Run the app from the project root:
   ```bash
   python Main.py
   ```
3. Cleaned CSV files will be written to the `output/` folder.

## Current Project Structure

- **Main.py** - project entry point
- **README.md** - project documentation
- **input/** - raw statement files
- **output/** - processed statement files
- **utils/** - shared utilities and processing logic
  - `Reader.py` - routes files to the correct handler
  - `Categories.py` - category keyword mappings
  - `Helper.py` - legacy helper functions
  - `Utils.py` - generic helpers like string contains checks
  - `handlers/` - bank/card-specific handlers
    - `ChaseHandler.py`
    - `AmexHandler.py`
    - `C1VentureHandler.py`
    - `AllyHandler.py`
    - `LegacyHandlers.py`

## Processing Logic

The app identifies the file type from the filename and routes it to the matching handler:
- filenames containing "chase" → `ChaseHandler`
- filenames containing "c1 venture", "venture", or "transaction_download" → `C1VentureHandler`
- filenames containing "c1" → legacy `C1Handler`
- filenames containing "bilt" → legacy `BiltHandler`
- filenames containing "amex" or "activity" → `AmexHandler`
- filenames containing "ally" or "transactions" → `AllyHandler`

## Notes

- Original input files are not overwritten.
- Output files keep the same name as the source file.
- Malformed or partial rows are skipped gracefully.
- The code is organized into a dedicated `utils` package to keep the project easier to maintain.
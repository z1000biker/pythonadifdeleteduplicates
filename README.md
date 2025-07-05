# ADIF Duplicate Remover

**Remove duplicate QSO entries from multi-line ADIF log files (e.g. exported from Ham Radio Deluxe).**

This Python script ensures that only the first occurrence of each full QSO record is retained while preserving the ADIF file structure, including headers.

---

## 📦 Repository

**GitHub:** [z1000biker/pythonadifdeleteduplicates](https://github.com/z1000biker/pythonadifdeleteduplicates)

---

## 🐍 File: `adifremoveduplicates.py`

### What it does:

- Reads an ADIF file (including headers).
- Parses each QSO record, which may span multiple lines.
- Deduplicates full QSO records (based on identical byte content).
- Writes a new `.adi` file with only the unique entries, preserving the original header.

---

## 🚀 How to Use

### 1. Prepare Your ADIF File

Place your original `.adi` file (e.g., `logbook.adi`) in the same folder as the script.

### 2. Run the Script

```bash
python adifremoveduplicates.py
The script will:

Read logbook.adi

Create logbook_deduped.adi with duplicates removed

🔧 Customization
Input/output filenames are hardcoded in the script for simplicity:

input_file = "logbook.adi"

output_file = "logbook_deduped.adi"

You can change these names in the script as needed.

✅ Requirements
Python 3.x

No external libraries needed (pure standard library)

📝 ADIF Compatibility
Designed for ADIF 2.x+ (including v3.x files)

Handles multi-line QSO records

Assumes records start with <a_index:...> and end with <EOR>

📌 Example Use Case
Useful for cleaning up export files from logging software like:

Ham Radio Deluxe

WSJT-X

Log4OM

N1MM Logger+

# PII Report Generator

This project is a Personal Information (PII) Report Generator that scans a CSV file for specific patterns, identifies columns containing PII, and generates a DOCX report with the findings.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Heuristics](#heuristics)
- [Contributing](#contributing)
- [License](#license)

## Description
The PII Report Generator script identifies personal information in a CSV file by applying heuristics such as detecting credit card numbers, special characters, and Medicare Beneficiary Identifiers. The results are compiled into a DOCX report, including a timestamp, the scanned file name, and details about the matched columns.

## Installation
To run this project, ensure you have Python installed and install the necessary packages using the following command:
```sh
pip install pandas python-docx numpy
```sh

## Usage
Run the script from the Windows Command Prompt with the following command:
```sh
python pii_report.py <csv_file_path> <report_file_path>
```sh

where :
* <csv_file_path>: Path to the input CSV file.
* <report_file_path>: Path where the DOCX report will be saved.

# PII Report Generator

This project is a Personal Information (PII) Report Generator that scans a CSV file for specific patterns, identifies columns containing PII, and generates a DOCX report with the findings.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Answers_to_questions](#Answers_to_questions)
- [Example](#example)


## Description
The PII Report Generator script identifies personal information in a CSV file by applying heuristics such as detecting credit card numbers, special characters, and Medicare Beneficiary Identifiers. The results are compiled into a DOCX report, including a timestamp, the scanned file name, and details about the matched columns.

## Installation
To run this project, ensure you have Python installed and install the necessary packages using the following command:
```sh
pip install pandas python-docx numpy
```

## Usage
Run the script from the Windows Command Prompt with the following command:
```sh
python pii_report.py <csv_file_path> <report_file_path>
```

where :
* <csv_file_path>: Path to the input CSV file.
* <report_file_path>: Path where the DOCX report will be saved.

## Answers_to_questions
1. What problems did you encounter when working with the data, if any?
    * A: The problem is that credit card numbers are similar to some of the phone numbers.
        Also, there is the arcitecure question of wether to make the code ready for orgenised csv or any type of data format,
        I choes to look for the highst probabale column in a csv and to take the columns that reached huristics-agreemant-threshold (can be modified)
2. In the provided file, there is a Street Address column. How would you approach
   identifying this data?
    * A: To Identify a stree adress I would look for a pattern of letters (street name), one set of numbers (hous number) and a comma, usually found in string representations of street adresses 

## Example
Report Example can be found in "notebooks" folder

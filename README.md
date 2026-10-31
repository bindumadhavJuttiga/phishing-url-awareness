# EWB Phishing URL Awareness Checker

## Overview
This Python project checks URL text for selected warning signs
that may be associated with phishing. It is an educational tool
that helps users understand suspicious URL characteristics.

## Features
- Detects the @ symbol
- Detects URLs longer than 100 characters
- Flags IP-address hostnames
- Flags five or more hostname segments
- Detects punycode-style hostnames
- Flags HTTP URLs
- Supports repeated checks and a quit option
- Handles malformed URL input

## Requirements
Python 3.10 or later. No extra packages are required.

## How to Run
Windows:
python phishing_checker.py

Mac/Linux:
python3 phishing_checker.py

## Testing
Five sample tests are documented in tests/test_samples.md.

## Screenshots
![Sample Run](screenshots/sample_run.png)
![Test Results](screenshots/test_results.png)

## Improvements
1. Added a loop to check multiple URLs without restarting.
2. Added error handling for malformed URL input.

## Limitations
This program checks URL text only. It does not visit websites,
scan for malware, or prove that a URL is safe.

## Ethical Use
Use the sample URLs from the project workbook.
Do not collect credentials or probe websites.

## Author
Juttiga Bindu Madhav
B.Tech - CSE (Artificial Intelligence)
EWB Cybersecurity Internship
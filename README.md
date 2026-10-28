
# Automation Data Validator

A Python CLI tool that validates customer records from a JSON file and separates valid and invalid data.

## Features

- Read customer records from JSON
- Validate names, email formats, and Iranian mobile numbers
- Detect missing or incorrectly formatted fields
- Separate valid and invalid records
- Save validation errors for each invalid record
- Generate a summary report
- Handle missing files and invalid JSON

## Requirements

- Python 3
- No external packages required

## How to Run

1. Place your input data in `customers.json`.
2. Open a terminal in the project directory.
3. Run:

   `python3 main.py`

4. Review the generated output files.

## Output Files

- `valid_customers.json`: Records that passed validation
- `invalid_customers.json`: Records with validation errors

## What I Practiced

در این پروژه، اعتبارسنجی داده‌ها، استفاده از `return`،
مدیریت خطاها و بررسی نوع داده‌ها را تمرین کردم.

همچنین یاد گرفتم اطلاعات ورودی را پردازش کنم و خروجی‌های
مناسب برای مراحل بعدی یک فرایند اتوماسیون تولید کنم.

## Limitations

- Email validation checks a basic format only.
- Phone validation checks the expected Iranian mobile number format.
- The program does not verify whether an email or phone number actually exists.
- Input data is read from a local JSON file.

## Future Improvements

- Support additional phone number formats
- Export reports to CSV
- Integrate with an API or an n8n workflow

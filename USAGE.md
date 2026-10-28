# Usage Guide — Automation Data Validator

## 1. Prepare the Input File

Create a file named `customers.json` in the project directory.

Each customer should contain these fields:

- `name`: Customer name
- `email`: Customer email address
- `phone`: Iranian mobile number as text

Example:

```json
[
    {
        "name": "Ali Ahmadi",
        "email": "ali@example.com",
        "phone": "09123456789"
    }
]
```

شماره تلفن را به‌صورت متن ذخیره کن تا صفر ابتدای شماره حفظ شود.

## 2. Run the Program

Open a terminal in the project directory and execute:

```bash
python3 main.py
```

The program reads the input file and validates each customer record.

## 3. Understand the Results

After a successful run, the program creates two files.

### valid_customers.json

Contains customer records that passed all validation checks.

### invalid_customers.json

Contains invalid records and a list of reasons explaining why each record failed validation.

## 4. Read the Summary

At the end, the program displays:

- Total records processed
- Number of valid records
- Number of invalid records
- Names of the generated output files

## 5. Test Invalid Data

Try changing a customer's email to `ali.example.com`, removing the name, or entering a phone number with fewer than 11 digits.

Run the program again and check `invalid_customers.json`.

## 6. Important Notes

- The program expects the input file to contain a JSON list.
- Email validation is basic and does not confirm that an address exists.
- Phone validation checks the format of Iranian mobile numbers only.
- Output files are overwritten each time the program runs.
- Use sample data instead of real customer information when publishing this project on GitHub.

## یادداشت فارسی

هدف این پروژه تمرین یک مرحله مهم در اتوماسیون است: بررسی کیفیت داده‌ها قبل از ارسال آن‌ها به مرحله بعد.

در یک پروژه واقعی، می‌توان همین منطق را برای بررسی اطلاعات فرم، سفارش مشتری یا داده‌های دریافت‌شده از API استفاده کرد.

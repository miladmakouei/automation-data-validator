
import json

INPUT_FILE = "customers.json"
VALID_FILE = "valid_customers.json"
INVALID_FILE = "invalid_customers.json"


def load_customers():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            customers = json.load(file)

    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} was not found.")
        return None

    except json.JSONDecodeError:
        print(f"Error: {INPUT_FILE} contains invalid JSON.")
        return None

    if not isinstance(customers, list):
        print("Error: The JSON data must be a list.")
        return None

    return customers


def validate_customer(customer):
    errors = []

    if not isinstance(customer, dict):
        return ["Customer data must be a JSON object."]

    name = customer.get("name", "")
    email = customer.get("email", "")
    phone = customer.get("phone", "")

    if not isinstance(name, str) or not name.strip():
        errors.append("Name is missing.")

    if not isinstance(email, str):
        errors.append("Email must be text.")
    elif (
        not email.strip()
        or email.count("@") != 1
        or "." not in email.split("@")[-1]
    ):
        errors.append("Email format is invalid.")

    if not isinstance(phone, str):
        errors.append("Phone must be text.")
    elif (
        len(phone) != 11
        or not phone.isdigit()
        or not phone.startswith("09")
    ):
        errors.append("Phone must be an 11-digit Iranian mobile number.")

    return errors


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    customers = load_customers()

    if customers is None:
        return

    valid_customers = []
    invalid_customers = []

    for customer in customers:
        errors = validate_customer(customer)

        if len(errors) == 0:
            valid_customers.append(customer)
        else:
            invalid_customers.append({
                "customer": customer,
                "errors": errors
            })

    save_json(VALID_FILE, valid_customers)
    save_json(INVALID_FILE, invalid_customers)

    print("\n--- Validation Report ---")
    print(f"Total records: {len(customers)}")
    print(f"Valid records: {len(valid_customers)}")
    print(f"Invalid records: {len(invalid_customers)}")
    print(f"Valid data saved to: {VALID_FILE}")
    print(f"Invalid data saved to: {INVALID_FILE}")


if __name__ == "__main__":
    main()

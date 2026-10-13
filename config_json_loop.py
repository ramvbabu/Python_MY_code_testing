import json
from pathlib import Path


def print_values(value, prefix=""):
    if isinstance(value, dict):
        for key, nested_value in value.items():
            key_path = f"{prefix}.{key}" if prefix else key
            print_values(nested_value, key_path)
    # elif isinstance(value, list):
    #     for index, nested_value in enumerate(value, start=1):
    #         key_path = f"{prefix}[{index}]" if prefix else f"[{index}]"
    #         print_values(nested_value, key_path)
    else:
        print(f"{prefix}: {value}")


def main():
    json_file = Path(__file__).resolve().parent / "data" / "config_data.json"

    try:
        with json_file.open("r", encoding="utf-8") as file:
            records = json.load(file)

        for record_number, record in enumerate(records, start=1):
            print(f"Record {record_number}:")
            print_values(record)
            print()
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read JSON data from {json_file}: {error}")


if __name__ == "__main__":
    main()
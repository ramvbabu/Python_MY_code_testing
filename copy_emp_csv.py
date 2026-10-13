from pathlib import Path

import pandas as pd


def main():
    data_folder = Path(__file__).resolve().parent / "data"
    input_csv = data_folder / "emp1.csv"
    output_csv = data_folder / "emp1_top2.csv"

    employee_data = pd.read_csv(input_csv)
    employee_data.head(2).to_csv(output_csv, index=False)

    print(f"Wrote the first 2 rows to {output_csv}")


if __name__ == "__main__":
    main()

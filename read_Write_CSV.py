import csv
from pathlib import Path


def read_csv(file_path):
	"""Read a CSV file with uniquely named columns."""
	with Path(file_path).open("r", newline="", encoding="utf-8-sig") as csv_file:
		reader = csv.DictReader(csv_file)
		fieldnames = reader.fieldnames
		# if not fieldnames:
		# 	raise ValueError("CSV file must contain a header row")
		# if len(set(fieldnames)) != len(fieldnames):
		# 	raise ValueError("CSV column names must be unique")

		rows = []
		for row_number, row in enumerate(reader, start=2):
			if None in row or any(value is None for value in row.values()):
				raise ValueError(
					f"CSV row {row_number} does not contain exactly "
					f"{len(fieldnames)} values"
				)
			rows.append(row)

	return rows


def write_csv(file_path, fieldnames, rows):
	"""Write dictionaries to a CSV file using the supplied column names."""
	if not fieldnames or len(set(fieldnames)) != len(fieldnames):
		raise ValueError("Provide at least one unique column name")

	for row_number, row in enumerate(rows, start=1):
		if set(row) != set(fieldnames):
			raise ValueError(
				f"Data row {row_number} must contain exactly these columns: {fieldnames}"
			)

	output_path = Path(file_path)
	output_path.parent.mkdir(parents=True, exist_ok=True)
	with output_path.open("w", newline="", encoding="utf-8") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(rows)

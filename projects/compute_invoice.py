import csv
import os
from datetime import datetime, timedelta
from decimal import Decimal


def read_invoice_file(filepath):
    with open(filepath, "r") as r:
        contents = csv.reader(filepath)
        record_row = next(contents, None)

        if record_row is None:
            raise ValueError("File is empty")

        # on second column
        vat_exc_converted = int(record_row[2])
        vat_exc = Decimal(vat_exc_converted) / 100

        # on third column
        vat_converted = int(record_row[3])
        vat = Decimal(vat_converted) / 100

    return vat_exc, vat


START_DATE = "2003-07-01"
END_DATE = "2020-07-01"
BASE_DIR_PATH = "/go-hotel/dir"


def compute():
    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    end = datetime.strptime(END_DATE, "%Y-%m-%d")

    d = start
    while d < end:
        month_dir_path = f"{BASE_DIR_PATH}/{d.month}-{d.year}"
        try:
            list_files = os.listdir(month_dir_path)
        except FileNotFoundError as e:
            print(f"Failed to open directory {month_dir_path}: {e}")
            d += timedelta(days=30)
            continue

        for name in list_files:
            file_path = os.path.join(month_dir_path, name)
            try:
                vat_exc, vat = read_invoice_file(file_path)
                print(f"Invoice: {name}, VAT Excluded: {vat_exc}, VAT: {vat}")
            except Exception as e:
                print(f"Failed to parse invoice {file_path}: {e}")

        d += timedelta(days=30)

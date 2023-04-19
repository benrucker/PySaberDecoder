
# TODO write to csv

import csv
from typing import Any
from safe_open import safe_open_w
from structs import ReplayData
from output_format import output_format

# TODO: unpack nested values into individual columns

def write_to_csv(replay: dict[str, list[ReplayData]], output_filename):
    for key, table in output_format.items():
        filename = table['Name']
        data = replay[key]

        with safe_open_w(f'{output_filename}/{filename}.csv', newline='') as f:
            write_file(f, data, table['fields'])


def write_file(f, data: list[ReplayData], fields_to_write: set[str]):
    writer = csv.DictWriter(f, fieldnames=fields_to_write)

    writer.writeheader()
    for row in data:
        write_row(writer, row, fields_to_write)


def write_row(writer: csv.DictWriter, row: ReplayData, fields_to_write: set[str]):
    raw_row = row.to_dict()
    filtered_row = dict(
        (entry_key, process_row(raw_row[entry_key])) for entry_key in fields_to_write
    )
    writer.writerow(filtered_row)


def process_row(replay_data_or_primitive: ReplayData | Any):
    if hasattr(replay_data_or_primitive, 'to_dict'):
        return replay_data_or_primitive.to_dict()
    return replay_data_or_primitive

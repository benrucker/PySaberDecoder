import csv
from typing import Any
from safe_open import safe_open_w
from structs import ReplayData
from output_format import output_format


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
    filtered_row = nested_values_to_dict(
        [process_row(row, entry_key) for entry_key in fields_to_write]
    )
    writer.writerow(filtered_row)


def process_row(replay_data_or_primitive: ReplayData | Any, entry_key: str):
    is_key_nested = '.' in entry_key
    [this_key, next_key] = entry_key.split('.', 1) if is_key_nested else [entry_key, None]
    
    if hasattr(replay_data_or_primitive, 'to_dict') and is_key_nested:
        return (entry_key, process_row(replay_data_or_primitive.to_dict()[this_key], next_key)[1])
    
    elif hasattr(replay_data_or_primitive, 'to_dict'):
        return (entry_key, replay_data_or_primitive.to_dict()[this_key])

    return (entry_key, replay_data_or_primitive[this_key])


def nested_values_to_dict(values: list) -> dict:
    accumulator = {}
    for value_or_values in values:
        if type(value_or_values) is tuple:
            accumulator[value_or_values[0]] = value_or_values[1]

        elif type(value_or_values) is list:
            accumulator.update(
                nested_values_to_dict(value_or_values)
            )
    return accumulator
import argparse

from decode_file import decompress, deserialize
from write_to_csv import write_to_csv


if __name__ == '__main__':
    # Setup and read the command line arguments
    parser = argparse.ArgumentParser(
        description='Decompress & decode a ScoreSaber replay file'
    )

    parser.add_argument(
        '-i',
        '--input',
        help='path to the file to parse',
        default="replay.dat"
    )

    parser.add_argument(
        '-o',
        '--output',
        help='path to the output folder',
        default="output"
    )

    args = parser.parse_args()

    # Parse the input and save it to the output file
    write_to_csv(deserialize(decompress(args.input)), args.output)
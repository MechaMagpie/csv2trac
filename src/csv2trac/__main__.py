"""Runner for CSV-Trac table converter script."""
import argparse
import csv
from pathlib import Path

from csv2trac.csv2trac import trac_table_iter


def convert_files(infile: Path | str, outfile: Path | str) -> None:
    """Convert input CSV to output .txt."""
    with Path(infile).open('r', encoding='ascii') as in_f, \
         Path(outfile).open('w', encoding='ascii') as out_f:
        inreader = csv.reader(in_f)
        trac_generator = trac_table_iter(inreader)
        for fragment in trac_generator:
            out_f.write(fragment)


def main() -> None:
    """Run main script."""
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    convert_files(args.input, args.output)


if __name__ == '__main__':
    main()

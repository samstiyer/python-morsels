"""
I'd like you to create a program, ini2csv.py, which accepts an INI-like file and converts it to a CSV-like file.

The input files will look like this (this is an EditorConfig file):

[*.py]
indent_style = space
indent_size = 4

[*.js]
indent_style = space
indent_size = 2

Given that input file, .editorconfig, executing our program like this:

$ python ini2csv.py .editorconfig editorconfig.csv

Will produce an output file, editorconfig.csv, like this:

*.py,indent_style,space
*.py,indent_size,4
*.js,indent_style,space
*.js,indent_size,2

Note that the order of lines in this CSV file should match the order of sections and properties in the given INI file.

Bonus

There's just one bonus this week. For the bonus, I'd like you to accept a --collapsed argument that, when present, will collapse the rows to one row per section.

So this:

$ python ini2csv.py --collapsed .editorconfig editorconfig.csv

Will result in a editorconfig.csv file that contains this:

header,indent_style,indent_size
*.py,space,4
*.js,space,2
"""

import csv
from argparse import ArgumentParser, FileType
from configparser import ConfigParser

parser = ArgumentParser()
parser.add_argument('ini_file', type=FileType('rt'))
parser.add_argument('csv_file', type=FileType('wt'))
parser.add_argument('--collapsed', action='store_true')
args = parser.parse_args()


config = ConfigParser()
config.read_file(args.ini_file)

if args.collapsed:
    rows = [
        {'header': name, **section}
        for name, section in config.items()
        if section
    ]
    csv_writer = csv.DictWriter(args.csv_file, fieldnames=rows[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(rows)
else:
    csv_writer = csv.writer(args.csv_file)
    csv_writer.writerows(
        [name, key, value]
        for name, section in config.items()
        for key, value in section.items()
    )

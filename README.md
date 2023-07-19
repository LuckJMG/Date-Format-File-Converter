# Date Format Converter

A small python script to convert the date format from a file to another.

## Requirements

- Python 3

## Install

Clone this repo on your machine, or download the `date_format_converter.py` file.

## Usage

Execute the script using,

``` bash
python3 date_format_converter.py # For linux
py date_format_converter.py # For windows
```

Input the name of the file to convert, the time format of the input file, the name of the output file and the desired format to be converted.

The input file must be in the directory of the script, or you can pass an absolute path to the script.

The output file will be created, if it already exists, it will be overwritten.

Currently it only supports date formats with any combination of this elements:

- `YY` or `YYYY`
- `MM`
- `DD`
- Any separator without the previus characters between them.

For example `YYYY-MM-DD`, `DD/MM/YY` or `MM.DD.YY`.

Currently it doesn't support time format.

After running it would say `Convertion Completed`.

## Comments

I made this script because I recently changed from Notion to Obsidian, and I am trying the best date format to have in my markdown files, so instead of doing a repetitive task for 10 minutes, I spent 1 hour automating the task like a good programmer.

import re
from datetime import datetime

def date_regex(date_format):
    separator = re.search("\W{1}", date_format).group()
    date = {
        "Y": date_format.count("Y"),
        "M": date_format.count("M"),
        "D": date_format.count("D"),
    }

    regex = ""
    cache = [separator]
    for char in date_format:
        if (char == separator):
            regex += separator
            continue

        if (char not in cache):
            cache.append(char)
            regex += "\d{" + str(date[char]) + "}"

    return regex

def date_replacement(date_format):
    DATE = ["Y", "M", "D"]
    replacement = ""

    for char in date_format:
        if (char in DATE and replacement.count(char) == 0):
            replacement += char
            continue

        if (char not in DATE):
            replacement += char

    return replacement

CURRENT_YEAR = int(str(datetime.now().year)[2:4])

input_file = open(input("Input File Name: "), "r")
input_date_format = input("Date Format of the Input File: ")
input_regex = date_regex(input_date_format)

output_file = open(input("Output File Name: "), "w")
output_date_format = input("Date Format of the Output File: ")

for line in input_file:
    date = re.search(input_regex, line)
    while (date is not None):
        mark = date.span()
        date = date.group()
        line = line.split(date)

        split_date = {
            "Y": "",
            "M": "",
            "D": "",
        }

        for i in range(len(date)):
            if (input_date_format[i] not in split_date.keys()): continue
            split_date[input_date_format[i]] += date[i]

        if (input_date_format.count("Y") == 4 and output_date_format.count("Y") == 2):
            split_date["Y"] = split_date["Y"][2:4]
        elif (input_date_format.count("Y") == 2 and output_date_format.count("Y") == 4):
            if (int(split_date["Y"]) <= CURRENT_YEAR):
                split_date["Y"] = "20" + split_date["Y"]
            else:
                split_date["Y"] = "19" + split_date["Y"]

        date = date_replacement(output_date_format)
        for key, value in split_date.items():
            date = date.replace(key, value)

        line = date.join(line)

        date = re.search(input_regex, line)
        if (date is None or mark == date.span()): break

    output_file.write(line)

print("Conversion Completed")

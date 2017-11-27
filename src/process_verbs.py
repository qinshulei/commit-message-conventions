#!/usr/bin/env python3
import re

from config import Directories
from file_utils import open_file_dir_safe

input_file = open(f"{Directories.raw_data}/verbs.txt")
output_file = open_file_dir_safe(f"{Directories.processed_data}/infinitive.txt", "w")

with input_file, output_file:
    for line in input_file:
        match = re.match("""^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s([a-zA-Z]*)\s""", line)
        if match:
            word = match.group(1)
            if not word == "initial":
                output_file.write(match.group(1) + "\n")

    additional = [
        "sync",
        "shut",
        # "merge" is also missing but it probably shouldn't be included
        # because messages with "merge" are often auto-generated by Git
    ]

    for word in additional:
        output_file.write(word + "\n")

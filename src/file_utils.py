import json
import os


def open_file_dir_safe(path, mode='r'):
    """Make directories for the file given (if they don't exist) and open the file."""
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    return open(path, mode)


def save_json(content, path):
    """Save JSON into a file."""
    encoded = json.dumps(content, indent=2)

    file = open_file_dir_safe(path, 'w')
    with file:
        file.write(encoded)


def load_json(path):
    """Load JSON from a file."""
    file = open_file_dir_safe(path)
    return json.load(file)


def load_txt_into_set(path, skip_first_line=True):
    """Load a txt file (one value per line) into a set."""
    result = set()
    file = open_file_dir_safe(path)
    with file:
        if skip_first_line:
            file.readline()

        for line in file:
            line = line.strip()
            result.add(line)

    return result

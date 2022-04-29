from pathlib import Path
import re

class Note:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

    @classmethod
    def from_file(cls, filepath):
        data = cls.read_from_file(filepath)
        return cls(data)

    @staticmethod
    def read_from_file(filepath):
        with open(filepath, 'r') as f:
            title_input, category_input, description_input = f.read().splitlines()
        if title_input[0:2] != "# ":
            raise ValueError("The specified file has an incorrectly formatted title")
        return title_input, description_input, category_input

    def write_to_file(self):
        path = Path('./data')
        path = path / self.category / f"{get_valid_filename(self.title)}.txt"
        with open(path, 'w') as f:
            f.write(f"# {self.title}\n")
            f.write(f"## {self.category}\n")
            f.write(f"{self.description}")

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)
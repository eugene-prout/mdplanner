from pathlib import Path

class Note:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

    @classmethod
    def from_file(cls, filepath):
        data = read_from_file(filepath)
        return cls(data)

    @staticmethod
    def read_from_file(filepath):
        with open(filepath, 'r') as f:
            title_input, category_input, description_input = f.read().splitlines()
        if title_input[0:2] != "# ":
            raise ValueError("The specified file has an incorrectly formatted title")
        self.title = title_input
        self.description = description_input
        self.category = category_input
    
    def write_to_file(self):
        path = Path('./data')
        path = path / self.category / f"{self.title.replace(' ', '_')}.md"
        with open(path, 'w') as f:
            f.write(f"# {self.title}\n")
            f.write(f"## {self.category}\n")
            f.write(f"{self.description}")

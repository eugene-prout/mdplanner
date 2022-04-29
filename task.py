from pathlib import Path
import re

class Task:
    def __init__(self, title, description, category):
        """Create task with given values

        :param title: Title for new task
        :type title: str
        :param description: Description for new task
        :type description: str
        :param category: Category for the new task
        :type category: str
        """
        self.title = title
        self.description = description
        self.category = category

    @classmethod
    def from_file(cls, filepath):
        """Create task object from given file.

        :param filepath: Path to file encoding the task
        :type filepath: Path
        """
        data = cls.read_from_file(filepath)
        return cls(title=data[0], description=data[1], category=data[2])

    @staticmethod
    def read_from_file(filepath):
        """Parse input file and output contents as title, description and category

        :param filepath: Path to file encoding the task
        :type filepath: Path
        ...
        :raises ValueError: if the file does not have the expected format
        ...
        :return: Returns a list containing parsed title, description and category 
        :rtype: List
        """
        with open(filepath, 'r') as f:
            title_input, category_input, description_input = f.read().splitlines()
        if title_input[0:2] != "# ":
            raise ValueError("The specified file has an incorrectly formatted title")
        return (title_input[2:], description_input, category_input[3:])

    def write_to_file(self):
        """Write the task to disk. Stores the contents of the task in "data/category/title.txt". Ensures the title is a safe filename.
        """
        path = Path('./data')
        path = path / self.category / f"{get_valid_filename(self.title)}.txt"
        with open(path, 'w') as f:
            f.write(f"# {self.title}\n")
            f.write(f"## {self.category}\n")
            f.write(f"{self.description}")

def get_valid_filename(s):
    """Create safe filename from string. https://stackoverflow.com/a/46801075/10718490

    :param s: Intended filename
    :type s: str
    """
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)
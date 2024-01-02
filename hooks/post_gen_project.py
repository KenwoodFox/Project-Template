import os
import sys
from shutil import rmtree

REMOVE_PATHS = [
    '{% if cookiecutter.gitprovider != "github" %} .github {% endif %}',
    '{% if cookiecutter.gitprovider != "gitea" %} .gitea {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            rmtree(path)  # Remove dir tree
        else:
            os.unlink(path)

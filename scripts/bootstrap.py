"""Interactive helper to fill in project-intent.md."""

import pathlib

TEMPLATE = pathlib.Path('project-intent.md').read_text()

print('Fill in project-intent.md using the template below:\n')
print(TEMPLATE)

# Klaxoon API Python Wrapper

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is a Python library for interacting with the Klaxoon API. It allows viewing, adding, and deleting ideas
from Klaxoon boards.

For configuring developer access, visit https://app.klaxoon.com/userspace/my-apps and for reference,
visit https://developers.klaxoon.com/

## Installation

You can install the library using pip.

```bash
pip install .
```

## De-Installation

```bash
pip uninstall klaxoon
```

## Initialisation

```bash
python gui/configure_token_gui.py
```

## Usage

```python
import os
from klaxoon.klaxoon_board import KlaxoonBoard
from klaxoon.klaxoon_idea import KlaxoonIdea
from requests.exceptions import HTTPError

# Create an instance of the Klaxoon API using the configuration file
board_api = KlaxoonBoard.from_config_file(os.path.expanduser("~/.api_klaxoon/.token"))
idea_api = KlaxoonIdea.from_config_file(os.path.expanduser("~/.api_klaxoon/.token"))

# Retrieve all Klaxoon boards
boards = board_api.get_boards()

# Display the ideas for each board
for board in boards:
    try:
        print(f"Board '{board.title}':")
        ideas = idea_api.get_board_ideas(board.id)
        for idea in ideas:
            print(f"- {idea.data.content}")
    except HTTPError as e:
        print(e)

# Get all the boards
boards = board_api.get_boards()
print("List of Klaxoon boards:")
for board in boards:
    print(board.title)

# Retrieve ideas from a specific board
board_id = "YOUR_BOARD_ID"
ideas = idea_api.get_board_ideas(board_id)
print(f"Ideas from board  {board_id}:")
for idea in ideas:
    print(idea.data.content)

# Add an idea to a board
new_idea = "New  idea"
idea_api.add_idea_to_board(board_id, new_idea)
print(f"Idea '{new_idea}' added to board {board_id}")

# Delete an idea from a board
idea_id_to_delete = "IDEA_ID_TO_DELETE"
idea_api.delete_idea_from_board(board_id, idea_id_to_delete)
print(f"Idea {idea_id_to_delete} deleted from board {board_id}")
```

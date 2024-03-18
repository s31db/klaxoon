# Klaxoon API Python Wrapper

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Ce projet est une bibliothèque Python pour interagir avec l'API Klaxoon. Il permet de voir, ajouter et supprimer des
idées à partir de tableaux Klaxoon.

Pour la configuration d'un accès développeur https://app.klaxoon.com/userspace/my-apps et le site de
référence https://developers.klaxoon.com/

## Installation

Vous pouvez installer la bibliothèque à l'aide de pip :

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

## Utilisation

```python
import os
from klaxoon.klaxoon_api import KlaxoonAPI
from requests.exceptions import HTTPError

# Créer une instance de l'API Klaxoon en utilisant le fichier de configuration
api = KlaxoonAPI.from_config_file(os.path.expanduser("~/.api_klaxoon/.token"))

# Récupérer tous les tableaux Klaxoon
boards = api.get_boards()

# Afficher les idées de chaque tableau
for board in boards:
    try:
        print(f"Tableau '{board.title}':")
        ideas = api.get_board_ideas(board.id)
        for idea in ideas:
            print(f"- {idea.data.content}")
    except HTTPError as e:
        print(e)

# Récupérer tous les tableaux
boards = api.get_boards()
print("Liste des tableaux Klaxoon:")
for board in boards:
    print(board.title)

# Récupérer les idées d'un tableau spécifique
board_id = "YOUR_BOARD_ID"
ideas = api.get_board_ideas(board_id)
print(f"Idées du tableau {board_id}:")
for idea in ideas:
    print(idea.title)

# Ajouter une idée à un tableau
new_idea = "Nouvelle idée"
api.add_idea_to_board(board_id, new_idea)
print(f"Idée '{new_idea}' ajoutée au tableau {board_id}")

# Supprimer une idée d'un tableau
idea_id_to_delete = "IDEA_ID_TO_DELETE"
api.delete_idea_from_board(board_id, idea_id_to_delete)
print(f"Idée {idea_id_to_delete} supprimée du tableau {board_id}")
```

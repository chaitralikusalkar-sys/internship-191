import json
from pathlib import Path


def save_json_to_file(data, filepath):
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except (OSError, TypeError) as exc:
        raise IOError(f"Could not write JSON data to {filepath}") from exc


def load_json_from_file(filepath):
    path = Path(filepath)
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        raise IOError(f"File not found: {filepath}") from exc
    except json.JSONDecodeError as exc:
        raise IOError(f"File contains invalid JSON: {filepath}") from exc
    except OSError as exc:
        raise IOError(f"Could not read file: {filepath}") from exc

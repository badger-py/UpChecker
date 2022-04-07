from typing import Any, Dict
import json

from config import CONFIG_FILENAME


def _dump(content: Dict[str, Any]) -> None:
    with open(CONFIG_FILENAME, mode="w", encoding="utf-8") as file:
        json.dump(content, file)


def _load() -> Dict[str, Any]:
    try:
        with open(CONFIG_FILENAME, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        _dump({})
        return {}


def set_setting(settings_name: str, setting_value) -> None:
    content = _load()
    content[settings_name] = setting_value
    _dump(content)


def get_setting(settings_name: str) -> Any:
    content = _load()
    return content.get(settings_name)

import os
import json
import logging
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
    return None

def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        logger.error(f"Error writing to file {file_path}: {str(e)}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Error creating directory {dir_path}: {str(e)}")
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(key, default)

def validate_response(response: Dict[str, Any], required_fields: list) -> bool:
    if not isinstance(response, dict):
        return False
    return all(field in response for field in required_fields)
import json


def load_config(file_path="files/config.json"):
    """
    Load the entire configuration from a JSON file.

    Args:
        file_path (str): Path to the config file. Default is "config.json".

    Returns:
        dict: The loaded configuration as a dictionary.

    Raises:
        FileNotFoundError: If the config file is not found.
        ValueError: If the config file contains invalid JSON.
    """
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file at {file_path}")


def get_email_credentials(file_path="files/config.json"):
    """
    Fetch email credentials from the configuration file.

    Args:
        file_path (str): Path to the config file. Default is "config.json".

    Returns:
        tuple: A tuple containing (email_id, email_password).

    Raises:
        ValueError: If email credentials are missing in the config.
    """
    config = load_config(file_path)
    email_id = config.get("email_id")
    email_password = config.get("email_password")

    if not email_id or not email_password:
        raise ValueError("Email credentials not found in config file.")

    return email_id, email_password


def get_database_credentials(file_path="files/config.json"):
    """
    Fetch database credentials from the configuration file.

    Args:
        file_path (str): Path to the config file. Default is "config.json".

    Returns:
        tuple: A tuple containing (db_host, db_user, db_password).

    Raises:
        ValueError: If database credentials are missing in the config.
    """
    config = load_config(file_path)
    db_host = config.get("db_host")
    db_user = config.get("db_user")
    db_password = config.get("db_password")

    if not db_host or not db_user or not db_password:
        raise ValueError("Database credentials not found in config file.")

    return db_host, db_user, db_password
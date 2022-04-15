import os


def retrieve_env_var(var_name, is_required=True):
    """
    Function to retrieve environment variable. If not set will raise an error
    """
    if is_required and not env_var_exists(var_name):
        raise ValueError(f"{var_name} envirionment variable is required")

    value = os.getenv(var_name)

    if value is not None:
        value = value.strip()

    return value


def env_var_exists(var_name):
    """
    Checks is an environment variable exists
    """
    return var_name in os.environ

import os


def safe_open_w(path, *args, **kwargs):
    """Open "path" for writing, creating any parent directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w', encoding="utf-8", *args, **kwargs)
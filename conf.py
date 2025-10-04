from pathlib import Path


PROG_DIR = str(Path(__file__).resolve().parent)

SQLITE_DB_FILE_PATH = PROG_DIR + "/mdb.sqlite3"
BASE_DB_CRYPT_KEY = "<past db cryptography string key>"

COMMANDS_REGISTRY_FOR_HELP = [
    ("add-note", "", ""),
    ("edit-note", "", ""),
    ("del-note", "", ""),
    ("list-notes", "", ""),
    ("show-note", "", ""),
]

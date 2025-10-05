from importlib import import_module

import sys

from logger import *

from conf import SQLITE_DB_FILE_PATH, BASE_DB_CRYPT_KEY
from sqlite3_db_api import DB


class EACore:
    version = "0.1"
    github_repo_link = "https://github.com/mk-samoilov/easy_notes"

    def __init__(self):
        self.db_api: DB | None = None

        self.looping: bool = True

    def init_db(self):
        self.db_api = DB(db_file=SQLITE_DB_FILE_PATH, bck=BASE_DB_CRYPT_KEY)

        if self.db_api.db_is_exist():
            master_key_is_new = False
        else:
            master_key_is_new = True

        master_key = self.get_master_key(is_new=master_key_is_new)

        ir = self.db_api.init_db(master_key=master_key)

        if type(ir) == str:
            log(lvl=ErrorLog(), content=ir)
            self.db_api = None

            sys.exit(1)
        else:
            log(lvl=InfoLog(), content="Database initialized")

    def print_welcome_(self):
        print(f"i:   Easy Notes v{self.version}")
        print("i: type 'github-repo' for print source code repository link")
        print("i: type 'help' for help")
        print(end="\n")

    def cl_loop(self):


        while self.looping:
            pass

    def get_master_key(self, is_new: bool = True) -> str:
        log(lvl=HintLog(), content="The database (with notes) encrypted by master key")

        prompt = "enter master key: " if is_new else "enter new master key for db: "

        uc_master_key = self.get_input(prompt=prompt)

        master_key = uc_master_key.strip()

        if master_key == "":
            master_key = "default"

        return master_key

    def process_command(self) -> int:
        uc_command = self.get_input(prompt="")
        c_command = uc_command.strip().lower().replace("-", "_")
        f_command = c_command.strip(" ")

        if c_command == "":
            return 0

        module = import_module(name=f"af.{f_command[0]}", package=__package__)
        return getattr(module, "main")(self, c_command)

    @staticmethod
    def get_input(prompt: str = "> ") -> str:
        return str(input(str(prompt)))

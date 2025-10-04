from dataclasses import dataclass


@dataclass
class CleanLog:
    prefix = ""
    prefix_color = ""
    log_color = ""


@dataclass
class InfoLog(CleanLog):
    prefix = "[INFO] "
    prefix_color = ""
    log_color = ""


@dataclass
class WarningLog(CleanLog):
    prefix = "[WARN] "
    prefix_color = ""
    log_color = ""


@dataclass
class ErrorLog(CleanLog):
    prefix = "[ERROR] "
    prefix_color = ""
    log_color = ""


@dataclass
class DebugLog(CleanLog):
    prefix = "debug: "
    prefix_color = ""
    log_color = ""


@dataclass
class HintLog(CleanLog):
    prefix = "hint: "
    prefix_color = ""
    log_color = ""


@dataclass
class SmallHintLog(CleanLog):
    prefix = "i: "
    prefix_color = ""
    log_color = ""


def log(lvl: CleanLog = InfoLog(), content: str = ""):
    formated_log = f"{lvl.prefix}{content}"
    print(formated_log)

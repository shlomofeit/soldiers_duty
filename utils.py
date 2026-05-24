from data import VALID_DAYS, VALID_STATUSES


def is_vaild_day(day: str) -> bool:
    return day in VALID_DAYS


def is_valid_name(name: str) -> bool:
    return name != ''


def is_valid_status(status: str) -> bool:
    return status in VALID_STATUSES
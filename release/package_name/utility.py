import datetime


def get_formatted_datetime() -> str:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")
    return formatted_datetime
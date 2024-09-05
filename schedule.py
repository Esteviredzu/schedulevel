# schedule.py
from datetime import datetime
import database


def get_week_number() -> int:
    """Возвращает номер недели: 1 - нечетная, 2 - четная"""
    current_week = datetime.now().isocalendar().week
    return 1 if current_week % 2 == 0 else 2


def get_day_number() -> int:
    """Возвращает текущий день недели (0 - понедельник, 6 - воскресенье)"""
    return datetime.now().weekday()


def get_schedule(day_offset: int) -> list:
    """Возвращает список строк расписания для указанного дня, day_offset = 0 - сегодня, 1 - завтра и т.д."""
    current_day = get_day_number() + day_offset
    current_week = get_week_number()

    if current_day > 6:
        current_day = 0  # Переход на новую неделю

    schedule = database.get_schedule_for_week(current_week, current_day)
    return schedule  # Возвращаем список, а не строку

from datetime import datetime, timedelta
import database

def get_schedule(day_offset: int) -> list:
    """Возвращает список строк расписания для указанного дня, day_offset = 0 - сегодня, 1 - завтра и т.д."""
    # Получаем текущую дату с учетом смещения
    target_date = datetime.now() + timedelta(days=day_offset)
    
    # Получаем номер недели (1 - нечетная, 2 - четная)
    current_week = 1 if target_date.isocalendar().week % 2 == 0 else 2
    
    # Получаем день недели (0 - понедельник, 6 - воскресенье)
    current_day = target_date.weekday()
    
    # Получаем расписание для конкретной недели и дня
    schedule = database.get_schedule_for_week(current_week, current_day)
    
    return schedule

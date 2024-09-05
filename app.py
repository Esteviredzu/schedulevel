# app.py
from flask import Flask, render_template
from schedule import get_schedule
import os

app = Flask(__name__)

# Маршрут для отображения расписания на сегодня
@app.route('/')
def index():
    schedule = get_schedule(0)  # Сегодня
    return render_template('schedule.html', day_name='сегодня', schedule=schedule)

# Маршрут для отображения расписания на завтра
@app.route('/tomorrow')
def tomorrow():
    schedule = get_schedule(1)  # Завтра
    return render_template('schedule.html', day_name='завтра', schedule=schedule)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

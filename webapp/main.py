import os
from flask import Flask, render_template
from psutil import pid_exists


app = Flask(__name__)


app_pid_file = "/tmp/labelapp.pid"
active_part_number_file = "/tmp/active_pn.txt"
fixture_file = "/boot/FIXTURE.TXT"
python_exe = "env/bin/python3"
app_exe = "main.py"


def get_app_pid_file():
    with open(app_pid_file, 'r') as f:
        app_pid = f.read()
    return app_pid


def get_active_part_number():
    with open(active_part_number_file, 'r') as f:
        part_number = f.read()
    return part_number


def get_fixture():
    with open(fixture_file, 'r') as f:
        fixture = f.read()
    return fixture


@app.route("/")
def index():
    app_pid = int(get_app_pid_file())
    is_pid = pid_exists(app_pid)
    if is_pid:
        program_status = "Running"
    else:
        program_status = "Not Running"

    try:
        part_number = get_active_part_number()
    except:
        part_number = "NO PART NUMBER SET!"

    fixture = get_fixture()

    template_data = {
        'title': 'Label Printing System',
        'fixture': fixture,
        'part_number': part_number,
        'program_status': program_status,
    }
    return render_template('main.html', **template_data)

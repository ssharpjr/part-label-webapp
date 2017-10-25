#! /usr/bin/env bash

APP="main.py"
export FLASK_APP=${APP}
export FLASK_DEBUG=1

. env/bin/activate

flask run --host=0.0.0.0

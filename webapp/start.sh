#! /usr/bin/env bash

APP="main.py"
export FLASK_APP=${APP}
export FLASK_DEBUG=1

if [ -d "env" ]; then
	. env/bin/activate
fi

flask run --host=0.0.0.0

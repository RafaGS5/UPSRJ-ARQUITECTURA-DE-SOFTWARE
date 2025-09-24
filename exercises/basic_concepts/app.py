from flask import Flask, jsonify
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

from exercises.basic_concepts.controller.routes import app

# Set up logging configuration
set_logging(log_file='app.log')

if __name__ == "__main__":
    # Entry point: runs the Flask development server in debug mode.
    plog("Starting Flask app", INFO)
    app.run(debug=True)
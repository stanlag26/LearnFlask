from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)

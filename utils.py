from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def build_uri_sqlalchemy(username_, password_, server_, data_base_):
    return f'mssql+pyodbc://{username_}:{password_}@{server_}/{data_base_}?driver=ODBC+Driver+17+for+SQL+Server'


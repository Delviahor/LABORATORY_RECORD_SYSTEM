from flask import Flask, jsonify, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from utils import build_uri_sqlalchemy # Import the function from utils.py

app = Flask(__name__)


"""
GET = OBTENER INFORMACION
POST = CREAR INFORMACION
DELETE = ACTUALIZAR INFORMACION
PUT = BORRAR
"""

username = 'sa'
password = '12345678'
server = 'LAPTOP-F6NVJ00I\\MSSQLSERVER01'
database = 'CONTROL_LABORATORY_SYSTEM'


# Construir la URI de conexión de prueba
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Crear el motor de conexión
engine = create_engine(connection_string)

# Intentar conectarse a la base de datos
try:
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
except SQLAlchemyError as e:
    print(f"Error en la conexión: {e}")

# Configurar la URI de la base de datos SQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = build_uri_sqlalchemy(username, password, server, database)
db = SQLAlchemy(app)

class Administrator(db.Model):
    __tablename__ = 'tbl_administrator'  # table name in SQL Server

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key
    admin_user = db.Column(db.String(100), nullable=False)
    admin_password = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('security.html')  # Redirige a la ruta de inicio de sesión

@app.route('/Security', methods=['GET','POST'])
def Security():
    if request.method == 'POST':  #si la solciitud es post
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to find the administrator with the given username
        administrator = Administrator.query.filter_by(admin_user=username).first()

        # Verify if the administrator exists and if the password is correct
        if administrator and administrator.admin_password == password:
            return redirect(url_for('registered_subject'))  # Redirect to the register page if login is successful
        else:
            flash('Invalid username or password')  # Flash an error message
    return render_template('security.html')

@app.route('/registered_subject')
def registered_subject():
    return render_template('registered_subject.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug = True)


from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


"""
GET = OBTENER INFORMACION
POST = CREAR INFORMACION
DELETE = ACTUALIZAR INFORMACION
PUT = BORRAR

"""
"""
# Configura la URI de la base de datos SQL Server
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:12345678@localhost/CONTROL_LABORATORY_SYSTEM?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:12345678@LAPTOP-F6NVJ00I\MSSQLSERVER01/CONTROL_LABORATORY_SYSTEM?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)
"""


username = 'sa'
password = '12345678'
server = 'LAPTOP-F6NVJ00I\\MSSQLSERVER01'
database = 'CONTROL_LABORATORY_SYSTEM'

def build_uri_sqlalchemy(username_, password_, server_, data_base_):
    return f'mssql+pyodbc://{username_}:{password_}@{server_}/{data_base_}?driver=ODBC+Driver+17+for+SQL+Server'


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
    return redirect(url_for('Security'))  # Redirige a la ruta de inicio de sesión


@app.route('/Security', methods=['GET','POST'])
def Security():
    username = request.form.get('username')
    password = request.form.get('password')
        
    # Consulta la base de datos para encontrar el administrador con el nombre de usuario dado
    administrator = Administrator.query.filter_by(admin_user=username).first()

    # Verifica si el administrador existe y si la contraseña es correcta
    if administrator and administrator.admin_password == password:
        return redirect(url_for('register'))  # Redirige a la página de inicio si el inicio de sesión es exitoso
    else:
        return 'Invalid username or password'
    
    #my damn knee is cracking
@app.route('/register', methods=['POST'])
def Register():
    if request.method == 'POST':
        # procesing forms data
        print("procesing data..")
    return render_template('register.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug = True)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                width: 50%;
                background-color: #f9f9f9;
            }
            .header {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }
            .header img {
                margin-right: 20px;
                border-radius: 10px;
            }
            .header h2 {
                margin: 0;
            }
            .content h3 {
                color: navy;
                text-align: center;
                margin: 10px 0;
            }
            .content label {
                display: block;
                text-align: center;
                margin: 5px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSBHzh8VgL1KUEaB8z8Qf8vn_e2Yjho54lQQ&s" alt="Logo" width="100">
                <h2>Universidad Tecnologica de la Huasteca Hidalguense</h2>
            </div>
            <div class="content">
                <h3>Ingeniería en Desarrollo y Gestión de Software</h3>
                <h3>Extracción de Conocimientos en Base de Datos</h3>
                <label>Alumno: José Arturo Hernández Campos - 20210675</label>
                <label>Noveno Cuatrimestre  Grupo A</label>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

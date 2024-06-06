from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los contactos
contacts = []

@app.route('/')
def home():
    def contact_item(contact):
        return f'''
        <li>
            {contact["name"]} - {contact["phone"]}
            <form action="/remove_contact" method="post" style="display: inline;">
                <input type="hidden" name="name" value="{contact["name"]}">
                <input type="hidden" name="phone" value="{contact["phone"]}">
                <input type="submit" value="Eliminar">
            </form>
        </li>
        '''
     
    contact_list = ''.join(contact_item(contact) for contact in contacts)
    return f'''
    <html>
    <head>
        <style>
            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                width: 50%;
                background-color: #f9f9f9;
            }}
            .header {{
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }}
            .header img {{
                margin-right: 20px;
                border-radius: 10px;
            }}
            .header h2 {{
                margin: 0;
            }}
            .content h3 {{
                color: navy;
                text-align: center;
                margin: 10px 0;
            }}
            .content label {{
                display: block;
                text-align: center;
                margin: 5px 0;
            }}
            .form-container {{
                margin-top: 20px;
                text-align: center;
                width: 100%;
            }}
            .form-container form {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .form-container input[type="text"], .form-container input[type="tel"] {{
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
                width: 80%;
                max-width: 300px;
            }}
            .form-container input[type="submit"] {{
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                background-color: navy;
                color: white;
                cursor: pointer;
                margin-top: 10px;
                width: 50%;
                max-width: 150px;
            }}
            .contact-list {{
                margin-top: 20px;
                text-align: center;
            }}
            .contact-list ul {{
                list-style-type: none;
                padding: 0;
            }}
            .contact-list li {{
                margin: 5px 0;
            }}
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
                <label>Cuatrimestre: Noveno  Grupo: A</label>
            </div>
            <div class="form-container">
                <form action="/add_contact" method="post">
                    <input type="text" name="name" placeholder="Nombre del contacto" required>
                    <input type="tel" name="phone" placeholder="Teléfono del contacto" required>
                    <input type="submit" value="Agregar Contacto">
                </form>
            </div>
            <div class="contact-list">
                <h3>Contactos</h3>
                <ul>
                    {contact_list}
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    contacts.append({'name': name, 'phone': phone})
    return redirect(url_for('home'))

@app.route('/remove_contact', methods=['POST'])
def remove_contact():
    name = request.form['name']
    phone = request.form['phone']
    contacts[:] = [contact for contact in contacts if not (contact['name'] == name and contact['phone'] == phone)]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

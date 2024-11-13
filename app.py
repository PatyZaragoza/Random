from flask import Flask, render_template, send_file
import nbformat
from nbconvert import HTMLExporter
import os

app = Flask(__name__)

# Ruta del archivo Notebook
NOTEBOOK_PATH = '/home/paty/Documentos/septimo7/Programacion_logica/RandomForest.ipynb'
HTML_OUTPUT_PATH = '/home/paty/Documentos/septimo7/Programacion_logica/RandomForest.html'


@app.route('/')
def index():
    # Convertir el notebook a HTML si no existe o está desactualizado
    if not os.path.exists(HTML_OUTPUT_PATH) or os.path.getmtime(NOTEBOOK_PATH) > os.path.getmtime(HTML_OUTPUT_PATH):
        with open(NOTEBOOK_PATH) as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)
        html_exporter = HTMLExporter()
        body, _ = html_exporter.from_notebook_node(notebook_content)
        with open(HTML_OUTPUT_PATH, 'w') as html_file:
            html_file.write(body)
    return render_template('index.html')


@app.route('/notebook')
def show_notebook():
    # Servir el HTML convertido
    return send_file(HTML_OUTPUT_PATH)


if __name__ == '__main__':
    app.run(debug=True)

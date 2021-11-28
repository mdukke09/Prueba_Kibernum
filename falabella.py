from flask import Flask, jsonify, request
from patentes import *
from matriz import *

app = Flask(__name__)

@app.route('/consultarporpatente/<patente>')
def buscarId(patente):
    return jsonify({"Id":consultarPatente(patente)})

@app.route('/consultarporid/<id>')
def buscarPatente(id):
    return jsonify({"patente": consultarPatente(int(id))})

@app.route('/matriz')
def matriz():
    parameter = request.args.to_dict()
    return jsonify({"Resultado":calcularMatriz(int(parameter['r']),int(parameter['c']),int(parameter['z']),int(parameter['x']),int(parameter['y']))})

if __name__ == '__main__':
    app.run(debug=True)
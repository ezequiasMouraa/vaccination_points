from flask import jsonify, request
from app import app, models

# Rota para obter os pontos de vacinação em formato JSON
@app.route('/api/vaccination-points', methods=['GET'])
def get_vaccination_points():
    return jsonify({'vaccination_points': [vars(point) for point in models.vaccination_points]})

# Rota para adicionar um novo ponto de vacinação
@app.route('/api/add-vaccination-point', methods=['POST'])
def add_vaccination_point():
    data = request.json
    new_point = models.VaccinationPoint(data['name'], data['coordinates'])
    models.vaccination_points.append(new_point)
    return jsonify({'message': 'Ponto de vacinação adicionado com sucesso!'})

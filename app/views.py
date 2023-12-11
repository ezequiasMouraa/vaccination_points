from flask import render_template
from app import app, models

# Rota principal que renderiza o mapa na página HTML
@app.route('/')
def index():
    return render_template('map.html', vaccination_points=models.vaccination_points)

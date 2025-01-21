from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.config import Config
import requests
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/novo-agendamento', methods=['GET', 'POST'])
def new_booking():
    if request.method == 'POST':
        # Captura os dados do formulário
        booking_data = {
            'responsavel': request.form.get('responsavel'),
            'sala': request.form.get('sala'),
            'data': request.form.get('data'),
            'hora_inicio': request.form.get('hora_inicio'),  # Corrigido
            'hora_fim': request.form.get('hora_fim'),        # Corrigido
            'email': request.form.get('email')
        }

        try:
            # Faz o POST para o backend
            response = requests.post(f"{Config.FASTAPI_URL}/agendamentos/", json=booking_data)
            if response.status_code == 200:
                flash('Agendamento realizado com sucesso!', 'success')
                return redirect(url_for('main.my_bookings'))
            else:
                flash('Erro ao realizar agendamento.', 'error')
        except requests.exceptions.RequestException:
            flash('Erro de conexão com o servidor.', 'error')
            
    return render_template('booking_form.html')

@main.route('/meus-agendamentos')
def my_bookings():
    try:
        # Faz o GET para listar os agendamentos
        response = requests.get(f"{Config.FASTAPI_URL}/agendamentos/")
        if response.status_code == 200:
            bookings = response.json().get('agendamentos', [])
        else:
            bookings = []
            flash('Erro ao carregar agendamentos.', 'error')
    except requests.exceptions.RequestException:
        bookings = []
        flash('Erro de conexão com o servidor.', 'error')
        
    return render_template('my_bookings.html', bookings=bookings)

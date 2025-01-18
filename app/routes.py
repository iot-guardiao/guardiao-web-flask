from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/novo-agendamento', methods=['GET', 'POST'])
def new_booking():
    if request.method == 'POST':
        booking_data = {
            'data': request.form.get('data'),
            'sala': request.form.get('sala'),
            'horario': request.form.get('horario'),
            'responsavel': request.form.get('responsavel'),
            'email': request.form.get('email'),
            'discord': request.form.get('discord', '')
        }
        
        try:
            response = requests.post(f"{Config.FASTAPI_URL}/agendar", json=booking_data)
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
        response = requests.get(f"{Config.FASTAPI_URL}/agendamentos")
        if response.status_code == 200:
            bookings = response.json()
        else:
            bookings = []
            flash('Erro ao carregar agendamentos.', 'error')
    except requests.exceptions.RequestException:
        bookings = []
        flash('Erro de conexão com o servidor.', 'error')
        
    return render_template('my_bookings.html', bookings=bookings)
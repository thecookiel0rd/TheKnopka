from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Глобальная переменная для хранения статуса
current_status = "unknown"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status_page():
    return f"Статус: {current_status}"

@app.route('/knopka_on')
def knopka_on():
    global current_status
    current_status = "ON"
    socketio.emit('status_update', {'status': current_status})
    return f"Статус изменен на: {current_status}"

@app.route('/knopka_off')
def knopka_off():
    global current_status
    current_status = "OFF"
    socketio.emit('status_update', {'status': current_status})
    return f"Статус изменен на: {current_status}"

@socketio.on('connect')
def handle_connect():
    emit('status_update', {'status': current_status})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    
    
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import threading

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '1234aboba'
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Глобальная переменная для хранения статуса
# current_status = "unknown"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/knopka_on')
# def knopka_on():
#     global current_status
#     current_status = "ON"
#     # Отправляем обновление всем подключенным клиентам
#     socketio.emit('status_update', {'status': current_status})
#     return f"Статус изменен на: {current_status}"

# @app.route('/knopka_off')
# def knopka_off():
#     global current_status
#     current_status = "OFF"
#     # Отправляем обновление всем подключенным клиентам
#     socketio.emit('status_update', {'status': current_status})
#     return f"Статус изменен на: {current_status}"

# @socketio.on('connect')
# def handle_connect():
#     # При подключении отправляем текущий статус
#     emit('status_update', {'status': current_status})

# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=5000, debug=True)
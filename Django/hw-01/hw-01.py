# Задание 1.
# Найдите ошибку в коде

# В декораторе @app.route('') отсутствует слэш /, который указывает на корневой URL.

# Задание 2.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello, {username} !'


if __name__ == '__main__':
    app.run(debug=True)

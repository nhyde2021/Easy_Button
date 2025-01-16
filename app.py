# from flask import Flask, render_template, request
# import random

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     chance = random.randint(1, 20)
#     value = random.randint(1, 20)
#     return f'Chance: {chance}, Value: {value}'

# if __name__ == '__main__':
#     app.run(debug=True)
# Лабораторная работа 3
# Ревва Евгений
# Вариант 8
#lr3.py
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']

        with open('answers.txt', 'a') as file:
            file.write(f'Имя: {name}\n')
            file.write(f'Любимое животное: {answer1}\n')
            file.write(f'Описание {answer1}: {answer2}\n')
            file.write('\n')

        return 'Спасибо за ответы!'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
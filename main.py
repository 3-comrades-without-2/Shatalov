from flask import Flask, render_template, request

app = Flask(__name__)
a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33},
     {'name': 'Tom', 'id': 2, 'surname': 'York', 'age': 50}]


@app.route('/')
def direct():
    return render_template('template1.html')


@app.route('/users')
def output():
    return render_template('template2.html', a=a)


@app.route('/info/<id>')
def info(id):
    numb = int(id)
    for i in a:
        if i['id'] == numb:
            dct = i
    return render_template('template3.html', dct=dct)


@app.route('/add_user', methods=['post'])
def add_user():
    name = request.form.get('name')
    surname = request.form.get('surname')
    age = request.form.get('age')
    maximum = 0
    for i in a:
        if i['id'] > maximum:
            maximum = i['id']
    a.append({'name': name, 'id': maximum + 1, 'surname': surname, 'age': age})
    return render_template('template2.html', a=a)


if __name__ == '__main__':
    app.run()

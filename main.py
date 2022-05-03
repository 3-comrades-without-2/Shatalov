from flask import Flask, render_template

app = Flask(__name__)
a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33},
     {'name': 'Tom', 'id': 2, 'surname': 'York', 'age': 50}]


@app.route('/')
def direct():
    return render_template('template1.html')


@app.route('/users', methods=['GET', 'POST'])
def output():
    return render_template('template2.html', a=a)


@app.route('/info/<id>', methods=['GET', 'POST'])
def info(id):
    numb = int(id)
    for i in a:
        if i['id'] == numb:
            dct = i
    return render_template('template3.html', dct=dct)


if __name__ == '__main__':
    app.run()

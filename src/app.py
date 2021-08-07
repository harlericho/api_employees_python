from flask import Flask, jsonify, request
from flask_cors import CORS
import employees

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    try:
        data = employees.getList()
        list = []
        for i in data:
            file = {'id': i[0], 'names': i[1], 'email': i[2],
                    'age': i[3]}
            list.append(file)
        return jsonify({'employees': list})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/<int:id>', methods=['GET'])
def search(id):
    try:
        data = employees.getListId(id)
        if data != None:
            return jsonify({'employees': data})
        else:
            return jsonify({'employees': 'No data'})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/', methods=['POST'])
def create():
    try:
        json = request.json
        if request.method == 'POST':
            names = json['names']
            email = json['email']
            age = json['age']
        data = employees.postData(names, email, age)
        if data == True:
            return jsonify({'employees': 'Save data'})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        json = request.json
        if request.method == 'PUT':
            names = json['names']
            email = json['email']
            age = json['age']
        data = employees.putData(names, email, age, id)
        if data == True:
            return jsonify({'employees': 'Updating data'})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        data = employees.deleteData(id)
        if data != None:
            return jsonify({'employees': 'DeLeting data'})
        else:
            return jsonify({'employees': 'No data'})
    except Exception as e:
        return jsonify({'Error': e})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

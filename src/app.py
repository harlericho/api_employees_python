from flask import Flask, jsonify, request
from flask_cors import CORS
import employees
import validations
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
            file = {'id': data[0], 'names': data[1], 'email': data[2],
                    'age': data[3]}
            return jsonify({'employees': file})
        else:
            return jsonify({'employees': 'No data with that id'})
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
        if validations.validations(names, email, age):
            return jsonify({'errors':'There are null values ​​in the data inputs'})
        else:
            data = employees.postData(names, email, age)
            if data == True:
                return jsonify({'employees': 'Save data'})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        file = employees.getListId(id)
        if file != None:
            json = request.json
            if request.method == 'PUT':
                names = json['names']
                email = json['email']
                age = json['age']
            data = employees.putData(names, email, age, id)
            if data == True:
                return jsonify({'employees': 'Updating data'})
        else:
            return jsonify({'employees': 'No data with that id'})
    except Exception as e:
        return jsonify({'Error': e})


@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        file = employees.getListId(id)
        if file != None:
            data = employees.deleteData(id)
            return jsonify({'employees': 'DeLeting data'})
        else:
            return jsonify({'employees': 'No data with that id'})
    except Exception as e:
        return jsonify({'Error': e})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

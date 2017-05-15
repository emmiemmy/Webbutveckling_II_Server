from flask import Flask, render_template, request, json, abort, jsonify
import codecs

import os, sys

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False
path = os.path.dirname(os.path.abspath(__file__)) + "/database.json";


# Route to startpage
@app.route('/')
def index():
    return render_template('index.html')


# Route to where the data is saved to file and user is getting redirected to confirmation page
@app.route('/done', methods=['POST'])
def confirmation():
    # Create new user

    new_user = {
        "firstname": request.form['firstNameInput'],
        "lastname": request.form['lastNameInput'],
        "ssn": request.form['ssnInput'],
        "email": request.form['emailInput'],
        "adress": request.form['adressInput'],
        "comment": request.form['commentInput']
    }

    #Specify path
    # path = os.path.dirname(os.path.abspath(__file__)) + "/database.json";

    # Check if there is a file, if not, create one
    if not os.path.isfile(path):
        print("Creating file...")
        with open(path, 'w') as file:
            json.dump([], file)
            file.close()

    # Open exisitng file content and store it in variable
    with open(path, 'r')as file:
        json_data = json.load(file)
        file.close()

        # append new data
        json_data.append(new_user)

    # save appended data in database
    with open(path, 'w+') as f:
        json.dump(json_data, f, indent=4, )

    return render_template('done.html', user=new_user)


# Route retrieves all data saved in file database.json and displays the data in JSON format
@app.route('/users')
def get_users():

    with open(
            path, 'r',
            encoding='utf-8') as file:
        json_users = json.load(file)

    return jsonify({'users':json_users})

#Route retrieves object matching with specified id
@app.route('/users/<ssn>', methods=['GET'])
def get_user(ssn):
    # read all users in file and store in list
    with open(path) as file:
        json_users = json.load(file)

    # search for specific user
    user = [user for user in json_users if user['ssn'] == ssn]

    # if user id was not found
    if len(user) == 0:
        return render_template('pagenotfound.html', errorMessage="User doesn't exist")

    # Package result as JSON
    return jsonify({'user': user[0]})

#route called if page is not found
@app.errorhandler(404)
def doesntexist(error):
    return render_template('pagenotfound.html', errorMessage="Page not found")





if __name__ == '__main__':
    app.run(debug=True)

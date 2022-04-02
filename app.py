from flask import Flask, jsonify, request

app = Flask(__name__)

my_dict = {'nama' : 'Runeka',
                'usia' : 18,
                'pekerjaan' : 'Neet'}

@app.route("/") # home page
def hello_world():
    return jsonify(my_dict)

@app.route("/input", methods=['POST'])
def profile():
    global my_dict
    content = request.json
    my_dict['nama'] = content['nama']
    my_dict['usia'] = content['usia']
    my_dict['pekerjaan'] = content['perkerjaan']

app.run()
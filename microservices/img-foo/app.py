from flask import Flask, Blueprint, jsonify
import requests

NAME = 'Foo API App'

api = Blueprint('api', __name__)

@api.route('/ping/<service>')
def get_service(service):
    res = None
    try:
        r = requests.get('http://'+service+'/')
        res = r.ok
    except ConnectionRefusedError:
        res = False
    return jsonify({
        'service-exists': res
    })

app = Flask(NAME)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def get_name():
    return jsonify({
        'name': NAME
    })

if __name__ == "__main__":
    print(app.url_map)
    app.run(host='0.0.0.0', port=80)
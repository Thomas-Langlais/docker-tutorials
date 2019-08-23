from flask import Flask, Blueprint, jsonify
from redis import Redis, RedisError
import requests, psycopg2

NAME = 'Bar API App'

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
pg = psycopg2.connect(host='db', dbname='postgres', user='postgres')

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


def get_name():
    visits = None
    users = None
    try:
        visits = redis.incr("counter")
        cur = pg.cursor()
        cur.execute('SELECT * FROM users;')
        users = list(cur)
        cur.close()
    except Exception:
        visits = -1
        users: []
    finally:
        return jsonify({
            'name': NAME,
            'visits': visits,
            'users': users
        })

app = Flask(NAME)

api = Blueprint('api', 'api')
api.add_url_rule('/ping/<service>', view_func=get_service, provide_automatic_options=False)

app.register_blueprint(api, url_prefix='/api')
app.add_url_rule('/', view_func=get_name, provide_automatic_options=False)

if __name__ == "__main__":
    print(app.url_map)
    app.run(host='0.0.0.0', port=80)
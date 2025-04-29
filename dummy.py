from flask import Flask, request, jsonify
from configparser import ConfigParser
import logging
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser()
config.read(f'{dir_path}/dummy.cfg')

logging.basicConfig(
    filename=config['LOGGING']['log_file'],
    level=config['LOGGING']['log_level'])

app = Flask(__name__)



@app.route('', methods=['GET'])
def landing():
    return f"Application is running successfully!"


@app.route('env_check', methods=['GET'])
def env_check():
    env_dict = {'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('RDS_DB_NAME',None),
            'USER': os.environ.get('RDS_USERNAME',None),
            'PASSWORD': os.environ.get('RDS_PASSWORD',None),
            'HOST': os.environ.get('RDS_HOSTNAME',None),
            'PORT': os.environ.get('RDS_PORT',None),
        }}
    return f"{env_dict} fetched successsfully!"



@app.route('/dummy', methods=['GET'])
def dummy():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    logging.info(f"{firstname} {lastname}")
    return f"{firstname} {lastname}"


if __name__ == "__main__":
    app.run(host=config['APISERVER']['api_host'],
            port=config['APISERVER']['api_port'])

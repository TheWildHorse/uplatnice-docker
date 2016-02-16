from flask import Flask
from flask import request
from flask import send_from_directory
from uplatnica import kreiraj_uplatnicu

app = Flask(__name__)

@app.route("/uplatnica", methods=['POST'])
def generirajUplatnicu():
	uplatnica = kreiraj_uplatnicu(request.data)
	open('generated/uplatnica.pdf', 'w').write(uplatnica)
	return send_from_directory('generated', 'uplatnica.pdf')

if __name__ == "__main__":
	app.run(host='0.0.0.0')

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user<user_id>")
def get_user(user_id):
  user_data = {
    'user_id': user_id,
    'name': "Huck Finn",
    'email': 'huck.finn@example.com'
  }

  extra = request.args.get('extra')
  if extra:
    user_data['extra'] = extra

  return jsonify(user_data), 200

@app.route('/create-user', methods=["Post"])
def create_user():
  data = request.get_json()

  return jsonify(data), 201

'''@app.route('/')
def home():
  return "Home" '''

if __name__ == "__main__":
  app.run(debug=True)
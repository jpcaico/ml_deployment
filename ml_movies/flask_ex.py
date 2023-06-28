from flask import Flask, jsonify, request


best_friends = {'Monica':'Rachel', 'Joey':'Chandler', 'Ross':'Phoebe'}

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    # Test through terminal by running curl http://0.0.0.0:80
    return jsonify(message = "Hello from root!")

@app.route("/find_friend", methods=['POST','GET'])
def get_best_friend():
    print(request.json)
    data = request.json
    person = data['person']
    #curl -X POST http://0.0.0.0:80/find_friend -H 'Content-Type: application/json' -d '{"person:"Joey"}'
    return {"best_friend": best_friends[person]}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80)
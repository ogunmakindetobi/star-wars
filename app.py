import os 
from flask import Flask


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("")
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
starships = mongo.db.ships

@app.route("/starships")
def starships():
    hyperdriveSorted = startships.find().sort({"hyperdrive": 1})
    return jsonify(data)



if __name__== "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

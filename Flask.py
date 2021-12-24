from flask import Flask, json,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "id":1,
        "name":"Rahul",
        "contact":"9988776655",
        "done":False
    },
    {
        "id":2,
        "name":"Rohan",
        "contact":"5544332211",
        "done":False
    }
]


@app.route("/")
def hello_words():
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    
    contact = {
        "id":contacts[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"sucsess",
        "message":"Contact added sucessfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts,
    })


if (__name__ == "__main__"):
    app.run(debug=True)
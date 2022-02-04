
from os import remove
from flask import Flask,request,jsonify

app=Flask(__name__)



FAKE_DATABASE=[]

count =0
#CRUD
#CREATE
@app.route("/register",methods=["POST"])
def home2():
    u=request.json["username"]
    p=request.json["password"]
    f=request.json["fname"]
    l=request.json["lname"]
    e=request.json["email"]

    global count
    count+=1
    user_object={
        "id":count,
        "username":u,
        "password":p,
        "fname":f,
        "lname":l,
        "email":e
    }
    
    FAKE_DATABASE.append(user_object)
    return jsonify(user_object)

#READ
@app.route("/users",methods=["GET"])
def home():
    return jsonify(FAKE_DATABASE)

#UPDATE
@app.route("/user/<int:id>",methods=["PATCH"])
def patch_users(id):
    for u in FAKE_DATABASE:
     if  u["id"]==id:
         u["username"]=request.json["username"]

    return jsonify(u)

#DELETE
@app.route("/user/<int:id>",methods=["DELETE"])
def delete_user(id):
    for u in FAKE_DATABASE:
        if u["id"]==id:
            FAKE_DATABASE.remove(u)
    return f"User with id {id} deleted"


if __name__ == '__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )


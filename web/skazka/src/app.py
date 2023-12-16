from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    make_response,
    request,
)
from os import environ
import jwt


app = Flask(__name__)

ids_with_images = {
    "111": "../static/111.png",
    "11": "../static/11.jpg",
    "12": "../static/12.jpg",
    "13": "../static/13.png",
    "15": "../static/15.png",
    "21": "../static/21.png",
    "22": "../static/22.png",
    "23": "../static/23.png",
    "42": "../static/42.png",
    "73": "../static/73.png",
    "85": "../static/85.png",
    "91": "../static/91.png",
    "72": "../static/72.png",
    "53": "../static/53.png",
}

hidden_id = "787"


def generate_jwt():
    payload = {"username": "user"}
    token = jwt.encode(payload, "G0nd0liN", algorithm="HS256")
    return token


def verify_jwt(token):
    try:
        decoded_token = jwt.decode(
            token, "G0nd0liN", algorithms=["HS256"], options={"verify_exp": False}
        )
        return decoded_token
    except Exception:
        print("Token Decode Error")
        return None


@app.route("/")
def home():
    token = generate_jwt()
    response = make_response(
        render_template(
            "home.html", ids_with_images=ids_with_images, hidden_id=hidden_id
        )
    )
    response.set_cookie("jwt", token, httponly=True)
    return response


@app.route("/object/id=<string:id>")
def object(id):
    token = request.cookies.get("jwt")
    decoded_token = verify_jwt(token) if token else None
    print(f"Token: {token}")
    print(f"Decoded Token: {decoded_token}")

    if id == hidden_id and decoded_token and decoded_token.get("username") == "admin":
        print("Flag is shown!")
        return environ.get("FLAG")
    if id in ids_with_images or id == hidden_id:
        image_path = ids_with_images.get(id, "../static/787.png")
        return render_template("object.html", id=id, image_path=image_path)
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

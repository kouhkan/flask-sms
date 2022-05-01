import os

from flask import Flask, request
from src.flask_sms import FLASKOtp

app = Flask(__name__)
app.config["KAVENEGAR_TOKEN"] = os.getenv("KAVENEGAR_TOKEN")

template = os.getenv("KAVENEGAR_TEMPLATE")

sms = FLASKOtp(app=None)
sms.init_app(app, template)


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()

    receptor = data["receptor"]
    token = "2345"
    response = sms.verify_lookup(phone_number=receptor,
                                 token=token)

    print(response)

    return "ok"

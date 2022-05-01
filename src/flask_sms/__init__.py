"""Flask SMS Module."""

import typing as t

from flask import Flask
from kavenegar import *


class FLASKOtp(KavenegarAPI):
    """Flask SMS Extension."""
    _client: KavenegarAPI

    def __init__(self, app: t.Optional[Flask] = None) -> None:
        """Initialize FlaskSMS."""
        if app is not None:
            self.init_app(app)

        self.template = None

    def init_app(self, app: Flask, template: str):
        """Initialize FlaskSMS with App Context."""
        super().__init__(
            app.config["KAVENEGAR_TOKEN"]
        )
        self.template = template
        app.extensions["sms"] = self

    def verify_lookup(self, phone_number: str, token: str):
        params = {
            'receptor': phone_number,
            'template': self.template,
            'token': token,
            'type': 'sms',
        }
        return KavenegarAPI.verify_lookup(self, params)


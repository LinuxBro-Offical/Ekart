from django.conf import settings
import pyotp
import telnyx
import requests


class OTPMixin():
    totp = pyotp.TOTP('base32secret3232', interval=60)

    def generate_otp(self, mobile):
        print(self.totp.now())
        # self.send_sms(mobile,self.totp.now())

    def verify_otp(self, otp):
        print("verification:", self.totp.verify(otp))
        return self.totp.verify(otp)

    def send_sms(mobile, otp):
        telnyx.api_key = settings.API_KEY
        status = telnyx.Message.create(
            to=mobile,
            from_= settings.FROM_NUMBER,
            text='Kart69 OTP is '+otp +
                 '.Use this to verify your mobile. -TM KART69'
        )
        return status


class BGremove():
    def post_image(self, path):
        response = requests.post(
            settings.BG_REMOVE_URL,
            files={'image_file': open(path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': settings.BG_REMOVE_API_KEY},
            verify=False
        )
        print("BG REMOVE RESPONSE:", response)
        return response

    def remove_bg(self, path):
        response = self.post_image(path)
        if response.status_code == requests.codes.ok:
            with open(path, 'wb') as out:
                out.write(response.content)
        else:
            return("Error:", response.status_code, response.text)

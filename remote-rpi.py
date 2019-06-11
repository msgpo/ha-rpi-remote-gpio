# example taken from https://community.home-assistant.io/t/remote-raspberry-pi-3-gpio/44406/10
from flask import Flask
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(21, GPIO.OUT)
# pin = 21

app = Flask(__name__)


@app.route('/GPIO/<strCommand>', methods={'GET', 'POST'})
def relay_control(strCommand):
    print('Received: ' + strCommand)
    if strCommand == 'on':
        print('On Processed')
        return "Now On"
        # GPIO.output(pin, GPIO.HIGH)
    elif strCommand == 'off':
        print('Off Processed')
        # GPIO.output(pin, GPIO.LOW)
        return "Now Off"
    else:
        print("echo back: "+strCommand)
        return "echo back: "+strCommand


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()

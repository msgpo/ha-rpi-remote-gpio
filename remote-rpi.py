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
        # GPIO.output(pin, GPIO.HIGH)
    elif strCommand == 'off':
        print('Off Processed')
        # GPIO.output(pin, GPIO.LOW)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

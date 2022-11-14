from flask import Flask
import time
import gphoto2 as gp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Kevin!</p>"

camera = gp.Camera()
print('Please connect and switch on your camera')
while True:
    try:
        camera.init()
    except gp.GPhoto2Error as ex:
        if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND:
            # no camera, try again in 2 seconds
            time.sleep(2)
            print('Trying again')
            continue
        # some other error we can't handle here
        raise
    # operation completed successfully so exit loop
    break
print('Camera connected')



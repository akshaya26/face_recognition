from flask import Flask, render_template, Response, request, jsonify
from recog import VideoCameraDetection



app = Flask(__name__)

@app.route('/mai')
def index():
    return render_template("detection.html")

def gen(camera):
    count = 0
    while True:
        frame, count1 = camera.get_frame(count)
        count = count1
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/detection')
def detection():
  #  ans = request.args.get('answer')
    #count = request.json
    #cnt = count['counts']
    #print(cnt)
    return Response(gen(VideoCameraDetection()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def ma():
    return render_template("initial.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
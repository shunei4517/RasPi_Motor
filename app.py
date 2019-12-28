from flask import Flask, render_template
import motor
import pigpio
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="モーターカー")

@app.route('/forward')
def forward_motor():
    Motor = motor.Motor_Ctrl(18,15,20,21)
    Motor.forward()
    return "forward"

@app.route('/back')
def back_motor():
    Motor = motor.Motor_Ctrl(18,15,20,21)
    Motor.back()
    return "back"

@app.route('/stop')
def stop_motor():
    Motor = motor.Motor_Ctrl(18,15,20,21)
    Motor.stop()
    return "stop"

@app.route('/right')
def right_motor():
    Motor = motor.Motor_Ctrl(18,15,20,21)
    Motor.right()
    return "right"

@app.route('/left')
def left_motor():
    Motor = motor.Motor_Ctrl(18,15,20,21)
    Motor.left()
    return "left"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    

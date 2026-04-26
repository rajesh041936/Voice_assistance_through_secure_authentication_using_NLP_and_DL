from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)

CONTROL_FILE = '/home/raspberrypi/Desktop/rover_control.txt'

logging.basicConfig(
    filename='/home/raspberrypi/Desktop/rover_flask/flask.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# ---------------------------
# HOME PAGE
# ---------------------------
@app.route('/')
def index():
    logging.info("Opened Home Page")
    return render_template('index.html')


# ---------------------------
# MODE SELECTION
# ---------------------------
@app.route('/select_mode', methods=['POST'])
def select_mode():
    mode = request.form.get('mode')

    if mode not in ['AUTO', 'MANUAL']:
        logging.error(f"Invalid mode selected: {mode}")
        return "Invalid mode", 400

    # Whenever mode changes → reset to STOP
    try:
        with open(CONTROL_FILE, 'w') as f:
            f.write(f"{mode},65,STOP\n")
        logging.info(f"Mode updated: {mode}, speed=65, STOP")
    except Exception as e:
        logging.error(f"Error writing mode: {str(e)}")
        return f"Write error: {str(e)}", 500

    if mode == 'AUTO':
        return redirect(url_for('autonomous'))
    else:
        return redirect(url_for('manual'))


# ---------------------------
# AUTONOMOUS PAGE
# ---------------------------
@app.route('/autonomous')
def autonomous():
    logging.info("Opened Autonomous Page")
    return render_template('autonomous.html')


# ---------------------------
# MANUAL PAGE
# ---------------------------
@app.route('/manual')
def manual():
    logging.info("Opened Manual Page")
    return render_template('manual.html')


# ---------------------------
# RECEIVE REAL-TIME COMMANDS
# ---------------------------
@app.route('/command', methods=['POST'])
def command():
    mode = request.form.get('mode', 'MANUAL')
    speed = request.form.get('speed', '65')
    cmd = request.form.get('command', 'STOP')

    logging.debug(f"CMD Received → Mode={mode} Speed={speed} Command={cmd}")

    try:
        # Write instantly — overwrite previous command
        with open(CONTROL_FILE, 'w') as f:
            f.write(f"{mode},{speed},{cmd}\n")

        logging.info(f"CMD Written → {mode},{speed},{cmd}")

    except Exception as e:
        logging.error(f"Error writing command: {str(e)}")
        return f"Write error: {str(e)}", 500

    return "OK"


# ---------------------------
# START SERVER
# ---------------------------
if __name__ == '__main__':
    logging.info("Starting Flask control server…")
    app.run(host='0.0.0.0', port=8080, debug=True)

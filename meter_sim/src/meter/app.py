from meter_sim.src.meter import app
import os

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/start', methods=['GET'])
def start():
    return "Starting.."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import *
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = False


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('Prototype.html')
        
if __name__ == '__main__':
   app.run()
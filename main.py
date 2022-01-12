print("Shammi")

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return " \n This is flask application da kumaru "



if __name__ == "__main__":
    app.run()

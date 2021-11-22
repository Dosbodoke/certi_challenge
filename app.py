from src.utils import number_is_valid, number_to_text_format
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return f"Do a GET request to '{request.host_url}<number>' where number is an integer in the range from -99999 to 99999."

@app.route("/<number>", methods=['GET'])
def translate(number):
    if number_is_valid(number):
        return {"extenso": number_to_text_format(number)}

    return {"error": "Incorrect input format, input should be a number and be in the range from -99999 to 99999"}

if __name__ == "__main__":
    app.run(debug=True)

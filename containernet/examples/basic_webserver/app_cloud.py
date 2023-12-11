from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def save():
    return "Hello world.\n"
    myFile = open("data", 'a+')
    myFile.write(str(request.data))
    myFile.close()
    return "{'success':'true'}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    

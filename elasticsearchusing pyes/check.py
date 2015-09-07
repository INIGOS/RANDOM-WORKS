from flask import Flask, request
app=Flask(__name__)

@app.route('/', methods=['GET'])
def names():
    name = request.args.get("input")
    return name

if __name__=="__main__":
    app.run(debug=True)
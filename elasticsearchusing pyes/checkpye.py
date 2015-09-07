from flask import Flask, request
from pyes import *
app=Flask(__name__)
conn = ES('176.9.26.112:9200')
conn.default_indices=["twitter-index"]

@app.route('/', methods=['GET'])
def name():
    name = request.args.get("input")
    res=conn.search({ "match_all": {}},index="twitter-index")
    for r in res:
        print r
    return name

if __name__=="__main__":
    app.run(debug=True)
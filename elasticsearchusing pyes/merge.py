from flask import Flask, request
from pyes import *
app=Flask(__name__)
conn = ES('176.9.26.112:9200')
conn.default_indices=["twitter-index"]

@app.route('/', methods=['GET'])
def name():
    name = request.args.get("input")
    print name
    q = name

    a={
        "query_string":{
            "query": q
        }
    }
    res=conn.search(a,index="twitter-index")
    print res.total
    a=[]
    for r in res:
        a.append(r)

    return str(a)

if __name__=="__main__":
    app.run(debug=True)
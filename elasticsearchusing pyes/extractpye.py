from flask import Flask, request
from pyes import *
app = Flask(__name__)


@app.route('/', methods=['GET'])
def name():
    name = request.args.get("input")
    return name

conn = ES('176.9.26.112:9200')
conn.default_indices = ["twitter-index"]
#conn.indices.refresh(indices="twitter-index")
a = {
    "query_string": {
        "query": "(text:online) "
    }
}
res = conn.search(a, index="twitter-index")
print res.total
for r in res:
    print r

if __name__ == "__main__":
    app.run(debug=True)
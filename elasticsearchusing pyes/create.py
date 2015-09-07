from pyes import *
conn=ES('localhost:9200')
#conn.indices.create_index("try-index")
#conn.index({"name":"Joe Tester", "parsedtext":"Joe Testere nice guy", "uuid":"11111", "position":1}, "test-index", "test-type", 1)
conn.indices.refresh
curl -XPUT 'localhost:9200/test/tweet/1' -d '{
    "user":"inigo",
    "post_date":"2015-11-12t14:12:21",
    "message":"trying out elastic search"
}'
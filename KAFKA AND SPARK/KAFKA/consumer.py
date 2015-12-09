from kafka import KafkaConsumer
from pyes import ES
import json

# To consume messages
es=ES()
consumer = KafkaConsumer('test',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print message.value
    es.index(json.loads(message.value),'tweets','tweet',1)
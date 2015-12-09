import sys
from kafka import SimpleProducer, KafkaClient

# To send messages synchronously
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
#f = open('qwe.txt', 'r')
#file_contents = f.read()
#print (file_contents)

# Note that the application is responsible for encoding messages to type bytes
producer.send_messages(b'test', "hey this is INIGO SOLOMON")

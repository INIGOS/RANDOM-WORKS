#bin/spark-submit --jars /home/naren/Desktop/spark/spark-1.5.1-bin-hadoop2.6/spark-streaming-kafka-assembly_2.10-1.5.1.jar spark_kafka.py localhost:2181 test
import multiprocessing
import json
import sys
import uuid
import traceback
from pyspark import SparkContext
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
kafka =  KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
def sendTokafka(partitionData):
    record = partitionData
    Records  = []
    new_record = {'Data':record}
    Records.append(new_record)
    kafka1 =  KafkaClient("localhost:9092")
    producer1 = SimpleProducer(kafka1)
    producer1.send_messages("too",bytes(Records))
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(-1)

    sc = SparkContext(appName="PythonStreamingKafkaWordCount")
    ssc = StreamingContext(sc, 1)

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    lines = kvs.map(lambda x: x[1])
    lines.foreachRDD(lambda rdd: rdd.foreach(sendTokafka))

    ssc.start()
    ssc.awaitTermination()
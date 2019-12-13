import json
import configparser
from kafka import KafkaProducer


cf = configparser.ConfigParser()
cf.read("config.ini")

brokers = cf.get("Kafka", "kafka_brokers")

print(brokers)


#
# producer = KafkaProducer(bootstrap_servers='xxxx:x')
#
#
# producer.send('test_rhj', msg, partition=0)
# producer.close()import json
import configparser
from kafka import KafkaProducer


cf = configparser.ConfigParser()
cf.read("config.ini")

brokers = cf.get("Kafka", "kafka_brokers")

print(brokers)


#
# producer = KafkaProducer(bootstrap_servers='xxxx:x')
#
#
# producer.send('test_rhj', msg, partition=0)
# producer.close()

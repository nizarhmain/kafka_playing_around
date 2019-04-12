you must two external volumes called "cassandra" and "cassandra2_data"

# ENTREPRISE BUSINESS ANALYTICS PART

```
docker volume create cassandra
docker volume create cassandra2_data

```


Then you can have to specify where you want the cassandra tables to be stored, You can do the following by change this line to in the composers/cassandra-compose.yml

```
cassandra:/var/lib/docker/volumes/cassandra

cassandra2_data:/var/lib/docker/volumes/cassandra

# INSTEAD SPECIFY A PATH YOU WANT

cassandra:C:\MY_WINDOWS_PATH

cassandra2_data:C:\MY_WINDOWS_PATH

```

Finally the base image boots up with 4 GB of RAMS for each cassandra container (8GB of RAM total), if you have limited RAM, just comment out in the cassandra-compose.yml file 
```
services:
  cassandra1:
    image: 'cassandra'

    volumes:
      - cassandra:/var/lib/docker/volumes/cassandra
          
    environment:
      - CASSANDRA_BROADCAST_ADDRESS=cassandra1
  
  # cassandra2:
  #   image: 'cassandra'
  #   volumes:
  #     - 'cassandra2_data:/var/lib/docker/volumes/cassandra'
    
  #   environment:
  #     - CASSANDRA_BROADCAST_ADDRESS=cassandra2
  #     - CASSANDRA_SEEDS=cassandra1

```

Now you can start the cassandra containers

```
cd composers
docker-compose --file cassandra-compose.yml up
```

and check on the state of the running containers with 
```
docker ps
```

and finally you can open a new terminal, and run the following command to open a cqlsh session with the cassandra node
```
docker exec -it composers_cassandra1_1 cqlsh
```

# END of ENTREPRISE BUSINESS ANALYTICS PART


```
docker volume create my-vol
```

Then start the docker-compose for kafka and zookeeper
```
docker-compose up -d
```

Then start the docker-compose for cassandra cluster
```
docker-compose -f cassandra-compose.yml up -d
```

# create a new topic kafka
```
bin/kafka-topics.sh --create --zookeeper 172.40.0.5:2181 --replication-factor 1 --partitions 1 --topic test 
```

# find out which topics are running
```
kafka-topics.sh --list --zookeeper 172.40.0.5:2181
```
# install cassandra-sink jar file 

put this thing to libs

```
wget https://github.com/Landoop/stream-reactor/releases/download/1.2.1/kafka-connect-cassandra-1.2.1-2.1.0-all.tar.gz

tar -xvf kafka-connect-cassandra-1.2.1-2.1.0-all.tar.gz
```

# start kafka connect
```
bin/connect-distributed.sh conf/connect-distributed.properties
```

# enable the cassandra connector
```
curl -X POST -H "Content-Type: application/json" -d @connect-cassandra-sink.json 172.40.0.6:8083/connectors



bin/kafka-avro-console-producer \
 --broker-list localhost:9092 --topic orders-topic \
 --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"id","type":"int"},{"name":"created","type":"string"},{"name":"product","type":"string"},{"name":"price","type":"double"}, {"name":"qty", "type":"int"}]}'

```

# testing basic commands with kafkacat

Internal producer command:
```
/opt/bitnami/kafka/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic test


Internal consumer command:

/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning

External producer command:
kafkacat -b 172.40.0.6:9092 -P -t test

External consumer command:
kafkacat -b 172.40.0.6:9092 -C -t test
```


```

curl -X POST -H "Content-Type: application/json" -d @connect-cassandra-source.json localhost:8083/connectors

```

```

CREATE TABLE IF NOT EXISTS "pack_events" (
    event_id TEXT, 
    event_ts TIMESTAMP, 
    event_data TEXT, 
PRIMARY KEY ((event_id),event_ts));


INSERT INTO pack_events (event_id, event_ts, event_data) 
VALUES ('500', '2018–01–22T20:28:50.869Z', '{"foo":"bar"}');

```


# additional useful information
https://medium.com/walmartlabs/getting-started-with-the-kafka-connect-cassandra-source-e6e06ec72e97


#TODO
https://www.baeldung.com/kafka-connectors-guide

# current development now 

```
cd composers

spin up the main broker and the ui

docker-compose -f confluent.yml up

spin up an additional broker 

docker-compose -f test-composer.yml up

```

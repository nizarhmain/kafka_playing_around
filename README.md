you must need to do create an external volume called "cassandra"

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

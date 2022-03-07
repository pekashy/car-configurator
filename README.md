# Car Configurator

### Usage

Start:

```
docker-compose up --build -d
```

Use:
```0.0.0.0:8050/configure``` - to create an order

```0.0.0.0:8050/report``` - to see, how many orders were created


### Components

```
                       Backend Instances
                            +------+
                            |      |
            +---------------+      |<-------+
            |               |      |        |
            |               +------+        |
            |                               |
            |               +------+        |
            |               |      |        |
            |       +-------+      |<-------+   Envoy        Configurator UI
        +---v---+   |       |      |        | +------+          +------+
        |       |   |       +------+        | |      |          |      |
MongoDB |       <---+                       +-+      |<---------+      |
        |       |   |       +------+        | |      |          |      |
        +---^---+   |       |      |        | +------+          +------+
            |       +-------+      |<-------+
            |               |      |        |
            |               +------+        |
            |                               |
            |               +------+        |
            |               |      |        |
            +---------------+      |<-------+
                            |      |
                            +------+
```

- Web UI to place orders
- Envoy as an example, to balance load and perform heathchecks of services
- Backend that is replicated to 4 instances to handle more load
- Mongo as an example of storage. Perhaps in real project this would be not mongo, but some queue for orders which store them before main processing starts.
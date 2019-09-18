# celery-backends-rediscluster

[Celery](http://www.celeryproject.org/)'s custom result backend for [RedisCluster].

This implementation is `Fork` from `@hbasria`'s [repo](github.com/hbasria/celery-redis-cluster-backend.git)

## Usage

1. pip install celery-redis-cluster-backend

2. Add the following to `celeryconfig.py`.

```
CELERY_RESULT_BACKEND = "celery_redis_cluster_backend.backend.RedisClusterBackend"
CELERY_REDIS_CLUSTER_SETTINGS = { 'startup_nodes': [
    {"host": "localhost", "port": "6379"},
    {"host": "localhost", "port": "6380"},
    {"host": "localhost", "port": "6381"}
]}
```

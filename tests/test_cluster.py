from celery import Celery
from redis_cluster_backend import RedisClusterBackend


class Config:
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = 'Europe/Istanbul'
    CELERY_REDIS_CLUSTER_SETTINGS = {'startup_nodes': [
        {"host": "127.0.0.1", "port": "30001"},
        {"host": "127.0.0.1", "port": "30002"},
        {"host": "127.0.0.1", "port": "30003"},
    ]}


def test_basic_set():
    app = Celery()
    app.config_from_object(Config)
    rb = RedisClusterBackend(app=app)
    rb.set('a', 'b1')

# project


https://docs.mongodb.com/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/

# python

## env

```
virtualenv tumbleblogenv
source tumbleblogenv/bin/activate
pip install -r /path/to/requirements.txt
```

## test

```
python manage.py runserver
```

# mongodb

mongodb-linux-x86_64-3.0.1

start_mongodb.sh
```shell
export PATH=$PATH:/home/berg/Work/mongo/mongodb-linux-x86_64-3.0.1/bin/
echo "start mongod (mongodb server part)"
mongod --bind_ip=127.0.0.1 --dbpath /home/berg/Work/mongo/databases &
```

# python module

- [flask-script](http://flask-script.readthedocs.io/en/latest/)
- [Flask-MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [flask MethodView](http://flask.pocoo.org/docs/0.11/views/)
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

# SourceCodes
## modules.py
ORM 管理器
三种表格定义：
- db.Document: 基本类型
- db.EmbeddedDocument： 可嵌入类型
- db.DynamicDocument： 可继承类型

# Dependences
## mongodb

mongodb-linux-x86_64-3.0.1

start_mongodb.sh
```shell
export PATH=$PATH:/home/berg/Work/mongo/mongodb-linux-x86_64-3.0.1/bin/
echo "start mongod (mongodb server part)"
mongod --bind_ip=127.0.0.1 --dbpath /home/berg/Work/mongo/databases &
```

## bootstrap

http://getbootstrap.com/
Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.
最流行的移动优先的响应式框架

向导： http://getbootstrap.com/getting-started/

# python module

- [flask-script](http://flask-script.readthedocs.io/en/latest/)
- [Flask-MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [flask MethodView](http://flask.pocoo.org/docs/0.11/views/)
- [【译】WTForms 2 中文入门教程(速成课程)](https://segmentfault.com/a/1190000002531677)
- Flask之旅 [中文版](http://spacewander.github.io/explore-flask-zh/) [English](http://exploreflask.com)
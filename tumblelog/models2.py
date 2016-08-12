# -*- coding: utf-8 -*-
'''
 本文件参照 https://mongoengine-odm.readthedocs.io/tutorial.htm来编写
'''

from mongoengine import Document, StringField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField, \
    CASCADE


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


'''
An embedded document should be treated no differently that a regular document;
it just doesn’t have its own collection in the database.
'''
class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

'''
We are storing a reference to the author of the posts using a ReferenceField object.
These are similar to foreign key fields in traditional ORMs, and are automatically
translated into references when they are saved, and dereferenced when they are loaded.

MongoDB allows us to store lists of items natively, so rather than having a link table,
we can just store a list of tags in each post.

可以使用to_json或者to_mongo来显示document的内容：
json.loads(post1.to_json())
{u'_cls': u'Post.TextPost',
 u'_id': {u'$oid': u'57ac28a0541ccf99ac3eb44a'},
 u'author': {u'$oid': u'57ac2878541ccf99ac3eb449'},
 u'comments': [],
 u'content': u'Took a look at MongoEngine today, looks pretty cool.',
 u'tags': [u'mongodb', u'mongoengine'],
 u'title': u'Fun with MongoEngine'}

'''
class Post(Document):
    title = StringField(max_length=120, required=True)

    # reverse_delete_rule: To delete all the posts if a user is deleted set the rule:
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {"allow_inheritance": True}


class TextPost(Post):
   content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()



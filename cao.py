# from mongoengine import *
# connect("test")
# class Page(DynamicDocument):
#     title = StringField(max_length = 200, required = True)
# page = Page(title = 'Using MongoEngine')
# page.tags = ['mongodb', 'mongoengine']
# page.save()
#
# from mongoengine import *
# connect("test")
# class User(Document):
#     name = StringField()
# class Page(Document):
#     content = StringField()
#     authors = ListField(ReferenceField(User))
#
# bob = User(name = "Bob Jones").save()
# john = User(name = "John Smith").save()
#
# Page(content = 'Test Page', authors=[bob, john]).save()
# Page(content = "Another Page", authors = [john]).save()
#
# Page.objects(authors__in = [bob])
# print Page.authors.name
#
# Page.objects(authors__all = [bob, john])
from mongoengine import *
connect("test")
class Page(Document):
    title = StringField()

page = Page(title = "test")
page.save()
print page.id

# class User(Document):
#     email = StringField(required = True)
#     first_name = StringField(max_length = 50)
#     last_name = StringField(max_length = 50)
#     #meta = {'ab_alias' : 'mydata'}
#
# class Post(Document):
#     title = StringField(max_length = 120, required=True)
#     author = ReferenceField(User)
#     tags = ListField(StringField(max_length = 30))
#     comments = ListField(EmbeddedDocumentField(Comment))
#     meta = {'allow_inheritance' : True}
#     meta = {'ab_alias':"mydata"}
#
# s = Post(title = "test for fun")
# s.save()
#
# class TextPost(Post):
#     content = StringField()
#
# class ImagePost(Post):
#     image_path = StringField()
#
# class LinkPost(Post):
#     link_url = StringField()
#
# ross = User(email = '442621753@qq.com', first_name = 'Ross', last_name = 'lawley').save()
# post1 = TextPost(title = 'Fun with MongoEngine', author = ross)
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()
#
# john = User(email = 'yangqihang231@outloo.com', first_name = 'john', last_name = 'jeffery').save()
# post2 = LinkPost(title = "joy with MongoEngine", author = john)
# post2.link_url = "www.baidu.com"
# post2.tags = ['mongoengine']
# post2.save()
#
# for post in Post.objects(tags = 'mongodb'):
#     print post.title

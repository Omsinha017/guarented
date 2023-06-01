from mongoengine import Document, StringField, ListField, URLField

class Item(Document):
    item_id = StringField(required=True, unique=True)
    images = ListField(URLField())

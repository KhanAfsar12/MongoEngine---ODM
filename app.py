from mongoengine import connect
from mongoengine.errors import NotUniqueError
from orm.user import User

connect(
    db = "project1",
    host = "localhost",
    port = 27017,
)
try:
    user = User(email = "afsar@easemyai.com")
    user.first_name = "Afsar"
    user.last_name = "Khan"
    user.save()
except NotUniqueError as e:
    print("Email already exists")
from mongoengine import connect
from mongoengine.errors import NotUniqueError
from orm.user import User

connect(
    db = "project1",
    host = "localhost",
    port = 27017,
)

# Add 
# try:
#     user = User(email = "afsar@easemyai.com")
#     user.first_name = "Afsar"
#     user.last_name = "Khan"
#     user.save()
# except NotUniqueError as e:
#     print("Email already exists")


# Update
user = User.objects(email = "afsar@easemyai.com")
user.update(first_name="Ishtiyaque", last_name="Hussain")

user2 = User.objects(email = "afsar@easemyai.com")
fields = {
    "first_name": "Afsar",
    "last_name": "Khan"
}
user2.update(**fields)
from rest_framework import serializers

class User:

    """User class
    params:
        first_name: str
        last_name: str
        email: str             
    """
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


user = User('John', 'Doe', 'johon@mail.com')

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
# Serialize the user object
serializer = UserSerializer(user)
print(serializer.data)





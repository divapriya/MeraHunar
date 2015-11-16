from rest_framework import serializers
from .models import User_Details


class User_Details_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User_Details
        fields=('name','details','slug','qualification','extra_curricullums','employment','personalinterest','qualification_preference','extra_curricullums_preference','employment_preference','personalinterest_preference')
from rest_framework import serializers
from .models import Task
from users.models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    # Optional: assigned_to ko username/email se display karna
    assigned_to_email = serializers.ReadOnlyField(source='assigned_to.email')

    class Meta:
        model = Task
        fields = "__all__"
        
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

# Function to send email to employee when task is assigned
def send_task_email(user, task_title):
    print("EMAIL FUNCTION CALLED")          # debug print
    print("Sending to:", user.email)        # debug print

    send_mail(
        subject="New Task Assigned",
        message=f"Hello {user.first_name},\n\nYou have been assigned a new task: {task_title}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )

# ---------------------------
# Permissions
# ---------------------------

# Only admin or manager can create task
class IsAdminOrManagerCreateTask(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["admin", "manager"]

# Only admin or manager can delete task
class IsAdminOrManagerDeleteTask(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["admin", "manager"]

# ---------------------------
# Task Views
# ---------------------------

# Task Create View with email notification
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrManagerCreateTask]

    def perform_create(self, serializer):
        print("PERFORM CREATE HIT")  
        task = serializer.save()
        if task.assigned_to:
            print("USER EMAIL:", task.assigned_to.email)  
            send_task_email(task.assigned_to, task.title)

            
# Task List View
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return Task.objects.all()
        elif user.role == "manager":
            return Task.objects.filter(assigned_by=user)
        else:  # employee
            return Task.objects.filter(assigned_to=user)

# Task Update Status View
class TaskUpdateStatusView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "employee":
            return Task.objects.filter(assigned_to=user)
        return Task.objects.all()

# Task Delete View
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrManagerDeleteTask]
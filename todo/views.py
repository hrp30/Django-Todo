from dataclasses import field

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status

from todo.models import Todo, Comments
from todo.services import create_new_todo, get_all_todos, update_todo
from rest_framework.pagination import PageNumberPagination


# Create your views here.


class TodoCommentsView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        todo_id = serializers.IntegerField()
        comment = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comments
            fields = '__all__'

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = Comments.objects.create(user_id=request.user.id, todo_id=serializer.validated_data['todo_id'],
                                          comment=serializer.validated_data['comment'])

        return Response({"comments": self.OutputSerializer(comment).data}, status=status.HTTP_201_CREATED)


class TodoList(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()

    class UpdateInputSerializer(serializers.Serializer):
        todo_id = serializers.IntegerField()
        title = serializers.CharField()
        description = serializers.CharField(allow_blank=True)
        completed = serializers.BooleanField(default=False)

    class OutputSerializer(serializers.Serializer):
        comments = serializers.JSONField()
        id = serializers.IntegerField()
        title = serializers.CharField()
        description = serializers.CharField()
        completed = serializers.BooleanField()
        created_at = serializers.CharField()
        updated_at = serializers.CharField()


    def get(self, request):
        users_todos = get_all_todos(user_id=request.user.pk)
        results = self.paginate_queryset(users_todos, request, view=self)
        serializer = self.OutputSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        todo = create_new_todo(user_id=request.user.pk, title=serializer.validated_data['title'],
                               description=serializer.validated_data['description'])

        return Response({"todos": self.OutputSerializer(todo, many=True).data}, status=status.HTTP_201_CREATED)

    def patch(self, request):
        serializer = self.UpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            todo = update_todo(user_id=request.user.pk, title=serializer.validated_data['title'],
                               description=serializer.validated_data['description'],
                               todo_id=serializer.validated_data['todo_id'],
                               completed=serializer.validated_data['completed'])
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"todos": self.OutputSerializer(todo, many=True).data}, status=status.HTTP_200_OK)

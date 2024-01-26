from django.urls import path

from todo.views import TodoList, TodoCommentsView

urlpatterns = [
    path('todo/', TodoList.as_view(), name='todo'),
    path('comments/', TodoCommentsView.as_view(), name='comments')
]

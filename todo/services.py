from todo.models import Todo


def create_new_todo(user_id, title, description):
    todo = Todo(user_id=user_id, title=title, description=description)
    todo.save()
    users_todo_list = get_all_todos(user_id=user_id)
    return users_todo_list


def update_todo(user_id, todo_id, title, description, completed=False):
    todo = Todo.objects.get(id=todo_id)
    if todo.user_id != user_id:
        raise Exception('This user does not have permission to update this item')
    todo.title = title
    todo.description = description
    todo.completed = completed
    todo.save()
    users_todo_list = get_all_todos(user_id=user_id)
    return users_todo_list


def get_all_todos(user_id):
    user_todos = Todo.objects.filter(user_id=user_id).prefetch_related('comments_set')
    todo_data = []
    for todo in user_todos:
        comments_data = []
        for comment in todo.comments_set.all():
            comment_info = {
                'user_id': comment.user.id,
                'comment': comment.comment,
                'created_at': comment.created_at,
                'updated_at': comment.updated_at
            }
            comments_data.append(comment_info)
        todo_info = {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
            'created_at': todo.created_at,
            'updated_at': todo.updated_at,
            'comments': comments_data
        }
        todo_data.append(todo_info)
    return todo_data

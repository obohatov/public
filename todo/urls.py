from django.urls import path


from todo import views


urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),
    path(
        "tags/",
        views.tag_list,
        name="tag_list"
    ),
    path(
        "add_task/",
        views.add_task,
        name="add_task"
    ),
    path(
        "add_tag/",
        views.add_tag,
        name="add_tag"
    ),
    path(
        "update_task/<int:task_id>/",
        views.update_task,
        name="update_task"
    ),
    path(
        "delete_task/<int:task_id>/",
        views.delete_task,
        name="delete_task"
    ),
    path(
        "complete_task/<int:task_id>/",
        views.complete_task,
        name="complete_task"
    ),
    path(
        "undo_task/<int:task_id>/",
        views.undo_task,
        name="undo_task"
    ),
    path(
        "update_tag/<int:tag_id>/",
        views.update_tag,
        name="update_tag"
    ),
    path(
        "delete_tag/<int:tag_id>/",
        views.delete_tag,
        name="delete_tag"),
]

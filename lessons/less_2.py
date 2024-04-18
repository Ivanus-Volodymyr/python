from typing import TypedDict, Callable, Dict, List, TypeVar, Any

# # 1.
# def task():
#     tasks: [dict] = [{'id': 1, 'name': 'do this'}, {'id': 2, 'name': 'do next'}]
#
#     def add(new_task):
#         tasks.append(new_task)
#         return 'task added'
#
#     def get_tasks():
#         return tasks
#
#     return {'get_tasks': get_tasks, 'add_task': add}
#
#
# actions = task()
# print(actions['get_tasks']())
# print(actions['add_task']({'id': 3, 'name': 'do this'}))
# print(actions['get_tasks']())


# # 2.
# Task = TypedDict('Task', {"id": int, "name": str})
# TasksAction = TypedDict('TasksAction', {
#     'add_task': Callable[[Dict[str, str]], str],
#     'get_tasks': Callable[[], List[Dict[str, str]]]
# })
#
#
# def task_actions() -> TasksAction:
#     tasks: [Task] = [{'id': 1, 'name': 'do this'}, {'id': 2, 'name': 'do next'}]
#
#     def add(new_task: Task) -> str:
#         tasks.append(new_task)
#         return 'task added'
#
#     def get_tasks() -> list:
#         return tasks
#
#     return {'get_tasks': get_tasks, 'add_task': add}
#
#
# actions = task_actions()
# print(actions['get_tasks']())
# print(actions['add_task']({'id': 3, 'name': 'do this'}))
# print(actions['get_tasks']())


# # 3.
# def expanded_form(num: int) -> str:
#     result = []
#     multiplier = 1
#
#     while num > 0:
#         digit = num % 10
#         if digit != 0:
#             result.append(str(digit * multiplier))
#         num //= 10
#         multiplier *= 10
#
#     return ' + '.join(reversed(result))
#
#
# print(expanded_form(1201))

# # 4.
# T = TypeVar('T', bound=Callable)
#
#
# def count(func: T) -> T:
#     number = 0
#
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         nonlocal number
#         number += 1
#         res = func(*args, **kwargs)
#         print(f'Function {func.__name__} called {number} times.')
#         return res
#
#     return wrapper
#
#
# @count
# def hello() -> None:
#     print("Hello World!")
#
#
# hello()
# hello()
# hello()
# hello()

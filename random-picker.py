import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop

from server.app import server_load_app
from tasks.app import tasks_load_app


if __name__ == '__main__':
    # Создаем мост между tornado и asyncio
    AsyncIOMainLoop().install()
    # Запускаем tornado ws сервер
    server_app = server_load_app()
    server_app.listen(port=8888)
    # Запускаем задачи
    tasks_app = tasks_load_app()

    loop = asyncio.get_event_loop()
    # Собираем количество активных задач
    tasks_active_count = len(asyncio.Task.all_tasks())
    if tasks_active_count > 0:
        loop.run_forever()
    else:
        print("Configure your configuration.yml file.")

# Д.З. 4. Задание 2. Взять информацию по URL
import requests  as req

API_URL = "https://api.github.com/users/"

github_login = input("Введите требуемый логин на github (пустой ввод - vdovydenkov):")
if not github_login:
    github_login = "vdovydenkov"
url = API_URL + github_login
print("-" * 30)
print("Пытаемся загрузить страницу ", url)
query_result = req.get(url)
if query_result.status_code == 200:
    data = query_result.json()
    print("Имя:         ", data["name"])
    print("Логин:       ", data["login"])
    print("Репозиториев:", data["public_repos"])
else:
    print("Не удалось загрузить страницу. Код ошибки: ", query_result.status_code)

# Ждем реакции пользователя
input("Нажмите Enter для завершения программы...")
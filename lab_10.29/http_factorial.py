from flask import Flask, request

# HTML заголовки и прочие сообщения
BEGIN = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вычисление факториала</title>
</head>
<body>
'''

END = "\n</body>\n</html>"

DESCRIPTION = '''
<h3>Описание</h3>
<p>Этот web-скрипт подсчитывает факториал числа, переданного ему в параметре num.</p>
<p>Обратиться к скрипту можно по ссылке:<br />
<a href="http://localhost:5000">http://localhost:5000?num=N</a>
<p>Где N - целое положительное число.</p>
'''

ERROR_TITLE = "\n<h3>Ошибка</h3>\n"

def factorial(n):
    if n in [0, 1]: return 1
    factorial_n = n
    for c in range(n, 2, -1):
        factorial_n *= c -1
    return factorial_n


app = Flask(__name__)

@app.route("/")
def get_factorial():
    if len(request.args) == 0:
        return BEGIN + DESCRIPTION + END
    # Преобразуем параметры к нижнему регистру
    args = {k.lower(): v for k, v in request.args.items()}

    num = args.get("num", None)
    if num is None:
        return BEGIN + ERROR_TITLE + "<p>Параметр num не передан.</p>\n" + DESCRIPTION + END
    try: num = int(num)
    except ValueError:
        return BEGIN + ERROR_TITLE + "<p>В параметре num передано не число.</p>\n" + DESCRIPTION + END
    
    if num < 0:
        return BEGIN + ERROR_TITLE + "<p>Переданное число должно быть положительным.</p>\n" + DESCRIPTION + END

    factorial_n = factorial(num)
    return BEGIN + f"<p>{num}! = {factorial_n}</p>" + END

app.run(debug=True)
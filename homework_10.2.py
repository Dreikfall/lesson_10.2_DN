from flask import Flask
import json

with open("candidates.json", "r") as f:
    candidates = json.load(f)

app = Flask(__name__)


@app.route("/")
def main_page():
    """Отображает на главной странице полный список кандидатов с некоторыми ключами"""

    page = ""
    for c in candidates:
        page += f'{c.get("name")}\n'
        page += f'{c.get("position")}\n'
        page += f'{c.get("skills")}\n\n'
    return f'<pre>\n{page[:len(page) - 1]}</pre>'  # такая конструкция используется для корректного местоположения
    # тегов в коде страницы(если это имеет значение)


@app.route("/candidates/<int:id>")
def data_candidate(id):
    """По id отображается конкретный кандидат с некоторыми свойствами"""

    page = ""
    for c in candidates:
        if c.get("id") == id:
            page += f'<img src="{c["picture"]}">\n<pre>\n'
            page += f'{c.get("name")}\n{c.get("position")}\n{c.get("skills")}'
    return f'\n{page}\n</pre>'


@app.route("/skills/<skill>")
def candidate_skill(skill):
    """Выводит список кандидатов по наличию определенного скилла """

    page = ""
    for c in candidates:
        if skill.lower() in c.get("skills").lower().split(", "):  # сравниваю скилл со словарем, в который возможно
            page += f'{c.get("name")}\n{c.get("position")}\n{c.get("skills")}\n\n'  # вложено данное слово
    return f'<pre>\n{page[:len(page) - 1]}</pre>'  # т.к. при сравнении со строкой могут приниматься неправильные
# запросы (например часть слова)


app.run()

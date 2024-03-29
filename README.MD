# Сервис "CookBook"

## 
Функционал
Приложение предоставляtn следующие HTTP функции, получающие параметры методом 
GET

`add_product_to_recipe` с параметрами recipe_id, product_id, weight. Функция
добавляет к указанному рецепту указанный продукт с указанным весом. Если в 
рецепте уже есть такой продукт, то функция меняет его вес в этом рецепте на 
указанный.

`cook_recipe` c параметром recipe_id. Функция увеличивает на единицу 
количество приготовленных блюд для каждого продукта, входящего в указанный 
рецепт.

`show_recipes_without_product` с параметром product_id. Функция возвращает 
HTML страницу, на которой размещена таблица. В таблице отображены id и 
названия всех рецептов, в которых указанный продукт отсутствует, или 
присутствует в количестве меньше 10 грамм.

### Зависимости
    python = "^3.10"
    django = "^5.0.1"
    psycopg2-binary = "^2.9.9"
    python-dotenv = "^1.0.1"

## Установка

Выполнить настройку в файле ```.env```

#### Управление через менеджер зависимостей ```Poetry```:
```sh
$ pip install poetry
```
Установка зависимостей:
```sh
$ poetry install
```

#### Примените миграции
```shell
python manage.py migrate
```

#### Создайте Администратора

```shell
python manage.py createsuperuser
```

#### Запустите локально

python manage.py runserver

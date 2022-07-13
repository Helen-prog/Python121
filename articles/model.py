import pickle
import os.path

class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


# Создадим базу данных статей
class ArticleModel:
    def __init__(self):  # словарь статей
        self.db_name = "db.txt"
        self.articles = self.load_data()  # {'title': article}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())  # все что будет записано в словаре (распаковываем список из
        # значений словаря)
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        try:
            article = self.articles[user_title]
        except KeyError:  # Эмулируем ошибку БД
            raise ValueError("Такой статьи не существует")
        else:
            dict_article = {
                "название": article.title,
                "автор": article.author,
                "количество страниц": article.pages,
                "описание": article.description,
            }
            return dict_article

    def remove_article(self, user_title):
        try:
            return self.articles.pop(user_title)
        except KeyError:
            raise ValueError("Такой статьи не существует")

    def load_data(self):  # рабочая директория - это папка откуда была запущена наша программа
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.articles, f)

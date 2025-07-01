import random
import requests
import allure
from faker import Faker
import string
import logging
from data import Endpoints, Urls
import json

# Основная часть API клиента взята из 2 части дипломной работы, с небольшими изменениями и сокращениями.
class Request:

    @staticmethod
    @allure.step('POST request.')
    def post(path, payload, access_token):
        return requests.post(Urls.URL_SERVICE + path, headers=Funcs.auth_header(access_token), data=json.dumps(payload))

    @staticmethod
    @allure.step('DELETE request.')
    def delete(path, access_token):
        return requests.delete(Urls.URL_SERVICE + path, headers=Funcs.auth_header(access_token))

    @staticmethod
    @allure.step('GET request.')
    def get(path, access_token):
        return requests.get(Urls.URL_SERVICE + path, headers=Funcs.auth_header(access_token))


class User:

    @staticmethod
    @allure.step('Регистрация пользователя, проверка успешного ответа и возвращение всех данных для дальнейшего использования.')
    def register():
        user = Generator.get_user_payload()
        response = Request.post(Endpoints.USER_REGISTER, user, '')
        if response.status_code == 200:
            Funcs.message(f'Пользователь создан')
            resp = response.json()
            resp["user"]["password"] = user.get("password")
            return resp
        else:
            Funcs.message(f'Пользователь не создан: {response.status_code}, {response.text}.')

    @staticmethod
    @allure.step('Удаление пользователя и проверка успешного ответа.')
    def delete(access_token):
        response = Request.delete(Endpoints.USER, access_token)
        if response.status_code == 202:
            Funcs.message(f'Пользователь удален')
        else:
            Funcs.message(f'Пользователь не удален: {response.status_code}, {response.text}.')


class Order:

    @staticmethod
    @allure.step('Получение данных об ингредиентах.')
    def get_ingredients():
        response = Request.get(Endpoints.INGREDIENTS, '')
        if response.status_code == 200:
            Funcs.message(f'Список ингредиентов получен')
            return response.json()
        else:
            Funcs.message(f'Список ингредиентов не получен: {response.status_code}, {response.text}.')

    @staticmethod
    @allure.step('Создание списка ингредиентов с сортировкой по типу.')
    def sorted_ingredients():
        ingredients = Order.get_ingredients()
        sorted_ings = {
            "buns": [],
            "fillings": [],
            "sauces": []
            }
        for ing in ingredients.get('data'):
            if ing["type"] == "bun":
                sorted_ings["buns"].append(ing)
            elif ing["type"] == "sauce":
                sorted_ings["sauces"].append(ing)
            elif ing["type"] == "main":
                sorted_ings["fillings"].append(ing)
        return sorted_ings

    @staticmethod
    @allure.step('Создание бургера.')
    def make_burger():
        list =[]
        ings_list = Order.sorted_ingredients()
        bun = ings_list["buns"][random.randint(0, len(ings_list["buns"])-1)]
        sauce = ings_list["sauces"][random.randint(0, len(ings_list["sauces"])-1)]
        filling = ings_list["fillings"][random.randint(0, len(ings_list["fillings"])-1)]
        list.append(bun.get("_id"))
        list.append(bun.get("_id"))
        list.append(sauce.get("_id"))
        list.append(filling.get("_id"))
        burger = {
            "ingredients": list
            }
        return burger

    @staticmethod
    @allure.step('Создание заказа и получение его номера.')
    def submit_order(user):
        payload = Order.make_burger()
        token = user.get("accessToken")
        response = Request.post(Endpoints.ORDER, payload, token)
        if response.status_code == 200:
            Funcs.message(f'Заказ создан')
            return str(response.json()['order']['number'])
        else:
            Funcs.message(f'Заказ не создан: {response.status_code}, {response.text}.')

class Generator:

    @staticmethod
    @allure.step('Генерация уникальных данных пользователя.')
    def get_user_payload():
        fake = Faker()
        return {
            "email": f'"{fake.email()}"',
            "password": f'"{fake.password()}"',
            "name": ''.join(random.choice(string.ascii_lowercase) for i in range(8)).capitalize()
            }


class Funcs:

    @staticmethod
    def message(message):
        allure.attach('', message, attachment_type=allure.attachment_type.TEXT)
        logging.info(message)

    @staticmethod
    @allure.step('Создание header c токеном авторизации.')
    def auth_header(token):
        header = {
            "Content-Type": "application/json",
            'Authorization': f'{token}'
            }
        return header

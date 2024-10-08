## Описание автотестов для сервиса Stellar Burgers

1) Проверка ответов на вопросы выпадающего списка "Вопросы о важном" - test_question
2) Проверка создания заказа через кнопку "Заказать" в шапке - test_create_order_header_btn
3) Проверка создания заказа через кнопку "Заказать" в середине главной страницы - test_create_order_main_page_btn
4) Проверка редиректа на главную по клику на лого Самоката в шапке - test_redirect_samokat_logo
5) Проверка редиректа на страницу Дзена по клику на лого Яндекса в шапке - test_redirect_yandex_logo

## Запуск проекта

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/marinatambova/Sprint_7.git
   cd Sprint_7
   ```
   
2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запуск тестов выполняется по команде `export BROWSER=chrome && pytest` или `export BROWSER=chrome && pytest --alluredir=allure_results`

Возможные параметры для браузера:

* chrome
* firefox

4. Просмотр отчетов в формате веб-страницы выполняется командой `allure serve allure_results`





"""
Тест файл для задания 3-6-9, https://stepik.org/course/575
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# Браузер передается из фикстуры
def test_page_has_button_for_add_to_cart(browser):
    # Открываем ссылку
    browser.get(link)
    # Получаем список элементов с нужным нам селектором
    buttons = browser.find_elements_by_css_selector(".btn-add-to-basket")
    # По длине списка проверяем наличие кнопки
    # опционально проверяем ее задваивание или то что мы выбрали уникальный селектор
    buttons_len = len(buttons)
    # assert buttons_len < 2, "There are more than one 'Button for add to cart'"
    assert buttons_len == 1, "Button for add to cart NOt FOUND!"
    # Опционально выводим текст с кнопки для проверки языка заданного при запуске
    # print(buttons[0].text)

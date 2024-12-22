from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

URL = ""
TIMEOUT = 20

st.title("Test Selenium")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
import json
import time

# Настройки Chrome
options = Options()
options.add_argument("start-minimized")

# Инициализация WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Переход на главную страницу
    # driver.get("https://hotline.ua")

    # Переход на страницу мобильных телефонов
    # driver.get("https://hotline.ua/mobile/mobilnye-telefony-i-smartfony/")

    # Ожидание загрузки страницы

    file = open("search.json", "r")
    content = file.read()
    print("CONT: " + content)

    # Ссылка на конкретный товар
    product_link = content
    time.sleep(2)

    # Переход на страницу товара
    driver.get(product_link)
    product_name = driver.find_element(By.CLASS_NAME, "title__main").text
    time.sleep(3)  # Ожидание загрузки страницы товара

    # Извлечение информации о магазинах и ценах
    shops = driver.find_elements(By.CSS_SELECTOR, ".list .list__item")

    shop_data = []
    for shop in shops:
        try:
            shop_name = shop.find_element(By.CLASS_NAME, "shop__title").text
            shop_href = shop.find_element(By.CLASS_NAME, "shop__title").get_attribute("href")
            shop_price = shop.find_element(By.CLASS_NAME, "price__value").text

            if shop_name.strip():  # Проверка, что shop_name не пустая строка
                shop_data.append({"shop_name": shop_name, "price": shop_price, "shop_link": shop_href})
        except Exception as e:
            print(f"Ошибка при извлечении данных магазина: {e}")

    # Подготовка данных для записи
    data = {
        "product_link": product_link,
        "product_name": product_name,
        "shops": shop_data
    }

    # Запись данных в JSON-файл
    with open("product.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("================Данные успешно записаны в файл product.json")

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    print("================Завершение программы")
    driver.quit()

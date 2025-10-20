import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from preentrega import realizar_login
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    realizar_login(driver)
    assert "Swag Labs" in driver.title
    print("login correcto")
    time.sleep(3)

def test_catalogo(driver):
    realizar_login(driver)
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"🐾 Brandon encontró {len(productos)} productos")
    assert len(productos) > 0
    
def test_carrito(driver):
    realizar_login(driver)
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    boton_agregar = productos[0].find_element(By.TAG_NAME, "button")
    boton_agregar.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"
    print("🛍️ Producto añadido correctamente al carrito")

 

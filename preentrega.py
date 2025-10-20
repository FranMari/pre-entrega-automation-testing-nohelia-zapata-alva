
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def realizar_login(driver):
    # Ir a la página del login

    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    # usuario y contraseña

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

 #   hacer clic en el boton de login

    driver.find_element(By.ID, "login-button").click()

    # espera de la pagina de inventario

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    print("✅ Login exitoso")
    print("✅ Título correcto:", driver.title)

# validar si hay productos
   
def validar_catalogo(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    if productos:
        print(f"✅ Se encontraron {len(productos)} productos")
        print("✅ Elementos de interfaz presentes")
        for producto in productos:
            nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
            precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
            print(f"🛍️ Producto: {nombre} - Precio: {precio}")
    else:
        print("⚠️ No se encontraron productos en el catálogo")

    return productos

# validar si se agregan productos 

def agregar_al_carrito(driver, producto):
    boton_agregar = producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print("✅ Contador del carrito actualizado:", contador)

    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"🛍️ Producto en carrito: {nombre} - Precio: {precio}")

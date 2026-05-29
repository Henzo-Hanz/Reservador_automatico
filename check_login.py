from selenium import webdriver
from selenium.webdriver.common.by import By

def check_login(driver: webdriver.Chrome) -> None:
    try:
        error_note = driver.find_element(By.CLASS_NAME, "errornote")
    except:
        error_note = None
    
    if not error_note or not error_note.is_displayed():
        print("Login realizado com sucesso!")
        return True
    else :
        print("Falha no login. Verifique suas credenciais.")
        return False
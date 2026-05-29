from selenium import webdriver
from selenium.webdriver.common.by import By

from check_login import check_login


driver = webdriver.Chrome()
driver.get("https://suap.ifpi.edu.br/accounts/login/?next=/")


user_input_field = driver.find_element(By.ID, "id_username")
password_input_field = driver.find_element(By.ID, "id_password")
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[5]/input")


key_user = "2026113TADS0018"
key_password = "Guts2007@!"

user_input_field.send_keys(key_user)
password_input_field.send_keys(key_password)
submit_button.click()

if check_login(driver):
    try:
        side_bar_menu = driver.find_element(By.XPATH, '//*[@id="toggleSidebar"]')
        if side_bar_menu:
            side_bar_menu.click()
        else:
            raise ValueError("Menu lateral não encontrado.")
        atividades_estudantis=driver.find_element(By.XPATH,'//*[@id="mainmenu"]/ul[1]/li[8]/a')
        if atividades_estudantis:
            atividades_estudantis.click()
        else:
            raise ValueError("Menu de atividades estudantis não encontrado.")
        Menu_restaurante = driver.find_element(By.XPATH,'//*[@id="mainmenu"]/ul[1]/li[8]/ul/li[3]/a')
        if Menu_restaurante:
            Menu_restaurante.click()
        else:
            raise ValueError("Menu de restaurante não encontrado.")  
        link_to_reservas = driver.find_element(By.XPATH,'//*[@id="menu-item-atividadesestudantis_restauranteinstitucional_reservarrefeições"]/a')
        if link_to_reservas:
            link_to_reservas.click()
        else:
            raise ValueError("Link para reservas não encontrado.")
        Botão_reservar = driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div/ul/li/a')
        if Botão_reservar:
            Botão_reservar.click()
        else:
            raise ValueError("Botão de reservar não encontrado.")
        p_feedback_error=driver.find_element(By.ID,'feedback_message')
        if p_feedback_error and p_feedback_error.is_displayed():
            print("Erro ao reservar: ", p_feedback_error.text.split("\n")[0])
        else:
            print("Reserva realizada com sucesso!")
        
    except:
        print("erro ao reservar!")
    
    


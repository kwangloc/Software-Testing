submitBTN = driver.find_element(By.ID, "submitBTN")
# sử dụng Javascript để bật button
driver.execute_script("arguments[0].removeAttribute('disabled')", submitBTN)
# driver.execute_script("arguments[0].scrollIntoView(true);", user_email)
driver.execute_script("arguments[0].click();", submitBTN)
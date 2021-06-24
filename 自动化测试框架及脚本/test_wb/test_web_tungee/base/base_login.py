def test_login(driver,username,pwd):
    driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[1]/div/div/span/span/span/span[2]/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[2]/div/div/span/span/input").send_keys(pwd)
    driver.find_element_by_xpath("//button[@class='ant-btn _2jejW ant-btn-primary']").click()
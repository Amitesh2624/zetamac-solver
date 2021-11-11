from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://arithmetic.zetamac.com')
startBox = driver.find_element_by_xpath('//*[@id="welcome"]/form/input')
startBox.click()

def runScript():
    answerBox = driver.find_element_by_xpath('//*[@id="game"]/div/div[1]/input')
    questionMath = driver.find_element_by_xpath('//*[@id="game"]/div/div[1]/span')
    textQuestion = questionMath.text
    qList = textQuestion.split(" ")
    num1 = qList[0]
    num2 = qList[-1]
    operator = qList[1]
    if operator == "+":
        answerBox.send_keys(str(int(num1) + int(num2)))

    elif operator == "–":
        answerBox.send_keys(str(int(num1) - int(num2)))

    elif operator == "×":
        answerBox.send_keys(str(int(num1) * int(num2)))

    else:
        answerBox.send_keys(str(int(int(num1)/int(num2))))
    print(qList)
    print(num1)
    print(num2)
for i in range(1,150):
    runScript()
    time.sleep(1)

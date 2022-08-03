from selenium import webdriver 
import smtplib
path='C:\\Users\AlieZ\Desktop\geckodriver.exe'

driver=webdriver.Firefox(executable_path=path)

driver.get('https://web.whatsapp.com/')



def send_mail(message):
    
    owner='x@gmail.com'
    acc_to_send='y@gmail.com' 
    mail='x@gmail.com'
    pw='x!123'
    server=smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(mail,pw)
    server.sendmail(owner, acc_to_send, message)
    server.quit()

control=True
control2=True
control3=False
while True:
    try:
        driver.find_element_by_xpath("//span[text()='online']")
        if control==True:
            msg2="online"
            send_mail(msg2)
            begin=time.time()
            control=False
            control2=True
    except:
     if  control2==True:
         msg="Offline"
         send_mail(msg)
         if control3==True:
            finish=time.time() - begin
            send_mail(str(finish))
            control2=False
         control2=False
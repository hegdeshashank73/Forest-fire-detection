
from calendar import c
import streamlit as st
from email.message import EmailMessage
import os
import cv2
import threading
import playsound
import smtplib
import ssl
from email.message import EmailMessage

import numpy as np
from tkinter import *
# print(dir(tkinter))
wi = Tk()
wi.title("Python application")
wi.geometry("500x300")


c = 0
b = 0


a = ["tiger", 86.9, "elephant", 86.7, "tiger2", 85.9, "deer", 84.8,
     "antelope", 86.9, "monkey", 87.2, "ape", 87.3, "ape2", 87.4, "monkey2", 87.0]

fire_location = 87


def send_mail_function():
    email_sender = 'Sender email'
    email_password = 'password'
    email_receiver = 'receiver email'
    subject = 'EMERGENCY'
    body = """
    Confirmation of fire at coordinates(11.93420,76.190)
    Exhaust the fire and initiate evacuation of animals immediately
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def play_alarm_sound_function():
    playsound.playsound('fire_alarm.mp3', True)
    print("Fire alarm end")


def send_mail(temp, levels):
    a = temp
    b = levels
    email_sender = 'sendere mail'
    email_password = 'password'
    email_receiver = 'receiver mail'
    subject = 'EMERGENCY'
    body = """"
    Co2 levels of %d ppm and temperature of %d degree celsius is found at coordinates (11.93420,76.190)
    Drones are to be deployed to the affected region for visual confirmation.
    """ % (b, a)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def onclick():
    print("FOREST FIRE DETECTION AND ANIMAL RESCUE ")
    print("Automating fire detection at early stage and preventing wildlife casualities ")
    print("CO2 level detector")

    number = int(input('ENTER THE C02 Level(in ppm)'))

    number1 = int(input('ENTER THE Temperature(degree celsius)'))

    if (number > 1000):
        c = 1
        print('Co2 levels are high')
    if (number1 > 100):
        b = 1
        print('Temperature levels are high')
    if (c == 1 and b == 1):
        print('Drones need to be deployed ,Danger levels are high')
        send_mail(number1, number)

    if (c == 1 and b == 0 or b == 1 and c == 0):
        print('Danger levels are cautionary')


def onclick1():
    fire_cascade = cv2.CascadeClassifier(
        'C:\\Users\\shsha\\OneDrive\\Desktop\\IEEE HACKATHON\\fire_detection_cascade_model.xml')
    vid = cv2.VideoCapture(0)
    runOnce = False
    while (True):
        Alarm_Status = False
        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fire = fire_cascade.detectMultiScale(
            frame, 1.2, 5)
        for (x, y, w, h) in fire:
            cv2.rectangle(frame, (x-20, y-20),
                          (x+w+20, y+h+20), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            print("Fire alarm initiated")
            threading.Thread(target=play_alarm_sound_function).start()
            if runOnce == False:
                print("Mail send initiated")
                threading.Thread(target=send_mail_function).start()
                runOnce = True
            if runOnce == True:
                print("Mail is already sent once")
                runOnce = True
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def onclick2():
    cap = cv2.VideoCapture(0)

    _, prev = cap.read()
    prev = cv2.flip(prev, 1)
    _, new = cap.read()
    new = cv2.flip(new, 1)
    while True:
        diff = cv2.absdiff(prev, new)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)
        threh = cv2.dilate(thresh, None, 3)
        thresh = cv2.erode(thresh, np.ones((4, 4)), 1)
        contor, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.circle(prev, (20, 200), 5, (0, 0, 255), -1)
        for contors in contor:
            if cv2.contourArea(contors) > 30000:
                (x, y, w, h) = cv2.boundingRect(contors)
                (x1, y1), rad = cv2.minEnclosingCircle(contors)
                x1 = int(x1)
                y1 = int(y1)
                cv2.line(prev, (20, 200), (x1, y1), (255, 0, 0), 4)
                cv2.putText(prev, "{}".format(int(np.sqrt((x1 - 20)**2 + (y1 - 200)**2))),
                            (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.rectangle(prev, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.circle(prev, (x1, y1), 5, (0, 0, 255), -1)

        cv2.imshow("orig", prev)
        prev = new
        _, new = cap.read()
        new = cv2.flip(new, 1)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def onclick3():
    for i in range(0, len(a)):
        if (i % 2 == 1):
            print('')
            if (a[i] >= 86.5 and a[i] <= 87.5):
                print(
                    a[i-1], "IS STUCK NEAR A FIRE AND THE COORDINATE IS = ",  a[i]-40.23, a[i], end=" ")


l1 = Label(wi, text=' ').pack()
lab1 = Label(wi, text="Click to input the amount of carbon dioxide",
             bg='Black', fg='White').pack()
bt1 = Button(wi, text="CO2", command=onclick)
bt1.pack()

l2 = Label(wi, text=' ').pack()
lab2 = Label(wi, text="Click for fire detection",
             bg='Black', fg='White').pack()
bt2 = Button(wi, text="FIRE", command=onclick1)
bt2.pack()

l3 = Label(wi, text=' ').pack()
lab3 = Label(wi, text="Click to calculate distance between animals and fire",
             bg='Black', fg='White').pack()
bt3 = Button(wi, text="DISTANCE", command=onclick2)
bt3.pack()

l4 = Label(wi, text=' ').pack()
lab4 = Label(wi, text="Proximity detector", bg='Black', fg='White').pack()
bt4 = Button(wi, text="ANIMALS", command=onclick3)
bt4.pack()
wi.mainloop()

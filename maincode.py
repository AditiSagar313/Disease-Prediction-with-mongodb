#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import dns as ds
#from prediction import *
#from functools import partialx
from pymongo import MongoClient
#window

client = MongoClient('______________ ENTER YOUR CONNECTION STRING ______________')
db = client.get_database('disease_prediction')       
collection = db.disease 
records= db.prediction

def disease_p(usernam):
    l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)

        # TESTING DATA
    tr=pd.read_csv("Testing.csv")
    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X_test= tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)

    # TRAINING DATA
    df=pd.read_csv("Training.csv")

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X= df[l1]

    y = df[["prognosis"]]
    np.ravel(y)

    def message():
        if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
            messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
        else :
            NaiveBayes()

    def NaiveBayes():
        from sklearn.naive_bayes import MultinomialNB
        gnb = MultinomialNB()
        gnb=gnb.fit(X,np.ravel(y))
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)
        #print(accuracy_score(y_test, y_pred))
        #print(accuracy_score(y_test, y_pred, normalize=False))

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(disease[predicted] == disease[a]):
                psymptoms = {
                 'Name':usernam,
                 'Symptom1':Symptom1.get(),
                 'Symptom2':Symptom2.get(),
                 'Symptom3':Symptom3.get(),
                 'SyPmtom4':Symptom4.get(),
                 'Symptom5':Symptom5.get(),
                 'Disease': disease[predicted],
                }
                records.insert_one(psymptoms)
                if ((Symptom1.get()=="high_fever" or Symptom2.get()=="high_fever" or Symptom3.get()=="high_fever" or Symptom4.get()=="high_fever" or Symptom5.get()=="high_fever") and (Symptom1.get()=="cough" or Symptom2.get()=="cough" or Symptom3.get()=="cough" or Symptom4.get()=="cough" or Symptom5.get()=="cough") and (Symptom1.get()=="breathlessness" or Symptom2.get()=="breathlessness" or Symptom3.get()=="breathlessness" or Symptom5.get()=="breathlessness")):
                    disease[predicted]="corona"
                h='yes'
                break

        if (h=='yes'):
            t3.delete("1.0", END)
            t3.insert(END, disease[a])
        else:
            t3.delete("1.0", END)
            t3.insert(END, "No Disease")

    root = Toplevel()
    root.title(" Disease Prediction From Symptoms")
    root.geometry('5000x1500')
    bg = PhotoImage(file="pic2.png")
    my = Label(root,image=bg)
    my.place(x=0,y=0,relwidth=1, relheight=1)
    Symptom1 = StringVar()
    Symptom1.set(None)
    Symptom2 = StringVar()
    Symptom2.set(None)
    Symptom3 = StringVar()
    Symptom3.set(None)
    Symptom4 = StringVar()
    Symptom4.set(None)
    Symptom5 = StringVar()
    Symptom5.set(None)

    w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
    w2.config(font=("Elephant", 30))
    #w2.grid(row=1, column=0, columnspan=2, padx=100)
    w2.place(x=320,y=0)

    '''label = Label(root, text="DISEASE PREDICTION FROM SYMPTOMS",font=("Times", "28", "bold"),fg="white",bg="#5489dd",height=2)
    label.place(x=250,y=0)'''

    NameLb1 = Label(root, text="")
    NameLb1.config(font=("Elephant", 20))
    NameLb1.grid(row=5, column=2, pady=10,  sticky=W)

    S1Lb = Label(root,  text="SYMPTOM 1")
    S1Lb.config(font=("Elephant", 20))
    #S1Lb.grid(row=10, column=1, pady=10 , sticky=W)
    S1Lb.place(x=400,y=150)

    S2Lb = Label(root,  text="SYMPTOM 2")
    S2Lb.config(font=("Elephant", 20))
    #S2Lb.grid(row=11, column=1, pady=10, sticky=W)
    S2Lb.place(x=400,y=210)

    S3Lb = Label(root,  text="SYMPTOM 3")
    S3Lb.config(font=("Elephant", 20))
    #S3Lb.grid(row=12, column=1, pady=10, sticky=W)
    S3Lb.place(x=400,y=270)

    S4Lb = Label(root,  text="SYMPTOM 4")
    S4Lb.config(font=("Elephant", 20))
    #S4Lb.grid(row=13, column=1, pady=10, sticky=W)
    S4Lb.place(x=400,y=330)

    S5Lb = Label(root,  text="SYMPTOM 5")
    S5Lb.config(font=("Elephant", 20))
    #S5Lb.grid(row=14, column=1, pady=10, sticky=W)
    S5Lb.place(x=400,y=390)

    lr = Button(root, text="PREDICT",height=2, width=20, command=message)
    lr.config(font=("Elephant", 15))
    #lr.grid(row=17, column=2,pady=20)
    lr.place(x= 550,y=450)


    OPTIONS = sorted(l1)

    S1En = OptionMenu(root, Symptom1,*OPTIONS)
    #S1En.grid(row=10, column=2)
    S1En.place(x=900,y=150)


    S2En = OptionMenu(root, Symptom2,*OPTIONS)
    #S2En.grid(row=11, column=2)
    S2En.place(x=900,y=210)

    S3En = OptionMenu(root, Symptom3,*OPTIONS)
    #S3En.grid(row=12, column=2)
    S3En.place(x=900,y=270)

    S4En = OptionMenu(root, Symptom4,*OPTIONS)
    #S4En.grid(row=13, column=2)
    S4En.place(x=900,y=330)

    S5En = OptionMenu(root, Symptom5,*OPTIONS)
    #S5En.grid(row=14, column=2)
    S5En.place(x=900,y=390)

    '''NameLb = Label(root, text="")
    NameLb.config(font=("Elephant", 20))
    NameLb.grid(row=13, column=1, pady=10,  sticky=W)

    NameLb = Label(root, text="")
    NameLb.config(font=("Elephant", 15))
    NameLb.grid(row=18, column=1, pady=10,  sticky=W)'''

    t3 = Text(root, height=2, width=30)
    t3.config(font=("Elephant", 20))
    #t3.grid(row=22, column=2 , padx=10)
    t3.place(x= 400,y=550)
    root.mainloop()


def signup():
    database = []
    for i in collection.find():
        my_dict = {
        'username': i['username'],
        'password' : i['password']
        }
        database.append(my_dict)
    #print(len(database))
    f=0
    for i in range(len(database)):
        if (username.get() == database[i]['username'] and password.get() == database[i]['password']):
            f=1
            disease_p(username.get())
            break
        #elif i == len(database) - 1:
         #   new_user = {'username': username.get(), 'password':password.get()}
          #  collection.insert_one(new_user)
        else:
            #print(i)
            continue
    #print(i)
    #print(len(database))
    if f==0:
        new_user = {'username': username.get(), 'password':password.get()}
        collection.insert_one(new_user)
        messagebox.showinfo("registered")

        
tkWindow = Tk()  
tkWindow.geometry('5000x1500')  
tkWindow.title('disease prediction.org')
bg = PhotoImage(file="image2.png")
my = Label(tkWindow,image=bg)
my.place(x=0,y=0,relwidth=1, relheight=1)
predictLabel = Label(tkWindow, text="DISEASE PREDICTION SYSTEM",font=("Arial Bold", 35)).place(x=330, y=150)
#predictLabel.(width=200)
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",font=("Arial Bold", 20)).place(x=450, y=300)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username,width=20,font=("Arial Bold", 20)).place(x=630, y=300)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",font=("Arial Bold", 20)).place(x=450, y=360)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*',width=20,font=("Arial Bold", 20)).place(x=630, y=360)  

#validateLogin = partial(validateLogin, username, password)

#login button
signupButton = Button(tkWindow, text="Sign up", command=signup,font=("Elephant", 15)).place(x=630, y=420)
loginButton = Button(tkWindow, text="Login", command=signup,font=("Elephant", 15)).place(x=750, y=420)

tkWindow.mainloop()



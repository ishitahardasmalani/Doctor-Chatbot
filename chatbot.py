from tkinter import *
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
data = pd.read_csv(r"C:/Users/ACER/Documents/dataset.csv")

# Define the features and target
features = data['Symptoms']
target = data['Disease']

# Vectorize the features using CountVectorizer
vectorizer = CountVectorizer()
features_vectorized = vectorizer.fit_transform(features)

# Train the model
model = MultinomialNB()
model.fit(features_vectorized, target)

# Save the model and vectorizer to disk
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

root = Tk()
root.title("Chatbot")
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if (user == "hi" or user == "hii" or user == "hiiii" or user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, please enter your symptoms(min3)")

    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")

    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert( END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

    elif user == "goodbye" or user == "see you later" or user == "see yaa" or user=="bye" :
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    else:
        user_input_vectorized = vectorizer.transform([user])
        predicted_disease = model.predict(user_input_vectorized)
        txt.insert(END, "\n" + "Bot -> Based on your symptoms you may have " + predicted_disease[0])

    e.delete(0, END)

lable1 = Label(root, bg="deeppink", fg="BLACK", text="Docbot", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg="BEIGE", fg="GREEN", font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)


e = Entry(root, bg="WHITE", fg="BLACK", font=FONT, width=55)
e.grid(row=2, column=0)
send = Button(root, text="Send", font=FONT_BOLD, bg="RED",command=send).grid(row=2, column=1)
root.mainloop()
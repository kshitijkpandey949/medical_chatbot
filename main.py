import convo

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp    # pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as sp
import threading



engine = pp.init()


voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        # printing current voice rate
engine.setProperty('rate', 135)     # setting up new voice rate


def speak(word):
    engine.say(word)
    engine.runAndWait()


chatbot = ChatBot("My_Bot")


trainer = ListTrainer(chatbot)
# now training the bot with the help of trainer
trainer.train(convo.conversation)

# Taking console-based input
# response = chatbot.get_response("Hello")
# print(response)

# Taking input from the user
# print(".....Start Your Conversation..... ")
# while True:
#    query = input()
#    if query == 'exit':
#        break
#    response = chatbot.get_response(query)

#    print("bot :" , response)

main = Tk()
main.geometry("900x850")
main.configure(bg="#2F4F4F")
main.title("My Chatbot")


img = PhotoImage(file="med_img.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

# take query : it takes audio as input from user and convert it to text.


def takeQuery():
    sr = sp.Recognizer()
    sr.pause_threshold = 1

    print("your bot is listening try to speak")

    with sp.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("audio is not recognised")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END, "HUMAN : "+" " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "BOT : "+" " + str(answer_from_bot))
    speak(answer_from_bot)
    msgs.insert(END, "\n")
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)


sc = Scrollbar(frame)
msgs = Listbox(frame, bg="#2F4F4F", fg="#DA70D6", width=150, height=18, font=("Times", "13", "bold"), yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=5)

frame.pack()


# head label
head_label = Label(bg="#2F4F4F", fg="red",
                   text="Welcome, This is a Medical chatbot that help patients to find the Drugs or Medicines for the different types of diseases simulating through the conversations.", font=("Helvetica", "14", "italic"), pady=0)
head_label.place(relwidth=1)

# creating text field

textF = Entry(main, font=("Helvetica", "22", "italic"), bg="#555555", fg="#FFA54F")
textF.pack(fill=X, pady=28)

btn = Button(main, text="SEND", bg="#ABB2B9", width=12,  font=("Times", "22", "bold italic"), command=ask_from_bot)
btn.pack()


# the label for textF
user_name = Label(main,text="Ask From Below: ", font=("Times", "14"), bg="#2F4F4F",
                  fg="#7CFC00").place(x=1, y=550)


# creating a function for enter key.


def enter_function(event):
    btn.invoke()


# going to bind main window with enter key.

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()




main.mainloop()


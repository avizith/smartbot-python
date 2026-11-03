
#rull based ai chatbot
import datetime
import time
name=input("Please enter your name: ")
presentHours = datetime.datetime.now().hour
if 5<= presentHours < 11:
 print("Good Morning!",name)
 if 11<= presentHours < 17:
  print("Good Afternoon!",name)
  if 17<= presentHours < 21:
    print("Good Evening!",name)
    if 21<= presentHours < 5:
     print("Good Night!",name) 
      
print("WELCOME TO RULE BASED CHATBOT")
print("You can ask me basic questions. Type 'bye' to exit.")

# Chatbot memory creation (dictionary of responses)
responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you!",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep going. Every bug in a project makes you stronger.",
    "happy": "Great to hear that!"
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to answer this question. I am still learning!"

# Take user input
while True:
    userInput = input("Please ask your question: ")

    if "bye" in userInput.lower():
        print("Bot: Goodbye! Have a nice day.")
        break

    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

import streamlit as lit

code_1 = '''
word = "Hello"
new_word = word[::-1]
print(new_word)'''
  
code_2 = '''
def mystery(n):
  if n == 0:
    return 1
  else:
    return n * mystery(n - 1)
result = mystery(4)
print(result)'''

code_3 = '''
def alien_translator(sentence):
    translation = ""
    for char in sentence:
        if char.lower() == "a":
            translation += "Z"
        elif char.lower() == "e":
            translation += "Y"
        else:
            translation += char
    return translation
earth_sentence = "Hello, aliens!"
alien_sentence = alien_translator(earth_sentence)
print("Alien Sentence:", alien_sentence)'''

code_4 = '''
bat_signal = 1
cape_on = 0

def Caped_Crusader(bat_signal, cape_on):
    if bat_signal and not cape_on:
        print("Time to be the Dark Knight Gotham deserves!")
        cape_on = 1
    elif not bat_signal and cape_on:
        print("No signal, but I'm always prepared.")
    elif not bat_signal and not cape_on:
        print("Just another night in Gotham.")
        cape_on = 1
    if not (cape_on):
        print("I am Batman!")

Caped_Crusader(bat_signal, cape_on)'''

code_5 = '''
def code(number):
    copy = number
    rev = 0
    while number != 0:
        rem = number%10
        rev = rev *10 + rem
        number = number//10
    if copy == rev:
        print("True")
    else:
        print("False")
    
code(12321)'''

lit.session_state.points = lit.session_state.get("points", 0)

pages = {
  "STEAM@Abu Dhabi": "STEAM@Abu Dhabi",
  "Question 1": "Question 1",
  "Question 2": "Question 2",
  "Question 3": "Question 3",
  "Question 4": "Question 4",
  "Question 5": "Question 5",
}

for page_name, page_title in pages.items():
    if lit.sidebar.button(page_title, key=page_name):
        lit.session_state.page = page_name

page = getattr(lit.session_state, "page", list(pages.keys())[0])

if page == "STEAM@Abu Dhabi":
    lit.title("Welcome to the MTC Exhibit!")
    lit.write("Complete this simple programming-based quiz to win this challenge!")
    lit.subheader("How To Complete This Quiz")
    lit.write("Each of the pages has a code snippet in Python. Analyse the given code and type in the output of the code exactly as it would be printed. You can start by going to any of the questions in the sidebar. Good luck!")
    lit.subheader("If You Don't Know Programming...")
    lit.write("Don't worry! Python is a super-readable and beginner-friendly programming language, so try to treat this quiz as your first encounter with programming logic! Feel free to take your friend's help or running these codes on an online interpreter and figure the answers out later!")

if page == "Question 1":
    lit.code(code_1, language='python')
    lit.write("What is the output of the above code?")
    code_1_ans = lit.text_input("Enter your answer here...")
    if code_1_ans == "olleH":
        lit.write("Good job!")
        lit.session_state.points += 10
        lit.write("Points earned: " + str(lit.session_state.points))

if page == "Question 2":
    lit.code(code_2, language='python')
    lit.write("What is the output of the above code?")
    code_2_ans = lit.text_input("Enter your answer here...")
    if code_2_ans == "24":
        lit.write("Good job!")
        lit.session_state.points += 10
        lit.write("Points earned: " + str(lit.session_state.points))

if page == "Question 3":
    lit.code(code_3, language='python')
    lit.write("What is the output of the above code?")
    code_3_ans = lit.text_input("Enter your answer here...")
    if code_3_ans == "Alien Sentence: HYllo, ZliYns!":
        lit.write("Good job!")
        lit.session_state.points += 10
        lit.write("Points earned: " + str(lit.session_state.points))

if page == "Question 4":
    lit.code(code_4, language='python')
    lit.write("What is the output of the above code?")
    code_4_ans = lit.text_input("Enter your answer here...")
    if code_4_ans == "Time to be the Dark Knight Gotham deserves!":
        lit.write("Good job!")
        lit.session_state.points += 10
        lit.write("Points earned: " + str(lit.session_state.points))

if page == "Question 5":
    lit.code(code_5, language='python')
    lit.write("What is the output of the above code?")
    code_5_ans = lit.text_input("Enter your answer here...")
    if code_5_ans == "True":
        lit.write("Good job!")
        lit.session_state.points += 10
        lit.write("Points earned: " + str(lit.session_state.points))

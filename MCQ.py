from Quest import Quest

MCQ_questions = [
    "\n\napples are of which color ? \n (A) Red\n (B) Blue\n (C) Green \n\n",
    "\n\nbananas are of which color ? \n (A) yellow\n (B) Blue\n (C) Green \n\n",
    "\n\ngrapes are of which color ? \n (A) Purple\n (B) Blue\n (C) Green \n\n"
]

quests =[
    Quest(MCQ_questions[0],"a"),
    Quest(MCQ_questions[1],"a"),
    Quest(MCQ_questions[2],"a")

]



def check(MCQ_questions):
    score = 0
    for q in MCQ_questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score+= 1
     
    print("You Got " + str(score)+ "/" + str(len(quests)))   
        



check(quests)
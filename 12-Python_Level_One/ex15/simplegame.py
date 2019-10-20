import random
#Codebreaker game
#GET Guess
def get_guess():
    return input('input your guess')

#generate digits
def gen_dig():
    dig = [str(num) for num in range(10)]
    random.shuffle(dig)
    return dig[:3]

#generate clues
def gen_clues(code,guess):
    if guess == code: return "Мамкин хакер угадал код"
    clues = []
    for ind,num in enumerate(guess):
        if num == code[ind]:
            clues.append("Точно")
        elif num in code:
            clues.append("Близко")
    if clues ==[]:
        return ["Nope"]
    else:
        return clues

#run game logic
print("Привет, мамкин хакер")
secret_code=gen_dig()
clue_rep= []
while clue_rep != "Мамкин хакер угадал код":
    guess=get_guess()
    clue_rep=gen_clues(guess,secret_code)
    print("Вот что ты нагадал: ")
    for clue in clue_rep:
        print(clue)

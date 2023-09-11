def read_words():
    words = []
    with open('WordleWords.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        words.extend(line.split())
    print(len(words))
    return words


def grader(poss_words):
    grades = []
    for i in range(5):
        grades.append([0] * 26)
    for word in poss_words:
        for i in range(5):
            grades[i][ord(word[i]) - ord("a")] += 1
    return grades


def word_grader(poss_words, grades):
    word_grades = [0] * len(poss_words)
    for i in range(len(poss_words)):
        for j in range(5):
            word_grades[i] += grades[j][ord(poss_words[i][j]) - ord("a")]
    return word_grades


def greenLetter(poss_words, letter, loc):
    temp_words = []
    for word in poss_words:
        if word[loc] == letter:
            temp_words.append(word)
    return temp_words


def yellowLetter(poss_words, letter, loc):
    temp_words = []
    for word in poss_words:
        if letter in word and word[loc] != letter:
            temp_words.append(word)
    return temp_words


def greyLetter(poss_words, letter):
    temp_words = []
    for word in poss_words:
        if letter not in word:
            temp_words.append(word)
    return temp_words


def game():
    guess_num = 1
    found = False
    poss_words = read_words()
    print("welcome to wordle slover")
    print("my first guess is:")
    grades = grader(poss_words)
    word_grades = word_grader(poss_words,grades)
    guess = poss_words[word_grades.index(max(word_grades))]
    print(guess)
    print("please rate my guess as follows:")
    print("0 - letter isnt in the word")
    print("1 - letter is at another location")
    print("2 - letter is correct")
    rating = input()
    if rating == "22222":
        found = True
        print("wow first guess!")
    else:
        for i in range(5):
            if rating[i] == "0":
                poss_words = greyLetter(poss_words, guess[i])
            if rating[i] == "1":
                poss_words = yellowLetter(poss_words, guess[i], i)
            if rating[i] == "2":
                poss_words = greenLetter(poss_words, guess[i], i)
        # print(len(poss_words), "possible words")
        for i in range(5):
            guess_num += 1
            print("my next guess is:")
            grades = grader(poss_words)
            word_grades = word_grader(poss_words, grades)
            guess = poss_words[word_grades.index(max(word_grades))]
            print(guess)
            print("please rate my guess")
            rating = input()
            if rating == "22222":
                found = True
                break
            for i in range(5):
                if rating[i] == "0":
                    poss_words = greyLetter(poss_words, guess[i])
                if rating[i] == "1":
                    poss_words = yellowLetter(poss_words, guess[i], i)
                if rating[i] == "2":
                    poss_words = greenLetter(poss_words, guess[i], i)
            # print(len(poss_words), "possible words")
            if len(poss_words) == 0:
                print("are you sure your word is legal?")
                break
        if found:
            print("yay i made it in", guess_num, "guesses")
        else:
            print("maybe next time ill make it :(")
        print("start again? (y/n)")
        answer = input()
        if answer == "y":
            game()
game()
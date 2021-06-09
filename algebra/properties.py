import random


# associative property
def assoc_prop():
    problems = ["a(b * c) = (a * b)c", "x * 4 * y = 4x * y", "(x - y) - z = x - (y - z)", "a + (b + c) + d = (a + b) + (c + )d"]
    selection = random.randrange(len(problems))
    correct = 't'
    if selection == 3:
        corect = 'f'

    answer = input("Is "+problems[selection]+"true(t) or false(f): ")
    
    if input == correct:
        print("Correct! +1 point for you!")
        return 1
    
    print("sorry, that is incorrect. -1 point.")
    return -1


# cummutative property
def cummut_prop():
    problems = ["a * b = b * a", "x + y + z = x + z + y", "x/y = y/z","a * b * c = c * a * b"]
    selection = random.randrange(len(problems))
    correct = 't'
    if selection == 3:
        corect = 'f'
    
    answer = input("Is "+problems[selection]+"true(t) or false(f): ")
    
    if input == correct:
        print("Correct! +1 point for you!")
        return 1
    
    print("sorry, that is incorrect. -1 point.")
    return -1


# distributive property
def dist_prop():
    problems = ["x(y + z) = xy + xz", "a(b - c) * d = abd - acd", "(a /d)c = (ac / dc)", "a / (b + c)d = a/(bd + cd)"]
    selection = random.randrange(len(problems))
    correct = 't'
    if selection == 3:
        corect = 'f'
    
    answer = input("Is "+problems[selection]+"true(t) or false(f): ")
    
    if input == correct:
        print("Correct! +1 point for you!")
        return 1
    
    print("sorry, that is incorrect. -1 point.")
    return -1
    
    
score = 0
total_correct = 0
total_wrong = 0
options = [assoc_prop, cummut_prop, dist_prop]

while True:
    result = random.choice(options)()

    score += result

    if result > 0:
        total_correct += 1
    else:
        total_wrong += 1

    print("Score = "+str(score)+" ("+str(total_correct)+" correct answers & "
          +str(total_wrong)+" incorrect answers)")


with open("day2.txt", "r") as f:
    content = f.readlines()

    rps = {
        "A X": "Z",
        "A Y": "X",
        "A Z": "Y",
        "B X": "X",
        "B Y": "Y",
        "B Z": "Z",
        "C X": "Y",
        "C Y": "Z",
        "C Z": "X"
    }

    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    winnings = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    score = 0
    for r in content:
        elf_move = r[0]
        my_decision = r[2]

        my_move = rps.get(r[:-1])

        score += points.get(my_move) + winnings.get(my_decision)

    print(score)

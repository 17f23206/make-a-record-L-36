game = {"score": 0, 
          "level": 0, 
          "username": "RICKY"}
print("Enter username:")
game["username"] = input()
print("Enter level in integers:")
game["level"] = int(input())
print("Enter level in integers:")
game["score"] = int(input())
print("Username:", game["username"])
print("level: ", game["level"])
print("score: ", game["score"])
players = []

add_players = True
while add_players:
    print("Enter a username:")
    username = input()
    print("Enter a password:")
    password = input()
    print("Enter a score")
    score = input()

    player = {"username" : username,
              "password" : password,
              "score" : score}

    players.append(player)

    print("Would you like to add another player? Y/N")
    answer = input().upper()
    if answer == "N":
        add_players = False

print(players)

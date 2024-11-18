import random
def play_game():
    player1_hand = []
    player2_hand = []
    table = []
    for _ in range(5):
        player1_hand.append(random.randint(1, 9))
        player2_hand.append(random.randint(1, 9))

    current_player = 1

    while True:
        if current_player == 1:
            card = player1_hand.pop()
        else:
            card = player2_hand.pop()

        table.append(card)

        if len(table) > 1 and table[-1] == table[-2]:
            if current_player == 1:
                player2_hand.insert(0, table.pop())
            else:
                player1_hand.insert(0, table.pop())

        if sum(table) >= 20 or not player1_hand or not player2_hand:
            break

        current_player = 3 - current_player

    winner = 1 if sum(table) % 2 == 0 else 2
    print(f"Переміг гравець {winner}")


play_game()
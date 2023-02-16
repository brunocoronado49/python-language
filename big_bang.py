def big_bang_game(games):

    rules = {
        'piedra': ['tijera', 'lagarto'],
        'papel': ['piedra', 'spok'],
        'tijera': ['papel', 'lagarto'],
        'lagarto': ['spok', 'papel'],
        'spok': ['piedra', 'tijera']
    }

    player_one = 0
    player_two = 0

    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]

        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1


    return "Tie" if player_one == player_two else 'Player 1' if player_one > player_two else 'Player 2'

juego = big_bang_game([('piedra', 'piedra')])

print(juego)

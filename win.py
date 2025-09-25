def check_win(turns):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
        [0, 4, 8], [2, 4, 6]               # Диагональные линии
    ]

    main_set = set(turns)
    for combination in win_combinations:
        if set(combination).issubset(main_set):
            return True
        return False

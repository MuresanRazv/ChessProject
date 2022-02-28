from Utils import draw


def check_possible_movements(type_of_piece, pos, groups):
    if type_of_piece == "blt60.png" or type_of_piece == "bdt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]

        while x < 680 and not draw.check_collision((x, y), groups) and y < 680:  # RIGHT-UP
            x += 80
            y += 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x > 40 and not draw.check_collision((x, y), groups) and y < 680:  # LEFT-UP
            x -= 80
            y += 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x < 680 and not draw.check_collision((x, y), groups) and y > 0:  # DOWN-RIGHT
            x += 80
            y -= 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x > 40 and not draw.check_collision((x, y), groups) and y > 0:  # DOWN-LEFT
            x -= 80
            y -= 80
            possible_movements.append((x, y))
        return possible_movements

    if type_of_piece == "plt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]
        if not draw.check_collision((x, y + 80), groups):
            possible_movements.append((x, y + 80))
        return possible_movements

    if type_of_piece == "pdt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]
        if not draw.check_collision((x, y - 80), groups):
            possible_movements.append((x, y - 80))
        return possible_movements

    if type_of_piece == "klt60.png" or type_of_piece == "kdt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]
        if not draw.check_collision((x + 80, y), groups) and x + 80 < 680:  # RIGHT
            possible_movements.append((x + 80, y))
        if not draw.check_collision((x + 80, y - 80), groups) and x + 80 < 680 and y - 80 > 40:  # DOWN-RIGHT
            possible_movements.append((x + 80, y - 80))
        if not draw.check_collision((x, y - 80), groups) and y - 80 > 40:  # DOWN
            possible_movements.append((x, y - 80))
        if not draw.check_collision((x - 80, y - 80), groups) and x - 80 > 40 and y - 80 > 40:  # DOWN-LEFT
            possible_movements.append((x + 80, y))
        if not draw.check_collision((x - 80, y), groups) and x - 80 > 0:  # LEFT
            possible_movements.append((x - 80, y))
        if not draw.check_collision((x - 80, y + 80), groups) and x - 80 > 40 and y + 80 < 680:  # UP-LEFT
            possible_movements.append((x - 80, y + 80))
        if not draw.check_collision((x, y + 80), groups) and y + 80 < 680:  # UP
            possible_movements.append((x, y + 80))
        if not draw.check_collision((x + 80, y + 80), groups) and x + 80 < 680 and y + 80 < 680:  # UP-RIGHT
            possible_movements.append((x + 80, y + 80))
        return possible_movements

    if type_of_piece == "ndt60" or type_of_piece == "nlt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]
        if not draw.check_collision((x + 2 * 80, y + 80), groups) and x + 2 * 80 < 680 and y + 80 < 680:  # RIGHT-UP
            possible_movements.append((x + 2 * 80, y + 80))
        if not draw.check_collision((x + 2 * 80, y - 80), groups) and x + 2 * 80 < 680 and y - 80 > 40:  # RIGHT-DOWN
            possible_movements.append((x + 2 * 80, y - 80))
        if not draw.check_collision((x - 80, y + 2 * 80), groups) and x - 80 > 40 and y + 2 * 80 < 680:   # DOWN-LEFT
            possible_movements.append((x - 80, y + 2 * 80))
        if not draw.check_collision((x + 80, y + 2 * 80), groups) and x + 80 > 40 and y + 2 * 80 < 680:  # DOWN-RIGHT
            possible_movements.append((x - 80, y + 2 * 80))
        if not draw.check_collision((x - 2 * 80, y + 80), groups) and x - 2 * 80 > 40 and y + 80 < 680:  # LEFT-UP
            possible_movements.append((x - 2 * 80, y + 80))
        if not draw.check_collision((x - 2 * 80, y - 80), groups) and x - 2 * 80 > 40 and y - 80 > 40:  # LEFT-DOWN
            possible_movements.append((x - 2 * 80, y - 80))
        if not draw.check_collision((x - 80, y - 2 * 80), groups) and x - 80 > 40 and y - 2 * 80 > 40:  # LEFT-DOWN
            possible_movements.append((x - 80, y - 2 * 80))
        if not draw.check_collision((x + 80, y - 2 * 80), groups) and x + 80 < 680 and y - 2 * 80 > 40:  # LEFT-RIGHT
            possible_movements.append((x + 80, y - 2 * 80))
        return possible_movements

    if type_of_piece == "rlt60.png" or type_of_piece == "rdt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]

        while not draw.check_collision((x, y), groups) and x < 680:  # RIGHT
            possible_movements.append((x, y))
            x += 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x, y), groups) and x > 40:  # LEFT
            possible_movements.append((x, y))
            x -= 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x, y), groups) and y < 680:  # UP
            possible_movements.append((x, y))
            y += 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x, y), groups) and y > 40:  # DOWN
            possible_movements.append((x, y))
            y -= 80
        return possible_movements

    if type_of_piece == "qlt60.png" or type_of_piece == "qdt60.png":
        possible_movements = []
        x = pos[0]
        y = pos[1]

        while not draw.check_collision((x + 80, y), groups) and x < 680:  # RIGHT
            possible_movements.append((x, y))
            x += 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x - 80, y), groups) and x > 40:  # LEFT
            possible_movements.append((x, y))
            x -= 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x, y + 80), groups) and y < 680:  # UP
            possible_movements.append((x, y + 80))
            y += 80

        x = pos[0]
        y = pos[1]
        while not draw.check_collision((x, y - 80), groups) and y > 40:  # DOWN
            possible_movements.append((x, y))
            y -= 80

        x = pos[0]
        y = pos[1]
        while x < 680 and not draw.check_collision((x, y), groups) and y < 680:  # RIGHT-UP
            x += 80
            y += 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x > 40 and not draw.check_collision((x, y), groups) and y < 680:  # LEFT-UP
            x -= 80
            y += 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x < 680 and not draw.check_collision((x, y), groups) and y > 0:  # DOWN-RIGHT
            x += 80
            y -= 80
            possible_movements.append((x, y))

        x = pos[0]
        y = pos[1]
        while x > 40 and not draw.check_collision((x, y), groups) and y > 0:  # DOWN-LEFT
            x -= 80
            y -= 80
            possible_movements.append((x, y))

        return possible_movements

#Tic Tac Toe Game
import pygame, os, time, random
pygame.init(), pygame.display.set_caption('Tic Tac Toe')
while True:
    WIDTH, HEIGHT, switch = 500, 500, 1
    WIN, board, mode, bot_choices, indicator, letter_O, letter_X, COMPUTER, PLAYER, G_COMPUTER, G_PLAYER = pygame.display.set_mode((WIDTH, HEIGHT)), [], None, [1, 2, 3, 4, 5, 6, 7, 8, 0], None, pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'Glow_O3.png')), (WIDTH/3, HEIGHT/3)), pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'Glow_X3.png')), (WIDTH/3, HEIGHT/3)), pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'COMPUTER.png')), (WIDTH, HEIGHT/2)), pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'PLAYER.png')), (WIDTH, HEIGHT/2)), pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'G_COMPUTER.png')), (WIDTH, HEIGHT/2)), pygame.transform.scale(pygame.image.load(os.path.join('Tic_Tac_Toe_Game', 'G_PLAYER.png')), (WIDTH, HEIGHT/2))
    while True:
        FONT, XO_FONT, streak_B3B1, streak_A1A3, streak_C1C3, streak_A1C1, streak_A2C2, streak_A3C3, bot = pygame.font.SysFont('comicsans', 150), pygame.font.SysFont('comicsans', 70), pygame.Rect((WIDTH/2)-5, (HEIGHT/3)/2, 10, (HEIGHT/3)*2), pygame.Rect(((WIDTH/3)/2)-5, (HEIGHT/3)/2, 10, (HEIGHT/3)*2), pygame.Rect((WIDTH/3)*2.5, (HEIGHT/3)/2, 10, (HEIGHT/3)*2), pygame.Rect((WIDTH/3)/2, ((HEIGHT/3)*2.5)-5, (WIDTH/3)*2, 10), pygame.Rect((WIDTH/3)/2, (HEIGHT/2)-5, (WIDTH/3)*2, 10), pygame.Rect((WIDTH/3)/2, ((HEIGHT/3)/2)-5, (WIDTH/3)*2, 10), random.choice(bot_choices)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if mode == None:
                if indicator == None:
                    WIN.blit(COMPUTER, (0, 0))
                    WIN.blit(PLAYER, (0, HEIGHT/2))
                    pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT/2), (WIDTH, HEIGHT/2), 10)#MIDDLE
                    pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 10)#DOWN
                    pygame.draw.line(WIN, (255, 255, 255), (0, 0), (WIDTH, 0), 10)#UP
                    pygame.draw.line(WIN, (255, 255, 255), (0, 0), (0, HEIGHT), 10)#LEFT
                    pygame.draw.line(WIN, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 10)#RIGHT
                elif indicator == 'computer':
                    WIN.blit(PLAYER, (0, HEIGHT/2))
                    WIN.blit(G_COMPUTER, (0, 0))
                    pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 10)
                    pygame.draw.line(WIN, (255, 255, 255), (0, 0), (0, HEIGHT), 10)
                    pygame.draw.line(WIN, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, HEIGHT/2), (WIDTH, HEIGHT/2), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, 0), (WIDTH, 0), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, 0), (0, HEIGHT/2), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (WIDTH, 0), (WIDTH, HEIGHT/2), 10)
                elif indicator == 'player':
                    WIN.blit(G_PLAYER, (0, HEIGHT/2))
                    WIN.blit(COMPUTER, (0, 0))
                    pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 10)
                    pygame.draw.line(WIN, (255, 255, 255), (0, 0), (0, HEIGHT), 10)
                    pygame.draw.line(WIN, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, HEIGHT/2), (WIDTH, HEIGHT/2), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, HEIGHT), (WIDTH, HEIGHT), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (0, HEIGHT/2), (0, HEIGHT), 10)
                    pygame.draw.line(WIN, (128, 128, 128), (WIDTH, HEIGHT/2), (WIDTH, HEIGHT), 10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        indicator = 'computer'
                    elif event.key == pygame.K_DOWN:
                        indicator = 'player'
                    if indicator == 'computer' and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                        pygame.display.update(), time.sleep(1), WIN.fill((0, 0, 0))
                        mode = 'computer'
                    elif indicator == 'player' and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                        pygame.display.update(), time.sleep(1), WIN.fill((0, 0, 0))
                        mode = 'player'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mode == 'computer':
                M_WIDTH, M_HEIGHT = pygame.mouse.get_pos()
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board)):
                    board.append('WIN.blit(letter_X, (0, 0))'), WIN.blit(letter_X, (0, 0)), bot_choices.remove(0)
                    switch -= 1
                elif bot == 0 and (switch == 0) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board)):
                    board.append('WIN.blit(letter_O, (0, 0))'), WIN.blit(letter_O, (0, 0)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, 0))'), WIN.blit(letter_X, (WIDTH/3, 0)), bot_choices.remove(1)
                    switch -= 1
                elif bot == 1 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, 0))'), WIN.blit(letter_O, (WIDTH/3, 0)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, 0))'), WIN.blit(letter_X, ((WIDTH/3)*2, 0)), bot_choices.remove(2)
                    switch -= 1
                elif bot == 2 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, 0))'), WIN.blit(letter_O, ((WIDTH/3)*2, 0)), bot_choices.remove(bot)
                    switch += 1
                #A2C2
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, (0, HEIGHT/3))'), WIN.blit(letter_X, (0, HEIGHT/3)), bot_choices.remove(3)
                    switch -= 1
                elif bot == 3 and (switch == 0) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, (0, HEIGHT/3))'), WIN.blit(letter_O, (0, HEIGHT/3)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))'), WIN.blit(letter_X, (WIDTH/3, HEIGHT/3)), bot_choices.remove(4)
                    switch -= 1
                elif bot == 4 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))'), WIN.blit(letter_O, (WIDTH/3, HEIGHT/3)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))'), WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3)), bot_choices.remove(5)
                    switch -= 1
                elif bot == 5 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))'), WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3)), bot_choices.remove(bot)
                    switch += 1
                #A1C1
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, (0, (HEIGHT/3)*2))'), WIN.blit(letter_X, (0, (HEIGHT/3)*2)), bot_choices.remove(6)
                    switch -= 1
                elif bot == 6 and (switch == 0) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, (0, (HEIGHT/3)*2))'), WIN.blit(letter_O, (0, (HEIGHT/3)*2)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))'), WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2)), bot_choices.remove(7)
                    switch -= 1
                elif bot == 7 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))'), WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2)), bot_choices.remove(bot)
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))'), WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2)), bot_choices.remove(8)
                    switch -= 1
                elif bot == 8 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))'), WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2)), bot_choices.remove(bot)
                    switch += 1
                # if (bot == 8 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board))) or (bot == 7 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board))) or (bot == 6 and (switch == 0) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board))) or (bot == 5 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board))) or (bot == 4 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board))) or (bot == 3 and (switch == 0) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board))) or (bot == 2 and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board))) or (bot == 1 and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board))) or (bot == 0 and (switch == 0) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board))):
                #     switch += 1
                # elif ((M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board))) or ((M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board))) or ((M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board))) or ((M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board))) or ((M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board))) or ((M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board))) or ((M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board))) or ((M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board))) or ((M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board))):
                #     switch -= 1
            #do the same thing in the switch
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mode == 'player':
                M_WIDTH, M_HEIGHT = pygame.mouse.get_pos()
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board)):
                    board.append('WIN.blit(letter_X, (0, 0))'), WIN.blit(letter_X, (0, 0))
                    switch -= 1
                elif (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 0) and (('WIN.blit(letter_X, (0, 0))' not in board) and ('WIN.blit(letter_O, (0, 0))' not in board)):
                    board.append('WIN.blit(letter_O, (0, 0))'), WIN.blit(letter_O, (0, 0))
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, 0))'), WIN.blit(letter_X, (WIDTH/3, 0))
                    switch -= 1
                elif (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, 0))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, 0))'), WIN.blit(letter_O, (WIDTH/3, 0))
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, 0))'), WIN.blit(letter_X, ((WIDTH/3)*2, 0))
                    switch -= 1
                elif (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= 10 and M_HEIGHT <= ((HEIGHT/3)-10)) and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, 0))'), WIN.blit(letter_O, ((WIDTH/3)*2, 0))
                    switch += 1
                #A2C2
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, (0, HEIGHT/3))'), WIN.blit(letter_X, (0, HEIGHT/3))
                    switch -= 1
                elif (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 0) and (('WIN.blit(letter_X, (0, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, (0, HEIGHT/3))'), WIN.blit(letter_O, (0, HEIGHT/3))
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))'), WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))
                    switch -= 1
                elif (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))'), WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))'), WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))
                    switch -= 1
                elif (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= ((HEIGHT/3)+10) and M_HEIGHT <= (((HEIGHT/3)*2)-10)) and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))'), WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))
                    switch += 1
                #A1C1
                if (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, (0, (HEIGHT/3)*2))'), WIN.blit(letter_X, (0, (HEIGHT/3)*2))
                    switch -= 1
                elif (M_WIDTH >= 10 and M_WIDTH <= ((WIDTH/3)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 0) and (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, (0, (HEIGHT/3)*2))'), WIN.blit(letter_O, (0, (HEIGHT/3)*2))
                    switch += 1
                if (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))'), WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))
                    switch -= 1
                elif (M_WIDTH >= ((WIDTH/3)+10) and M_WIDTH <= (((WIDTH/3)*2)-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 0) and (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))'), WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))
                    switch += 1
                if (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 1) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))'), WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))
                    switch -= 1
                elif (M_WIDTH >= (((WIDTH/3)*2)+10) and M_WIDTH <= (WIDTH-10)) and (M_HEIGHT >= (((HEIGHT/3)*2)+10) and M_HEIGHT <= (HEIGHT-10)) and (switch == 0) and (('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' not in board)):
                    board.append('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))'), WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))
                    switch += 1
        if mode == 'player' or mode == 'computer':
            #BORDERS
            pygame.draw.line(WIN, (255, 255, 255), (WIDTH/3, 0), (WIDTH/3, HEIGHT), 10)
            pygame.draw.line(WIN, (255, 255, 255), ((WIDTH/3)*2, 0), ((WIDTH/3)*2, HEIGHT), 10)
            pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT/3), (WIDTH, HEIGHT/3), 10)
            pygame.draw.line(WIN, (255, 255, 255), (0, (HEIGHT/3)*2), (WIDTH, (HEIGHT/3)*2), 10)
            #FRAMES
            pygame.draw.line(WIN, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 10)
            pygame.draw.line(WIN, (255, 255, 255), (0, 0), (WIDTH, 0), 10)
            pygame.draw.line(WIN, (255, 255, 255), (0, 0), (0, HEIGHT), 10)
            pygame.draw.line(WIN, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 10)
        # RED
        if ('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, 0))' in board):#A3C3
            pygame.draw.rect(WIN, (239, 161, 161), streak_A3C3), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (0, HEIGHT/3))' in board):#A2C2
            pygame.draw.rect(WIN, (239, 161, 161), streak_A2C2), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#A1C1
            pygame.draw.rect(WIN, (239, 161, 161), streak_A1C1), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, (0, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board):#A1A3
            pygame.draw.rect(WIN, (239, 161, 161), streak_A1A3), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, (WIDTH/3, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' in board):#B1B3
            pygame.draw.rect(WIN, (239, 161, 161), streak_B3B1), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#C1C3
            pygame.draw.rect(WIN, (239, 161, 161), streak_C1C3), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#A1C3
            pygame.draw.line(WIN, (239, 161, 161), ((WIDTH/3)/2, (HEIGHT/3)/2), ((WIDTH/3)*2.5, (HEIGHT/3)*2.5), 15), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board):#A3C1
            pygame.draw.line(WIN, (239, 161, 161), ((WIDTH/3)/2, (HEIGHT/3)*2.5), ((WIDTH/3)*2.5, (HEIGHT/3)/2), 15), WIN.blit(XO_FONT.render('Player X Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player X Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        # BLUE
        elif ('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' in board):#A3C3
            pygame.draw.rect(WIN, (145, 224, 255), streak_A3C3), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' in board):#A2C2    
            pygame.draw.rect(WIN, (145, 224, 255), streak_A2C2), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#A1C1
            pygame.draw.rect(WIN, (145, 224, 255), streak_A1C1), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board):#A1A3
            pygame.draw.rect(WIN, (145, 224, 255), streak_A1A3), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, (WIDTH/3, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' in board):#B1B3
            pygame.draw.rect(WIN, (145, 224, 255), streak_B3B1), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#C1C3
            pygame.draw.rect(WIN, (145, 224, 255), streak_C1C3), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board):#A1C3
            pygame.draw.line(WIN, (145, 224, 255), ((WIDTH/3)/2, (HEIGHT/3)/2), ((WIDTH/3)*2.5, (HEIGHT/3)*2.5), 15), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board):#A3C1
            pygame.draw.line(WIN, (145, 224, 255), ((WIDTH/3)/2, (HEIGHT/3)*2.5), ((WIDTH/3)*2.5, (HEIGHT/3)/2), 15), WIN.blit(XO_FONT.render('Player O Wins!', True, (31, 214, 85)), (WIDTH / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - XO_FONT.render('Player O Wins!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        elif len(board) == 9:
            WIN.blit(FONT.render('TIE!', True, (31, 214, 85)), (WIDTH / 2 - FONT.render('TIE!', True, (255, 255, 255)).get_width() / 2, HEIGHT / 2 - FONT.render('TIE!', True, (255, 255, 255)).get_height() / 2)), pygame.display.update(), time.sleep(3), WIN.fill((0, 0, 0))
        pygame.display.update()
        if ((('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, 0))' in board)) or (('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (0, HEIGHT/3))' in board)) or (('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, (0, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_X, (WIDTH/3, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, (WIDTH/3, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_X, (0, 0))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_X, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_X, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_X, ((WIDTH/3)*2, 0))' in board)) or (len(board) == 9)) or ((('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, 0))' in board)) or (('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' in board)) or (('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, (0, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_O, (WIDTH/3, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, (WIDTH/3, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_O, (0, 0))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, (HEIGHT/3)*2))' in board)) or (('WIN.blit(letter_O, (0, (HEIGHT/3)*2))' in board) and ('WIN.blit(letter_O, (WIDTH/3, HEIGHT/3))' in board) and ('WIN.blit(letter_O, ((WIDTH/3)*2, 0))' in board)) or (len(board) == 9)):
            break
'''
(3/4 KG )Pickles
Salt (1/4 Cup)
Sugar (1.5 Cup)
Ground Mustard Seed (2 Tb)
White Vinegar (1 Cup)
Garlic (1/2 Whole)
Whole Peppercorn 2 Tb
Dill
'''
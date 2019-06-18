import random
import sys

import pygame

background_image = pygame.image.load('NandC_Back.png')
nought = pygame.image.load('Nought.png')
cross = pygame.image.load('Cross.png')


class Piece:
    def __init__(self, position, surf):
        self.N_or_C = 0
        self.game_piece = pygame.draw.rect(surf, (255, 0, 0), (position))
        self.location = position
        self.size = 158
        self.surfs = surf

    def get_image(self):
        self.mouse = pygame.mouse.get_pos()
        if(self.N_or_C == 0):
            if(self.on_square()):
                self.game_piece = pygame.draw.rect(
                    self.surfs, (220, 220, 220), (self.location))
            else:
                self.game_piece = pygame.draw.rect(
                    self.surfs, (255, 255, 255), (self.location))

        if self.N_or_C == 1:
            self.game_piece = pygame.draw.rect(
                self.surfs, (255, 255, 255), (self.location))
            self.surfs.blit(nought, self.location)
        elif self.N_or_C == 2:
            self.game_piece = pygame.draw.rect(
                self.surfs, (255, 255, 255), (self.location))
            self.surfs.blit(cross, self.location)

    def play_square(self, player):
        if(self.N_or_C == 0):
            if(self.on_square()):
                if(player == 1):
                    self.N_or_C = 1
                    return(2)
                elif(player == 2):
                    self.N_or_C = 2
                    return(1)

        return(player)

    def on_square(self):
        self.mouse = pygame.mouse.get_pos()
        return(self.location[0] < self.mouse[0] and self.location[0]+self.size > self.mouse[0] and self.location[1] < self.mouse[1] and self.location[1]+self.size > self.mouse[1])

    def reset(self):
        self.N_or_C = 0


class Reset_Button:
    def __init__(self, surf):
        self.height = 50
        self.width = 150
        self.x_loc = 830
        self.y_loc = 650
        self.reset = pygame.draw.rect(
            surf, (190, 190, 190), (self.x_loc, self.y_loc, self.width, self.height))

    def on_button(self):
        self.mouse = pygame.mouse.get_pos()
        return(self.reset.collidepoint(self.mouse))


class Board:
    HEIGHT = 800
    WIDTH = 1000

    def __init__(self):
        pygame.init()
        self.starting_player = 1
        self.player = self.starting_player
        self.reset_flag = False
        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0

        # setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill((255, 255, 255))

        self.screen.blit(background_image, (0, 0))
        self.reset_button = Reset_Button(self.screen)

        # Init score area
        self.border = pygame.draw.rect(
            self.screen, (0, 0, 0), (800, 0, 5, 800))
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        # Create the game pieces
        self.one = Piece([50, 50, 158, 158], self.screen)
        self.two = Piece([288, 50, 158, 158], self.screen)
        self.three = Piece([550, 50, 158, 158], self.screen)
        self.four = Piece([50, 300, 158, 158], self.screen)
        self.five = Piece([288, 300, 158, 158], self.screen)
        self.six = Piece([550, 300, 158, 158], self.screen)
        self.seven = Piece([50, 550, 158, 158], self.screen)
        self.eight = Piece([288, 550, 158, 158], self.screen)
        self.nine = Piece([550, 550, 158, 158], self.screen)

    def Draw_Score_Area(self):

        wins = self.myfont.render("Scores", False, (0, 0, 0))
        reset = self.myfont.render("RESET", False, (0, 0, 0))
        X_score_label = self.myfont.render("X ", False, (0, 0, 0))
        O_score_label = self.myfont.render("O ", False, (0, 0, 0))
        draw_score = self.myfont.render("Draw", False, (0, 0, 0))
        equals = self.myfont.render("=", False, (0, 0, 0))
        player_turn = self.myfont.render("Turn", False, (0, 0, 0))

        X_score_display = self.myfont.render(
            str(self.x_score), False, (0, 0, 0))
        O_score_display = self.myfont.render(
            str(self.o_score), False, (0, 0, 0))
        draw_score_display = self.myfont.render(
            str(self.draw_score), False, (0, 0, 0))

        pygame.draw.rect(self.screen, (255, 255, 255), (935, 230, 50, 300))
        self.screen.blit(wins, (835, 170))

        self.screen.blit(X_score_display, (935, 230))
        self.screen.blit(O_score_display, (935, 280))
        self.screen.blit(draw_score_display, (935, 330))
        self.screen.blit(X_score_label, (815, 230))
        self.screen.blit(O_score_label, (815, 280))
        self.screen.blit(draw_score, (815, 330))
        self.screen.blit(equals, (910, 230))
        self.screen.blit(equals, (910, 280))
        self.screen.blit(equals, (910, 330))
        self.screen.blit(player_turn, (815, 80))
        self.screen.blit(equals, (910, 80))
        if(self.player == 1):
            pygame.draw.rect(self.screen, (255, 255, 255), (935, 80, 50, 50))
            self.screen.blit(O_score_label, (935, 80))
        elif(self.player == 2):
            pygame.draw.rect(self.screen, (255, 255, 255), (935, 80, 50, 50))
            self.screen.blit(X_score_label, (935, 80))

        self.screen.blit(reset, (855, 655))

    def Update_Board(self):
        self.game_board = [[self.one.N_or_C, self.two.N_or_C, self.three.N_or_C], [
            self.four.N_or_C, self.five.N_or_C, self.six.N_or_C], [self.seven.N_or_C, self.eight.N_or_C, self.nine.N_or_C]]

    def Check_Win(self, player):
        self.win = False
        if(self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == player):
            self.win = True
        elif(self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == player):
            self.win = True
        elif(self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == player):
            self.win = True
        elif(self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == player):
            self.win = True
        elif(self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == player):
            self.win = True
        elif(self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == player):
            self.win = True
        elif(self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == player):
            self.win = True
        elif(self.game_board[2][2] == self.game_board[1][1] == self.game_board[0][2] == player):
            self.win = True
        return(self.win)

    def Reset_board(self):
        self.reset_flag = False
        self.one.reset()
        self.two.reset()
        self.three.reset()
        self.four.reset()
        self.five.reset()
        self.six.reset()
        self.seven.reset()
        self.eight.reset()
        self.nine.reset()
        if(self.starting_player == 1):
            self.starting_player = 2
        else:
            self.starting_player = 1
        self.player = self.starting_player

    def game_loop(self):

        while True:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    # check for click on squares
                    self.player = self.one.play_square(self.player)
                    self.player = self.two.play_square(self.player)
                    self.player = self.three.play_square(self.player)
                    self.player = self.four.play_square(self.player)
                    self.player = self.five.play_square(self.player)
                    self.player = self.six.play_square(self.player)
                    self.player = self.seven.play_square(self.player)
                    self.player = self.eight.play_square(self.player)
                    self.player = self.nine.play_square(self.player)
                    # check if reset button is clicked
                    if(self.reset_button.on_button()):
                        self.reset_flag = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # update pieces
            self.Update_Board()
            self.one.get_image()
            self.two.get_image()
            self.three.get_image()
            self.four.get_image()
            self.five.get_image()
            self.six.get_image()
            self.seven.get_image()
            self.eight.get_image()
            self.nine.get_image()

            # check if a player won or there is a draw
            if(self.Check_Win(1)):
                self.o_score += 1
                self.Reset_board()
            if(self.Check_Win(2)):
                self.x_score += 1
                self.Reset_board()
            if(not any(0 in row for row in self.game_board)):
                self.draw_score += 1
                self.Reset_board()

            # reset the scores when reset button is pressed
            if(self.reset_flag):
                self.Reset_board()
                self.x_score = 0
                self.o_score = 0
                self.draw_score = 0

            self.Draw_Score_Area()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    board = Board()
    board.game_loop()

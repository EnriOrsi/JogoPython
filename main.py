# -*- coding: utf-8 -*-
import sys, pygame
import pygame_menu
from game.jogo import *

pygame.init()
icone = pygame.image.load ('./img/dinheiro.png')

pygame.display.set_caption("Quem dá mais?")
pygame.display.set_icon(icone)

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
menuBG= pygame_menu.baseimage.BaseImage(image_path='./img/menuBG.jpg', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL, drawing_offset=(0,0))

def startTheGame():
    comecarJogo()
    pass

def howToPlay():
    comoJogarT = pygame_menu.Menu('Como Jogar', 800, 600, center_content=True, onclose=menu, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green, title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    comoJogarT.add.label("O produto será apresentado junto com o valor minino.", font_color=green, font_name='Impact', selection_color=green) 
    comoJogarT.add.label("Apos isso, as Ofertas são abertas!", font_color=green, font_name='Impact', selection_color=green)
    comoJogarT.add.label("quem dar mais fica com a obra", font_color=green, font_name='Impact', selection_color=green)
    comoJogarT.mainloop(screen)
    pass

def creditos():
    creditosT = pygame_menu.Menu('Creditos', 800, 600, center_content=True, onclose=menu, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green, title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    creditosT.add.label('Feito por:', font_color=green, font_name='Impact', selection_color=green)
    creditosT.add.label('Enri Bernardi Carvalho Orsi', font_color=green, font_name='Impact', selection_color=green)
    creditosT.add.label('Vitor Setsuo Noda Cheung', font_color=green, font_name='Impact', selection_color=green)
    creditosT.add.label('')
    creditosT.add.label('')
    creditosT.add.label('Desenvolvido para a aula de Algoritimos e Programação II', font_color=green, font_name='Impact', selection_color=green)
    creditosT.add.label('da Universidade Presbiteriana Mackenzie', font_color=green, font_name='Impact', selection_color=green)
    creditosT.add.label('mestrada pelo Professor Tomaz Mikio Sasaki', font_color=green, font_name='Impact', selection_color=green)
    creditosT.mainloop(screen)
    pass

def menu():
    menu = pygame_menu.Menu('Quem da mais', 800, 600, center_content=True, onclose=pygame_menu.events.EXIT, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green, title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    menu.add.button('Começar', startTheGame, background_color=white, font_color=black, font_name='Impact', selection_color=green)
    menu.add.label('')
    menu.add.button('Como Jogar', howToPlay, background_color=white, font_color=black, font_name='Impact', selection_color=green)
    menu.add.label('')
    menu.add.button('Créditos', creditos, background_color=white, font_color=black, font_name='Impact', selection_color=green)
    menu.mainloop(screen)
    pass

menu()
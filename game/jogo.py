import sys, pygame
import pygame_menu
import random

pygame.init()

icone = pygame.image.load ('./img/dinheiro.png')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
menuBG= pygame_menu.baseimage.BaseImage(image_path='./img/menuBG.jpg', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL, drawing_offset=(0,0))
pygame.display.set_caption("Quem dá mais?")
pygame.display.set_icon(icone)
font = 'Impact', 30, green, white, black, True
money = '100.00'
sortProd = 0, 1, 2, 3
produtos = './img/moedaV.png', './img/moedaF.png', './img/vasoV.png', './img/vasoF.png'
precoProd = '20.00', '20.00', '30.00', '30.00'
prodCompred = []
vProdCompred = []
i = 0
sellPrice = 10, 7, 5, 0
wl= 'w', 'l'
getProd = 0, 1, 2


def comecarJogo():
    game = pygame_menu.Menu('Quem da mais', 800, 600, center_content=True, onclose=pygame_menu.events.RESET, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    game.add.label("Insira seu nome:", font_color=green, font_name='Impact', selection_color=green) 
    game.add.text_input(title='', copy_paste_enable=False, onreturn=home).set_font(font[0], font[1], font[2], font[3], font[4], font[5], background_color='#000000')
    game.add.label("Pressione \"Enter\" para continuar", font_color=green, font_name='Impact', selection_color=green) 
    game.mainloop(screen)
    pass

def home(value):
    global nome 
    nome = value
    home = pygame_menu.Menu('Quem da mais', 800, 600, center_content=True, onclose=pygame_menu.events.RESET, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    home.add.label('Olá ' + value, font_color=green, font_name='Impact', selection_color=green)
    home.add.label('')
    home.add.button('Ver os produtos comprados', verProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    home.add.label('')
    home.add.button('Ajuda nas compras e vendas', ajuda, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    home.add.label('')
    home.add.button('Comprar Produtos', compraProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    home.add.label('')
    home.add.button('Vender Produtos', vender, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    home.add.label('')
    home.add.label('Seu dinheiro: R$' + money, font_color=green, font_name='Impact', selection_color=green).set_alignment(pygame_menu.locals.ALIGN_CENTER)
    home.mainloop(screen)
    pass

def verProd():
    if len(prodCompred) <= 0:
        semProd()
    else:
        seeProd = pygame_menu.Menu('Produtos de ' + nome, 800, 600, center_content=True, onclose=takeHome, columns=3, rows=3, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
        seeProd.add.label('')
        seeProd.add.button('Anterior', prev, background_color=white, font_color=black, font_name='Impact', selection_color=black)
        seeProd.add.label('')
        seeProd.add.image(prodCompred[i], scale=(0.2, 0.2))
        seeProd.add.label('Preço: R$' + vProdCompred[i], font_color=green, font_name='Impact', selection_color=green)
        seeProd.add.label('')
        seeProd.add.label('')
        seeProd.add.button('Próximo', prox, background_color=white, font_color=black, font_name='Impact', selection_color=black)
        seeProd.add.label('')
        seeProd.mainloop(screen)
    pass

def ajuda():
    ajudaT = pygame_menu.Menu('Ajuda', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    ajudaT.add.label("Cuidado!!", font_color=green, font_name='Impact', selection_color=green) 
    ajudaT.add.label("Apenas algumas obras são verdadeiras!", font_color=green, font_name='Impact', selection_color=green)
    ajudaT.add.label("Se você comprar uma obra falsa, você não conseguirá vender!", font_color=green, font_name='Impact', selection_color=green)
    ajudaT.add.label("As obras verdadeiras são: ", font_color=green, font_name='Impact', selection_color=green)
    ajudaT.add.label("Moeda Verdadeira:", font_color=green, font_name='Impact', selection_color=green)
    ajudaT.add.image(produtos[0], scale=(0.1, 0.1))
    ajudaT.add.label("Vaso Verdadeiro:", font_color=green, font_name='Impact', selection_color=green)
    ajudaT.add.image(produtos[2], scale=(0.1, 0.1))
    ajudaT.mainloop(screen)
    pass

def compraProd():
    global leilao
    leilao = random.choice(sortProd)
    buy = pygame_menu.Menu('Quem da mais', 800, 600, center_content=True, onclose=takeHome, columns=2, rows=5, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    buy.add.image(produtos[leilao], scale=(0.1, 0.1))
    buy.add.label('Lance Mínimo: R$' + precoProd[leilao], font_color=green, font_name='Impact', selection_color=green)
    buy.add.label('')
    buy.add.label('')
    buy.add.label('')
    buy.add.button('Comprar', darLance, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    buy.add.label('')
    buy.add.button('Passar', compraProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    buy.add.label('')
    buy.add.label('Seu dinheiro: R$' + money, font_color=green, font_name='Impact', selection_color=green)
    buy.mainloop(screen)
    pass

def vender():
    if len(prodCompred) <= 0:
        semProd()
    else:
        sell = pygame_menu.Menu('Produtos de ' + nome, 800, 600, center_content=True, onclose=takeHome, columns=3, rows=3, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
        sell.add.label('')
        sell.add.button('Anterior', prevV, background_color=white, font_color=black, font_name='Impact', selection_color=black)
        sell.add.label('')
        sell.add.image(prodCompred[i], scale=(0.2, 0.2))
        sell.add.label('Preço: R$' + vProdCompred[i], font_color=green, font_name='Impact', selection_color=green)
        sell.add.button('Vender', makeSell, background_color=white, font_color=black, font_name='Impact', selection_color=black)
        sell.add.label('')
        sell.add.button('Próximo', proxV, background_color=white, font_color=black, font_name='Impact', selection_color=black)
        sell.add.label('')
        sell.mainloop(screen)
    pass

def semProd():
    semProd = pygame_menu.Menu('Produtos de ' + nome, 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    semProd.add.label("Você ainda não possui Produtos", font_color=green, font_name='Impact', selection_color=green)
    semProd.add.label('')
    semProd.add.button('Comprar Produtos', compraProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    semProd.mainloop(screen)
    pass

def darLance():
    lance = pygame_menu.Menu('Dar Lance', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    lance.add.label('Digite o Valor do seu Lance e pressione \"Enter\"', font_color=green, font_name='Impact', selection_color=green)
    lance.add.text_input(title='R$', copy_paste_enable=False, input_type=pygame_menu.locals.INPUT_FLOAT, onreturn=makePurchase).set_font(font[0], font[1], font[2], font[3], font[4], font[5], background_color='#000000')
    lance.add.label('')
    lance.add.label('')
    lance.add.label('Seu dinheiro: R$' + money, font_color=green, font_name='Impact', selection_color=green).set_alignment(pygame_menu.locals.ALIGN_RIGHT)
    lance.mainloop(screen)
    pass

def lanceMtGrande():
    bigLance = pygame_menu.Menu('Dar Lance', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    bigLance.add.label('Digite o Valor do seu Lance e pressione \"Enter\"', font_color=green, font_name='Impact', selection_color=green)
    bigLance.add.label('Você deve ter a quantia do lance para que ele possa ser feito!', font_color=(255, 0, 0), font_size=20, font_name='Impact', selection_color=(255, 0, 0))
    bigLance.add.text_input(title='R$', copy_paste_enable=False, input_type=pygame_menu.locals.INPUT_FLOAT, onreturn=makePurchase).set_font(font[0], font[1], font[2], font[3], font[4], font[5], background_color='#000000')
    bigLance.add.label('')
    bigLance.add.label('')
    bigLance.add.label('Seu dinheiro: R$' + money, font_color=green, font_name='Impact', selection_color=green).set_alignment(pygame_menu.locals.ALIGN_RIGHT)
    bigLance.mainloop(screen)
    pass

def lanceMin():
    minLance = pygame_menu.Menu('Dar Lance', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    minLance.add.label('Digite o Valor do seu Lance e pressione \"Enter\"', font_color=green, font_name='Impact', selection_color=green)
    minLance.add.label('O lance tem que ser maior do que o valor mínimo apresentado junto ao produto!', font_color=(255, 0, 0), font_size=20, font_name='Impact', selection_color=(255, 0, 0))
    minLance.add.text_input(title='R$', copy_paste_enable=False, input_type=pygame_menu.locals.INPUT_FLOAT, onreturn=makePurchase).set_font(font[0], font[1], font[2], font[3], font[4], font[5], background_color='#000000')
    minLance.add.label('')
    minLance.add.label('')
    minLance.add.label('Seu dinheiro: R$' + money, font_color=green, font_name='Impact', selection_color=green).set_alignment(pygame_menu.locals.ALIGN_RIGHT)
    minLance.mainloop(screen)
    pass

def prodNotGet():
    notGet = pygame_menu.Menu('Produto Nao Adquirido', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    notGet.add.label('O produto não foi adquirido, pois seu lance não foi o mais alto', font_color=(255, 0, 0), font_name='Impact', selection_color=(255, 0, 0))
    notGet.add.label('')
    notGet.add.button('Tentar em outro produto', compraProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    notGet.mainloop(screen)
    pass

def prodGet():
    notGet = pygame_menu.Menu('Produto Nao Adquirido', 800, 600, center_content=True, onclose=takeHome, theme=pygame_menu.themes.Theme(background_color=menuBG, cursor_color=green,  title_close_button=True, title_background_color=black, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, title_font=pygame_menu.font.FONT_8BIT, title_font_color=green))
    notGet.add.label('Parabéns, você comprou o produto!!', font_color=green, font_name='Impact', selection_color=green)
    notGet.add.label('')
    notGet.add.button('Ver produtos comprados', verProd, background_color=white, font_color=black, font_name='Impact', selection_color=black)
    notGet.mainloop(screen)
    pass


def takeHome():
    home(nome)
    pass

def prox():
    global i
    i+=1
    if len(prodCompred) > i:
        verProd()
    else:
        i=0
        verProd()
    pass

def prev():
    global i
    i-=1
    if i > -1:
        verProd()
    else:
        i=len(prodCompred)-1
        verProd()
    pass

def makePurchase(value):
    global money
    if value >= float(precoProd[leilao]):
        if random.choice(getProd) != 0:
            if value <= float(money):
                prodCompred.append(produtos[leilao])
                if leilao == 1 or leilao == 3:
                    vProdCompred.append('00.00')
                else:
                    if random.choice(wl) == 'w':
                        sp= value + random.choice(sellPrice)
                        vProdCompred.append(str(sp))
                    else:
                        sp= value - random.choice(sellPrice)
                        vProdCompred.append(str(sp))
                nm = float(money) - float(value)
                money = str(nm)
                prodGet()
            else:
                lanceMtGrande()
        else:
            prodNotGet()
    else:
        lanceMin()
    pass

def proxV():
    global i
    i+=1
    if len(prodCompred) > i:
        vender()
    else:
        i=0
        vender()
    pass

def prevV():
    global i
    i-=1
    if i > -1:
        vender()
    else:
        i=len(prodCompred)-1
        vender()
    pass

def makeSell():
    global money
    nm = float(money) + float(vProdCompred[i])
    money = str(nm)
    prodCompred.remove(prodCompred[i])
    vProdCompred.remove(vProdCompred[i])
    takeHome()
    pass

# importando a função LISTENER da lib pynput para ler as entradas do KEYBOARD
from pynput.keyboard import Listener
    
# lista de teclas especiais
special_keys = ['Key.esc', 'Key.tab', 'Key.caps_lock', 'Key.shift', 'Key.ctrl_l',
                'Key.cmd', 'Key.alt_l', 'Key.ctrl_l', 'Key.alt_r', 'Key.shift_r', 
                'Key.enter', 'Key.backspace', 'Key.delete', 'Key.home', 'Key.page_up', 
                'Key.page_down', 'Key.end', 'Key.f1', 'Key.f2', 
                'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 
                'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12', 
                'Key.print_screen', 'Key.pause', 'Key.space', 'Key.left', 'Key.right',
                'Key.up', 'Key.down']


# função para imprimir as teclas digitadas
def get_key(key):
    key = str(key)

    # nesse if, as teclas especiais são formatadas entre <>
    if(key in special_keys):
        print(f'<{key}>')

    # classifica as entradas na num board, "traduz" a tabela ascii     
    elif (key == '<96>'):
        print("'0'")
    
    elif (key == '<97>'):
        print("'1'")
    
    elif (key == '<98>'):
        print("'2'")
    
    elif (key == '<99>'):
        print("'3'")
    
    elif (key == '<100>'):
        print("'4'")
    
    elif (key == '<101>'):
        print("'5'")
    
    elif (key == '<102>'):
        print("'6'")
    
    elif (key == '<103>'):
        print("'7'")
    
    elif (key == '<104>'):
        print("'8'")
    
    elif (key == '<105>'):
        print("'9'")
    
    elif (key == '<110>'):
        print("','") 
    
    # caso o botão power seja acionado
    elif (key == '<255>'):
        print("'Power'")
        
    # mostra a tecla digitada caso não seja uma tecla especial ou num board
    else:
        print(key)


# executa o programa e obtém as teclas
with Listener(on_press = get_key) as listen:
    listen.join() 


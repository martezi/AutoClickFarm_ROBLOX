import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

ativo = False

def autoclick():
    global ativo

    teclado = keyboard.Controller()

    while True:
        if ativo:

            teclado.press('1')
            teclado.release('1')
            time.sleep(1)

            teclado.press('2')
            teclado.release('2')
            time.sleep(1)

            teclado.press('3')
            teclado.release('3')
            time.sleep(1)

            teclado.press('4')
            teclado.release('4')

            mouse.click(Button.left)

            time.sleep(1)

        else:
            time.sleep(0.1)


def alternar(tecla):
    global ativo

    try:
        if tecla.char.lower() == 'g':
            ativo = not ativo

            if ativo:
                print("Autoclick: ATIVADO")
            else:
                print("Autoclick: DESATIVADO")

    except AttributeError:
        pass

threading.Thread(target=autoclick, daemon=True).start()

print("G = ativar/desativar")
print("ESC = fechar")

with keyboard.Listener(
    on_press=alternar
) as listener:
    listener.join()
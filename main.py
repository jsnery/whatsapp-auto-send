import subprocess
from pyautogui import hotkey
from time import sleep


m = open('msg.txt', encoding='utf-8')
msg = m.read().replace('\n', '%0A').replace(' ', '%20')
m.close()


def send_msg(contato: str | int, msg: str):
    def hotkey_tab(x):
        for i in range(x):
            hotkey('tab')

    wpp_api = f"https://api.whatsapp.com/send?phone={contato}&text={msg}"
    cmd = f'cmd /c start chrome "{wpp_api}" --new-window --start-maximized'
    subprocess.Popen(cmd, shell=True)

    sleep(5)
    hotkey_tab(8)
    hotkey('enter')
    sleep(2)
    hotkey_tab(2)
    hotkey('enter')
    sleep(15)
    hotkey('enter')
    sleep(1)
    hotkey('ctrl', 'w')


if __name__ == '__main__':
    send_msg(5579999068342, msg)

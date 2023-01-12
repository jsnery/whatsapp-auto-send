import webbrowser
import pyautogui

contato = 5579999068342
msg = f"https://api.whatsapp.com/send?phone={contato}&text=Sua%20assinatura%20Expirou%20%E2%9A%A0%EF%B8%8F%0A%0A%F0%9F%92%B2%20Mensal:%20R$35,00%0A%F0%9F%92%B2%20Bimensal:%20R$60,00%0A%F0%9F%92%B2%20Trimestral:%20R$85,00%0A%F0%9F%92%B2%20Semestral:%20R$160,00%0A%F0%9F%92%B2%20Anual:%20R$300,00%0A%0A%F0%9F%92%B5%20Pix:%2008323217530"

webbrowser.open(msg, new=2)
pyautogui.press

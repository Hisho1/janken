import webbrowser , pyautogui, tkinter as tk
from time import sleep

def send_message():

    number = box.get()
    message = box2.get()
    times = int(box3.get())

    if number == "" or message == "" or times == "": return
    
    webbrowser.open('https://web.whatsapp.com/send?phone='+number)
    sleep(10)
    for i in range(times):
        pyautogui.write(message)
        pyautogui.press("enter")
    

window = tk.Tk()
window.title("What'Spam")
window.geometry("300x200")
window.configure(bg="black")
window.resizable(False,False)

label1 = tk.Label(window,bg="black",fg="white", text="phone number")
label1.place(x=20, y=20)  
box = tk.Entry(window)
box.place(x=20 ,y=40)

label2 = tk.Label(window,bg="black",fg="white", text="message")
label2.place(x=20, y=60)
box2 = tk.Entry(window)
box2.place(x=20, y=80)

label2 = tk.Label(window,bg="black",fg="white", text="repeat message")
label2.place(x=150, y=60)
box3 = tk.Entry(window, width=4)
box3.place(x=200, y=80)

button = tk.Button(window,width=10, text="Send",bg="red",fg="white", command=send_message)
button.place(x=20, y=120)
window.mainloop()
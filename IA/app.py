from tkinter import *
import webbrowser


def open_eboo_channel():
    webbrowser.open_new('https://www.youtube.com/watch?v=-vqL3vdlVzs')


window = Tk()

window.config(background='#41B77F')
window.title('Mon super appli')
window.geometry("1080x720")
window.minsize(480, 360)

# frame 1
frame = Frame(window, bg='#41B77F')

label = Label(frame, text="Welcome to my new application", font=('Courrier', 40), bg='#41B77F', fg='white')
label.pack(expand=YES)

label_susbtitle = Label(frame, text="Hi, it s by eboo", font=('Courrier', 25), bg='#41B77F', fg='white')
label_susbtitle.pack(expand=YES)

yt_button = Button(frame, text="Ouvrir Youtube", font=('Courrier', 25), bg='white', fg='#41B77F',
                   command=open_eboo_channel)
yt_button.pack(pady=25, fill=X)

frame.pack(side=LEFT, padx=30, pady=30)
""" 
bouton = Button(window, text="Fermer", command=window.quit)
bouton.pack()
# liste

liste = Listbox(window, bg='#41B77F')
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

"""
window.mainloop()

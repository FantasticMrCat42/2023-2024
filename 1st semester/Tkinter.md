# Tkinter #

today in class we worked with Tkinter python library wich can be used to create GUIs. in class I followed the video on creating a simple inerface for a calculater. we combined this with the lamda function wich made the prosses easier. in the final last year there was a lambda example that we did not understand and confused multiple people.

```
from tkinter import *

window = Tk()

label_1 = Label(window, text= "first number")
label_2 = Label(window, text= "second number")
label_3 = Label(window, text= "result number")

field_1 = Entry()
field_2 = Entry()
field_3 = Entry()


label_1.place(x=100,y=50)
field_1.place(x=250,y=50)

label_2.place(x=100,y=100)
field_2.place(x=250,y=100)

label_3.place(x=100,y=200)
field_3.place(x=250,y=200)

button_1 = Button(window, text = 'Add', command= lambda :add(field_1.get(), field_2.get(), field_3))
button_2 = Button(window, text = 'Subtract', command= lambda :sub(field_1.get(), field_2.get(), field_3))

button_1.place(x=100,y=150)
button_2.place(x=250,y=150)

def add(num_1, num_2, result_field):
  result_field.delete(0,'end')
  result = int(num_1) + int(num_2)
  result_field.insert(END, str(result))

def sub(num_1, num_2, result_field):
  result_field.delete(0,'end')
  result = int(num_1) - int(num_2)
  result_field.insert(END, str(result))

window.title("Intro to Tkinter")
window.geometry("600x300")
window.mainloop()
```

afterwards we experimented with diferent drawing programs. I asume we will be using this as insperation next class.
<img width="1227" alt="Screen Shot 2023-10-30 at 2 20 47 PM" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/62b5bd2e-19b7-40e7-b1b7-56424aeb8d29">


from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

i = w.create_line(0,0,300,200,fill="red")
w.coords(i,0,0,300,100) # 좌표 변경
w.itemconfig(i,fill="blue") # 색상 변경

#w.delete(i) # 삭제
#w.delete(ALL) # 모든 항목 삭제
window.mainloop()

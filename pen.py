#coding=utf-8

from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

#窗口宽度和高度
win_width=900
win_height=450

class Application(Frame):
    def __init__(self, master=None, bgcolor="#000000"):
        super().__init__(master)
        self.master = master
        self.bgcolor=bgcolor
        self.x = 0
        self.y = 0
        self.fgcolor = "#ff0000"
        self.lastDraw = 0                  #最后绘制图形的ID
        self.startDrawFlag = False         #
        self.pack()
        self.createWidget()

    def createWidget(self):
        #创建矩形区域
        self.drawpad = Canvas(root,width=win_width,height=win_height*0.9,bg=self.bgcolor)
        self.drawpad.pack()

        #创建按钮
        btn_start = Button(root, text="开始", name="start")
        btn_start.pack(side="left",padx="10")
        btn_pen = Button(root, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(root, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(root, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_erasor = Button(root, text="橡皮擦", name="erasor")
        btn_erasor.pack(side="left", padx="10")
        btn_line = Button(root, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(root, text="箭头", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(root, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")


        #事件处理
        btn_pen.bind_class("Button","<1>",self.eventManager)
        self.drawpad.bind("<ButtonRelease-1>",self.stopDraw)


    def eventManager(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawpad.bind("<B1-Motion>",self.myline)
    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0


    def myline(self,event):
        self.drawpad.delete(self.lastDraw)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y


        self.lastDraw = self.drawpad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)

if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width)+"x"+str(win_height)+"+200+300")
    root.title("百战程序员画图软件")
    app = Application(master=root)
    root.mainloop()
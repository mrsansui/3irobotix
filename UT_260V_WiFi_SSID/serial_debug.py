import serial.tools.list_ports
import serial
import tkinter
from tkinter import END, ttk
import datetime
import threading


class moudbustk():

    def __init__(self, tk):

        self.tk = tk
        self.tk.title("串口工具")
        self.tk.geometry("600x380")
        self.tk.resizable(0, 0)
        self.tk.configure(background='ghostwhite')

        port_list = list(serial.tools.list_ports.comports())
        self.ser_port1 = []
        for i in port_list:
            port = list(i)

            self.ser_port1.append(port[0])
        self.serial_yu = 1
        self.while_all = 1
        self.page_one()

    def page_one(self):
        self.pageone = tkinter.Frame(self.tk)
        self.pageone.place(x=10, y=5, anchor="nw")
        but1 = tkinter.Label(self.pageone, text="COM:").grid(row=0, column=0)
        self.name = tkinter.StringVar()
        nametntry = ttk.Combobox(self.pageone, width=6, textvariable=self.name)
        # print(self.ser_port1)
        nametntry['values'] = self.ser_port1
        nametntry.grid(row=0, column=1)
        tkinter.Label(self.pageone, text="波特率:").grid(row=0, column=2)
        self.ent = tkinter.Entry(self.pageone, width=15)
        self.ent.insert(0, '4800')
        self.ent.grid(row=0, column=3)
        self.bu_name = tkinter.StringVar()
        self.bu_name.set('连接')
        tkinter.Button(self.pageone, textvariable=self.bu_name, command=self.link_com, width=5, ).grid(row=0, column=4)
        self.la_name = tkinter.StringVar()
        self.label_1 = tkinter.Label(self.pageone, textvariable=self.la_name).grid(row=0, column=5)

        self.page_two = tkinter.Frame(self.tk)
        self.page_two.place(x=10, y=35, anchor="nw")
        tkinter.Label(self.page_two, text="数据：").grid(row=0, column=0)
        self.ent1 = tkinter.Entry(self.page_two, width=45)
        self.ent1.grid(row=0, column=1)
        tkinter.Button(self.page_two, text="发送", command=self.send_data, width=5, ).grid(row=0, column=7)
        tkinter.Button(self.page_two, text="清空接收区", command=self.clear_recv, width=9, ).grid(row=0, column=8)
        self.page_three = tkinter.Frame(self.tk)
        self.page_three.place(x=10, y=75, anchor="nw")
        tkinter.Label(self.page_three, text="接收数据:").grid(row=0, column=0)
        self.text = tkinter.Text(self.page_three, width=80, height=35)
        self.text.grid(row=1, column=0)
        self.text.tag_config("tag", foreground="red")
        self.text.tag_config("tag1", foreground="blue")

    def clear_recv(self):
        self.text.delete(1.0, END)

    def link_com(self):
        try:
            if self.serial_yu == 1:
                self.ser = serial.Serial(  # 下面这些参数根据情况修改
                    port=self.name.get(),
                    baudrate=self.ent.get(),
                    parity=serial.PARITY_EVEN,
                    timeout=0.2,
                    stopbits=serial.STOPBITS_ONE,  # 停止位
                    bytesize=serial.EIGHTBITS  # 数据位8位
                )
                self.la_name.set('连接成功')
                self.bu_name.set("关闭")
                self.serial_yu = 0
                thread = threading.Thread(target=self.recv_data)
                thread.setDaemon(True)
                thread.start()

            else:
                self.ser.close()
                self.serial_yu = 1
                self.bu_name.set('连接')
                self.la_name.set('关闭连接')
        except:
            self.la_name.set("无法连接")

    def send_data(self):
        try:
            self.la_name.set("")
            list = []
            data = self.ent1.get().split(" ")
            for i in data:
                list.append(int(i, 16))
            print(list)
            self.ser.write(bytes(list))
            self.text.insert(END, "%s 发送：%s\n" % (datetime.datetime.now(), self.hexShow(list)), "tag1")

        except ValueError:
            self.la_name.set("未填入数据")
        except AttributeError:
            self.la_name.set("未打开连接")

    def recv_data(self):
        x = 0
        while 1:
            data = self.ser.readall()
            if len(data) == 0:
                continue
            return_data = self.hexShow(data)
            self.text.insert(END, "%s 接收：%s\n" % (datetime.datetime.now(), return_data), "tag")
            x += 1
            if x == 35:
                self.text.delete(1.0, END)
                x = 0

    def hexShow(self, argv):  # 接收数据格式调整
        result = ''
        hlen = len(argv)
        for i in range(hlen):
            hvol = argv[i]
            hhex = hex(hvol)[2:]

            result += hhex.upper() + ' '
        return result

    def file_writer(self, data):  # 记录数据
        file = open('C:/Users/Administrator/Desktop/协议.txt', 'a')
        file.write(data)
        file.close()


if __name__ == "__main__":
    tk = tkinter.Tk()
    moudbustk(tk)
    tk.mainloop()
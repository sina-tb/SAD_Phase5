import tkinter as tk
from tkinter import ttk
import TkinterBaseInterface as Base

class Command:
    def __init__(self, header, body):
        self._header = header # str
        self._body = body # dict of dicts

class TkinterBaseInterface:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Health Service")

        style = ttk.Style()
        style.configure("BW.TLabel", background="pink")

        homePage = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")
        packages = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")
        fillPrerequisites = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")
        successfulMessage = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")

        self.pages = [homePage, packages, fillPrerequisites, successfulMessage]
        self.my_command = Command(header='', body={'options':{}})

    def mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def show_page(self, page):
        for p in self.pages:
            p.pack_forget()

        page.pack()
    
    def home_page_handler(self):
        self.show_page(self.pages[0])

        label_home = tk.Label(self.pages[0], text="Welcome to Home Page", font=("Comic Sans MS", 18), fg="purple", bg= "pink")
        label_home.pack(side="top", padx=10, pady=10)

        button1 = tk.Button(self.pages[0], text="Request New Package", font=("Comic Sans MS", 11, "bold"), fg= "blue", bg= "pink" , command=lambda: self.update_command('request_new_package',{}) )
        button1.pack()

        button2 = tk.Button(self.pages[0], text="Show Last Status of Requests",font=("Comic Sans MS", 11, "bold") ,fg= "orange", bg= "pink" , command=lambda: self.update_command('show_last_status_of_requests',{}))
        button2.pack()

        button3 = tk.Button(self.pages[0], text="Profile", font=("Comic Sans MS", 11, "bold") ,fg= "green", bg= "pink", command=lambda: self.update_command('show_profile',{}))
        button3.pack()

        button4 = tk.Button(self.pages[0], text="Logout",font=("Comic Sans MS", 11, "bold") ,fg= "black", bg= "pink",  command=lambda: self.update_command("logout",{}))
        button4.pack()

    def package_page_handler(self, list_of_packages):
        self.show_page(self.pages[1])

        label_package = tk.Label(self.pages[1], text="Select a Package:",font=("Comic Sans MS", 18), fg="purple", bg= "pink")
        label_package.pack()
        v = tk.IntVar()

        def ShowChoice():
            print(v.get())

        for x in range(len(list_of_packages)):
            tk.Radiobutton(self.pages[1], text=list_of_packages[x], font=("Comic Sans MS", 11, "bold"), fg= "blue", bg= "pink" , variable=v, command=ShowChoice,value= x).pack(anchor=tk.W)


        button1 = tk.Button(self.pages[1], text="Submit", font=("Comic Sans MS", 11, "bold"), fg= "green", bg= "pink" , command=lambda: self.update_command("fill_prerequisites", {}))
        button1.pack()

        button2 = tk.Button(self.pages[1], text="Back to Home Page", font=("Comic Sans MS", 11, "bold"), fg= "red", bg= "pink" , command=lambda: self.update_command("return_to_home",{}))
        button2.pack()

    def show_prerequisites(self, list_of_preRequitsites):
        scrollbar = tk.Scrollbar(self.pages[2])
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(self.pages[2], bg="pink", yscrollcommand=scrollbar.set,  width=100, height=100)
        canvas.pack()

        scrollbar.config(command=canvas.yview)

        canvas.bind_all("<MouseWheel>", self.mouse_wheel)

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame)

        for i in range(len(list_of_preRequitsites)):
            label = tk.Label(content_frame, text= list_of_preRequitsites[i],font=("Comic Sans MS", 11), fg="black")
            label.pack()
            entry_name = tk.Entry(content_frame,font=("Comic Sans MS", 11), fg="grey", bg= "white")
            entry_name.pack()

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


    def prerequisites_page_handler(self, preRequisites):
        self.show_page(self.pages[2])

        label_pre = tk.Label(self.pages[2], text="Please Fill Prerequisites",font=("Comic Sans MS", 18), fg="purple", bg= "pink")
        label_pre.pack()

        self.show_prerequisites(preRequisites)

        button1 = tk.Button(self.pages[2], text="Submit",font=("Comic Sans MS", 11), fg="green", bg= "pink", command=lambda: self.update_command("show_message",{}))
        button1.pack()

        button2 = tk.Button(self.pages[2], text="Back to Package Page",font=("Comic Sans MS", 11), fg="red", bg= "pink", command=lambda: self.update_command("return_to_select_package",{}))
        button2.pack()

    def successful_message_page(self,message):
        self.show_page(self.pages[3])

        label_success = tk.Label(self.pages[3], text="Your Package Saved Successfully",font=("Comic Sans MS", 18), fg="purple", bg= "pink")
        label_success.pack()

        label_success = tk.Label(self.pages[3], text=message ,font=("Comic Sans MS", 11), fg="black", bg= "pink")
        label_success.pack()

        button1 = tk.Button(self.pages[3], text="Back to Home Page",font=("Comic Sans MS", 11), fg="red", bg= "pink", command=lambda: self.update_command("return_to_home",{}))
        button1.pack()
            

    def update_command(self,header, body):
        self.my_command = (header, body)

    def get_command(self):
        return self.my_command

    
# list_of_packages = ["first", "second", "third"]
# preRequisites = ["blood type", "gender", "Your pre visit tests","this","that","those"]
# message = "Cost : 200$\nSupporter : Ali Payande\nTracking Number : 80101021312\n"




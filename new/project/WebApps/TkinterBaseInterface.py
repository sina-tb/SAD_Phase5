import tkinter as tk
from tkinter import ttk

class Command:
    def __init__(self, header, body):
        self._header = header # str
        self._body = body # dict of dicts

class TkinterBaseInterface:

    def __init__(self, sys):
        self.root = tk.Tk()
        self.root.title("Health Service")
        self._sys = sys

        style = ttk.Style()
        style.configure("BW.TLabel", background="pink")

        homePage = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")
        packages = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")
        fillPrerequisites = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")
        successfulMessage = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")

        self.pages = [homePage, packages, fillPrerequisites, successfulMessage]

    def mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def show_page(self, page):
        for p in self.pages:
            p.pack_forget()

        page.pack()
    
    def home_page_handler(self):
        self.pages[0] = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")

        self.show_page(self.pages[0])

        label_home = tk.Label(self.pages[0], text="Welcome to Home Page", font=("Palatino", 18), fg="purple", bg= "pink")
        label_home.pack(side="top", padx=10, pady=10)

        button1 = tk.Button(self.pages[0], text="Request New Package", font=("Palatino", 11, "bold"), fg= "blue", bg= "pink" , command=lambda: self.update_command('request_new_package',{}) )
        button1.pack()

        button2 = tk.Button(self.pages[0], text="Show Last Status of Requests",font=("Palatino", 11, "bold") ,fg= "orange", bg= "pink" , command=lambda: self.update_command('show_last_status_of_requests',{}))
        button2.pack()

        button3 = tk.Button(self.pages[0], text="Profile", font=("Palatino", 11, "bold") ,fg= "green", bg= "pink", command=lambda: self.update_command('show_profile',{}))
        button3.pack()

        button4 = tk.Button(self.pages[0], text="Logout",font=("Palatino", 11, "bold") ,fg= "black", bg= "pink",  command=lambda: self.update_command("logout",{}))
        button4.pack()

    def package_page_handler(self, list_of_packages):
        list_of_packages = eval(list_of_packages)
        self.pages[1] = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200,style="BW.TLabel")

        self.show_page(self.pages[1])

        label_package = tk.Label(self.pages[1], text="Select a Package:",font=("Palatino", 18), fg="purple", bg= "pink")
        label_package.pack()
        v = tk.IntVar()

        def ShowChoice():
            print(v.get())

        for package in list_of_packages:
            tk.Radiobutton(self.pages[1], text=package['name'], font=("Palatino", 18, "bold"), fg= "blue", bg= "pink" , variable=v, command=ShowChoice,value=package['id']).pack(anchor=tk.W)

        button1 = tk.Button(self.pages[1], text="Submit", font=("Palatino", 11, "bold"), fg= "green", bg= "pink" , command=lambda: self.update_command("fill_prerequisites", {'package_id' : v.get()}))
        button1.pack()

        button2 = tk.Button(self.pages[1], text="Back to Home Page", font=("Palatino", 11, "bold"), fg= "red", bg= "pink" , command=lambda: self.update_command("return_to_home",{}))
        button2.pack()

    def show_prerequisites(self, list_of_preRequitsites):
        scrollbar = tk.Scrollbar(self.pages[2])
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(self.pages[2], bg="pink", yscrollcommand=scrollbar.set,  width=180, height=200)
        canvas.pack()

        scrollbar.config(command=canvas.yview)

        canvas.bind_all("<MouseWheel>", self.mouse_wheel)

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame)

        for i in range(len(list_of_preRequitsites)):
            label = tk.Label(content_frame, text= list_of_preRequitsites[i],font=("Palatino", 11), fg="black")
            label.pack()
            entry_name = tk.Entry(content_frame,font=("Palatino", 11), fg="grey", bg= "white")
            entry_name.pack()

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


    def prerequisites_page_handler(self, preRequisites):
        preRequisites = eval(preRequisites)
        print(preRequisites)
        self.pages[2] = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")

        self.show_page(self.pages[2])

        label_pre = tk.Label(self.pages[2], text="Please Fill Prerequisites",font=("Palatino", 18), fg="purple", bg= "pink")
        label_pre.pack()

        self.show_prerequisites(preRequisites)

        button1 = tk.Button(self.pages[2], text="Submit",font=("Palatino", 11), fg="green", bg= "pink", command=lambda: self.update_command("show_message",{}))
        button1.pack()

        button2 = tk.Button(self.pages[2], text="Back to Package Page",font=("Palatino", 11), fg="red", bg= "pink", command=lambda: self.update_command("return_to_select_package",{}))
        button2.pack()

    def successful_message_page(self,message):
        self.pages[3] = ttk.Frame(self.root, padding=0, relief="groove", borderwidth=200, style="BW.TLabel")

        self.show_page(self.pages[3])

        label_success = tk.Label(self.pages[3], text="Your Package Saved Successfully",font=("Palatino", 18), fg="purple", bg= "pink")
        label_success.pack()

        label_success = tk.Label(self.pages[3], text=message ,font=("Palatino", 11), fg="black", bg= "pink")
        label_success.pack()

        button1 = tk.Button(self.pages[3], text="Back to Home Page",font=("Palatino", 11), fg="red", bg= "pink", command=lambda: self.update_command("return_to_home",{}))
        button1.pack()
            

    def update_command(self,header, body):
        self._sys.run_command(Command(header=header,
                                      body=body))

    
list_of_packages = ["first", "second", "third"]
preRequisites = ["blood type", "gender", "Your pre visit tests","this","that","those"]
message = "Cost : 200$\nSupporter : Ali Payande\nTracking Number : 80101021312\n"



# examine the pages
# hey = TkinterBaseInterface()
# hey.prerequisites_page_handler(preRequisites)
# hey.successful_message_page(message)
# hey.package_page_handler(list_of_packages)
# hey.home_page_handler()
# hey.root.mainloop()
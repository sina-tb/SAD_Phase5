import tkinter as tk
from tkinter import ttk
import TkinterBaseInterface as Base


def mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def show_page(page):
    for p in pages:
        p.pack_forget()

    page.pack()


def home_page_handler(homePage, root):

    label_home = tk.Label(homePage, text="Welcome to Home Page")
    label_home.pack()

    button1 = tk.Button(homePage, text="Request New Package", command=lambda: show_page(packages))
    button1.pack()

    button2 = tk.Button(homePage, text="Show Last Status of Requests", command=lambda: show_page(homePage))
    button2.pack()

    button3 = tk.Button(homePage, text="Profile", command=lambda: show_page(homePage))
    button3.pack()

    button4 = tk.Button(homePage, text="Logout", command=lambda: root.destroy())
    button4.pack()


def package_page_handler(packages, list_of_packages):
    
    label_package = tk.Label(packages, text="Select a Package:")
    label_package.pack()
    v = tk.IntVar()

    def ShowChoice():
        print(v.get())

    for x in range(len(list_of_packages)):
        tk.Radiobutton(packages, text=list_of_packages[x], padx = 20, variable=v, command=ShowChoice,value= x).pack(anchor=tk.W)

    # Set initial selection

    button1 = tk.Button(packages, text="Submit", command=lambda: show_page(fillPrerequisites))
    button1.pack()

    button2 = tk.Button(packages, text="Back to Home Page", command=lambda: show_page(homePage))
    button2.pack()

def show_prerequisites(fillPrerequisites, list_of_preRequitsites):
    # Create a scrollbar
    scrollbar = tk.Scrollbar(fillPrerequisites)
    scrollbar.pack(side="right", fill="y")

    # Create a canvas
    canvas = tk.Canvas(fillPrerequisites, bg="white", yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    # Configure the scrollbar to work with the canvas
    scrollbar.config(command=canvas.yview)

    # Bind the mouse wheel event to the canvas
    canvas.bind_all("<MouseWheel>", mouse_wheel)

    # Create a frame inside the canvas for the content
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Add content to the frame (you can add any widgets here)
    for i in range(len(list_of_preRequitsites)):
        label = tk.Label(content_frame, text= list_of_preRequitsites[i])
        label.pack()
        entry_name = tk.Entry(content_frame)
        entry_name.pack()

    # Update the canvas scroll region
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def prerequisites_page_handler(fillPrerequisites, preRequisites):

    label_pre = tk.Label(fillPrerequisites, text="Please Fill Prerequisites")
    label_pre.pack()

    show_prerequisites(fillPrerequisites, preRequisites)

    button1 = tk.Button(fillPrerequisites, text="Submit", command=lambda: show_page(successfulMessage))
    button1.pack()

    button2 = tk.Button(fillPrerequisites, text="Back to Package Page", command=lambda: show_page(packages))
    button2.pack()


def successful_message_page(successfulMessage):

    label_success = tk.Label(successfulMessage, text="successful message")
    label_success.pack()

    button1 = tk.Button(successfulMessage, text="Back to Home Page", command=lambda: show_page(homePage))
    button1.pack()




# Create the main window
root = tk.Tk()
root.title("Health Service")

# Create the pages as frames
list_of_packages = ["first", "second", "third"]
preRequisites = ["blood type", "gender", "feel good?", "beeeee"," bpppppppppp", "sssssssssssss","s","f","sf","sdf","sfd","sdfsdfs" ]
homePage = tk.Frame(root)
packages = tk.Frame(root)
fillPrerequisites = tk.Frame(root)
successfulMessage = tk.Frame(root)
pages = [homePage, packages, fillPrerequisites, successfulMessage]

home_page_handler(homePage, root)

package_page_handler(packages, list_of_packages)

prerequisites_page_handler(fillPrerequisites, preRequisites)

successful_message_page(successfulMessage)

#Initially show page 1

show_page(homePage)

# Start the tkinter event loop
root.mainloop()

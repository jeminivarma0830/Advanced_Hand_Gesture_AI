import tkinter as tk
def launch_gui():
    root = tk.Tk()
    root.title('AI Hand Gesture Control')
    root.geometry('900x600')
    tk.Label(root,text='AI Hand Gesture Control Dashboard',font=('Arial',20)).pack(pady=20)
    tk.Label(root,text='Production Ready Project Structure').pack()
    root.mainloop()

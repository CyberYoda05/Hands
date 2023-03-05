import tkinter as tk
from tkinter import ttk
class Settings:
    def __init__(self, gesture: object = "Null", Landmaks:object = "Null"):
        self.gesture = gesture
        self.landmaks = Landmaks
        self.is_open = False
        self.Stop = False
        #allows input of gesture and Landmarks
    def stop(self):
        self.Stop = True
    def scroll(self):
        self.scrollval = str(self.var.get())
        print(self.scrollval)
        # scroll bar
    def main(self):
        self.is_open = True
        gesture = self.gesture
        root = tk.Tk()
        root.title("settings")
        tabControl = ttk.Notebook(root)
        # creation of tabs

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)
        # adding the tabs to the GUI

        tabControl.add(tab1, text='Instructions')
        tabControl.add(tab2, text='speed')
        tabControl.add(tab3, text='Gesture shown')
        tabControl.add(tab4, text='landmark log')
        tabControl.add(tab5, text='stop program')
        tabControl.pack(expand=1, fill="both")
        # actually defining tabs values

        self.var = tk.DoubleVar(tab2)
        ttk.Label(tab1,#instructions
                  text='''
                  Instuctions
                  Thumbs up   -> increase volume
                  Thumbs down -> decrease volume
                  call me     -> opens youtube
                  stop        -> uses up arrow 
                  live long   -> tab button 
                  okay        -> presses windows button
                  fist        -> closes tab
                  rock        -> down arrow 
                  peice       -> enter key
                  ''').grid(column=0,
                            row=1,
                            padx=0,
                            pady=0, )
        # defines widgets
        Scala2 = tk.Scale(tab2, from_=10, to=40, variable=self.var)
        setvalue = tk.Button(master=tab2, text="Get Scale Value", command=self.scroll())
        setvalue.pack()
        Scala2.pack(padx=5, pady=5)
        stop_button = tk.Button(master=tab5, text="STOP", command=self.Stop)
        stop_button.pack()
        ttk.Label(tab3,
                  text=gesture).grid(column=0, row=1)


        ttk.Label(tab4,
                  text=self.landmaks).grid(column=0, row=1)
        # importing an icon
        root.iconbitmap("tools.ico")
        # tab usage
        root.mainloop()




if __name__ == "__main__":
    s = Settings()
    s.main()
    None

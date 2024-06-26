import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.frames = {}

        # Create three frames
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: parent.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: parent.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Back to Start Page",
                           command=lambda: parent.show_frame(StartPage))
        button.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Back to Start Page",
                           command=lambda: parent.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

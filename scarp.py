import tkinter as tk
import itertools

class LoadingAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading Animation")

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.logo = self.canvas.create_oval(150, 100, 250, 200, fill='blue')
        self.text = self.canvas.create_text(200, 250, text="Loading...", font=('Helvetica', 16))

        self.angle = itertools.cycle(range(360))
        self.animate()

    def animate(self):
        angle = next(self.angle)
        self.canvas.itemconfig(self.logo, start=angle, extent=270)  # Create a rotating effect
        self.root.after(50, self.animate)

root = tk.Tk()
app = LoadingAnimation(root)
root.mainloop()

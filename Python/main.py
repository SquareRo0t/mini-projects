import tkinter as tk
import time


def update_clock(label: tk.Label) -> None:
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock, label)


def create_clock_window() -> None:
    root = tk.Tk()
    root.title('Digital Clock')
    root.geometry('300x100')
    root.resizable(False, False)

    clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
    clock_label.pack(expand=True, fill='both')

    update_clock(clock_label)
    root.mainloop()


if __name__ == '__main__':
    create_clock_window()

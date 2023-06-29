from tkinter import *
import math

# ---------------------------- CONSTANTES ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

# ---------------------------- REINICIO ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Temporizador")
    check_marks.config(text="")
    start_button.config(state=NORMAL)  # Habilitar el botón "Iniciar"
    global repetitions
    repetitions = 0

# ---------------------------- TEMPORIZADOR ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1
    start_button.config(state=DISABLED)  # Desactivar el botón "Iniciar"
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text="Descanso", fg=RED)
    elif repetitions % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text="Descanso", fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text="Trabajo", fg=GREEN)


# ---------------------------- CUENTA REGRESIVA  ------------------------------- #
def count_down(count):
    # convertimos el contador numérico en formato de minutos-segundos
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # cambiamos el formato cuando sean menos de 10 segundos para mantener el doble digito (tipado dinámico)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repetitions/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)
# ---------------------------- CONFIGURACIÓN UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

top_label = Label(text="Temporizador", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
top_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highl...  elimina el bor del canvas
# x value and y value para centrar la imagen
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# OJO hay que corregir borde negro
start_button = Button(text="Iniciar", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reiniciar", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

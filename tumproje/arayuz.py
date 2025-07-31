from tkinter import *
from hesaplama import hesapla_bmi
from error import EmptyInputError, InvalidHeightError, InvalidWeightError

def arayuz():
    root = Tk()
    root.title("BMI Hesaplama Arayüzü")
    root.geometry("300x300")

    Label(root, text="BMI Hesaplamak için bilgilerinizi girin:").pack(pady=10)

    Label(root, text="Boy (cm):").pack()
    boy_entry = Entry(root)
    boy_entry.pack()

    Label(root, text="Kilo (kg):").pack()
    kilo_entry = Entry(root)
    kilo_entry.pack()

    sonuc_var = StringVar()
    sonuc_label = Label(root, textvariable=sonuc_var)
    sonuc_label.pack(pady=10)

    def hesapla():
        try:
            bmi = hesapla_bmi(boy_entry.get(), kilo_entry.get())
            sonuc_var.set(f"BMI: {bmi}")
        except EmptyInputError as e:
            sonuc_var.set(str(e))
        except InvalidHeightError as e:
            sonuc_var.set(str(e))
        except InvalidWeightError as e:
            sonuc_var.set(str(e))

    Button(root, text="Hesapla", command=hesapla).pack(pady=10)

    root.mainloop()

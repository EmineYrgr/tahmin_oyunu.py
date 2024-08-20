import tkinter as tk
import random

def tahmin_oyunu():
    def kontrol_et():
        tahmin = int(entry.get())
        if tahmin < gizli_sayi:
            sonuc_label.config(text="Daha yüksek bir sayı söylemelisin!")
        elif tahmin > gizli_sayi:
            sonuc_label.config(text="Daha düşük bir sayı söylemelisin!")
        else:
            sonuc_label.config(text=f"Tebrikler! {gizli_sayi} sayısını doğru tahmin ettiniz!")

    pencere = tk.Tk()
    pencere.title("Tahmin Oyunu")

    alt_sinir = 1
    ust_sinir = 100

    gizli_sayi = random.randint(alt_sinir, ust_sinir)

    label = tk.Label(pencere, text=f"{alt_sinir} ile {ust_sinir} arasında bir sayı tuttum. Tahmin edin:")
    label.pack()

    entry = tk.Entry(pencere)
    entry.pack()

    sonuc_label = tk.Label(pencere, text="")
    sonuc_label.pack()

    button = tk.Button(pencere, text="Tahmin Et", command=kontrol_et)
    button.pack()

    pencere.mainloop()

if __name__ == "__main__":
    tahmin_oyunu()

import tkinter as tk
from PIL import Image, ImageTk
import random
import requests
from io import BytesIO
import threading
import time

def move_window():
    """Déplace la fenêtre principale à une position aléatoire."""
    x = random.randint(0, root.winfo_screenwidth() - 200)
    y = random.randint(0, root.winfo_screenheight() - 100)
    root.geometry(f"200x100+{x}+{y}")

def on_hover(event):
    """Déplace la fenêtre principale et affiche une image à une position aléatoire."""
    move_window()
    show_image_popup()

def show_image_popup():
    """Affiche une image dans une fenêtre popup à une position aléatoire."""
    popup = tk.Toplevel(root)
    popup.title("Surprise !")
    
    # Taille et position aléatoire de la fenêtre popup
    popup_width, popup_height = 300, 300
    x = random.randint(0, root.winfo_screenwidth() - popup_width)
    y = random.randint(0, root.winfo_screenheight() - popup_height)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    
    # Télécharger et charger l'image depuis l'URL
    url = "https://sunbren.com/wp-content/uploads/2019/01/youhavebeenhacked.jpg"
    response = requests.get(url)
    response.raise_for_status()  # Vérifie si la requête a réussi
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((250, 250))  # Redimensionner l'image si nécessaire
    photo = ImageTk.PhotoImage(img)
    
    # Afficher l'image dans la fenêtre popup
    label = tk.Label(popup, image=photo)
    label.image = photo  # Nécessaire pour éviter que l'image soit supprimée par le garbage collector
    label.pack()

def prevent_close():
    """Empêche la fermeture de la fenêtre principale."""
    pass  # Ne fait rien quand on tente de fermer

def start_matrix_effect():
    """Lance une fenêtre avec un effet 'Matrix'."""
    matrix_window = tk.Toplevel(root)
    matrix_window.title("Matrix Effect")
    matrix_window.attributes('-fullscreen', True)  # Plein écran
    matrix_window.configure(bg='black')

    canvas = tk.Canvas(matrix_window, bg='black', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    columns = matrix_window.winfo_screenwidth() // 10
    drops = [0] * columns

    def draw_matrix():
        """Anime l'effet Matrix."""
        while True:
            for i in range(len(drops)):
                text = chr(random.randint(33, 126))  # Caractères ASCII aléatoires
                canvas.create_text(i * 10, drops[i] * 15, text=text, fill="green", font=("Courier", 12))
                if drops[i] * 15 > matrix_window.winfo_screenheight() or random.random() > 0.95:
                    drops[i] = 0
                drops[i] += 1
            canvas.update()
            time.sleep(0.05)  # Réduisez pour accélérer l'animation

    def on_keypress(event):
        """Ferme la fenêtre Matrix uniquement si 'G' est pressé."""
        if event.keysym.lower() == 'g':
            matrix_window.destroy()

    # Bloquer les autres méthodes de fermeture
    matrix_window.protocol("WM_DELETE_WINDOW", prevent_close)
    matrix_window.bind("<Key>", on_keypress)

    # Utilisation d'un thread pour éviter que tkinter freeze
    threading.Thread(target=draw_matrix, daemon=True).start()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Fenêtre Troll")
root.geometry("200x100")

# Empêcher la fermeture par la croix
root.protocol("WM_DELETE_WINDOW", prevent_close)
start_matrix_effect()
# Création du bouton troll
btn_troll = tk.Button(root, text="Clique ici si tu peux !", command=start_matrix_effect)
btn_troll.pack(expand=True)

# Détecter le survol du bouton
btn_troll.bind("<Enter>", on_hover)

# Démarrage de la boucle principale
root.mainloop()

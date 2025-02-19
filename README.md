# Fenêtre Troll

Un script Python utilisant Tkinter pour créer une fenêtre "troll" qui se déplace de manière aléatoire, affiche des images surprises et lance un effet "Matrix" en plein écran.

## Fonctionnalités

- **Fenêtre mobile** : Se déplace aléatoirement à chaque survol du bouton.
- **Popup image** : Affiche une image surprise à un emplacement aléatoire.
- **Effet "Matrix"** : Affiche un effet Matrix en plein écran (fermeture uniquement avec la touche `G`).
- **Blocage de fermeture** : Empêche la fermeture normale des fenêtres.

## Prérequis

Assurez-vous d'avoir Python installé (à partir de la version 3.x) et installez les dépendances suivantes :

```bash
pip install pillow requests
```

## Utilisation

Exécutez simplement le script :

```bash
python script.py
```

## Explication du code

- **`move_window()`** : Déplace la fenêtre principale à une position aléatoire.
- **`on_hover(event)`** : Déplace la fenêtre et affiche une image surprise.
- **`show_image_popup()`** : Ouvre une popup avec une image depuis une URL.
- **`prevent_close()`** : Empêche la fermeture normale de la fenêtre.
- **`start_matrix_effect()`** : Lance un effet "Matrix" en plein écran.

## Capture d'écran

![Exemple](https://sunbren.com/wp-content/uploads/2019/01/youhavebeenhacked.jpg)

## Avertissement

Ce programme est un simple troll amusant et ne doit pas être utilisé de manière malveillante.

---

Amusez-vous bien ! 😈


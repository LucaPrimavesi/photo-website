import os
import json

def generate():
    # Cartella dove si trovano le immagini
    image_dir = "img"
    
    # Estensioni supportate
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    
    if not os.path.exists(image_dir):
        print(f"Errore: La cartella '{image_dir}' non esiste!")
        return

    # Legge i file nella cartella img
    files = [f for f in os.listdir(image_dir) if f.lower().endswith(valid_extensions)]
    
    # Ordina i file alfabeticamente (così le categorie sono raggruppate)
    files.sort()

    # Salva il file gallery.json
    with open("gallery.json", "w", encoding="utf-8") as f:
        json.dump(files, f, indent=2)

    print(f"Successo! {len(files)} immagini trovate e salvate in gallery.json")

if __name__ == "__main__":
    generate()

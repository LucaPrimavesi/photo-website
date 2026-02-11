import os
import json

def generate():
    image_dir = "img"
    # Supporta maiuscole e minuscole per le estensioni
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.JPG', '.JPEG', '.PNG')
    
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print(f"Creata cartella {image_dir}")

    # Legge i file ed evita file nascosti del sistema (come .DS_Store)
    files = [f for f in os.listdir(image_dir) if f.lower().endswith(valid_extensions) and not f.startswith('.')]
    
    # Ordinamento alfabetico di base
    files.sort()

    # Forza 'Street' in cima alla lista
    street_files = [f for f in files if f.lower().startswith("street")]
    other_files = [f for f in files if not f.lower().startswith("street")]
    
    final_list = street_files + other_files

    with open("gallery.json", "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)

    print(f"Successo! {len(final_list)} immagini trovate.")

if __name__ == "__main__":
    generate()

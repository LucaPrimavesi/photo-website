import os
import json

def generate():
    image_dir = "img"
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG')
    
    if not os.path.exists(image_dir):
        # Invece di crashare, crea la cartella se manca
        os.makedirs(image_dir)
        print(f"Cartella '{image_dir}' creata.")

    files = [f for f in os.listdir(image_dir) if f.lower().endswith(valid_extensions)]
    
    # Ordinamento: Street sempre per primo
    street_files = sorted([f for f in files if f.lower().startswith("street")])
    other_files = sorted([f for f in files if not f.lower().startswith("street")])
    
    final_list = street_files + other_files

    with open("gallery.json", "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2)

    print(f"Gallery aggiornata con {len(final_list)} immagini.")

if __name__ == "__main__":
    generate()

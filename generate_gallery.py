import os
import json

def generate():
    image_dir = "img"
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    
    if not os.path.exists(image_dir):
        print(f"Errore: La cartella '{image_dir}' non esiste!")
        return

    # 1. Legge i file nella cartella img
    files = [f for f in os.listdir(image_dir) if f.lower().endswith(valid_extensions)]
    
    # 2. Ordina alfabeticamente per avere una base pulita
    files.sort()

    # 3. LOGICA DI PRIORITÀ: Portiamo Street in cima
    # Creiamo due liste: una per Street e una per tutto il resto
    street_files = [f for f in files if f.lower().startswith("street")]
    other_files = [f for f in files if not f.lower().startswith("street")]

    # Uniamo le liste: Street sarà sempre la prima
    final_list = street_files + other_files

    # 4. Salva il file gallery.json
    with open("gallery.json", "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2)

    print(f"Successo! {len(street_files)} foto Street e {len(other_files)} altre foto salvate.")

if __name__ == "__main__":
    generate()

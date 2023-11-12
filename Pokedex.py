import tkinter as tk
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO
import pypokedex

# based on neuralnine

window = tk.Tk()
window.geometry("800x650")
window.title("Pokedex Project")
window.config(padx=10, pady=10)

title_label = tk.Label(window, bg=window.cget('bg'), text="Pokedex Project")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_ability = tk.Label(window)
pokemon_ability.config(font=("Arial", 20))
pokemon_ability.pack(padx=10, pady=10)

def updating_window_color(pokemon_type_bg):
    type_colors = {
        "electric": "yellow",
        "water": "#add8e6",
        "fire": "orange",
        "grass": "lightgreen",
        "ice": "lightblue",
        "fighting": "brown",
        "poison": "purple",
        "ground": "orange",
        "flying": "skyblue",
        "psychic": "pink",
        "bug": "#lightscreen",
        "rock": "#D2B48C",
        "ghost": "#9370DB",
        "dragon": "indigo",
        "dark": "darkgray",
        "steel": "lightgray",
        "fairy": "lightpink",
    }
    
    lowercased_type = pokemon_type_bg.lower()
    color = type_colors.get(lowercased_type, "white")
    window.config(bg=color)
    return color


# FUNCTION TO LOAD POKEMON


def loadPokemon():
    # Pokemon info based on the user input
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    # color associated to the pokemon type
    pokemon_type_bg = pokemon.types[0].title()

    # Get the color associated with the Pokemon type
    box_color = updating_window_color(pokemon_type_bg)

    # background associated with the box
    pokemon_information.config(bg=box_color)
    pokemon_types.config(bg=box_color)
    pokemon_ability.config(bg=box_color)

    # pokemon info like: pokedex number, type, ability and name
    pokemon_information.config(text=f"#{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    pokemon_ability.config(text="\n".join([ability.name for ability in pokemon.abilities]).title())

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img, bg=box_color)
    pokemon_image.image = img

    # get the color associated with the Pokemon type
    box_color = updating_window_color(pokemon_type_bg)
    # title background associated with the pokemon type 
    title_label.config(bg=box_color)
    # insert associated with pokemon type
    label_id_name.config(font=("Arial", 20), bg=box_color)

def clearText():
    text_id_name.delete("1.0", tk.END)

    
label_id_name = tk.Label(window, text="Please insert the Pokémon name or number in the box below")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=0.5)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)
text_id_name.bind("<Return>", lambda event=None: loadPokemon())

button_load = tk.Button(window, text="Find Pokemon", command=loadPokemon)
button_load.config(font=("Arial", 20))
button_load.pack(padx=10, pady=10)

clear_button = tk.Button(window, text="Clear entry box", command=clearText)
clear_button.config(font=("Arial", 10))
clear_button.pack()


window.mainloop()

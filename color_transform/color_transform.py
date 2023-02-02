from PIL import Image
from tqdm import tqdm


def change_color(image_path, image_destination,hex):
    #img est le chemin de l'image
    #hex est la nouvelle couleur en hexadécimal

    img = Image.open(image_path)

    # couleur HEX en tuple RGB
    hex = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    data = img.getdata()

    newData = []
    for item in data:
        if item[3] == 255:
            newData.append(hex)
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(image_destination, "PNG")
    print("Image sauvegardée en tant que " + image_destination)

def reduce_image_size(file_path):
    #réduire la taille de l'image par 4
    # Ouvrir l'image
    with Image.open(file_path) as im:
        # Réduire la taille de l'image par 4
        im = im.resize((im.width//4, im.height//4))
        # Enregistrer l'image réduite
        im.save(file_path)
        print("Image réduite en tant que " + file_path)

def add_background(image_path: str, fond_couleur: str, output_path: str):

    fond_couleur = tuple(int(fond_couleur[i:i+2], 16) for i in (0, 2, 4))
    print(fond_couleur)


    img = Image.open(image_path)
    img = img.convert("RGBA")

    # on crée une nouvelle image de la même taille
    print(img.size)
    new_img = Image.new("RGB", img.size, fond_couleur)

    # on colle l'image PNG sur la nouvelle image
    new_img.paste(img, (0, 0))
    new_img.save(output_path)




def main(hex):
    assets_path = ["./color_transform/assets_init/chat_rect.png",
                    "./color_transform/assets_init/chat_round.png",
                    "./color_transform/assets_init/text_rect.png",
                    "./color_transform/assets_init/text_round.png"]
    assets_destination = ["./color_transform/assets_init/entry_2.png",
                        "./color_transform/assets_init/image_2.png",
                        "./color_transform/assets_init/image_1.png",
                        "./color_transform/assets_init/entry_1.png"]

    for i in range(len(assets_path)):
        change_color(assets_path[i], assets_destination[i], hex)
        reduce_image_size(assets_destination[i])

    #add_background("color_transform/assets_init/ico_send.png", hex, "color_transform/assets/button_2.png")
    #add_background("color_transform/assets_init/ico_settings.png", hex, "color_transform/assets/button_1.png")

if __name__ == "__main__":
    #couleur = input("Entrez la couleur en hexadécimal (sans le #): ")
    couleur = "00FBFF"
    main(couleur)
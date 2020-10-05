from PIL import Image
from PIL.Image import new

#on charge l'image qui sera notre conteneur
Original = Image.open(
    "C:\\Users\\320065245\\Desktop\\ECE\\ING5\\Sécurité des SI 2\\TP1 - Stéganographie\\pythonProject\\Original.jpg")
#on charge l'image secret que nous devons cacher dans le conteneur
ToHide = Image.open(
    "C:\\Users\\320065245\\Desktop\\ECE\\ING5\\Sécurité des SI 2\\TP1 - Stéganographie\\pythonProject\\ToHide.jpg")

# Original.show()
largeur, hauteur = Original.size#on récupére la taille de notre conteneur, cad l'image Originale

NewImage = new("RGB", (largeur, hauteur))#on créé la nouvelle image, qui sera le secret à l'intérieur du conteneur

for y in range(hauteur):
    for x in range(largeur):#double boucle parcourant chaque pixel de l'image
        p = Original.getpixel((x, y))#on récupére la valeur du pixel de l'image Originale qui restera visible
        r, v, b = p[0] & 240, p[1] & 240, p[2] & 240#on supprime les bits de poids faible du conteneur, cad de l'image originale

        p2 = ToHide.getpixel((x, y))#on récupére la valeur du pixel du secret
        r2, v2, b2 = p2[0] >> 4, p2[1] >> 4, p2[2] >> 4 #on décale les bits de poid fort en bits de poid faible

        r3, v3, b3 = r | r2, v | v2, b | b2#on ajoute les bits de poid fort du conteneur aux bits de poid faible du secret
        NewImage.putpixel((x, y), (r3, v3, b3))#on écrit le pixel modifié sur l'image de destination, cad le conteneur

NewImage.save("Image.bmp", "BMP") #on sauvegarde l'image en BMP pour éviter la compression
NewImage.show()#on affiche l'image avec le secret caché dans Originale


#on charge l'image dont on doit extraire le secret
ToUnhide = Image.open("C:\\Users\\320065245\\Desktop\\ECE\\ING5\\Sécurité des SI 2\\TP1 - Stéganographie\\pythonProject\\image.bmp")

largeur, hauteur = ToUnhide.size #on récupérer la taille de l'image

Resultat = new("RGB", (largeur, hauteur))#on crée l'image qui sera le résultat de l'extraction du secret

for y in range(hauteur):
    for x in range (largeur):
        p = ToUnhide.getpixel((x,y))#on récupére la valeur du pixel de l'image à extraire
        r, v, b = p[0], p[1], p[2]

        r = r << 4    #on décale les bits de poid faible en bits de poid fort avec un décalage à gauche
        v = v << 4
        b = b << 4

        r = r&240   #on supprime les bits de poid faible
        v = v&240
        b = b&240

        Resultat.putpixel((x,y), (r,v,b))#on insére le pixel dans l'image de sortie


Resultat.save("Resulat.png", "PNG")#on sauvegarde l'image en PNG
Resultat.show()#on affiche l'image du secret extrait
from msilib.schema import Component


BACKGROUND = "black"
BACKGROUND_CARPETA  = "#F1C617"
BACKGROUND_ARCHIVO  = "#FFFCD9"

FONT = ("Arial", 16) #Si se quiere agregar algun efecto como Negrita, se agrega otro parameto como: "Bold"
COMPONENT = "#363636"
TEXT = "#84C9FB"
TEXT_NEGRO = 'black'

STYLE = {
    "font": FONT,
    "bg": COMPONENT,
    "fg": TEXT
}

STYLE_CARPETA = {
    "font": FONT,
    "bg": BACKGROUND_CARPETA,
    "fg": TEXT_NEGRO
}
STYLE_ARCHIVO = {
    "font": FONT,
    "bg": BACKGROUND_ARCHIVO,
    "fg": TEXT_NEGRO
}

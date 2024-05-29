import requests

IMAGGA_API_KEY = '*********'
IMAGGA_API_SECRET = '*********'
IMAGGA_COLORS_URL = 'https://api.imagga.com/v2/colors'

def get_image_colors(image_url):
    response = requests.get(
        IMAGGA_COLORS_URL,
        auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET),
        params={'image_url': image_url}
    )
    return response.json()

# URL de una imagen a analizar
image_url = 'https://w0.peakpx.com/wallpaper/349/411/HD-wallpaper-alejandro-da-silva-chico-guapo-tableta-thumbnail.jpg'

# Obtener los colores predominantes
colors = get_image_colors(image_url)
print(colors)

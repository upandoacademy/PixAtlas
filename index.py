from PIL import Image
import math

# Paleta de cores — cada sub-lista representa um conjunto de tons (do mais claro ao mais escuro)
color_sets = [
    ["#FFD9A6", "#FFA845", "#FF6F1F", "#993D00"],  # Laranja
    ["#E6CCFF", "#B399FF", "#7A33FF", "#4C0099"],  # Roxo
    ["#D4F2C4", "#90E070", "#50B33B", "#26721B"],  # Verde
    ["#FFB3B3", "#FF4D4D", "#CC0000", "#660000"],  # Vermelho
    ["#FFF5B3", "#FFE74D", "#FFCC00", "#996600"],  # Amarelo
    ["#E5E5E5", "#B3B3B3", "#808080", "#333333"],  # Cinza
    ["#E6C9A8", "#C99A6B", "#8C5E3B", "#4D2B1A"],  # Marrom
    ["#666666", "#333333", "#1A1A1A", "#000000"],  # Preto
    ["#FFD6A6", "#FF9E52", "#CC5F1E", "#662E0F"],  # Laranja Queimado
    ["#FFE2A0", "#FFC159", "#FF9B1F", "#996613"],  # Dourado
    ["#D4BBA6", "#A8876B", "#7A5742", "#3D2B1A"],  # Madeira
    ["#CBBFAF", "#A68E76", "#7A5F42", "#3D2F1B"],  # Terra
    ["#E2CCF5", "#B893E6", "#8F52BF", "#4C1F66"],  # Lilás
    ["#FFB3C1", "#FF6685", "#CC004D", "#660026"],  # Rosa Escuro
    ["#D9E6B3", "#AADD70", "#78B33B", "#3D661A"],  # Verde Oliva
    ["#CFCFCF", "#A6A6A6", "#737373", "#2E2E2E"],  # Neutro Escuro
]

# Número total de conjuntos e tons
num_colors = len(color_sets)
tones_per_color = len(color_sets[0])

# Tentar formar um grid quadrado (ex: 8x8, 4x4, etc.)
cols = math.ceil(math.sqrt(num_colors))
rows = math.ceil(num_colors / cols)

# Cada tom = 1 pixel
cell_width = tones_per_color
cell_height = 1

# Tamanho total do atlas
width = cols * cell_width
height = rows * cell_height

# Criar imagem
img = Image.new("RGB", (width, height))

# Preencher pixels
for i, shades in enumerate(color_sets):
    row = i // cols
    col = i % cols
    for x, hex_color in enumerate(shades):
        px = col * cell_width + x
        py = row
        rgb = tuple(int(hex_color[j:j+2], 16) for j in (1, 3, 5))
        img.putpixel((px, py), rgb)

# Salvar imagem
img.save("color_atlas.png")
print(f"✅ Atlas salvo como color_atlas.png ({width}x{height}px)")

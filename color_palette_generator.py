from PIL import Image, ImageDraw

# Paleta de cores — cada sub-lista representa um conjunto de tons (do mais claro ao mais escuro)
color_sets = [
    ["#FFB3B3", "#FF4D4D", "#CC0000", "#660000"],  # Vermelho
    ["#FFB3C1", "#FF6685", "#CC004D", "#660026"],  # Rosa Escuro
    ["#E2CCF5", "#B893E6", "#8F52BF", "#4C1F66"],  # Lilás
    ["#E6CCFF", "#B399FF", "#7A33FF", "#4C0099"],  # Roxo
    ["#D6D1FF", "#A8A0FF", "#5E63FF", "#2B2D99"],  # Azul-violeta
    ["#C4E0FF", "#66B3FF", "#0073E6", "#003366"],  # Azul puro
    ["#B3CCFF", "#6699FF", "#004DCC", "#002266"],  # Azul escuro
    ["#B3F0FF", "#66E0FF", "#00B3CC", "#006680"],  # Azul turquesa
    ["#B3FFF2", "#66FFE0", "#00CC99", "#00664D"],  # Ciano
    ["#B9E6C2", "#5FBF72", "#2F8045", "#143D1E"],  # Verde Floresta
    ["#D4F2C4", "#90E070", "#50B33B", "#26721B"],  # Verde
    ["#D9E6B3", "#AADD70", "#78B33B", "#3D661A"],  # Verde Oliva
    ["#FFF5B3", "#FFE74D", "#FFCC00", "#996600"],  # Amarelo
    ["#FFE2A0", "#FFC159", "#FF9B1F", "#996613"],  # Dourado
    ["#FFD9A6", "#FFA845", "#FF6F1F", "#993D00"],  # Laranja
    ["#FFD6A6", "#FF9E52", "#CC5F1E", "#662E0F"],  # Laranja Queimado
    ["#C9A889", "#8C5E3C", "#4D2B1A", "#26140D"],  # Marrom Escuro
    ["#E6C9A8", "#C99A6B", "#8C5E3B", "#4D2B1A"],  # Marrom
    ["#D4BBA6", "#A8876B", "#7A5742", "#3D2B1A"],  # Madeira
    ["#CBBFAF", "#A68E76", "#7A5F42", "#3D2F1B"],  # Terra
    ["#E5E5E5", "#B3B3B3", "#808080", "#333333"],  # Cinza
    ["#CFCFCF", "#A6A6A6", "#737373", "#2E2E2E"],  # Neutro Escuro
    ["#666666", "#333333", "#1A1A1A", "#000000"],  # Preto
    ["#A3B3B8", "#52656D", "#2E3F45", "#273238"]   # Verde-Azul Escuro
]

# Função de interpolação


def hex_to_rgb(h):
    return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))


def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def interpolate_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


# Gerar 10 tons para cada grupo
expanded_color_sets = []
steps = 10

for shades in color_sets:
    rgb_shades = [hex_to_rgb(h) for h in shades]
    new_shades = []
    for i in range(len(rgb_shades) - 1):
        for t in range(steps // (len(rgb_shades) - 1)):
            ratio = t / (steps // (len(rgb_shades) - 1))
            new_color = interpolate_color(
                rgb_shades[i], rgb_shades[i + 1], ratio)
            new_shades.append(rgb_to_hex(new_color))
    # Garantir exatamente 10 tons
    while len(new_shades) < steps:
        new_shades.append(rgb_to_hex(rgb_shades[-1]))
    expanded_color_sets.append(new_shades)

# Configurações
tones_per_color = len(expanded_color_sets[0])
num_colors = len(expanded_color_sets)
block_size = 40
atlas_width = num_colors * block_size
atlas_height = tones_per_color * block_size
gradient_height = 400

img = Image.new("RGB", (atlas_width, atlas_height + gradient_height), "white")
draw = ImageDraw.Draw(img)

# Parte 1: Atlas Pixel
for i, shades in enumerate(expanded_color_sets):
    for j, hex_color in enumerate(reversed(shades)):
        rgb = tuple(int(hex_color[k:k+2], 16) for k in (1, 3, 5))
        x0 = i * block_size
        y0 = j * block_size
        draw.rectangle([x0, y0, x0 + block_size, y0 + block_size], fill=rgb)

# Parte 2: Degradê Fluido
for x in range(atlas_width):
    color_index = int(x / block_size)
    t = (x % block_size) / block_size
    if color_index < num_colors - 1:
        base_color = tuple(
            int(expanded_color_sets[color_index][5][i:i+2], 16) for i in (1, 3, 5))
        next_color = tuple(
            int(expanded_color_sets[color_index+1][5][i:i+2], 16) for i in (1, 3, 5))
        r = int(base_color[0]*(1-t) + next_color[0]*t)
        g = int(base_color[1]*(1-t) + next_color[1]*t)
        b = int(base_color[2]*(1-t) + next_color[2]*t)
    else:
        r, g, b = tuple(
            int(expanded_color_sets[-1][5][i:i+2], 16) for i in (1, 3, 5))
    for y in range(atlas_height, atlas_height + gradient_height):
        blend = (y - atlas_height) / gradient_height
        r2 = int(r + (255 - r) * blend)
        g2 = int(g + (255 - g) * blend)
        b2 = int(b + (255 - b) * blend)
        img.putpixel((x, y), (r2, g2, b2))

img.save("color_atlas_full_10tones.png")
print("✅ Gerado color_atlas_full_10tones.png (10 tons por cor)")

# 🎨 PixAtlas

Um simples e poderoso gerador de **atlas de cores em degradê**, ideal para uso em **jogos, design gráfico, texturas ou ferramentas de arte procedural**.

---

## 🧩 Sobre o Projeto

Este script Python cria uma imagem (`color_atlas.png`) contendo uma **grade de conjuntos de cores**, onde cada linha representa uma **variação tonal** (do mais claro ao mais escuro) de uma cor principal.

Ele é útil para quem precisa **visualizar, organizar ou gerar automaticamente paletas de cores** em um formato compacto e reutilizável.

---

## 🖼️ Exemplo de Saída

O resultado é uma imagem semelhante a:

```
🟥🟥🟥🟥  🟩🟩🟩🟩  🟦🟦🟦🟦  ...
```

Cada grupo horizontal mostra tons de uma mesma cor.
O script calcula automaticamente o tamanho ideal do grid e salva o atlas final no diretório atual.

---

## ⚙️ Funcionalidades

* 🎨 Gera um **atlas de cores completo** com múltiplos grupos de tons.
* 📐 Calcula automaticamente as **dimensões do grid**.
* 🧠 Baseado em **valores hexadecimais** fáceis de editar e expandir.
* 🖼️ Exporta uma **imagem compacta em PNG**, pronta para uso.
* 💡 Ideal para texturas, shaders, estudos visuais e ferramentas de prototipagem.

---

## 🧰 Requisitos

* **Python 3.7+**
* Biblioteca **Pillow (PIL)**

Instalação:

```bash
pip install pillow
```

---

## 🚀 Como Usar

1. Salve o código em um arquivo, por exemplo `color_atlas.py`.
2. Execute o script:

```bash
python color_atlas.py
```

3. O atlas será salvo automaticamente no mesmo diretório:

```
✅ Atlas salvo como color_atlas.png (40x4px)
```

---

## 🧪 Personalização

O script é totalmente personalizável.
Você pode modificar a lista de cores ou ajustar o número de tons conforme desejar.

### Exemplo: adicionando um novo grupo de cores

```python
color_sets.append(["#FFE5B4", "#FFB347", "#FF8C00", "#CC5500"])  # Laranja suave
```

### Exemplo: alterando a quantidade de tons

Cada sublista dentro de `color_sets` representa os tons de uma cor:

```python
["#E6CCFF", "#B399FF", "#7A33FF", "#4C0099"]
```

Basta adicionar ou remover cores dentro de cada lista.

---

## 💡 Aplicações Possíveis

* Criação de **texture atlases** para jogos
* Desenvolvimento de **materiais procedurais**
* Visualização de **paletas de design**
* Ferramentas educacionais sobre **gradientes e cor**
* **Prototipagem** em engines como Unreal, Unity ou Godot

---

Aqui está a seção reescrita com a **licença MIT**, mantendo o mesmo estilo visual do README:

---

## 📜 Licença

Este projeto é licenciado sob a **Licença MIT**.

Você tem permissão para **usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias** deste software, desde que mantenha o aviso de copyright e a nota de permissão em todas as cópias ou partes substanciais do código.

O software é fornecido **"como está"**, sem qualquer garantia expressa ou implícita — incluindo, mas não se limitando a garantias de comercialização, adequação a um propósito específico ou não violação.

Para mais detalhes, consulte o arquivo [`LICENSE`](LICENSE).

---

## 👤 Autor

**Upando**
🧠 Desenvolvedor de jogos e criador de experiências interativas
🎮 Unreal Engine | Blender | Game Design

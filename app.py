from flask import Flask, render_template, request

app = Flask(__name__)

# Dimensões da peça de tecido original
TECIDOR_COMPRIMENTO = 1  # metro
TECIDOR_LARGURA = 1.4  # metros

@app.route('/')
def index():
    # Renderiza a página inicial sem resultados na primeira vez
    return render_template('index.html', custo=None, preco_cliente=None)

@app.route('/calcular', methods=['POST'])
def calcular():
    # Recebendo os dados do formulário
    preco_metro = float(request.form['preco_metro'])
    comprimento_usado_cm = float(request.form['comprimento_usado'])
    largura_usada_cm = float(request.form['largura_usada'])

    # Convertendo centímetros para metros
    comprimento_usado = comprimento_usado_cm / 100
    largura_usada = largura_usada_cm / 100

    # Calculando a área usada e o custo
    area_usada = comprimento_usado * largura_usada
    area_total = TECIDOR_COMPRIMENTO * TECIDOR_LARGURA
    custo = (area_usada / area_total) * preco_metro
    preco_cliente = custo * 1.5  # Adicionando margem de lucro de 50%

    return render_template('index.html', custo=custo, preco_cliente=preco_cliente)

if __name__ == '__main__':
    app.run(debug=True)

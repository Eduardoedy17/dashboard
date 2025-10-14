from flask import Flask, render_template

# Criação da aplicação Flask.
app = Flask(__name__)

# Rotas da aplicação e navegação entre páginas.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/config')
def configuracoes():
    return render_template('config.html')




#Método 'main' sempre no final do arquivo.
if __name__ == '__main__':
    app.run(debug=True)
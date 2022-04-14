from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'atualizador_titulos'

@app.route('/')
def index_login():
    return render_template('pagina_inicial.html',titulo ='Atulizador de Títulos')

@app.route('/autenticar',methods = ['POST',])
def autenticar():
    if (request.form["senha"] == 'usuario' and request.form["usuario"] == 'usuario'):
        session['usuario_logado'] = request.form["usuario"]
        flash(f'{request.form["usuario"]} Seu login foi efetuado com sucesso.')
        return redirect('/tipo_titulo')
    else:
        flash('Nome de usuário ou senha estão incorretos')
        return redirect('/')

@app.route('/tipo_titulo')
def selecionar_tipo():
    return render_template('tipo_titulo.html')
    
@app.route('/titulo_selecionado', methods = ['POST',])
def titulo_selecionado():
    if request.form['my_html_select_box'] == 'Processar baixa':
        return redirect('/titulo_selecionado/processar_baixa')
    return redirect('/titulo_selecionado/processar_liquidacao')
    # print('\n\n\n',request.form['my_html_select_box'],'\n\n\n')
    # return render_template('teste.html')

@app.route('/titulo_selecionado/processar_baixa')
def processar_baixa():
    print('\n\n\n',request.form,'\n\n\n')
    return render_template('processar_baixa.html')

@app.route('/titulo_selecionado/processar_liquidacao')
def processar_liquidacao():
    return render_template('processar_liquidacao.html')



@app.route('/teste')
def test_1():
    return render_template('teste.html')

@app.route('/teste2')
def test_2():
    return render_template('teste_2.html')

@app.route('/atualizar_titulos')
def atualizar_titulos():
    return render_template('atuliza_titulos.html',titulo = 'Atulizador de Títulos')



@app.route('/nova busca', methods = ['POST',])
def nova_busca():
    return redirect('/busca_candidatos')


if __name__ == "__main__":  # Para poder executar quando o arquivo não for importado
    app.run(debug=True)     # Para ir atualizando as modificações que o codigo faz no site

# Heroku: https://dashboard.heroku.com/apps/busca-exp-candidatos/deploy/heroku-git

# Download: https://www.w3schools.com/tags/att_a_download.asp
# Video sobre linkl de download no html = https://www.youtube.com/watch?v=Jszz7M676y8
# Site com os typos de midia: https://www.iana.org/assignments/media-types/media-types.xhtml
# Duvidas hmtl: https://www.w3schools.com/tags/att_a_download.asp

# sites:
# https://tutorialehtml.com/pt/html-tutorial-upload-formulario/
# 
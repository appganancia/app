#!/usr/bin/env python3
"""Monta as pastas de acesso do AppGanancia a partir dos arquivos da raiz.

E o mesmo desenho do app do Brasil (lucronamao/app, montar-pastas.py): a chave de
acesso mora no CAMINHO (/app/<chave>/), porque e a unica coisa que faz o icone da
tela inicial do iPhone nascer liberado. Toda pagina que a compradora possa abrir
existe dentro de cada pasta, copiada de UMA fonte, pra nao haver versao divergente.

Aqui so as paginas sao geradas: o manifest de cada pasta (start_url propria) ja
existe e nao muda.

Uso:  python montar-pastas.py
Depois: publicar a pasta inteira em appganancia/app.
"""
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))
# nome na raiz -> nome dentro da pasta. index.html da raiz e o Mis Ventas; dentro
# da pasta, index.html e o MENU (o hub), entao o app vira controle.html.
APPS = {'index.html': 'controle.html',
        'divulga.html': 'divulga.html',
        'catalogo.html': 'catalogo.html'}
MENU = 'hub.html'
PASTAS = ['sx01fzn', '83aby3u', 'm7081wh']
ASSETS = ['favicon-16.png', 'favicon-32.png', 'favicon-48.png', 'favicon-96.png',
          'favicon-180.png', 'icone-192.png', 'icone-512.png',
          'logo-branca.png', 'logo-vinho.png', 'catalogo-faixa.jpg', 'ativacao.js']


def ajustar(html):
    """Dentro da pasta, os assets moram um nivel acima."""
    for a in ASSETS:
        html = html.replace('"' + a + '"', '"../' + a + '"')
        html = html.replace("'" + a + "'", "'../" + a + "'")
    return html


def copiar(origem, destino):
    with open(os.path.join(RAIZ, origem), encoding='utf-8', newline='') as fh:
        html = ajustar(fh.read())
    with open(destino, 'w', encoding='utf-8', newline='') as fh:
        fh.write(html)


def main():
    for pasta in PASTAS:
        dir_ = os.path.join(RAIZ, pasta)
        copiar(MENU, os.path.join(dir_, 'index.html'))
        for origem, destino in APPS.items():
            copiar(origem, os.path.join(dir_, destino))
        print('  ' + pasta + '/  ->  index.html (menu) + ' + ' + '.join(APPS.values()))
    print('\nNunca edite dentro da pasta: edite a raiz e rode este script de novo.')


if __name__ == '__main__':
    main()

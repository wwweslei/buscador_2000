# coding: utf-8
import os
import re
import time
from argparse import ArgumentParser

parser = ArgumentParser(argument_default='/home/weslei/PycharmProjects/')
parser.add_argument('regex', help='Digite uma expressão regular ')
parser.add_argument('diretorio', nargs='?', help='Diretório da busca')
argumentos = parser.parse_args()
resultado = {}


def busca(regex=argumentos.regex, dir_name=argumentos.diretorio):
    for name in os.listdir(dir_name):
        path = os.path.join(dir_name, name)
        if os.path.isfile(path):
            time.sleep(0.02)
            try:
                with open(os.path.join(dir_name, name)) as doc:
                    confirme = re.findall(regex, doc.read())
                    if confirme:
                        resultado[path] = name
                        print('\033[36m', '## Encontrado no diretorio ', path, '#'*40,
                              'arquivo ', name, '\033[0;0m')
                    else:
                        print(dir_name, name, '  ****   Nada encontrado  *****')
            except:
                print('\033[31m'+name, '   Não foi possivel abrir o arquivo'+'\033[0;0m')
        else:
            busca(regex, path)
    return resultado

if __name__ == '__main__':
    b = busca()
    print('\n\n\nSua busca retornou os seguintes resultados: \n')
    for x in b:
        print('Diretório  ', x, '\033[32m',  '\t\tarquivo\t', b[x], '\033[0;0m')

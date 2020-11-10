"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""


def front_x(words):
    # +++ SUA SOLUÇÃO +++
    '''
    lista_com_x = []
    lista_sem_x = []
    for i in range(len(words)):
        if words[i][0] == 'x':
            lista_com_x.append(words[i])
        else:
            lista_sem_x.append(words[i])
        i += 1
    return sorted(lista_com_x) + sorted(lista_sem_x)
    '''
    # return sorted([lista_com_x for lista_com_x in words if lista_com_x[0] == 'x']) + sorted([lista_sem_x for lista_sem_x in words if lista_sem_x[0] != 'x'])
    padraoOrganizacao = [0, 'x']
    return sorted(words, key=lambda palavra: str(([padraoOrganizacao[0], palavra]) if palavra.startswith(padraoOrganizacao[1]) else palavra))

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

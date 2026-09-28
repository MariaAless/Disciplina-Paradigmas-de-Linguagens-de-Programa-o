import operator
from lark import Tree

COMPARADORES = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}

def avaliar_condicao(condicao, estado):
    resultado = None
    operador_logico = None

    for filho in condicao.children:
        if isinstance(filho, Tree):
            nome, comparador, valor = filho.children
            nome = str(nome)
            valor = int(valor)

            val_atual = estado.get(nome, 0)
            parcial = COMPARADORES[str(comparador)](val_atual, valor)

            if resultado is None:
                resultado = parcial
            elif operador_logico == "and":
                resultado = resultado and parcial
            elif operador_logico == "or":
                resultado = resultado or parcial
        else:
            operador_logico = str(filho)

    return resultado

def run_instruction(t, estado, eventos):
    if t.data == "declare":
        nome = str(t.children[0])
        valor = int(t.children[1])
        estado[nome] = valor

    elif t.data == "alterar":
        operacao, nome, valor = t.children
        operacao = str(operacao)
        nome = str(nome)
        valor = int(valor)
        if nome not in estado:
            estado[nome] = 0
            
        if operacao == "aumentar":
            estado[nome] += valor
        else:
            estado[nome] -= valor

    elif t.data == "evento_decl":
        nome_evento = str(t.children[0])[1:-1]
        bloco = t.children[1]
        eventos[nome_evento] = bloco.children

    elif t.data == "evento_chamada":
        nome_evento = str(t.children[0])[1:-1]
        if nome_evento not in eventos:
            raise NameError(f"Evento '{nome_evento}' não foi declarado.")
        for instrucao in eventos[nome_evento]:
            run_instruction(instrucao, estado, eventos)

    elif t.data == "repetir":
        quantidade = int(t.children[0])
        bloco = t.children[1]
        for _ in range(quantidade):
            for instrucao in bloco.children:
                run_instruction(instrucao, estado, eventos)

    elif t.data == "condicional":
        condicao = t.children[0]
        block_se = t.children[1]
        block_senao = t.children[2] if len(t.children) > 2 else None

        if avaliar_condicao(condicao, estado):
            for instrucao in block_se.children:
                run_instruction(instrucao, estado, eventos)
        elif block_senao is not None:
            for instrucao in block_senao.children:
                run_instruction(instrucao, estado, eventos)

    elif t.data == "alerta":
        mensagem = str(t.children[0])[1:-1]
        print(f"[ALERTA] {mensagem}")

    elif t.data == "resetar":
        nome = str(t.children[0])
        estado[nome] = 0

    elif t.data == "mostrar":
        nome = str(t.children[0])
        print(f"[SAÍDA] {nome} = {estado.get(nome, 0)}")

def run_hormoniolang(arvore):
    estado = {}
    eventos = {}
    for instrucao in arvore.children:
        run_instruction(instrucao, estado, eventos)
    return estado
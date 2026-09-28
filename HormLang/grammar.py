from lark import Lark

HORMONE_GRAMMAR = r"""
start: instruction+

instruction: "hormonio" NAME NUMBER                          -> declare
           | OPERACAO NAME NUMBER                              -> alterar
           | "evento" STRING block                              -> evento_decl
           | "evento" STRING                                    -> evento_chamada
           | "repetir" NUMBER block                              -> repetir
           | "if" condicao block ("else" block)?                 -> condicional
           | "alerta" STRING                                       -> alerta
           | "resetar" NAME                                        -> resetar
           | "mostrar" NAME                                        -> mostrar

condicao: condicao_simples (LOGICO condicao_simples)*
condicao_simples: NAME COMPARADOR NUMBER

block: "{" instruction+ "}"

OPERACAO: "aumentar" | "diminuir"
COMPARADOR: ">" | "<" | ">=" | "<=" | "==" | "!="
LOGICO: "and" | "or"

%import common.CNAME -> NAME
%import common.INT -> NUMBER
%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS
"""

def get_parser():
    return Lark(HORMONE_GRAMMAR, parser="lalr")
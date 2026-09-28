from grammar import get_parser
from interpreter import run_hormoniolang

def main():
    exemplo1 = """
     hormonio cortisol 30
    """

    exemplo2 = """
      evento "estresse" {
          aumentar cortisol 20
      }
      repetir 12 {
          evento "estresse"
      }
    """

    exemplo3 = """
      hormonio cortisol 90
      if cortisol > 80 {
          alerta "nivel critico"
      } else {
          mostrar cortisol
      }

    """


    parser = get_parser()

    print("ÁRVORE DE ANÁLISE SINTÁTICA (.pretty())")
    arvore = parser.parse(exemplo1)
    print(arvore.pretty())

    print("EXECUÇÃO DO INTERPRETADOR ")
    estado_final = run_hormoniolang(arvore)
    print(f"Estado final dos hormônios: {estado_final}")

if __name__ == "__main__":
    main()
# inicia o programa por terminal 

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(prog="meu_projeto", description="Meu projeto Python")
    
    
    
    # adicionar depois o argumento de verbose para ativar o modo detalhado de saída

    # parser.add_argument(
    #     "-v", "--verbose", 
    #     action="store_true", 
    #     help="Ativa modo detalhado de saída"
    # )
    
    parser.add_argument(
        "-r","run",
        help="Roda a aplicação"
    )

    

    args = parser.parse_args()

    # if args.verbose:
    #     print(f"Modo detalhado ativado para: {args.arquivo}")
    #     print(f"Saída definida para: {args.output}")

    # Sua lógica principal aqui
    # print(f"Processando {args.arquivo}...")

    if args.run:
        exec(open("reservador.pyc").read())

if __name__ == "__main__":
    main()
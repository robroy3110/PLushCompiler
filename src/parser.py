import subprocess
from typing import Any

from ply import yacc, lex

from semantic import *
from compilador import compilador
from tokens import *
from rules import *


# Using the parse
def get_input(file=False):
    if file:
        f = open(file, "r")
        data = f.read()
        f.close()
    else:
        data = ""
        while True:
            try:
                data += raw_input() + "\n"
            except:
                break
    return data


def ast_to_dict(node: ASTNode) -> Any:
    if isinstance(node, list):
        return [ast_to_dict(item) for item in node]
    elif isinstance(node, ASTNode):
        result = {'type': node.__class__.__name__}
        for field in node.__dataclass_fields__:
            value = getattr(node, field)
            result[field] = ast_to_dict(value)
        return result
    else:
        return node


def main(options={}, filename=False):
    logger = yacc.NullLogger()
    parser = yacc.yacc(debug=logger, errorlog=logger)
    # debug = True, debugfile = "parser_debug.log", errorlog = logger
    datafile = get_input(filename)
    ast = parser.parse(datafile, lexer=lex.lex(nowarn=1))  # ,debug=True)

    if options.tree:
        import json
        ast_json = json.dumps(ast_to_dict(ast), indent=2)
        print(ast_json)
    try:
        check(ast)
        print("Análise semântica concluída com sucesso!")
    except (TypeError, NameError) as e:
        print(f"Erro semântico: {e}")

    try:
        codigo_llvm = compilador(ast)
        print("Compilado com sucesso!")

        with open(f"{filename.replace('.pl', '')}.ll", "w") as f:
            f.write(codigo_llvm)

        # ecutar o código LLVM usando lli
        result = subprocess.run(['lli', f"{filename.replace('.pl', '')}.ll"], capture_output=True, text=True)
        print("Resultado da execução:")
        print(result.stdout)
        if result.stderr:
            print("Erros:")
        print(result.stderr)
    except Exception as e:
        print(f"Erro de compilação: {e}")


if __name__ == '__main__':
    main()

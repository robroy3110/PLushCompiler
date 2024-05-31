# PLushCompiler Robert Cachapa fc62840
Compilador para a linguagem PLush:
O projeto é composto pelos ficheiros da pasta sorce que representam:
ast_nodes.py - que contem as classes das nodes da ast
compilador.py - que contem a geração de codigo de llvm a partir do codigo PLush
main.py - que recebe os argumentos como o ficheiro e passa-os ao parser
parser.py - que chama o parser, lexer e compilador e faz o parsing do codigo PLush usando o PLY
rules.py - que contem a gramatica da linguagem PLush
semantic.py - que contem o typechecker e realiza-o
tokens.py - que contem os tokens do lexer

How to run:
Primeiramente damos run ao setup.sh file para ter a certeza que temos todas as dependencias e apos garantirmos que estamos prontos para dar run ao programa
podemos correr o ficheiro plush.sh dando-lhe um ficheiro .pl por exemplo: ./plush.sh --tree tests/fizzBuzz.pl

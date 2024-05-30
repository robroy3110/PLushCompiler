
tokens = (

    # assignment
    'IDENTIFIER',
    'ASSIGN',
    'SEMICOLON',
    'COLON',
    'COMMA',

    'COMMENT',

    # main
    'PROGRAM',
    'DOT',

    # blocks
    'VAR',
    'VAL',
    'BEGIN',
    'END',

    # control flow
    'IF',
    'THEN',
    'ELSE',
    'FOR',
    'WHILE',
    'REPEAT',
    'UNTIL',
    'DO',
    'TO',
    'DOWNTO',

    # logic
    'AND',
    'OR',
    'NOT',
    'TRUE',
    'FALSE',

    # operations
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DIV',
    'MOD',
    'POWER',

    # comparations
    'EQ',
    'NEQ',
    'LT',
    'GT',
    'LE',
    'GE',

    # functions
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'PROCEDURE',
    'FUNCTION',

    # types
    'BOOLEAN',
    'INT',
    'STRING',
    'CHAR',
    'FLOAT',
    'VOID',
    'ARRAY',

    # types names
    'INT_TYPE',
    'BOOL_TYPE',
    'STRING_TYPE',
    'CHAR_TYPE',
    'FLOAT_TYPE',
    'VOID_TYPE'
)

# Expressões regulares para tokens simples

t_INT_TYPE = r'int'
t_FLOAT_TYPE = r'float'
t_BOOL_TYPE = r'boolean'
t_CHAR_TYPE = r'char'
t_STRING_TYPE = r'string'
t_VOID_TYPE = r'void'


t_FUNCTION = r'function'
t_WHILE = r'while'
t_IF = 'if'
t_ELSE = 'else'

t_ASSIGN = r':='
t_SEMICOLON = r';'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','

t_MOD = r'%'
t_AND = r'&&'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'

t_OR = r'\|\|'
t_NOT = r'!'
t_EQ = r'='
t_NEQ = r'!='
t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_DOT = r'\.'

reserved_keywords = {

    'function': 'FUNCTION',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'var':  'VAR',
    'val':  'VAL',
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'string': 'STRING_TYPE',
    'char': 'CHAR_TYPE',
    'void': 'VOID_TYPE',
    'boolean': 'BOOL_TYPE'
}

# Expressão regular para identificar inteiros com ou sem underscores
def t_INT(t):
    r'\d(_?\d)*'
    t.value = int(t.value.replace('_', ''))
    return t


# Expressão regular para identificar floats
def t_FLOAT(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


# Expressão regular para identificar strings
def t_STRING(t):
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    t.value = t.value[1:-1]  # Removendo as aspas
    return t

def t_CHAR(t):
    r"(\'([^\\\'])\')|(\"([^\\\"])\")"
    return t

def t_BOOLEAN(t):
    r'\b(true|false)\b'
    t.value = (t.value == 'true')  # Converta o valor para o tipo booleano do Python
    return t


# Expressão regular para identificar identificadores (variáveis e nomes de funções)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() in reserved_keywords:
        t.type = reserved_keywords[t.value.lower()]
    return t


# Ignorar espaços em branco e tabulações
t_ignore = ' \t'


# Ignorar comentários
def t_COMMENT(t):
    r'\#.*'
    pass

# Contador de número de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Tratamento de erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


if __name__ == '__main__':
    # Build the lexer
    from ply import lex
    import sys

    lexer = lex.lex()

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    else:
        data = ""
        while 1:
            try:
                data += raw_input() + "\n"
            except:
                break

    lexer.input(data)

    # Tokenize
    while 1:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

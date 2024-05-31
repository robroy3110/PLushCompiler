# Precedência e associação dos operadores
from ast_nodes import *

"""precedence = (
    ('nonassoc', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'MOD'),
    ('left', 'OR', 'AND'),
    ('right', 'UMINUS')
)"""
"""precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS'),  # Operador unário negativo
)"""
precedence = (
    ('nonassoc', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE', 'MOD'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'MOD'),
    ('left', 'OR', 'AND'),
    ('right', 'UMINUS')
)


# Regras de parsing
def p_program(p):
    """program : declarations"""
    p[0] = Program(p[1])


def p_declarations(p):
    """declarations : declaration declarations
                    | declaration"""
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


def p_declaration(p):
    """declaration : val_declaration
                   | var_declaration
                   | function_declaration
                  """
    p[0] = p[1]


def p_val_declaration(p):
    """val_declaration : VAL identifier COLON var_type ASSIGN expression SEMICOLON
                       | VAL identifier COLON var_type ASSIGN array_expression SEMICOLON"""
    p[0] = VariableDeclaration(p[2], p[4], True, p[6])


def p_var_declaration(p):
    """var_declaration : VAR identifier COLON var_type ASSIGN expression SEMICOLON
                       | VAR identifier COLON var_type ASSIGN array_expression SEMICOLON"""
    p[0] = VariableDeclaration(p[2], p[4], False, p[6])


def p_function_declaration(p):
    """function_declaration : function_declaration_body
                            | function_declaration_nobody"""
    p[0] = p[1]


def p_function_declaration_body(p):
    """function_declaration_body : FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type block"""
    p[0] = FunctionDeclaration(p[2], p[7], p[4], p[8])


def p_function_declaration_nobody(p):
    """function_declaration_nobody : FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type SEMICOLON"""
    p[0] = FunctionDeclaration(p[2], p[7], p[4])


def p_parameter_list(p):
    """ parameter_list : parameter COMMA parameter_list
                        | parameter
                        | empty"""
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_parameter(p):
    """ parameter : parameter_var
                  | parameter_val"""
    p[0] = p[1]


def p_parameter_var(p):
    """parameter_var : VAR identifier COLON var_type"""
    p[0] = VariableDeclaration(p[2], p[4], False)


def p_parameter_val(p):
    """parameter_val : VAL identifier COLON var_type"""
    p[0] = VariableDeclaration(p[2], p[4], True)


def p_block(p):
    """block : LBRACE statements RBRACE"""
    p[0] = p[2]


def p_statements(p):
    """statements : statement statements
                  | statement
                  | empty"""
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_statement(p):
    """statement : val_declaration
                 | var_declaration
                 | assignment_statement
                 | function_assignment
                 | if_statement
                 | while_statement
                 | function_call_statement
                 """
    p[0] = p[1]


def p_assignment_statement(p):
    """assignment_statement : identifier ASSIGN expression SEMICOLON"""
    p[0] = AssignmentStatement(p[1], p[3])


def p_function_assignment(p):
    """function_assignment : identifier ASSIGN block SEMICOLON"""
    p[0] = FunAssignmentStatement(p[1], p[3])


def p_function_call_statement(p):
    """function_call_statement : identifier LPAREN argument_list RPAREN SEMICOLON"""
    p[0] = FunCallStatement(p[1], p[3])


def p_argument_list(p):
    """argument_list : argument COMMA argument_list
                     | argument
                     | empty"""
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_argument(p):
    """argument : expression"""
    p[0] = p[1]


def p_if_statement(p):
    """if_statement : IF expression block
                    | IF expression block ELSE block"""
    if len(p) == 4:
        p[0] = IfStatement(p[2], p[3])
    else:
        p[0] = IfStatement(p[2], p[3], p[5])


def p_while_statement(p):
    """while_statement : WHILE expression block"""
    p[0] = WhileStatement(p[2], p[3])


def p_empty(p):
    """empty :"""
    pass


def p_expression(p):
    """expression : statement_expression"""
    p[0] = Expression(p[1])


def p_statement_expression(p):
    """statement_expression : statement_expression and_or expression_s
                            | expression_s"""
    if len(p) == 4:
        p[0] = AndOrOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]
#experimentar mudar o expression_s da priemira linha ora statenebt_exmrepssion


def p_and_or(p):
    """and_or : AND
              | OR"""
    p[0] = p[1]


def p_expression_s(p):
    """expression_s : expression_m csign expression_m
                    | expression_m"""
    if len(p) == 4:
        p[0] = CompareOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_expression_m(p):
    """expression_m : expression_m msign expression_l
                    | expression_l
                    | unary_expression_statement"""
    if len(p) == 4:
        p[0] = BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_expression_l(p):
    """expression_l : statement_literal
                    | identifier
                    | array_access
                    | LPAREN statement_expression RPAREN
                    | function_call_inline"""
    if isinstance(p[1], str) and (p[1] != '('):
        p[0] = IdentifierOp(p[1])
    elif len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_unary_expression_statement(p):
    """unary_expression_statement : unary_sign expression %prec UMINUS"""
    p[0] = UnaryOp(p[1], p[2])


def p_csign(p):
    """csign : EQ
            | NEQ
            | GT
            | GE
            | LT
            | LE
            """
    p[0] = p[1]


def p_msign(p):
    """msign : PLUS
            | MINUS
            | TIMES
            | DIVIDE
            | MOD
            | POWER
            """
    p[0] = p[1]


def p_statement_literal(p):
    """statement_literal : int
               | float
               | boolean
               | char
               | string"""
    p[0] = LiteralOp(p[1])


def p_unary_sign(p):
    """unary_sign : MINUS
                  | NOT"""
    p[0] = p[1]


def p_identifier(p):
    """identifier : IDENTIFIER"""
    p[0] = str(p[1]).lower()


def p_array_access(p):
    """array_access : identifier LBRACKET expression RBRACKET"""
    p[0] = ArrayAccessOp(p[1], p[3])


def p_function_call_inline(p):
    """function_call_inline : identifier LPAREN argument_list RPAREN"""
    p[0] = FunCallOp(p[1], p[3])


def p_array_expression(p):
    """array_expression : LBRACKET array_elements RBRACKET"""
    p[0] = ArrayExprOp(p[2])


def p_array_elements(p):
    """array_elements : expression COMMA array_elements
                      | expression"""
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]


def p_var_type(p):
    """var_type : type
                   | array_type
                   """
    p[0] = p[1]


def p_type(p):
    """type : INT_TYPE
                   | BOOL_TYPE
                   | STRING_TYPE
                   | CHAR_TYPE
                   | FLOAT_TYPE
                   | VOID_TYPE
                   """
    p[0] = p[1]


def p_array_type(p):
    """array_type : LBRACKET type RBRACKET"""
    p[0] = f"[{p[2]}]"


def p_int(p):
    """int : INT"""
    p[0] = Int(p[1])


def p_float(p):
    """float : FLOAT"""
    p[0] = Float(p[1])


def p_string(p):
    """string : STRING"""
    p[0] = String(p[1])


def p_char(p):
    """char : CHAR"""
    p[0] = Char(p[1])


def p_boolean(p):
    """boolean : BOOLEAN"""
    p[0] = Boolean(p[1])

# Tratamento de erros
def p_error(p):
    if p:
        print("Erro de sintaxe em '%s' na linha %d" % (p.value, p.lineno))
    else:
        print("Erro de sintaxe: fim inesperado do arquivo")

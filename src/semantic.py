from ast_nodes import *

types = ['int', 'float', 'char', 'string', 'boolean', 'void', '[int]', '[float]', '[char]', '[string]', '[boolean]']


class VarTable:
    def __init__(self, name=None):
        self.vars = {}
        self.name = name

    def add(self, name, vardetail):
        self.vars[name] = vardetail

    def has_var(self, name):
        return name in self.vars

    def get(self, name):
        return self.vars[name]

    def get_name(self):
        return self.name


class Var:
    def __init__(self, name, vartype, imutable):
        self.name = name
        self.vartype = vartype
        self.imutable = imutable


contexts = []
functions = {
    'print_int': ('void', [
        ("a", 'int')
    ]),
    'print_string': ('void', [
        ("a", 'string')
    ]),
    'print_float': ('void', [
        ("a", 'float')
    ]),
    'print_char': ('void', [
        ("a", 'char')
    ]),
    'print_boolean': ('void', [
        ("a", 'boolean')
    ])
}


def get_var(varn):
    var = varn.lower()
    for c in contexts[::-1]:
        if c.has_var(var):
            return c.get(var)
    raise Exception("Variable %s still wasn't declared" % var)


def get_var_type(var):
    if var not in types:
        return get_var(var)[0]
    else:
        return var


def add_var(varn, typ, imutabl):
    var = varn.lower()
    if var in functions and not contexts[-1].get_name() == var:
        raise Exception("A function called %s already exists" % var)
    if contexts[-1].has_var(var):
        raise Exception("Variable %s already defined" % var)
    else:
        contexts[-1].add(var, (typ.lower(), imutabl))


def check(node):
        if isinstance(node, Program):
            contexts.append(VarTable("global"))
            for declaration in node.declarations:
                check(declaration)
        elif isinstance(node, VariableDeclaration):
            var_name = node.varName
            var_type = node.varType

            if var_type not in types:
                raise Exception(f"Type mismatch: variable '{var_name}' doesn´t have a valid type")
            if var_type == 'void':
                raise Exception(f"Type mismatch: variable '{var_name}' cant be of type void")
            if node.varExpression is not None:
                expr_type = check(node.varExpression)
                if var_type != expr_type:
                    raise Exception(
                        f"Type mismatch: variable '{var_name}' expects type '{var_type}' but got '{expr_type}'")
            """if vartype.endswith("]"):
                if expressiontype != vartype.strip('[]'):
                    raise Exception(
                        "Variable %s is of type %s and does not support %s" % (varname, vartype, expressiontype))"""
            add_var(var_name, var_type, node.imutable)
        elif isinstance(node, FunctionDeclaration):
            fun_name = node.funName
            fun_type = node.funType
            if fun_name in functions:
                raise Exception(f"A function called {fun_name} already exists")
            if fun_type not in types:
                raise Exception(f"Type mismatch: function '{fun_name}' doesn´t have a valid type")
            args = []
            if len(node.parameters) > 0:
                for arg in node.parameters:
                    args.append((arg.varName,arg.varType))
            functions[fun_name] = (fun_type, args)
            contexts.append(VarTable(fun_name))
            add_var(fun_name, fun_type, False)
            for arg in node.parameters:
                check(arg)
            if len(node.block) > 0:
                for statement in node.block:
                    check(statement)
            contexts.pop()
        elif isinstance(node, IfStatement) or isinstance(node, WhileStatement):
            expression = check(node.expression)
            if expression != 'boolean':
                raise Exception(f"{node.__class__} expression has to be of type boolean but got {expression} instead")
            if len(node.block) > 0:
                contexts.append(VarTable())
                for statement in node.block:
                    check(statement)
                contexts.pop()
            if isinstance(node, IfStatement) and len(node.elseblock) > 0:
                contexts.append(VarTable())
                for statement in node.block:
                    check(statement)
                contexts.pop()
        elif isinstance(node, AssignmentStatement):
            var_name = node.varName
            var = get_var(var_name)

            if var_name in functions and var[0] == 'void':
                raise Exception("Function %s does not have a return type" % var_name)

            if var[1]:
                raise Exception("Variable %s is not mutable and its value can't be changed" % var_name)

            assgntype = check(node.expression)

            if var[0] != assgntype:
                raise Exception(f"Variable {var[0]} is of type and does not support {assgntype}")
        elif isinstance(node, FunAssignmentStatement):
            fun_name = node.funName
            if fun_name not in functions:
                raise Exception("Function %s is not defined" % fun_name)
            contexts.append(VarTable(fun_name))
            for statement in node.block:
                check(statement)
            contexts.pop()
        elif isinstance(node, FunCallStatement) or isinstance(node, FunCallOp):
            fun_name = node.funName
            if fun_name not in functions:
                raise Exception("Function %s is not defined" % fun_name)
            args = []
            for arg in node.arguments:
                args.append(check(arg.expression))

            functiontype, vargs = functions[fun_name]

            if len(args) != len(vargs):
                raise Exception("Function %s is expecting %d parameters and got %d" % (fun_name, len(vargs), len(args)))
            else:
                for i in range(len(vargs)):
                    if vargs[i][1] != args[i]:
                        raise Exception("Parameter #%d passed to function %s should be of type %s and not %s" % (
                            i + 1, fun_name, vargs[i][1], args[i]))
            return functiontype
        elif isinstance(node, Expression):
            return check(node.expression)
        elif isinstance(node, IdentifierOp):
            return get_var_type(node.id)
        elif isinstance(node, AndOrOp):
            left_type = check(node.left)
            right_type = check(node.right)
            if left_type != 'boolean' or right_type != 'boolean':
                raise TypeError("Logical operations require boolean operands")
            return 'boolean'
        elif isinstance(node, BinOp):
            left_type = check(node.left)
            right_type = check(node.right)
            if left_type == 'int' and right_type == 'int':
                return 'int'
            if left_type == 'float' and right_type == 'float':
                return 'float'
            raise TypeError("Arithmetic operations require integer operands")
        elif isinstance(node, CompareOp):
            left_type = check(node.left)
            right_type = check(node.right)
            if left_type != right_type:
                raise TypeError("Comparison operations require operands of the same type")
            return 'boolean'
        elif isinstance(node, UnaryOp):
            expr_type = check(node.expression)
            if node.sign == "-" and expr_type != "int" and expr_type != "float":
                raise Exception(f"Invalid type for unary negation: {expr_type}")
            elif node.sign == "!" and expr_type != "boolean":
                raise Exception(f"Invalid type for logical negation: {expr_type}")
            return expr_type
        elif isinstance(node, LiteralOp):
            if isinstance(node.type, Int):
                return "int"
            elif isinstance(node.type, Float):
                return "float"
            elif isinstance(node.type, Boolean):
                return "boolean"
            elif isinstance(node.type, Char):
                return "char"
            elif isinstance(node.type, String):
                return "string"
        elif isinstance(node, ArrayAccessOp):
            var_name = node.varName
            var = get_var(var_name)
            if var[0] not in ['[char]','[int]','[string]','[float]','[boolean]']:
                raise Exception(f"Variable {var_name} is not an array but is of type {var[0]}")
            expression_type = check(node.expression)
            if expression_type != 'int':
                raise Exception(f"Array position must be an int but got {expression_type} instead")
            return var[0].strip('[]')
        elif isinstance(node, ArrayExprOp):
            element_types = [check(elem.expression) for elem in node.array_elements]
            if len(set(element_types)) != 1:
                raise Exception(f"Array elements have inconsistent types: {element_types}")
            return f"[{element_types[0]}]"

        else:
            print("semantic missing:", node.type)

import re

from src.ast_nodes import *

program = (
    "program",
    [
        ("let", "a", ("literal", 1)),
        ("let", "k", ("var", "a")),
        ("let", "b", ("add", ("var", "a"), ("literal", 4))),
        (
            "do",
            [
                ("print", ("var", "b")),
                ("print", ("var", "a")),
                ("set", "a", ("add", ("var", "a"), ("literal", 1))),
            ],
            ("var", "a"),
            (("literal", 10)),
        ),
    ],
)


#TYPES: Int - i32
# Float - float
# Pointer - ptr
# Array - [4 x i32] (4 elementos de tipo int)
# Matrix - [ 3 x [4 x 32]]
# Structure - %T1 = type { <type list> }
#    Example: { i32, i32, i32 }  A triple of three i32 values
# Val(constants) - The two strings ‘true’ and ‘false’ are both valid constants of the i1 type.
# String - possivelmente i8*

#FALTA FAZER RETURN DA FUNÇAO FIZZBUZZ := 2

class Emitter(object):
    def __init__(self):
        self.count = 0
        self.global_count = 0
        self.lines = []
        self.global_lines = []
        self.declare_lines = []

    def get_count(self):
        self.count += 1
        return self.count

    def get_global_count(self):
        self.global_count += 1
        return self.global_count

    def get_id(self):
        id = self.get_count()
        return f"cas_{id}"

    def get_global_id(self):
        id = self.get_global_count()
        return f"str_{id}"

    def __lshift__(self, v):
        self.lines.append(v)

    def append(self, lines):
        if contexts[-1].get_name() == "global":
            self.lines.append(lines)
        else:
            self.global_lines.append(lines)

    def get_code(self):
        return "\n".join(self.declare_lines + self.lines + self.global_lines)

    def get_pointer_name(self, n):
        return f"%pont_{n}"


class VarTable:
    def __init__(self, name=None):
        self.vars = {}
        self.name = name

    def add(self, name, vtype):
        self.vars[name] = vtype

    def has_var(self, name):
        return name in self.vars

    def get(self, name):
        return self.vars[name]

    def get_name(self):
        return self.name


contexts = []
functions = {
    'print_int': ('void', [
        ("a", 'i32')
    ]),
    'print_string': ('void', [
        ("a", 'i8*')
    ]),
    'print_float': ('void', [
        ("a", 'float')
    ]),
    'print_char': ('void', [
        ("a", 'i8')
    ]),
    'print_boolean': ('void', [
        ("a", 'i1')
    ])
}


def get_var(varn):
    var = varn.lower()
    for c in contexts[::-1]:
        if c.has_var(var):
            return c.get(var)
    raise Exception("Variable %s still wasn't declared" % var)


def add_var(varn, typ):
    contexts[-1].add(varn, typ)


def varType(type_name):
    if type_name == "int":
        return "i32"
    elif type_name == "float":
        return "float"
    elif type_name == "string":
        return "i8*"
    elif type_name == "boolean":
        return "i1"
    elif type_name == "char":
        return "i8"
    else:
        raise ValueError(f"Unknown type: {type_name}")


def funType(type_name):
    if type_name == "int":
        return "i32"
    elif type_name == "float":
        return "float"
    elif type_name == "string":
        return "i8*"
    elif type_name == "boolean":
        return "i1"
    elif type_name == "char":
        return "i8"
    elif type_name == "void":
        return "void"
    else:
        raise ValueError(f"Unknown type: {type_name}")


def compilador(node, emitter=None):
    if isinstance(node, Program):
        emitter = Emitter()
        contexts.append(VarTable("global"))
        print_functions = """

define void @print_int(i32 %a) {
entry:
    %str = getelementptr inbounds [3 x i8], [3 x i8]* @.str_int, i32 0, i32 0
    call i32 (i8*, ...) @printf(i8* %str, i32 %a)
    ret void
}

define void @print_string(i8* %a) {
entry:
    %str = getelementptr inbounds [3 x i8], [3 x i8]* @.str_string, i32 0, i32 0
    call i32 (i8*, ...) @printf(i8* %str, i8* %a)
    ret void
}

define void @print_float(float %a) {
entry:
    %str = getelementptr inbounds [4 x i8], [4 x i8]* @.str_float, i32 0, i32 0
    call i32 (i8*, ...) @printf(i8* %str, float %a)
    ret void
}

define void @print_char(i8 %a) {
entry:
    %str = getelementptr inbounds [3 x i8], [3 x i8]* @.str_char, i32 0, i32 0
    call i32 (i8*, ...) @printf(i8* %str, i8 %a)
    ret void
}

define void @print_boolean(i1 %a) {
entry:
    %str_true = getelementptr inbounds [5 x i8], [5 x i8]* @.str_boolean_true, i32 0, i32 0
    %str_false = getelementptr inbounds [6 x i8], [6 x i8]* @.str_boolean_false, i32 0, i32 0
    %str = select i1 %a, i8* %str_true, i8* %str_false
    call i32 (i8*, ...) @printf(i8* %str)
    ret void
}"""

        powi32_function = """
define i32 @powi32(i32 %base, i32 %exp) {
entry:
    %is_zero_exp = icmp eq i32 %exp, 0
    br i1 %is_zero_exp, label %return_one, label %main_loop
return_one:
    ret i32 1
main_loop:
    %result = alloca i32, align 4
    store i32 1, i32* %result, align 4
    %b = alloca i32, align 4
    store i32 %base, i32* %b, align 4
    %e = alloca i32, align 4
    store i32 %exp, i32* %e, align 4
loop:
    %current_exp = load i32, i32* %e, align 4
    %is_exp_even = and i32 %current_exp, 1
    %is_exp_odd = icmp ne i32 %is_exp_even, 0
    br i1 %is_exp_odd, label %odd_case, label %even_case
odd_case:
    %current_result = load i32, i32* %result, align 4
    %current_base = load i32, i32* %b, align 4
    %new_result = mul i32 %current_result, %current_base
    store i32 %new_result, i32* %result, align 4
    br label %update_exp
even_case:
    br label %update_exp
update_exp:
    %current_exp2 = load i32, i32* %e, align 4
    %new_exp = ashr i32 %current_exp2, 1
    store i32 %new_exp, i32* %e, align 4
    %current_base2 = load i32, i32* %b, align 4
    %new_base = mul i32 %current_base2, %current_base2
    store i32 %new_base, i32* %b, align 4
    %updated_exp = load i32, i32* %e, align 4
    %is_exp_zero = icmp eq i32 %updated_exp, 0
    br i1 %is_exp_zero, label %end_loop, label %loop
end_loop:
    %final_result = load i32, i32* %result, align 4
    ret i32 %final_result
}
        """
        emitter.append(""" 
@.str_int = private unnamed_addr constant [3 x i8] c"%d\\00"
@.str_string = private unnamed_addr constant [3 x i8] c"%s\\00"
@.str_float = private unnamed_addr constant [4 x i8] c"%f\\00"
@.str_char = private unnamed_addr constant [3 x i8] c"%c\\00"
@.str_boolean_true = private unnamed_addr constant [5 x i8] c"true\\00"
@.str_boolean_false = private unnamed_addr constant [6 x i8] c"false\\00"
""")
        emitter.append("declare i32 @printf(i8*, ...)")
        emitter.append("declare i32 @powi32(i32, i32)")
        emitter.append("define i32 @main() #0 {")

        for decl in node.declarations:
            compilador(decl, emitter)

        emitter.append("   ret i32 0")
        emitter.append("}")

        emitter.append(powi32_function)
        emitter.append(print_functions)
        return emitter.get_code()
    elif isinstance(node, VariableDeclaration):
        vname = node.varName
        vtype = varType(node.varType)
        add_var(vname, vtype)
        expr = node.varExpression
        pname = emitter.get_pointer_name(vname)
        emitter.append(f"   {pname} = alloca {vtype}, align 4")
        registo = compilador(expr, emitter)
        emitter.append(f"   store {vtype} {registo}, {vtype}* {pname}, align 4")
    elif isinstance(node, FunctionDeclaration):
        fname = node.funName
        ftype = funType(node.funType)
        parameters = node.parameters
        paramList = []
        args = []
        contexts.append(VarTable(fname))
        add_var(fname, ftype)
        for parameter in parameters:
            paramList.append(f"{varType(parameter.varType)} %{parameter.varName}")
            args.append((varType(parameter.varType)))
            add_var(parameter.varName, varType(parameter.varType))
        paramString = ", ".join(paramList)
        declareString = re.sub(r' %[^,]*', '', paramString)
        functions[fname] = (ftype, args)
        emitter.declare_lines.append(f"declare {ftype} @{fname}({declareString})")
        emitter.append(f"define {ftype} @{fname}({paramString}) {{")
        for statement in node.block:
            compilador(statement, emitter)
        emitter.append("}")
        contexts.pop()
    elif isinstance(node, Expression):
        return compilador(node.expression, emitter)
    elif isinstance(node, IfStatement):
        # Evaluate the condition expression
        condition = compilador(node.expression, emitter)

        # Create labels for the then, else (if exists), and end blocks
        then_label = f"label_{emitter.get_id()}"
        else_label = f"label_{emitter.get_id()}" if node.elseblock else None
        end_label = f"label_{emitter.get_id()}"

        # Conditional branch based on the condition
        if else_label:
            emitter.append(f"  br i1 {condition}, label %{then_label}, label %{else_label}")
        else:
            emitter.append(f"  br i1 {condition}, label %{then_label}, label %{end_label}")

        # Then block
        emitter.append(f"{then_label}:")
        contexts.append(VarTable())
        for stmt in node.block:
            compilador(stmt, emitter)
        emitter.append(f"  br label %{end_label}")
        contexts.pop()
        # Else block
        if else_label:
            emitter.append(f"{else_label}:")
            contexts.append(VarTable())
            for stmt in node.elseblock:
                compilador(stmt, emitter)
            emitter.append(f"  br label %{end_label}")
            contexts.pop()
        # End block
        emitter.append(f"{end_label}:")
    elif isinstance(node, WhileStatement):
        # Generate labels for the start, body, and end of the while loop
        start_label = f"label_{emitter.get_id()}"
        body_label = f"label_{emitter.get_id()}"
        end_label = f"label_{emitter.get_id()}"

        # Start label for condition checking
        emitter.append(f"  br label %{start_label}")
        emitter.append(f"{start_label}:")

        # Evaluate the loop condition
        condition = compilador(node.expression, emitter)
        emitter.append(f"  br i1 {condition}, label %{body_label}, label %{end_label}")

        # Body of the loop
        emitter.append(f"{body_label}:")
        contexts.append(VarTable())
        for stmt in node.block:
            compilador(stmt, emitter)
        # Jump back to the start for the next iteration
        emitter.append(f"  br label %{start_label}")
        contexts.pop()
        # End of the loop
        emitter.append(f"{end_label}:")
        return
    elif isinstance(node, BinOp):
        left = compilador(node.left, emitter)
        right = compilador(node.right, emitter)
        result = f"%{emitter.get_id()}"
        if node.op == "+":
            emitter.append(f"  {result} = add i32 {left}, {right}")
        elif node.op == "-":
            emitter.append(f"  {result} = sub i32 {left}, {right}")
        elif node.op == "*":
            emitter.append(f"  {result} = mul i32 {left}, {right}")
        elif node.op == "/":
            emitter.append(f"  {result} = sdiv i32 {left}, {right}")
        elif node.op == "%":
            emitter.append(f"  {result} = srem i32 {left}, {right}")
        elif node.op == "**":
            emitter.append(f"  {result} = call i32 @powi32(i32 {left}, i32 {right})")
        else:
            raise ValueError(f"Operação não suportada: {node.op}")
        return result
    elif isinstance(node, CompareOp):
        left = compilador(node.left, emitter)
        right = compilador(node.right, emitter)
        cmp_result = f"%cmp{emitter.get_id()}"
        if node.op == "<":
            emitter.append(f"  {cmp_result} = icmp slt i32 {left}, {right}")
        elif node.op == ">":
            emitter.append(f"  {cmp_result} = icmp sgt i32 {left}, {right}")
        elif node.op == "=":
            emitter.append(f"  {cmp_result} = icmp eq i32 {left}, {right}")
        elif node.op == "<=":
            emitter.append(f"  {cmp_result} = icmp sle i32 {left}, {right}")
        elif node.op == ">=":
            emitter.append(f"  {cmp_result} = icmp sge i32 {left}, {right}")
        elif node.op == "!=":
            emitter.append(f"  {cmp_result} = icmp ne i32 {left}, {right}")
        return cmp_result
    elif isinstance(node, AndOrOp):
        left = compilador(node.left, emitter)

        if node.op == "&&":
            left_is_false = f"label_{emitter.get_id()}"
            evaluate_right = f"label_{emitter.get_id()}"
            end = f"label_{emitter.get_id()}"

            emitter.append(f"  br i1 {left}, label %{evaluate_right}, label %{left_is_false}")
            emitter.append(f"{evaluate_right}:")

            right_val = compilador(node.right, emitter)
            emitter.append(f"  br label %{end}")

            emitter.append(f"{left_is_false}:")
            false_result = "0"
            emitter.append(f"  br label %{end}")

            emitter.append(f"{end}:")
            final_result = f"%{emitter.get_id()}"
            emitter.append(f"  {final_result} = phi i1 [{right_val}, %{evaluate_right}], [{false_result}, %{left_is_false}]")
            return final_result

        elif node.op == "||":
            left_is_true = f"label_{emitter.get_id()}"
            evaluate_right = f"label_{emitter.get_id()}"
            end = f"label_{emitter.get_id()}"

            emitter.append(f"  br i1 {left}, label %{left_is_true}, label %{evaluate_right}")
            emitter.append(f"{left_is_true}:")
            true_result = "1"
            emitter.append(f"  br label %{end}")

            emitter.append(f"{evaluate_right}:")
            right_val = compilador(node.right, emitter)
            emitter.append(f"  br label %{end}")

            emitter.append(f"{end}:")
            final_result = f"%{emitter.get_id()}"
            emitter.append(f"  {final_result} = phi i1 [{true_result}, %{left_is_true}], [{right_val}, %{evaluate_right}]")
            return final_result
    elif isinstance(node, IdentifierOp):
        reg = f"%{emitter.get_id()}"
        pname = emitter.get_pointer_name(node.id)
        ptype = get_var(node.id)
        emitter.append(f"  {reg} = load {ptype}, {ptype}* {pname}")
        return reg
    elif isinstance(node, UnaryOp):
        expression = compilador(node.expression, emitter)
        result = f"%{emitter.get_id()}"
        if node.sign == "-":
            emitter.append(f"  {result} = sub i32 0, {expression}")

        elif node.sign == "!":
            temp = f"%{emitter.get_id()}"
            emitter.append(f"  {temp} = icmp eq i1 {expression}, 0")
            result = f"%{emitter.get_id()}"
            emitter.append(f"  {result} = zext i1 {temp} to i1")
        else:
            raise NotImplementedError(f"Unary operation '{node.sign}' not supported")
        return result
    elif isinstance(node, LiteralOp):
        if isinstance(node.type, Int):
            return str(node.type.value)
        elif isinstance(node.type, String):
            global_id = emitter.get_global_id()
            string_value = node.type.value
            string_length = len(string_value) + 1  # +1 para o caractere nulo terminador
            string_constant = f"@{global_id} = private unnamed_addr constant [{string_length} x i8] c\"{string_value}\\00\", align 1"
            emitter.declare_lines.append(string_constant)
            return f"getelementptr inbounds ([{string_length} x i8], [{string_length} x i8]* @{global_id}, i64 0, i64 0)"
        elif isinstance(node.type, Float):
            # Para floats, retorne o valor float formatado para LLVM
            return f"{node.type.value:.6f}"
        elif isinstance(node.type, Boolean):
            # Booleans em LLVM são representados como 1 (true) ou 0 (false)
            return "true" if node.type.value else "false"
        elif isinstance(node.type, Char):
            # Caracteres são tratados como inteiros em LLVM (ASCII value)
            return str(ord(node.type.value))
        elif isinstance(node.type, Array):
            # Arrays são mais complexos e precisam de manipulação de memória
            # Aqui você deve implementar a lógica para lidar com arrays
            pass
        else:
            raise NotImplementedError("Type not supported")
    elif isinstance(node, FunCallOp):
        fname = node.funName
        arguments = node.arguments
        arg_regs = []

        for i in range(len(arguments)):
            arg_reg = compilador(arguments[i], emitter)
            arg_regs.append((functions[fname][1][i], arg_reg))

        args_string = ", ".join([f"{arg[0]} {arg[1]}" for arg in arg_regs])
        result_reg = f"%{emitter.get_id()}"

        emitter.append(f"  {result_reg} = call {functions[fname][0]} @{fname}({args_string})")
        return result_reg
    elif isinstance(node, AssignmentStatement):
        var_name = node.varName
        expr_value = compilador(node.expression, emitter)  # Avalia a expressão
        vtype = get_var(var_name)
        if var_name == contexts[-1].get_name():
            emitter.append(f"  ret {vtype} {expr_value}")
        else:
            var_ptr = emitter.get_pointer_name(var_name)  # Obtém o ponteiro para a variável
            emitter.append(f"  store {vtype} {expr_value}, {vtype}* {var_ptr}, align 4")


if __name__ == "__main__":
    codigo_llvm = compilador(program)
    print(codigo_llvm)

    with open("code.ll", "w") as f:
        f.write(codigo_llvm)
    import subprocess

    # /usr/local/opt/llvm/bin/lli code.ll
    r = subprocess.call(
        "/usr/local/opt/llvm/bin/llc code.ll && clang code.s -o code && ./code",
        shell=True,
    )
    # print("Return code", r)

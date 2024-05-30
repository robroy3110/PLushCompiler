from abc import ABC
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ASTNode:
    pass


class Expr(ASTNode):
    pass


class Type(ASTNode):
    pass


class Statement(ASTNode):
    pass


class Declaration(Statement):
    pass


@dataclass
class Expression(Expr):
    expression: Expr


@dataclass
class BinOp(Expr):
    left: Expr
    op: str
    right: Expr


@dataclass
class AndOrOp(Expr):
    left: Expr
    op: str
    right: Expr


@dataclass
class CompareOp(Expr):
    left: Expr
    op: str
    right: Expr


@dataclass
class IdentifierOp(Expr):
    id: str


@dataclass
class UnaryOp(Expr):
    sign: str
    expression: Expr


@dataclass
class LiteralOp(Expr):
    type: Type


@dataclass
class ArrayAccessOp(Expr):
    varName: str
    expression: Expr


@dataclass
class ArrayExprOp(Expr):
    array_elements: List[Expression] = field(default_factory=list)


@dataclass
class FunCallOp(Expr):
    funName: str
    arguments: List[Expression] = field(default_factory=list)


@dataclass
class IfStatement(Statement):
    expression: Expression
    block: List[Statement] = field(default_factory=list)
    elseblock: List[Statement] = field(default_factory=list)


@dataclass
class WhileStatement(Statement):
    expression: Expression
    block: List[Statement] = field(default_factory=list)


@dataclass
class AssignmentStatement(Statement):
    varName: str
    expression: Expression


@dataclass
class FunAssignmentStatement(Statement):
    funName: str
    block: List[Statement] = field(default_factory=list)


@dataclass
class FunCallStatement(Statement):
    funName: str
    arguments: List[Expression] = field(default_factory=list)


@dataclass
class VariableDeclaration(Declaration):
    varName: str
    varType: str
    imutable: bool
    varExpression: Optional[Expression] = None


@dataclass
class FunctionDeclaration(Declaration):
    funName: str
    funType: str
    parameters: List[VariableDeclaration] = field(default_factory=list)
    block: List[Statement] = field(default_factory=list)


@dataclass
class Int(Type):
    value: int


@dataclass
class String(Type):
    value: str


@dataclass
class Float(Type):
    value: float


@dataclass
class Boolean(Type):
    value: bool


@dataclass
class Char(Type):
    value: str


@dataclass
class Array(Type):
    value: str


@dataclass
class Program(ASTNode):
    declarations: List[Declaration]



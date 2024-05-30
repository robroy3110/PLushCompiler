
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocEQNEQGTGELTLEMODleftPLUSMINUSleftTIMESDIVIDEleftMODleftORANDrightUMINUSAND ARRAY ASSIGN BEGIN BOOLEAN BOOL_TYPE CHAR CHAR_TYPE COLON COMMA COMMENT DIV DIVIDE DO DOT DOWNTO ELSE END EQ FALSE FLOAT FLOAT_TYPE FOR FUNCTION GE GT IDENTIFIER IF INT INT_TYPE LBRACE LBRACKET LE LPAREN LT MINUS MOD NEQ NOT OR PLUS POWER PROCEDURE PROGRAM RBRACE RBRACKET REPEAT RPAREN SEMICOLON STRING STRING_TYPE THEN TIMES TO TRUE UNTIL VAL VAR VOID VOID_TYPE WHILEprogram : declarationsdeclarations : declaration declarations\n                    | declarationdeclaration : val_declaration\n                   | var_declaration\n                   | function_declaration\n                  val_declaration : VAL identifier COLON var_type ASSIGN expression SEMICOLON\n                       | VAL identifier COLON var_type ASSIGN array_expression SEMICOLONvar_declaration : VAR identifier COLON var_type ASSIGN expression SEMICOLON\n                       | VAR identifier COLON var_type ASSIGN array_expression SEMICOLONfunction_declaration : function_declaration_body\n                            | function_declaration_nobodyfunction_declaration_body : FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type blockfunction_declaration_nobody : FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type SEMICOLON parameter_list : parameter COMMA parameter_list\n                        | parameter\n                        | empty parameter : parameter_var\n                  | parameter_valparameter_var : VAR identifier COLON var_typeparameter_val : VAL identifier COLON var_typeblock : LBRACE statements RBRACEstatements : statement statements\n                  | statement\n                  | emptystatement : val_declaration\n                 | var_declaration\n                 | assignment_statement\n                 | function_assignment\n                 | if_statement\n                 | while_statement\n                 | function_call_statement\n                 assignment_statement : identifier ASSIGN expression SEMICOLONfunction_assignment : identifier ASSIGN block SEMICOLONfunction_call_statement : identifier LPAREN argument_list RPAREN SEMICOLONargument_list : argument COMMA argument_list\n                     | argument\n                     | emptyargument : expressionif_statement : IF expression block\n                    | IF expression block ELSE blockwhile_statement : WHILE expression blockempty :expression : statement_expressionstatement_expression : statement_expression and_or expression_s\n                            | expression_sand_or : AND\n              | ORexpression_s : expression_m csign expression_m\n                    | expression_mexpression_m : expression_m msign expression_l\n                    | expression_l\n                    | unary_expression_statementexpression_l : statement_literal\n                    | identifier\n                    | array_access\n                    | LPAREN statement_expression RPAREN\n                    | function_call_inlineunary_expression_statement : unary_sign expression %prec UMINUScsign : EQ\n            | NEQ\n            | GT\n            | GE\n            | LT\n            | LE\n            msign : PLUS\n            | MINUS\n            | TIMES\n            | DIVIDE\n            | MOD\n            | POWER\n            statement_literal : int\n               | float\n               | boolean\n               | char\n               | stringunary_sign : MINUS\n                  | NOTidentifier : IDENTIFIERarray_access : identifier LBRACKET expression RBRACKETfunction_call_inline : identifier LPAREN argument_list RPARENarray_expression : LBRACKET array_elements RBRACKETarray_elements : expression COMMA array_elements\n                      | expressionvar_type : type\n                   | array_type\n                   type : INT_TYPE\n                   | BOOL_TYPE\n                   | STRING_TYPE\n                   | CHAR_TYPE\n                   | FLOAT_TYPE\n                   | VOID_TYPE\n                   array_type : LBRACKET type RBRACKETint : INTfloat : FLOATstring : STRINGchar : CHARboolean : BOOLEAN'
    
_lr_action_items = {'VAL':([0,3,4,5,6,9,10,19,42,80,81,103,104,119,120,121,127,129,130,131,132,133,134,135,140,149,150,151,152,155,156,],[7,7,-4,-5,-6,-11,-12,37,37,-7,-8,-9,-10,-13,-14,7,7,-26,-27,-28,-29,-30,-31,-32,-22,-40,-42,-33,-34,-35,-41,]),'VAR':([0,3,4,5,6,9,10,19,42,80,81,103,104,119,120,121,127,129,130,131,132,133,134,135,140,149,150,151,152,155,156,],[8,8,-4,-5,-6,-11,-12,36,36,-7,-8,-9,-10,-13,-14,8,8,-26,-27,-28,-29,-30,-31,-32,-22,-40,-42,-33,-34,-35,-41,]),'FUNCTION':([0,3,4,5,6,9,10,80,81,103,104,119,120,140,],[11,11,-4,-5,-6,-11,-12,-7,-8,-9,-10,-13,-14,-22,]),'$end':([1,2,3,4,5,6,9,10,12,80,81,103,104,119,120,140,],[0,-1,-3,-4,-5,-6,-11,-12,-2,-7,-8,-9,-10,-13,-14,-22,]),'IDENTIFIER':([7,8,11,36,37,38,40,49,56,58,64,65,78,79,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,115,121,124,127,129,130,131,132,133,134,135,137,138,140,142,143,149,150,151,152,155,156,],[14,14,14,14,14,14,14,14,14,14,-77,-78,14,14,-7,-8,14,-47,-48,14,14,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-9,-10,14,14,14,14,-26,-27,-28,-29,-30,-31,-32,14,14,-22,14,14,-40,-42,-33,-34,-35,-41,]),'COLON':([13,14,15,41,43,44,],[17,-79,18,74,76,77,]),'LPAREN':([14,16,38,40,45,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,136,137,138,142,143,],[-79,19,56,56,79,56,56,56,-77,-78,56,56,56,-47,-48,56,56,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,56,56,143,56,56,56,56,]),'LBRACKET':([14,17,18,38,40,45,74,76,77,],[-79,29,29,49,49,78,29,29,29,]),'EQ':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,89,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'NEQ':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,90,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'GT':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,91,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'GE':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,92,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'LT':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,93,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'LE':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,94,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,-49,-51,-57,-80,-81,]),'PLUS':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,95,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,95,-51,-57,-80,-81,]),'MINUS':([14,38,40,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,78,79,82,83,84,87,89,90,91,92,93,94,102,113,115,116,117,118,122,123,124,137,138,142,143,],[-79,64,64,-55,-44,64,-46,96,-52,-53,-54,-56,64,-58,64,-72,-73,-74,-75,-76,-77,-78,-94,-95,-98,-97,-96,64,64,64,-47,-48,64,-60,-61,-62,-63,-64,-65,-59,-45,64,96,-51,-57,-80,-81,64,64,64,64,64,]),'TIMES':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,97,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,97,-51,-57,-80,-81,]),'DIVIDE':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,98,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,98,-51,-57,-80,-81,]),'MOD':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,99,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,99,-51,-57,-80,-81,]),'POWER':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,102,113,116,117,118,122,123,],[-79,-55,-44,-46,100,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-59,-45,100,-51,-57,-80,-81,]),'AND':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,101,102,113,116,117,118,122,123,],[-79,-55,83,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,83,-59,-45,-49,-51,-57,-80,-81,]),'OR':([14,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,101,102,113,116,117,118,122,123,],[-79,-55,84,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,84,-59,-45,-49,-51,-57,-80,-81,]),'SEMICOLON':([14,21,22,23,24,25,26,27,28,45,46,47,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,71,72,73,102,105,113,114,116,117,118,122,123,140,146,147,153,],[-79,-85,-86,-87,-88,-89,-90,-91,-92,-55,80,81,-44,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-93,103,104,-59,120,-45,-82,-49,-51,-57,-80,-81,-22,151,152,155,]),'COMMA':([14,21,22,23,24,25,26,27,28,32,34,35,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,71,86,102,106,107,110,112,113,116,117,118,122,123,],[-79,-85,-86,-87,-88,-89,-90,-91,-92,42,-18,-19,-55,-44,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-93,115,-59,-20,-21,124,-39,-45,-49,-51,-57,-80,-81,]),'RBRACKET':([14,23,24,25,26,27,28,39,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,85,86,102,108,113,116,117,118,122,123,125,],[-79,-87,-88,-89,-90,-91,-92,71,-55,-44,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,114,-84,-59,122,-45,-49,-51,-57,-80,-81,-83,]),'RPAREN':([14,19,21,22,23,24,25,26,27,28,31,32,33,34,35,42,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,71,75,79,101,102,106,107,109,110,111,112,113,116,117,118,122,123,124,139,143,148,],[-79,-43,-85,-86,-87,-88,-89,-90,-91,-92,41,-16,-17,-18,-19,-43,-55,-44,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-93,-15,-43,118,-59,-20,-21,123,-37,-38,-39,-45,-49,-51,-57,-80,-81,-43,-36,-43,153,]),'LBRACE':([14,21,22,23,24,25,26,27,28,45,48,50,51,52,53,54,55,57,59,60,61,62,63,66,67,68,69,70,71,102,105,113,116,117,118,122,123,142,144,145,154,],[-79,-85,-86,-87,-88,-89,-90,-91,-92,-55,-44,-46,-50,-52,-53,-54,-56,-58,-72,-73,-74,-75,-76,-94,-95,-98,-97,-96,-93,-59,121,-45,-49,-51,-57,-80,-81,121,121,121,121,]),'ASSIGN':([14,20,21,22,23,24,25,26,27,28,30,71,136,],[-79,38,-85,-86,-87,-88,-89,-90,-91,-92,40,-93,142,]),'INT_TYPE':([17,18,29,74,76,77,],[23,23,23,23,23,23,]),'BOOL_TYPE':([17,18,29,74,76,77,],[24,24,24,24,24,24,]),'STRING_TYPE':([17,18,29,74,76,77,],[25,25,25,25,25,25,]),'CHAR_TYPE':([17,18,29,74,76,77,],[26,26,26,26,26,26,]),'FLOAT_TYPE':([17,18,29,74,76,77,],[27,27,27,27,27,27,]),'VOID_TYPE':([17,18,29,74,76,77,],[28,28,28,28,28,28,]),'NOT':([38,40,49,56,58,64,65,78,79,82,83,84,87,89,90,91,92,93,94,115,124,137,138,142,143,],[65,65,65,65,65,-77,-78,65,65,65,-47,-48,65,-60,-61,-62,-63,-64,-65,65,65,65,65,65,65,]),'INT':([38,40,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,137,138,142,143,],[66,66,66,66,66,-77,-78,66,66,66,-47,-48,66,66,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,66,66,66,66,66,66,]),'FLOAT':([38,40,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,137,138,142,143,],[67,67,67,67,67,-77,-78,67,67,67,-47,-48,67,67,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,67,67,67,67,67,67,]),'BOOLEAN':([38,40,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,137,138,142,143,],[68,68,68,68,68,-77,-78,68,68,68,-47,-48,68,68,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,68,68,68,68,68,68,]),'CHAR':([38,40,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,137,138,142,143,],[69,69,69,69,69,-77,-78,69,69,69,-47,-48,69,69,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,69,69,69,69,69,69,]),'STRING':([38,40,49,56,58,64,65,78,79,82,83,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,115,124,137,138,142,143,],[70,70,70,70,70,-77,-78,70,70,70,-47,-48,70,70,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,70,70,70,70,70,70,]),'IF':([80,81,103,104,121,127,129,130,131,132,133,134,135,140,149,150,151,152,155,156,],[-7,-8,-9,-10,137,137,-26,-27,-28,-29,-30,-31,-32,-22,-40,-42,-33,-34,-35,-41,]),'WHILE':([80,81,103,104,121,127,129,130,131,132,133,134,135,140,149,150,151,152,155,156,],[-7,-8,-9,-10,138,138,-26,-27,-28,-29,-30,-31,-32,-22,-40,-42,-33,-34,-35,-41,]),'RBRACE':([80,81,103,104,121,126,127,128,129,130,131,132,133,134,135,140,141,149,150,151,152,155,156,],[-7,-8,-9,-10,-43,140,-24,-25,-26,-27,-28,-29,-30,-31,-32,-22,-23,-40,-42,-33,-34,-35,-41,]),'ELSE':([140,149,],[-22,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([0,3,],[2,12,]),'declaration':([0,3,],[3,3,]),'val_declaration':([0,3,121,127,],[4,4,129,129,]),'var_declaration':([0,3,121,127,],[5,5,130,130,]),'function_declaration':([0,3,],[6,6,]),'function_declaration_body':([0,3,],[9,9,]),'function_declaration_nobody':([0,3,],[10,10,]),'identifier':([7,8,11,36,37,38,40,49,56,58,78,79,82,87,88,115,121,124,127,137,138,142,143,],[13,15,16,43,44,45,45,45,45,45,45,45,45,45,45,45,136,45,136,45,45,45,45,]),'var_type':([17,18,74,76,77,],[20,30,105,106,107,]),'type':([17,18,29,74,76,77,],[21,21,39,21,21,21,]),'array_type':([17,18,74,76,77,],[22,22,22,22,22,]),'parameter_list':([19,42,],[31,75,]),'parameter':([19,42,],[32,32,]),'empty':([19,42,79,121,124,127,143,],[33,33,111,128,111,128,111,]),'parameter_var':([19,42,],[34,34,]),'parameter_val':([19,42,],[35,35,]),'expression':([38,40,49,58,78,79,115,124,137,138,142,143,],[46,72,86,102,108,112,86,112,144,145,146,112,]),'array_expression':([38,40,],[47,73,]),'statement_expression':([38,40,49,56,58,78,79,115,124,137,138,142,143,],[48,48,48,101,48,48,48,48,48,48,48,48,48,]),'expression_s':([38,40,49,56,58,78,79,82,115,124,137,138,142,143,],[50,50,50,50,50,50,50,113,50,50,50,50,50,50,]),'expression_m':([38,40,49,56,58,78,79,82,87,115,124,137,138,142,143,],[51,51,51,51,51,51,51,51,116,51,51,51,51,51,51,]),'expression_l':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[52,52,52,52,52,52,52,52,52,117,52,52,52,52,52,52,]),'unary_expression_statement':([38,40,49,56,58,78,79,82,87,115,124,137,138,142,143,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'statement_literal':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'array_access':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'function_call_inline':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'unary_sign':([38,40,49,56,58,78,79,82,87,115,124,137,138,142,143,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'int':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'float':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'boolean':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'char':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'string':([38,40,49,56,58,78,79,82,87,88,115,124,137,138,142,143,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'and_or':([48,101,],[82,82,]),'array_elements':([49,115,],[85,125,]),'csign':([51,],[87,]),'msign':([51,116,],[88,88,]),'argument_list':([79,124,143,],[109,139,148,]),'argument':([79,124,143,],[110,110,110,]),'block':([105,142,144,145,154,],[119,147,149,150,156,]),'statements':([121,127,],[126,141,]),'statement':([121,127,],[127,127,]),'assignment_statement':([121,127,],[131,131,]),'function_assignment':([121,127,],[132,132,]),'if_statement':([121,127,],[133,133,]),'while_statement':([121,127,],[134,134,]),'function_call_statement':([121,127,],[135,135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarations','program',1,'p_program','rules.py',33),
  ('declarations -> declaration declarations','declarations',2,'p_declarations','rules.py',38),
  ('declarations -> declaration','declarations',1,'p_declarations','rules.py',39),
  ('declaration -> val_declaration','declaration',1,'p_declaration','rules.py',47),
  ('declaration -> var_declaration','declaration',1,'p_declaration','rules.py',48),
  ('declaration -> function_declaration','declaration',1,'p_declaration','rules.py',49),
  ('val_declaration -> VAL identifier COLON var_type ASSIGN expression SEMICOLON','val_declaration',7,'p_val_declaration','rules.py',55),
  ('val_declaration -> VAL identifier COLON var_type ASSIGN array_expression SEMICOLON','val_declaration',7,'p_val_declaration','rules.py',56),
  ('var_declaration -> VAR identifier COLON var_type ASSIGN expression SEMICOLON','var_declaration',7,'p_var_declaration','rules.py',61),
  ('var_declaration -> VAR identifier COLON var_type ASSIGN array_expression SEMICOLON','var_declaration',7,'p_var_declaration','rules.py',62),
  ('function_declaration -> function_declaration_body','function_declaration',1,'p_function_declaration','rules.py',67),
  ('function_declaration -> function_declaration_nobody','function_declaration',1,'p_function_declaration','rules.py',68),
  ('function_declaration_body -> FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type block','function_declaration_body',8,'p_function_declaration_body','rules.py',73),
  ('function_declaration_nobody -> FUNCTION identifier LPAREN parameter_list RPAREN COLON var_type SEMICOLON','function_declaration_nobody',8,'p_function_declaration_nobody','rules.py',78),
  ('parameter_list -> parameter COMMA parameter_list','parameter_list',3,'p_parameter_list','rules.py',83),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','rules.py',84),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','rules.py',85),
  ('parameter -> parameter_var','parameter',1,'p_parameter','rules.py',95),
  ('parameter -> parameter_val','parameter',1,'p_parameter','rules.py',96),
  ('parameter_var -> VAR identifier COLON var_type','parameter_var',4,'p_parameter_var','rules.py',101),
  ('parameter_val -> VAL identifier COLON var_type','parameter_val',4,'p_parameter_val','rules.py',106),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','rules.py',111),
  ('statements -> statement statements','statements',2,'p_statements','rules.py',116),
  ('statements -> statement','statements',1,'p_statements','rules.py',117),
  ('statements -> empty','statements',1,'p_statements','rules.py',118),
  ('statement -> val_declaration','statement',1,'p_statement','rules.py',128),
  ('statement -> var_declaration','statement',1,'p_statement','rules.py',129),
  ('statement -> assignment_statement','statement',1,'p_statement','rules.py',130),
  ('statement -> function_assignment','statement',1,'p_statement','rules.py',131),
  ('statement -> if_statement','statement',1,'p_statement','rules.py',132),
  ('statement -> while_statement','statement',1,'p_statement','rules.py',133),
  ('statement -> function_call_statement','statement',1,'p_statement','rules.py',134),
  ('assignment_statement -> identifier ASSIGN expression SEMICOLON','assignment_statement',4,'p_assignment_statement','rules.py',140),
  ('function_assignment -> identifier ASSIGN block SEMICOLON','function_assignment',4,'p_function_assignment','rules.py',145),
  ('function_call_statement -> identifier LPAREN argument_list RPAREN SEMICOLON','function_call_statement',5,'p_function_call_statement','rules.py',150),
  ('argument_list -> argument COMMA argument_list','argument_list',3,'p_argument_list','rules.py',155),
  ('argument_list -> argument','argument_list',1,'p_argument_list','rules.py',156),
  ('argument_list -> empty','argument_list',1,'p_argument_list','rules.py',157),
  ('argument -> expression','argument',1,'p_argument','rules.py',167),
  ('if_statement -> IF expression block','if_statement',3,'p_if_statement','rules.py',172),
  ('if_statement -> IF expression block ELSE block','if_statement',5,'p_if_statement','rules.py',173),
  ('while_statement -> WHILE expression block','while_statement',3,'p_while_statement','rules.py',181),
  ('empty -> <empty>','empty',0,'p_empty','rules.py',186),
  ('expression -> statement_expression','expression',1,'p_expression','rules.py',191),
  ('statement_expression -> statement_expression and_or expression_s','statement_expression',3,'p_statement_expression','rules.py',196),
  ('statement_expression -> expression_s','statement_expression',1,'p_statement_expression','rules.py',197),
  ('and_or -> AND','and_or',1,'p_and_or','rules.py',206),
  ('and_or -> OR','and_or',1,'p_and_or','rules.py',207),
  ('expression_s -> expression_m csign expression_m','expression_s',3,'p_expression_s','rules.py',212),
  ('expression_s -> expression_m','expression_s',1,'p_expression_s','rules.py',213),
  ('expression_m -> expression_m msign expression_l','expression_m',3,'p_expression_m','rules.py',221),
  ('expression_m -> expression_l','expression_m',1,'p_expression_m','rules.py',222),
  ('expression_m -> unary_expression_statement','expression_m',1,'p_expression_m','rules.py',223),
  ('expression_l -> statement_literal','expression_l',1,'p_expression_l','rules.py',231),
  ('expression_l -> identifier','expression_l',1,'p_expression_l','rules.py',232),
  ('expression_l -> array_access','expression_l',1,'p_expression_l','rules.py',233),
  ('expression_l -> LPAREN statement_expression RPAREN','expression_l',3,'p_expression_l','rules.py',234),
  ('expression_l -> function_call_inline','expression_l',1,'p_expression_l','rules.py',235),
  ('unary_expression_statement -> unary_sign expression','unary_expression_statement',2,'p_unary_expression_statement','rules.py',245),
  ('csign -> EQ','csign',1,'p_csign','rules.py',250),
  ('csign -> NEQ','csign',1,'p_csign','rules.py',251),
  ('csign -> GT','csign',1,'p_csign','rules.py',252),
  ('csign -> GE','csign',1,'p_csign','rules.py',253),
  ('csign -> LT','csign',1,'p_csign','rules.py',254),
  ('csign -> LE','csign',1,'p_csign','rules.py',255),
  ('msign -> PLUS','msign',1,'p_msign','rules.py',261),
  ('msign -> MINUS','msign',1,'p_msign','rules.py',262),
  ('msign -> TIMES','msign',1,'p_msign','rules.py',263),
  ('msign -> DIVIDE','msign',1,'p_msign','rules.py',264),
  ('msign -> MOD','msign',1,'p_msign','rules.py',265),
  ('msign -> POWER','msign',1,'p_msign','rules.py',266),
  ('statement_literal -> int','statement_literal',1,'p_statement_literal','rules.py',272),
  ('statement_literal -> float','statement_literal',1,'p_statement_literal','rules.py',273),
  ('statement_literal -> boolean','statement_literal',1,'p_statement_literal','rules.py',274),
  ('statement_literal -> char','statement_literal',1,'p_statement_literal','rules.py',275),
  ('statement_literal -> string','statement_literal',1,'p_statement_literal','rules.py',276),
  ('unary_sign -> MINUS','unary_sign',1,'p_unary_sign','rules.py',281),
  ('unary_sign -> NOT','unary_sign',1,'p_unary_sign','rules.py',282),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','rules.py',287),
  ('array_access -> identifier LBRACKET expression RBRACKET','array_access',4,'p_array_access','rules.py',292),
  ('function_call_inline -> identifier LPAREN argument_list RPAREN','function_call_inline',4,'p_function_call_inline','rules.py',297),
  ('array_expression -> LBRACKET array_elements RBRACKET','array_expression',3,'p_array_expression','rules.py',302),
  ('array_elements -> expression COMMA array_elements','array_elements',3,'p_array_elements','rules.py',307),
  ('array_elements -> expression','array_elements',1,'p_array_elements','rules.py',308),
  ('var_type -> type','var_type',1,'p_var_type','rules.py',316),
  ('var_type -> array_type','var_type',1,'p_var_type','rules.py',317),
  ('type -> INT_TYPE','type',1,'p_type','rules.py',323),
  ('type -> BOOL_TYPE','type',1,'p_type','rules.py',324),
  ('type -> STRING_TYPE','type',1,'p_type','rules.py',325),
  ('type -> CHAR_TYPE','type',1,'p_type','rules.py',326),
  ('type -> FLOAT_TYPE','type',1,'p_type','rules.py',327),
  ('type -> VOID_TYPE','type',1,'p_type','rules.py',328),
  ('array_type -> LBRACKET type RBRACKET','array_type',3,'p_array_type','rules.py',334),
  ('int -> INT','int',1,'p_int','rules.py',339),
  ('float -> FLOAT','float',1,'p_float','rules.py',344),
  ('string -> STRING','string',1,'p_string','rules.py',349),
  ('char -> CHAR','char',1,'p_char','rules.py',354),
  ('boolean -> BOOLEAN','boolean',1,'p_boolean','rules.py',359),
]

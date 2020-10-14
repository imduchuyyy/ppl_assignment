/**
 * Student Name: Bùi Đức Huy, Student ID: 1812336
 */
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

program: (var_declare | func_declare)? EOF;

// VARIABLE DECLARE
var_declare: VAR COLON ids_list SEMI;

ids_list: (id_declare) (COMMA id_declare)*;

id_declare: ID | (ID ASSIGN type_list) | array_declare;

array_declare: ARRAY_ID | (ARRAY_ID ASSIGN ARRAY);

ARRAY_ID: ID (LSB INTLIT RSB)+;

type_list: INTLIT | FLOATLIT | BOOLEAN | STRINGLIT;

// FUNCTION DECLARE
func_declare: header_stm (paramater_stm)? body_stm;

header_stm: FUNCTION COLON ID;
paramater_stm: PARAMETER COLON paramater_list;
paramater_list: (ID | ARRAY_ID) (COMMA paramater_list)
	| (ID | ARRAY_ID);
body_stm: BODY COLON statement_list ENDBODY DOT;
statement_list: statement (statement_list) | statement;

statement:
	var_declare
	| func_declare
	| if_statement
	| for_statement
	| while_statement
	| break_statement
	| continue_statement
	| function_call_statement
	| return_statement;

// IF STATEMENT
if_statement:
	IF expressions THEN statement_list (else_if_statement)? (
		else_statement
	)? ENDIF DOT;
else_if_statement:
	ELSEIF expressions THEN statement_list (else_if_statement)
	| (ELSEIF expressions THEN statement_list);
else_statement: ELSE statement_list;

// FOR STATEMENT
for_statement:
	FOR LB for_condition RB DO statement_list ENDFOR DOT;
for_condition: ((ID | ARRAY_ID) ASSIGN expressions) COMMA expressions COMMA (
		(ID | ARRAY_ID) ASSIGN expressions
	);

// WHILE STATEMENT
while_statement:
	WHILE expressions DO statement_list ENDWHILE DOT;

// DO WHILE STATEMENT
do_while_statement:
	DO statement_list WHILE expressions ENDWHILE DOT;

// BREAK STATEMENT
break_statement: BREAK SEMI;

// CONTINUE STATEMENT
continue_statement: CONTINUE SEMI;

// FUNCTION CALL STATEMENT
function_call_statement:
	ID LB expressions? (COMMA expressions)* RB SEMI;

// RETUNR STATEMENT
return_statement: RETURN expressions SEMI;

expressions:
	exp1 EQUALOP exp1
	| exp1 NOTEQUALOP exp1
	| exp1 LESSOP exp1
	| exp1 LESSOREQUALOP exp1
	| exp1 GREATEROP exp1
	| exp1 GREATEOREQUALOP exp1
	| exp1 NOTEQUALOPFLOAT exp1
	| exp1 LESSOPDOT exp1
	| exp1 LESSOREQUALOPDOT exp1
	| exp1 GREATEROPDOT exp1
	| exp1 GREATEOREQUALOPDOT exp1;
exp1: exp1 ANDOP exp2 | exp1 OROP exp2 | exp2;
exp2:
	exp2 ADDOP exp3
	| exp2 ADDOPDOT exp3
	| exp2 SUBOP exp3
	| exp2 SUBOPDOT exp3
	| exp3;
exp3:
	exp3 MULOP exp4
	| exp3 MULOPDOT exp4
	| exp3 DIVOP exp4
	| exp3 DIVOPDOT exp4
	| exp3 MODOP exp4
	| exp4;
exp4: NOTOP operand | operand;
operand:
	type_list
	| ID
	| sub_expression
	| ARRAY_ID
	| function_call
	| index_operator;

sub_expression: LB expressions RB;
function_call: ID LB list_expression? RB;
list_expression: type_list ( COMMA list_expression)*;
index_operator: ID LSB expressions RSB;
// IDENTIFIER
ID: [a-z][a-zA-Z0-9_]*;

// KEYWORD
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';

// OPERATORS
ASSIGN: '=';

ADDOP: '+';
ADDOPDOT: '+.';

SUBOP: '-';
SUBOPDOT: '-.';

MULOP: '*';
MULOPDOT: '*.';

DIVOP: '/';
DIVOPDOT: '/.';

MODOP: '%';

NOTOP: '!';
OROP: '||';
ANDOP: '&&';

EQUALOP: '==';

NOTEQUALOP: '!=';
NOTEQUALOPFLOAT: '=/=';

LESSOP: '<';
LESSOPDOT: '<.';

GREATEROP: '>';
GREATEROPDOT: '>.';

LESSOREQUALOP: '<=';
LESSOREQUALOPDOT: '<=.';

GREATEOREQUALOP: '>=';
GREATEOREQUALOPDOT: '>=.';

// SEPARATOR
LB: '(';
RB: ')';

LSB: '[';
RSB: ']';

COLON: ':';
DOT: '.';
COMMA: ',';
SEMI: ';';

LP: '{';
RP: '}';

// LITERALS
INTLIT: DEC | HEX | OCT;
fragment DEC: ([1-9][0-9]+) | [0-9];
fragment HEX: ([0][Xx][0-9]+) | ([0][Xx][A-F]+);
fragment OCT: [0][Oo][0-7]+;

SUBFLOATLIT: INTLIT [Ee]? [+-]? INTLIT?;
FLOATLIT: SUBFLOATLIT '.' SUBFLOATLIT?;

BOOLEAN: TRUE | FALSE;

// STRING
STRINGLIT:
	'"' STR_CHAR* '"' {
        self.text = self.text[1:-1];
    };
fragment STR_CHAR: STR_CHAR_NORMAL | STR_CHAR_QUOTE;
fragment STR_CHAR_NORMAL: ~[\b\t\n\f\r'"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [btnfr'\\];
fragment STR_CHAR_QUOTE: '\'"';

fragment INTLIT_LIST: INTLIT (COMMA INTLIT)*;
fragment FLOATLIT_LIST: FLOATLIT (COMMA FLOATLIT)*;
fragment STRING_LIST: STRINGLIT ( COMMA STRINGLIT)*;
fragment BOOLEAN_LIST: BOOLEAN (COMMA BOOLEAN)*;

ARRAY: (LP INTLIT_LIST RP)
	| ( LP FLOATLIT_LIST RP)
	| ( LP STRING_LIST RP)
	| ( LP BOOLEAN_LIST RP);
// fail

WS: [ \t\r\n]+ -> skip;
COMMENT: '**' .*? '**' -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (STR_CHAR)* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
	UNCLOSE_STRING '\\' ~([brnft] | '"' | '\\') { raise IllegalEscape(self.text[1:])};
UNTERMINATED_COMMENT: .;
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

program: (var_declare | func_declare)* EOF;

var_declare: VAR COLON ids_list SEMI;

ids_list: (id_declare) (COMMA id_declare)*;

id_declare: ID | (ID ASSIGN TYPE_LIST) | array_declare;

array_declare: ARRAY_ID | (ARRAY_ID ASSIGN ARRAY);

ARRAY_ID: ID (LSB INTLIT RSB)+;

TYPE_LIST: INTLIT | FLOATLIT | BOOLEAN | STRING;

func_declare: header_stm paramater_stm body_stm;

header_stm: FUNCTION COLON ID;
paramater_stm: PARAMETER COLON ids_list;
body_stm: BODY COLON ENDBODY DOT;

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
ENDDO: 'ENDDO';

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
DEC: [1-9][0-9]* | '0';
HEX: '0' [Xx][0-9][A-F]+;
OCT: '0' [Oo][0-7]+;
INTLIT: DEC | HEX | OCT;

SUBFLOATLIT: INTLIT [Ee]? [+-]? INTLIT;
FLOATLIT: SUBFLOATLIT '.' SUBFLOATLIT;

BOOLEAN: TRUE | FALSE;

STRING:;

INTLIT_LIST: INTLIT (COMMA INTLIT)*;
FLOATLIT_LIST: FLOATLIT (COMMA FLOATLIT)*;
STRING_LIST: STRING ( COMMA STRING)*;
BOOLEAN_LIST: BOOLEAN (COMMA BOOLEAN)*;

ARRAY: (LP INTLIT_LIST RP)
	| ( LP FLOATLIT_LIST RP)
	| ( LP STRING_LIST RP)
	| ( LP BOOLEAN_LIST RP); // fail

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
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

program: ID;

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
ENDDO: 'ENDO';

// OPERATORS
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
DEC: [1-9][0-9]+ | '0';
HEX: '0' [Xx][0-9][A-F]+;
OCT: '0' [Oo][0-7]+;
INILIT: DEC | HEX | OCT;

SUBFLOATLIT: INILIT [Ee]? [+-]? INILIT;
FLOATLIT: SUBFLOATLIT '.' SUBFLOATLIT;

BOOLEAN: TRUE | FALSE;

STRING:;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
# Generated from d:\Documents\Bach Khoa\PPL\Assignment\Assignment 1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\3\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'ENDO'", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'/'", "'/.'", "'%'", "'!'", 
                     "'||'", "'&&'", "'=='", "'!='", "'=/='", "'<'", "'<.'", 
                     "'>'", "'>.'", "'<='", "'<=.'", "'>='", "'>=.'", "'('", 
                     "')'", "'['", "']'", "':'", "'.'", "','", "';'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADDOP", 
                      "ADDOPDOT", "SUBOP", "SUBOPDOT", "MULOP", "MULOPDOT", 
                      "DIVOP", "DIVOPDOT", "MODOP", "NOTOP", "OROP", "ANDOP", 
                      "EQUALOP", "NOTEQUALOP", "NOTEQUALOPFLOAT", "LESSOP", 
                      "LESSOPDOT", "GREATEROP", "GREATEROPDOT", "LESSOREQUALOP", 
                      "LESSOREQUALOPDOT", "GREATEOREQUALOP", "GREATEOREQUALOPDOT", 
                      "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", 
                      "SEMI", "LP", "RP", "DEC", "HEX", "OCT", "INILIT", 
                      "SUBFLOATLIT", "FLOATLIT", "BOOLEAN", "STRING", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    ADDOP=23
    ADDOPDOT=24
    SUBOP=25
    SUBOPDOT=26
    MULOP=27
    MULOPDOT=28
    DIVOP=29
    DIVOPDOT=30
    MODOP=31
    NOTOP=32
    OROP=33
    ANDOP=34
    EQUALOP=35
    NOTEQUALOP=36
    NOTEQUALOPFLOAT=37
    LESSOP=38
    LESSOPDOT=39
    GREATEROP=40
    GREATEROPDOT=41
    LESSOREQUALOP=42
    LESSOREQUALOPDOT=43
    GREATEOREQUALOP=44
    GREATEOREQUALOPDOT=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    COLON=50
    DOT=51
    COMMA=52
    SEMI=53
    LP=54
    RP=55
    DEC=56
    HEX=57
    OCT=58
    INILIT=59
    SUBFLOATLIT=60
    FLOATLIT=61
    BOOLEAN=62
    STRING=63
    WS=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    UNTERMINATED_COMMENT=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






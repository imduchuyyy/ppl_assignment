# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3N")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\7\2\27\n\2\f\2\16\2\32\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4&\n\4\f")
        buf.write("\4\16\4)\13\4\3\5\3\5\3\5\3\5\3\5\5\5\60\n\5\3\6\3\6\3")
        buf.write("\6\3\6\5\6\66\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n")
        buf.write("\f\16\20\22\2\2\2E\2\30\3\2\2\2\4\35\3\2\2\2\6\"\3\2\2")
        buf.write("\2\b/\3\2\2\2\n\65\3\2\2\2\f\67\3\2\2\2\16;\3\2\2\2\20")
        buf.write("?\3\2\2\2\22C\3\2\2\2\24\27\5\4\3\2\25\27\5\f\7\2\26\24")
        buf.write("\3\2\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30")
        buf.write("\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\7\2\2\3")
        buf.write("\34\3\3\2\2\2\35\36\7\26\2\2\36\37\7\67\2\2\37 \5\6\4")
        buf.write("\2 !\7:\2\2!\5\3\2\2\2\"\'\5\b\5\2#$\79\2\2$&\5\b\5\2")
        buf.write("%#\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\7\3\2\2\2")
        buf.write(")\'\3\2\2\2*\60\7\5\2\2+,\7\5\2\2,-\7\33\2\2-\60\7\4\2")
        buf.write("\2.\60\5\n\6\2/*\3\2\2\2/+\3\2\2\2/.\3\2\2\2\60\t\3\2")
        buf.write("\2\2\61\66\7\3\2\2\62\63\7\3\2\2\63\64\7\33\2\2\64\66")
        buf.write("\7I\2\2\65\61\3\2\2\2\65\62\3\2\2\2\66\13\3\2\2\2\678")
        buf.write("\5\16\b\289\5\20\t\29:\5\22\n\2:\r\3\2\2\2;<\7\21\2\2")
        buf.write("<=\7\67\2\2=>\7\5\2\2>\17\3\2\2\2?@\7\23\2\2@A\7\67\2")
        buf.write("\2AB\5\6\4\2B\21\3\2\2\2CD\7\6\2\2DE\7\67\2\2EF\7\f\2")
        buf.write("\2FG\78\2\2G\23\3\2\2\2\7\26\30\'/\65")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'ENDDO'", "'='", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
                     "'*.'", "'/'", "'/.'", "'%'", "'!'", "'||'", "'&&'", 
                     "'=='", "'!='", "'=/='", "'<'", "'<.'", "'>'", "'>.'", 
                     "'<='", "'<=.'", "'>='", "'>=.'", "'('", "')'", "'['", 
                     "']'", "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ARRAY_ID", "TYPE_LIST", "ID", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "TRUE", "FALSE", "ENDDO", "ASSIGN", "ADDOP", "ADDOPDOT", 
                      "SUBOP", "SUBOPDOT", "MULOP", "MULOPDOT", "DIVOP", 
                      "DIVOPDOT", "MODOP", "NOTOP", "OROP", "ANDOP", "EQUALOP", 
                      "NOTEQUALOP", "NOTEQUALOPFLOAT", "LESSOP", "LESSOPDOT", 
                      "GREATEROP", "GREATEROPDOT", "LESSOREQUALOP", "LESSOREQUALOPDOT", 
                      "GREATEOREQUALOP", "GREATEOREQUALOPDOT", "LB", "RB", 
                      "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "LP", 
                      "RP", "DEC", "HEX", "OCT", "INTLIT", "SUBFLOATLIT", 
                      "FLOATLIT", "BOOLEAN", "STRING", "INTLIT_LIST", "FLOATLIT_LIST", 
                      "STRING_LIST", "BOOLEAN_LIST", "ARRAY", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_ids_list = 2
    RULE_id_declare = 3
    RULE_array_declare = 4
    RULE_func_declare = 5
    RULE_header_stm = 6
    RULE_paramater_stm = 7
    RULE_body_stm = 8

    ruleNames =  [ "program", "var_declare", "ids_list", "id_declare", "array_declare", 
                   "func_declare", "header_stm", "paramater_stm", "body_stm" ]

    EOF = Token.EOF
    ARRAY_ID=1
    TYPE_LIST=2
    ID=3
    BODY=4
    BREAK=5
    CONTINUE=6
    DO=7
    ELSE=8
    ELSEIF=9
    ENDBODY=10
    ENDIF=11
    ENDFOR=12
    ENDWHILE=13
    FOR=14
    FUNCTION=15
    IF=16
    PARAMETER=17
    RETURN=18
    THEN=19
    VAR=20
    WHILE=21
    TRUE=22
    FALSE=23
    ENDDO=24
    ASSIGN=25
    ADDOP=26
    ADDOPDOT=27
    SUBOP=28
    SUBOPDOT=29
    MULOP=30
    MULOPDOT=31
    DIVOP=32
    DIVOPDOT=33
    MODOP=34
    NOTOP=35
    OROP=36
    ANDOP=37
    EQUALOP=38
    NOTEQUALOP=39
    NOTEQUALOPFLOAT=40
    LESSOP=41
    LESSOPDOT=42
    GREATEROP=43
    GREATEROPDOT=44
    LESSOREQUALOP=45
    LESSOREQUALOPDOT=46
    GREATEOREQUALOP=47
    GREATEOREQUALOPDOT=48
    LB=49
    RB=50
    LSB=51
    RSB=52
    COLON=53
    DOT=54
    COMMA=55
    SEMI=56
    LP=57
    RP=58
    DEC=59
    HEX=60
    OCT=61
    INTLIT=62
    SUBFLOATLIT=63
    FLOATLIT=64
    BOOLEAN=65
    STRING=66
    INTLIT_LIST=67
    FLOATLIT_LIST=68
    STRING_LIST=69
    BOOLEAN_LIST=70
    ARRAY=71
    WS=72
    ERROR_CHAR=73
    UNCLOSE_STRING=74
    ILLEGAL_ESCAPE=75
    UNTERMINATED_COMMENT=76

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def func_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION or _la==BKITParser.VAR:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 18
                    self.var_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 19
                    self.func_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(BKITParser.VAR)
            self.state = 28
            self.match(BKITParser.COLON)
            self.state = 29
            self.ids_list()
            self.state = 30
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Id_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Id_declareContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.id_declare()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 33
                self.match(BKITParser.COMMA)
                self.state = 34
                self.id_declare()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def TYPE_LIST(self):
            return self.getToken(BKITParser.TYPE_LIST, 0)

        def array_declare(self):
            return self.getTypedRuleContext(BKITParser.Array_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_declare" ):
                return visitor.visitId_declare(self)
            else:
                return visitor.visitChildren(self)




    def id_declare(self):

        localctx = BKITParser.Id_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id_declare)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(BKITParser.ID)
                self.state = 42
                self.match(BKITParser.ASSIGN)
                self.state = 43
                self.match(BKITParser.TYPE_LIST)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.array_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_ID(self):
            return self.getToken(BKITParser.ARRAY_ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def ARRAY(self):
            return self.getToken(BKITParser.ARRAY, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = BKITParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_declare)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(BKITParser.ARRAY_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(BKITParser.ARRAY_ID)
                self.state = 49
                self.match(BKITParser.ASSIGN)
                self.state = 50
                self.match(BKITParser.ARRAY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header_stm(self):
            return self.getTypedRuleContext(BKITParser.Header_stmContext,0)


        def paramater_stm(self):
            return self.getTypedRuleContext(BKITParser.Paramater_stmContext,0)


        def body_stm(self):
            return self.getTypedRuleContext(BKITParser.Body_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.header_stm()
            self.state = 54
            self.paramater_stm()
            self.state = 55
            self.body_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_header_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader_stm" ):
                return visitor.visitHeader_stm(self)
            else:
                return visitor.visitChildren(self)




    def header_stm(self):

        localctx = BKITParser.Header_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_header_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(BKITParser.FUNCTION)
            self.state = 58
            self.match(BKITParser.COLON)
            self.state = 59
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamater_stm" ):
                return visitor.visitParamater_stm(self)
            else:
                return visitor.visitChildren(self)




    def paramater_stm(self):

        localctx = BKITParser.Paramater_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramater_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(BKITParser.PARAMETER)
            self.state = 62
            self.match(BKITParser.COLON)
            self.state = 63
            self.ids_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_stm" ):
                return visitor.visitBody_stm(self)
            else:
                return visitor.visitChildren(self)




    def body_stm(self):

        localctx = BKITParser.Body_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(BKITParser.BODY)
            self.state = 66
            self.match(BKITParser.COLON)
            self.state = 67
            self.match(BKITParser.ENDBODY)
            self.state = 68
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






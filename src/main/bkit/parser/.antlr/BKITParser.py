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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0191\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\7\2M\n\2\f\2\16\2P\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\7\4\\\n\4\f\4\16\4_\13\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5f\n\5\3\6\3\6\3\6\3\6\5\6l\n\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7r\n\7\3\b\3\b\5\bv\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0087\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\7\r\u0090\n\r\f\r\16\r\u0093")
        buf.write("\13\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00a2\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u00ae\n\21\3\21\5\21")
        buf.write("\u00b1\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u00c1\n\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00db\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\5\32\u00f4\n\32\3\32\3\32\7")
        buf.write("\32\u00f8\n\32\f\32\16\32\u00fb\13\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u0131\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u013c\n\35\f\35")
        buf.write("\16\35\u013f\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0150\n")
        buf.write("\36\f\36\16\36\u0153\13\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u0167\n\37\f\37\16\37\u016a\13\37\3 \3")
        buf.write(" \3 \5 \u016f\n \3!\3!\3!\3!\3!\3!\5!\u0177\n!\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\5#\u0180\n#\3#\3#\3$\3$\3$\7$\u0187")
        buf.write("\n$\f$\16$\u018a\13$\3%\3%\3%\3%\3%\3%\2\58:<&\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFH\2\4\3\2\27\30\3\2\3\4\2\u01a6\2N\3\2\2\2\4S\3")
        buf.write("\2\2\2\6X\3\2\2\2\be\3\2\2\2\nk\3\2\2\2\fq\3\2\2\2\16")
        buf.write("s\3\2\2\2\20y\3\2\2\2\22}\3\2\2\2\24\u0086\3\2\2\2\26")
        buf.write("\u0088\3\2\2\2\30\u0091\3\2\2\2\32\u0094\3\2\2\2\34\u00a1")
        buf.write("\3\2\2\2\36\u00a3\3\2\2\2 \u00a8\3\2\2\2\"\u00c0\3\2\2")
        buf.write("\2$\u00c2\3\2\2\2&\u00c5\3\2\2\2(\u00ce\3\2\2\2*\u00dc")
        buf.write("\3\2\2\2,\u00e3\3\2\2\2.\u00ea\3\2\2\2\60\u00ed\3\2\2")
        buf.write("\2\62\u00f0\3\2\2\2\64\u00ff\3\2\2\2\66\u0130\3\2\2\2")
        buf.write("8\u0132\3\2\2\2:\u0140\3\2\2\2<\u0154\3\2\2\2>\u016e\3")
        buf.write("\2\2\2@\u0176\3\2\2\2B\u0178\3\2\2\2D\u017c\3\2\2\2F\u0183")
        buf.write("\3\2\2\2H\u018b\3\2\2\2JM\5\4\3\2KM\5\16\b\2LJ\3\2\2\2")
        buf.write("LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3")
        buf.write("\2\2\2QR\7\2\2\3R\3\3\2\2\2ST\7\25\2\2TU\7\66\2\2UV\5")
        buf.write("\6\4\2VW\79\2\2W\5\3\2\2\2X]\5\b\5\2YZ\78\2\2Z\\\5\b\5")
        buf.write("\2[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\7\3\2\2\2")
        buf.write("_]\3\2\2\2`f\7\4\2\2ab\7\4\2\2bc\7\32\2\2cf\5\f\7\2df")
        buf.write("\5\n\6\2e`\3\2\2\2ea\3\2\2\2ed\3\2\2\2f\t\3\2\2\2gl\7")
        buf.write("\3\2\2hi\7\3\2\2ij\7\32\2\2jl\7?\2\2kg\3\2\2\2kh\3\2\2")
        buf.write("\2l\13\3\2\2\2mr\7<\2\2nr\7=\2\2or\t\2\2\2pr\7>\2\2qm")
        buf.write("\3\2\2\2qn\3\2\2\2qo\3\2\2\2qp\3\2\2\2r\r\3\2\2\2su\5")
        buf.write("\20\t\2tv\5\22\n\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\5\26")
        buf.write("\f\2x\17\3\2\2\2yz\7\20\2\2z{\7\66\2\2{|\7\4\2\2|\21\3")
        buf.write("\2\2\2}~\7\22\2\2~\177\7\66\2\2\177\u0080\5\24\13\2\u0080")
        buf.write("\23\3\2\2\2\u0081\u0082\5\32\16\2\u0082\u0083\78\2\2\u0083")
        buf.write("\u0084\5\24\13\2\u0084\u0087\3\2\2\2\u0085\u0087\5\32")
        buf.write("\16\2\u0086\u0081\3\2\2\2\u0086\u0085\3\2\2\2\u0087\25")
        buf.write("\3\2\2\2\u0088\u0089\7\5\2\2\u0089\u008a\7\66\2\2\u008a")
        buf.write("\u008b\5\30\r\2\u008b\u008c\7\13\2\2\u008c\u008d\7\67")
        buf.write("\2\2\u008d\27\3\2\2\2\u008e\u0090\5\34\17\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\31\3\2\2\2\u0093\u0091\3\2\2\2\u0094")
        buf.write("\u0095\t\3\2\2\u0095\33\3\2\2\2\u0096\u00a2\5\4\3\2\u0097")
        buf.write("\u00a2\5\16\b\2\u0098\u00a2\5\36\20\2\u0099\u00a2\5 \21")
        buf.write("\2\u009a\u00a2\5&\24\2\u009b\u00a2\5*\26\2\u009c\u00a2")
        buf.write("\5,\27\2\u009d\u00a2\5.\30\2\u009e\u00a2\5\60\31\2\u009f")
        buf.write("\u00a2\5\62\32\2\u00a0\u00a2\5\64\33\2\u00a1\u0096\3\2")
        buf.write("\2\2\u00a1\u0097\3\2\2\2\u00a1\u0098\3\2\2\2\u00a1\u0099")
        buf.write("\3\2\2\2\u00a1\u009a\3\2\2\2\u00a1\u009b\3\2\2\2\u00a1")
        buf.write("\u009c\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009e\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\35\3\2")
        buf.write("\2\2\u00a3\u00a4\5\32\16\2\u00a4\u00a5\7\32\2\2\u00a5")
        buf.write("\u00a6\5\66\34\2\u00a6\u00a7\79\2\2\u00a7\37\3\2\2\2\u00a8")
        buf.write("\u00a9\7\21\2\2\u00a9\u00aa\5\66\34\2\u00aa\u00ab\7\24")
        buf.write("\2\2\u00ab\u00ad\5\30\r\2\u00ac\u00ae\5\"\22\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af")
        buf.write("\u00b1\5$\23\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\f\2\2\u00b3\u00b4\7")
        buf.write("\67\2\2\u00b4!\3\2\2\2\u00b5\u00b6\7\n\2\2\u00b6\u00b7")
        buf.write("\5\66\34\2\u00b7\u00b8\7\24\2\2\u00b8\u00b9\5\30\r\2\u00b9")
        buf.write("\u00ba\5\"\22\2\u00ba\u00c1\3\2\2\2\u00bb\u00bc\7\n\2")
        buf.write("\2\u00bc\u00bd\5\66\34\2\u00bd\u00be\7\24\2\2\u00be\u00bf")
        buf.write("\5\30\r\2\u00bf\u00c1\3\2\2\2\u00c0\u00b5\3\2\2\2\u00c0")
        buf.write("\u00bb\3\2\2\2\u00c1#\3\2\2\2\u00c2\u00c3\7\t\2\2\u00c3")
        buf.write("\u00c4\5\30\r\2\u00c4%\3\2\2\2\u00c5\u00c6\7\17\2\2\u00c6")
        buf.write("\u00c7\7\62\2\2\u00c7\u00c8\5(\25\2\u00c8\u00c9\7\63\2")
        buf.write("\2\u00c9\u00ca\7\b\2\2\u00ca\u00cb\5\30\r\2\u00cb\u00cc")
        buf.write("\7\r\2\2\u00cc\u00cd\7\67\2\2\u00cd\'\3\2\2\2\u00ce\u00cf")
        buf.write("\5\32\16\2\u00cf\u00d0\7\32\2\2\u00d0\u00d1\5\66\34\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\u00d3\78\2\2\u00d3\u00d4\5")
        buf.write("\66\34\2\u00d4\u00da\78\2\2\u00d5\u00d6\5\32\16\2\u00d6")
        buf.write("\u00d7\7\32\2\2\u00d7\u00d8\5\66\34\2\u00d8\u00db\3\2")
        buf.write("\2\2\u00d9\u00db\5\66\34\2\u00da\u00d5\3\2\2\2\u00da\u00d9")
        buf.write("\3\2\2\2\u00db)\3\2\2\2\u00dc\u00dd\7\26\2\2\u00dd\u00de")
        buf.write("\5\66\34\2\u00de\u00df\7\b\2\2\u00df\u00e0\5\30\r\2\u00e0")
        buf.write("\u00e1\7\16\2\2\u00e1\u00e2\7\67\2\2\u00e2+\3\2\2\2\u00e3")
        buf.write("\u00e4\7\b\2\2\u00e4\u00e5\5\30\r\2\u00e5\u00e6\7\26\2")
        buf.write("\2\u00e6\u00e7\5\66\34\2\u00e7\u00e8\7\16\2\2\u00e8\u00e9")
        buf.write("\7\67\2\2\u00e9-\3\2\2\2\u00ea\u00eb\7\6\2\2\u00eb\u00ec")
        buf.write("\79\2\2\u00ec/\3\2\2\2\u00ed\u00ee\7\7\2\2\u00ee\u00ef")
        buf.write("\79\2\2\u00ef\61\3\2\2\2\u00f0\u00f1\7\4\2\2\u00f1\u00f3")
        buf.write("\7\62\2\2\u00f2\u00f4\5\66\34\2\u00f3\u00f2\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6\78\2\2")
        buf.write("\u00f6\u00f8\5\66\34\2\u00f7\u00f5\3\2\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7\63\2")
        buf.write("\2\u00fd\u00fe\79\2\2\u00fe\63\3\2\2\2\u00ff\u0100\7\23")
        buf.write("\2\2\u0100\u0101\5\66\34\2\u0101\u0102\79\2\2\u0102\65")
        buf.write("\3\2\2\2\u0103\u0104\58\35\2\u0104\u0105\7\'\2\2\u0105")
        buf.write("\u0106\58\35\2\u0106\u0131\3\2\2\2\u0107\u0108\58\35\2")
        buf.write("\u0108\u0109\7(\2\2\u0109\u010a\58\35\2\u010a\u0131\3")
        buf.write("\2\2\2\u010b\u010c\58\35\2\u010c\u010d\7*\2\2\u010d\u010e")
        buf.write("\58\35\2\u010e\u0131\3\2\2\2\u010f\u0110\58\35\2\u0110")
        buf.write("\u0111\7.\2\2\u0111\u0112\58\35\2\u0112\u0131\3\2\2\2")
        buf.write("\u0113\u0114\58\35\2\u0114\u0115\7,\2\2\u0115\u0116\5")
        buf.write("8\35\2\u0116\u0131\3\2\2\2\u0117\u0118\58\35\2\u0118\u0119")
        buf.write("\7\60\2\2\u0119\u011a\58\35\2\u011a\u0131\3\2\2\2\u011b")
        buf.write("\u011c\58\35\2\u011c\u011d\7)\2\2\u011d\u011e\58\35\2")
        buf.write("\u011e\u0131\3\2\2\2\u011f\u0120\58\35\2\u0120\u0121\7")
        buf.write("+\2\2\u0121\u0122\58\35\2\u0122\u0131\3\2\2\2\u0123\u0124")
        buf.write("\58\35\2\u0124\u0125\7/\2\2\u0125\u0126\58\35\2\u0126")
        buf.write("\u0131\3\2\2\2\u0127\u0128\58\35\2\u0128\u0129\7-\2\2")
        buf.write("\u0129\u012a\58\35\2\u012a\u0131\3\2\2\2\u012b\u012c\5")
        buf.write("8\35\2\u012c\u012d\7\61\2\2\u012d\u012e\58\35\2\u012e")
        buf.write("\u0131\3\2\2\2\u012f\u0131\58\35\2\u0130\u0103\3\2\2\2")
        buf.write("\u0130\u0107\3\2\2\2\u0130\u010b\3\2\2\2\u0130\u010f\3")
        buf.write("\2\2\2\u0130\u0113\3\2\2\2\u0130\u0117\3\2\2\2\u0130\u011b")
        buf.write("\3\2\2\2\u0130\u011f\3\2\2\2\u0130\u0123\3\2\2\2\u0130")
        buf.write("\u0127\3\2\2\2\u0130\u012b\3\2\2\2\u0130\u012f\3\2\2\2")
        buf.write("\u0131\67\3\2\2\2\u0132\u0133\b\35\1\2\u0133\u0134\5:")
        buf.write("\36\2\u0134\u013d\3\2\2\2\u0135\u0136\f\5\2\2\u0136\u0137")
        buf.write("\7&\2\2\u0137\u013c\5:\36\2\u0138\u0139\f\4\2\2\u0139")
        buf.write("\u013a\7%\2\2\u013a\u013c\5:\36\2\u013b\u0135\3\2\2\2")
        buf.write("\u013b\u0138\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013d\u013e\3\2\2\2\u013e9\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\b\36\1\2\u0141\u0142\5<\37\2\u0142")
        buf.write("\u0151\3\2\2\2\u0143\u0144\f\7\2\2\u0144\u0145\7\33\2")
        buf.write("\2\u0145\u0150\5<\37\2\u0146\u0147\f\6\2\2\u0147\u0148")
        buf.write("\7\34\2\2\u0148\u0150\5<\37\2\u0149\u014a\f\5\2\2\u014a")
        buf.write("\u014b\7\35\2\2\u014b\u0150\5<\37\2\u014c\u014d\f\4\2")
        buf.write("\2\u014d\u014e\7\36\2\2\u014e\u0150\5<\37\2\u014f\u0143")
        buf.write("\3\2\2\2\u014f\u0146\3\2\2\2\u014f\u0149\3\2\2\2\u014f")
        buf.write("\u014c\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0152\3\2\2\2\u0152;\3\2\2\2\u0153\u0151\3\2\2")
        buf.write("\2\u0154\u0155\b\37\1\2\u0155\u0156\5> \2\u0156\u0168")
        buf.write("\3\2\2\2\u0157\u0158\f\b\2\2\u0158\u0159\7\37\2\2\u0159")
        buf.write("\u0167\5> \2\u015a\u015b\f\7\2\2\u015b\u015c\7 \2\2\u015c")
        buf.write("\u0167\5> \2\u015d\u015e\f\6\2\2\u015e\u015f\7!\2\2\u015f")
        buf.write("\u0167\5> \2\u0160\u0161\f\5\2\2\u0161\u0162\7\"\2\2\u0162")
        buf.write("\u0167\5> \2\u0163\u0164\f\4\2\2\u0164\u0165\7#\2\2\u0165")
        buf.write("\u0167\5> \2\u0166\u0157\3\2\2\2\u0166\u015a\3\2\2\2\u0166")
        buf.write("\u015d\3\2\2\2\u0166\u0160\3\2\2\2\u0166\u0163\3\2\2\2")
        buf.write("\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169=\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c")
        buf.write("\7$\2\2\u016c\u016f\5@!\2\u016d\u016f\5@!\2\u016e\u016b")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f?\3\2\2\2\u0170\u0177")
        buf.write("\5\f\7\2\u0171\u0177\7\4\2\2\u0172\u0177\5B\"\2\u0173")
        buf.write("\u0177\7\3\2\2\u0174\u0177\5D#\2\u0175\u0177\5H%\2\u0176")
        buf.write("\u0170\3\2\2\2\u0176\u0171\3\2\2\2\u0176\u0172\3\2\2\2")
        buf.write("\u0176\u0173\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3")
        buf.write("\2\2\2\u0177A\3\2\2\2\u0178\u0179\7\62\2\2\u0179\u017a")
        buf.write("\5\66\34\2\u017a\u017b\7\63\2\2\u017bC\3\2\2\2\u017c\u017d")
        buf.write("\7\4\2\2\u017d\u017f\7\62\2\2\u017e\u0180\5F$\2\u017f")
        buf.write("\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\7\63\2\2\u0182E\3\2\2\2\u0183\u0188\5\f\7")
        buf.write("\2\u0184\u0185\78\2\2\u0185\u0187\5F$\2\u0186\u0184\3")
        buf.write("\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189G\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c")
        buf.write("\7\4\2\2\u018c\u018d\7\64\2\2\u018d\u018e\5\66\34\2\u018e")
        buf.write("\u018f\7\65\2\2\u018fI\3\2\2\2\35LN]ekqu\u0086\u0091\u00a1")
        buf.write("\u00ad\u00b0\u00c0\u00da\u00f3\u00f9\u0130\u013b\u013d")
        buf.write("\u014f\u0151\u0166\u0168\u016e\u0176\u017f\u0188")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
                     "'While'", "'True'", "'False'", "'EndDo'", "'='", "'+'", 
                     "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'/'", "'/.'", 
                     "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'=/='", 
                     "'<'", "'<.'", "'>'", "'>.'", "'<='", "'<=.'", "'>='", 
                     "'>=.'", "'('", "')'", "'['", "']'", "':'", "'.'", 
                     "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ARRAY_ID", "ID", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "ASSIGN", "ADDOP", "ADDOPDOT", "SUBOP", "SUBOPDOT", 
                      "MULOP", "MULOPDOT", "DIVOP", "DIVOPDOT", "MODOP", 
                      "NOTOP", "OROP", "ANDOP", "EQUALOP", "NOTEQUALOP", 
                      "NOTEQUALOPFLOAT", "LESSOP", "LESSOPDOT", "GREATEROP", 
                      "GREATEROPDOT", "LESSOREQUALOP", "LESSOREQUALOPDOT", 
                      "GREATEOREQUALOP", "GREATEOREQUALOPDOT", "LB", "RB", 
                      "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "LP", 
                      "RP", "INTLIT", "FLOATLIT", "STRINGLIT", "ARRAY", 
                      "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_ids_list = 2
    RULE_id_declare = 3
    RULE_array_declare = 4
    RULE_type_list = 5
    RULE_func_declare = 6
    RULE_header_stm = 7
    RULE_paramater_stm = 8
    RULE_paramater_list = 9
    RULE_body_stm = 10
    RULE_statement_list = 11
    RULE_id_var = 12
    RULE_statement = 13
    RULE_assign_statement = 14
    RULE_if_statement = 15
    RULE_else_if_statement = 16
    RULE_else_statement = 17
    RULE_for_statement = 18
    RULE_for_condition = 19
    RULE_while_statement = 20
    RULE_do_while_statement = 21
    RULE_break_statement = 22
    RULE_continue_statement = 23
    RULE_function_call_statement = 24
    RULE_return_statement = 25
    RULE_expressions = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_operand = 31
    RULE_sub_expression = 32
    RULE_function_call = 33
    RULE_list_expression = 34
    RULE_index_operator = 35

    ruleNames =  [ "program", "var_declare", "ids_list", "id_declare", "array_declare", 
                   "type_list", "func_declare", "header_stm", "paramater_stm", 
                   "paramater_list", "body_stm", "statement_list", "id_var", 
                   "statement", "assign_statement", "if_statement", "else_if_statement", 
                   "else_statement", "for_statement", "for_condition", "while_statement", 
                   "do_while_statement", "break_statement", "continue_statement", 
                   "function_call_statement", "return_statement", "expressions", 
                   "exp1", "exp2", "exp3", "exp4", "operand", "sub_expression", 
                   "function_call", "list_expression", "index_operator" ]

    EOF = Token.EOF
    ARRAY_ID=1
    ID=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    FUNCTION=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    VAR=19
    WHILE=20
    TRUE=21
    FALSE=22
    ENDDO=23
    ASSIGN=24
    ADDOP=25
    ADDOPDOT=26
    SUBOP=27
    SUBOPDOT=28
    MULOP=29
    MULOPDOT=30
    DIVOP=31
    DIVOPDOT=32
    MODOP=33
    NOTOP=34
    OROP=35
    ANDOP=36
    EQUALOP=37
    NOTEQUALOP=38
    NOTEQUALOPFLOAT=39
    LESSOP=40
    LESSOPDOT=41
    GREATEROP=42
    GREATEROPDOT=43
    LESSOREQUALOP=44
    LESSOREQUALOPDOT=45
    GREATEOREQUALOP=46
    GREATEOREQUALOPDOT=47
    LB=48
    RB=49
    LSB=50
    RSB=51
    COLON=52
    DOT=53
    COMMA=54
    SEMI=55
    LP=56
    RP=57
    INTLIT=58
    FLOATLIT=59
    STRINGLIT=60
    ARRAY=61
    WS=62
    COMMENT=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    UNTERMINATED_COMMENT=67

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




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION or _la==BKITParser.VAR:
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 72
                    self.var_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 73
                    self.func_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
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




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(BKITParser.VAR)
            self.state = 82
            self.match(BKITParser.COLON)
            self.state = 83
            self.ids_list()
            self.state = 84
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




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.id_declare()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 87
                self.match(BKITParser.COMMA)
                self.state = 88
                self.id_declare()
                self.state = 93
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

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def array_declare(self):
            return self.getTypedRuleContext(BKITParser.Array_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_id_declare




    def id_declare(self):

        localctx = BKITParser.Id_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id_declare)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(BKITParser.ID)
                self.state = 96
                self.match(BKITParser.ASSIGN)
                self.state = 97
                self.type_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
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




    def array_declare(self):

        localctx = BKITParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_declare)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(BKITParser.ARRAY_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(BKITParser.ARRAY_ID)
                self.state = 103
                self.match(BKITParser.ASSIGN)
                self.state = 104
                self.match(BKITParser.ARRAY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_type_list




    def type_list(self):

        localctx = BKITParser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.match(BKITParser.STRINGLIT)
                pass
            else:
                raise NoViableAltException(self)

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


        def body_stm(self):
            return self.getTypedRuleContext(BKITParser.Body_stmContext,0)


        def paramater_stm(self):
            return self.getTypedRuleContext(BKITParser.Paramater_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.header_stm()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 114
                self.paramater_stm()


            self.state = 117
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




    def header_stm(self):

        localctx = BKITParser.Header_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_header_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKITParser.FUNCTION)
            self.state = 120
            self.match(BKITParser.COLON)
            self.state = 121
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

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_stm




    def paramater_stm(self):

        localctx = BKITParser.Paramater_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramater_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKITParser.PARAMETER)
            self.state = 124
            self.match(BKITParser.COLON)
            self.state = 125
            self.paramater_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramater_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_var(self):
            return self.getTypedRuleContext(BKITParser.Id_varContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def paramater_list(self):
            return self.getTypedRuleContext(BKITParser.Paramater_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramater_list




    def paramater_list(self):

        localctx = BKITParser.Paramater_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramater_list)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.id_var()

                self.state = 128
                self.match(BKITParser.COMMA)
                self.state = 129
                self.paramater_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.id_var()
                pass


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

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body_stm




    def body_stm(self):

        localctx = BKITParser.Body_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKITParser.BODY)
            self.state = 135
            self.match(BKITParser.COLON)
            self.state = 136
            self.statement_list()
            self.state = 137
            self.match(BKITParser.ENDBODY)
            self.state = 138
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.statement() 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ARRAY_ID(self):
            return self.getToken(BKITParser.ARRAY_ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_id_var




    def id_var(self):

        localctx = BKITParser.Id_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==BKITParser.ARRAY_ID or _la==BKITParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(BKITParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKITParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BKITParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(BKITParser.Function_call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.func_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.assign_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 153
                self.while_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 154
                self.do_while_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 155
                self.break_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 156
                self.continue_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 157
                self.function_call_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 158
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_var(self):
            return self.getTypedRuleContext(BKITParser.Id_varContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_statement




    def assign_statement(self):

        localctx = BKITParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.id_var()
            self.state = 162
            self.match(BKITParser.ASSIGN)
            self.state = 163
            self.expressions()
            self.state = 164
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def else_if_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BKITParser.IF)
            self.state = 167
            self.expressions()
            self.state = 168
            self.match(BKITParser.THEN)
            self.state = 169
            self.statement_list()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 170
                self.else_if_statement()


            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 173
                self.else_statement()


            self.state = 176
            self.match(BKITParser.ENDIF)
            self.state = 177
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def else_if_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_if_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_statement




    def else_if_statement(self):

        localctx = BKITParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_else_if_statement)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(BKITParser.ELSEIF)
                self.state = 180
                self.expressions()
                self.state = 181
                self.match(BKITParser.THEN)
                self.state = 182
                self.statement_list()

                self.state = 183
                self.else_if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(BKITParser.ELSEIF)
                self.state = 186
                self.expressions()
                self.state = 187
                self.match(BKITParser.THEN)
                self.state = 188
                self.statement_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_statement




    def else_statement(self):

        localctx = BKITParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(BKITParser.ELSE)
            self.state = 193
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_statement




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(BKITParser.FOR)
            self.state = 196
            self.match(BKITParser.LB)
            self.state = 197
            self.for_condition()
            self.state = 198
            self.match(BKITParser.RB)
            self.state = 199
            self.match(BKITParser.DO)
            self.state = 200
            self.statement_list()
            self.state = 201
            self.match(BKITParser.ENDFOR)
            self.state = 202
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def id_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Id_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Id_varContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.id_var()
            self.state = 205
            self.match(BKITParser.ASSIGN)
            self.state = 206
            self.expressions()
            self.state = 208
            self.match(BKITParser.COMMA)
            self.state = 209
            self.expressions()
            self.state = 210
            self.match(BKITParser.COMMA)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 211
                self.id_var()
                self.state = 212
                self.match(BKITParser.ASSIGN)
                self.state = 213
                self.expressions()
                pass

            elif la_ == 2:
                self.state = 215
                self.expressions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_statement




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BKITParser.WHILE)
            self.state = 219
            self.expressions()
            self.state = 220
            self.match(BKITParser.DO)
            self.state = 221
            self.statement_list()
            self.state = 222
            self.match(BKITParser.ENDWHILE)
            self.state = 223
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(BKITParser.DO)
            self.state = 226
            self.statement_list()
            self.state = 227
            self.match(BKITParser.WHILE)
            self.state = 228
            self.expressions()
            self.state = 229
            self.match(BKITParser.ENDWHILE)
            self.state = 230
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKITParser.BREAK)
            self.state = 233
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BKITParser.CONTINUE)
            self.state = 236
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expressions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionsContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call_statement




    def function_call_statement(self):

        localctx = BKITParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(BKITParser.ID)
            self.state = 239
            self.match(BKITParser.LB)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ARRAY_ID) | (1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.NOTOP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 240
                self.expressions()


            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 243
                self.match(BKITParser.COMMA)
                self.state = 244
                self.expressions()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self.match(BKITParser.RB)
            self.state = 251
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_statement




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(BKITParser.RETURN)
            self.state = 254
            self.expressions()
            self.state = 255
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUALOP(self):
            return self.getToken(BKITParser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(BKITParser.NOTEQUALOP, 0)

        def LESSOP(self):
            return self.getToken(BKITParser.LESSOP, 0)

        def LESSOREQUALOP(self):
            return self.getToken(BKITParser.LESSOREQUALOP, 0)

        def GREATEROP(self):
            return self.getToken(BKITParser.GREATEROP, 0)

        def GREATEOREQUALOP(self):
            return self.getToken(BKITParser.GREATEOREQUALOP, 0)

        def NOTEQUALOPFLOAT(self):
            return self.getToken(BKITParser.NOTEQUALOPFLOAT, 0)

        def LESSOPDOT(self):
            return self.getToken(BKITParser.LESSOPDOT, 0)

        def LESSOREQUALOPDOT(self):
            return self.getToken(BKITParser.LESSOREQUALOPDOT, 0)

        def GREATEROPDOT(self):
            return self.getToken(BKITParser.GREATEROPDOT, 0)

        def GREATEOREQUALOPDOT(self):
            return self.getToken(BKITParser.GREATEOREQUALOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expressions




    def expressions(self):

        localctx = BKITParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expressions)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.exp1(0)
                self.state = 258
                self.match(BKITParser.EQUALOP)
                self.state = 259
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.exp1(0)
                self.state = 262
                self.match(BKITParser.NOTEQUALOP)
                self.state = 263
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.exp1(0)
                self.state = 266
                self.match(BKITParser.LESSOP)
                self.state = 267
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.exp1(0)
                self.state = 270
                self.match(BKITParser.LESSOREQUALOP)
                self.state = 271
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.exp1(0)
                self.state = 274
                self.match(BKITParser.GREATEROP)
                self.state = 275
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 277
                self.exp1(0)
                self.state = 278
                self.match(BKITParser.GREATEOREQUALOP)
                self.state = 279
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 281
                self.exp1(0)
                self.state = 282
                self.match(BKITParser.NOTEQUALOPFLOAT)
                self.state = 283
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 285
                self.exp1(0)
                self.state = 286
                self.match(BKITParser.LESSOPDOT)
                self.state = 287
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 289
                self.exp1(0)
                self.state = 290
                self.match(BKITParser.LESSOREQUALOPDOT)
                self.state = 291
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 293
                self.exp1(0)
                self.state = 294
                self.match(BKITParser.GREATEROPDOT)
                self.state = 295
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 297
                self.exp1(0)
                self.state = 298
                self.match(BKITParser.GREATEOREQUALOPDOT)
                self.state = 299
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 301
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ANDOP(self):
            return self.getToken(BKITParser.ANDOP, 0)

        def OROP(self):
            return self.getToken(BKITParser.OROP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 307
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 308
                        self.match(BKITParser.ANDOP)
                        self.state = 309
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 310
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 311
                        self.match(BKITParser.OROP)
                        self.state = 312
                        self.exp2(0)
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADDOP(self):
            return self.getToken(BKITParser.ADDOP, 0)

        def ADDOPDOT(self):
            return self.getToken(BKITParser.ADDOPDOT, 0)

        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def SUBOPDOT(self):
            return self.getToken(BKITParser.SUBOPDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 333
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 321
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 322
                        self.match(BKITParser.ADDOP)
                        self.state = 323
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 324
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 325
                        self.match(BKITParser.ADDOPDOT)
                        self.state = 326
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 327
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 328
                        self.match(BKITParser.SUBOP)
                        self.state = 329
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 330
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 331
                        self.match(BKITParser.SUBOPDOT)
                        self.state = 332
                        self.exp3(0)
                        pass

             
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULOP(self):
            return self.getToken(BKITParser.MULOP, 0)

        def MULOPDOT(self):
            return self.getToken(BKITParser.MULOPDOT, 0)

        def DIVOP(self):
            return self.getToken(BKITParser.DIVOP, 0)

        def DIVOPDOT(self):
            return self.getToken(BKITParser.DIVOPDOT, 0)

        def MODOP(self):
            return self.getToken(BKITParser.MODOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 356
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 341
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 342
                        self.match(BKITParser.MULOP)
                        self.state = 343
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 344
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 345
                        self.match(BKITParser.MULOPDOT)
                        self.state = 346
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 347
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 348
                        self.match(BKITParser.DIVOP)
                        self.state = 349
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 350
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 351
                        self.match(BKITParser.DIVOPDOT)
                        self.state = 352
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 353
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 354
                        self.match(BKITParser.MODOP)
                        self.state = 355
                        self.exp4()
                        pass

             
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(BKITParser.NOTOP, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp4)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(BKITParser.NOTOP)
                self.state = 362
                self.operand()
                pass
            elif token in [BKITParser.ARRAY_ID, BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def sub_expression(self):
            return self.getTypedRuleContext(BKITParser.Sub_expressionContext,0)


        def ARRAY_ID(self):
            return self.getToken(BKITParser.ARRAY_ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operand)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.type_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.sub_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(BKITParser.ARRAY_ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 370
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 371
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sub_expression




    def sub_expression(self):

        localctx = BKITParser.Sub_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sub_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(BKITParser.LB)
            self.state = 375
            self.expressions()
            self.state = 376
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(BKITParser.List_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(BKITParser.ID)
            self.state = 379
            self.match(BKITParser.LB)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 380
                self.list_expression()


            self.state = 383
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(BKITParser.Type_listContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def list_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.List_expressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.List_expressionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_list_expression




    def list_expression(self):

        localctx = BKITParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.type_list()
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 386
                    self.match(BKITParser.COMMA)
                    self.state = 387
                    self.list_expression() 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def expressions(self):
            return self.getTypedRuleContext(BKITParser.ExpressionsContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operator




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(BKITParser.ID)
            self.state = 394
            self.match(BKITParser.LSB)
            self.state = 395
            self.expressions()
            self.state = 396
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.exp1_sempred
        self._predicates[28] = self.exp2_sempred
        self._predicates[29] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         





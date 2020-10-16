# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0240\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\6\2\u00a5\n\2")
        buf.write("\r\2\16\2\u00a6\3\3\3\3\7\3\u00ab\n\3\f\3\16\3\u00ae\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3;\5;\u018b\n;\3<\3<\6<\u018f\n<\r<\16<\u0190")
        buf.write("\3<\5<\u0194\n<\3=\3=\3=\6=\u0199\n=\r=\16=\u019a\3=\3")
        buf.write("=\3=\6=\u01a0\n=\r=\16=\u01a1\5=\u01a4\n=\3>\3>\3>\6>")
        buf.write("\u01a9\n>\r>\16>\u01aa\3?\3?\5?\u01af\n?\3?\5?\u01b2\n")
        buf.write("?\3?\5?\u01b5\n?\3?\5?\u01b8\n?\3?\3?\5?\u01bc\n?\3?\5")
        buf.write("?\u01bf\n?\3?\5?\u01c2\n?\5?\u01c4\n?\3@\3@\7@\u01c8\n")
        buf.write("@\f@\16@\u01cb\13@\3@\3@\3@\3A\3A\5A\u01d2\nA\3B\3B\5")
        buf.write("B\u01d6\nB\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\7E\u01e2\nE\f")
        buf.write("E\16E\u01e5\13E\3F\3F\3F\3F\7F\u01eb\nF\fF\16F\u01ee\13")
        buf.write("F\3G\3G\3G\3G\7G\u01f4\nG\fG\16G\u01f7\13G\3H\3H\5H\u01fb")
        buf.write("\nH\3H\3H\3H\5H\u0200\nH\7H\u0202\nH\fH\16H\u0205\13H")
        buf.write("\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0217")
        buf.write("\nI\3J\6J\u021a\nJ\rJ\16J\u021b\3J\3J\3K\3K\3K\3K\7K\u0224")
        buf.write("\nK\fK\16K\u0227\13K\3K\3K\3K\3K\3K\3L\3L\3L\3M\3M\7M")
        buf.write("\u0233\nM\fM\16M\u0236\13M\3M\3M\3N\3N\3N\3N\3N\3O\3O")
        buf.write("\3\u0225\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w\2y\2{\2}=\177>\u0081\2\u0083\2\u0085\2")
        buf.write("\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091?\u0093")
        buf.write("@\u0095A\u0097B\u0099C\u009bD\u009dE\3\2\21\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\3\2\62;\3\2\62\62\4\2ZZzz\3\2CH\4")
        buf.write("\2QQqq\3\2\629\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\t\2")
        buf.write("))^^ddhhppttvv\5\2\13\f\17\17\"\"\t\2$$^^ddhhppttvv\2")
        buf.write("\u0255\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a8\3\2\2\2\7\u00af\3\2\2")
        buf.write("\2\t\u00b4\3\2\2\2\13\u00ba\3\2\2\2\r\u00c3\3\2\2\2\17")
        buf.write("\u00c6\3\2\2\2\21\u00cb\3\2\2\2\23\u00d2\3\2\2\2\25\u00da")
        buf.write("\3\2\2\2\27\u00e0\3\2\2\2\31\u00e7\3\2\2\2\33\u00f0\3")
        buf.write("\2\2\2\35\u00f4\3\2\2\2\37\u00fd\3\2\2\2!\u0100\3\2\2")
        buf.write("\2#\u010a\3\2\2\2%\u0111\3\2\2\2\'\u0116\3\2\2\2)\u011a")
        buf.write("\3\2\2\2+\u0120\3\2\2\2-\u0125\3\2\2\2/\u012b\3\2\2\2")
        buf.write("\61\u0131\3\2\2\2\63\u0133\3\2\2\2\65\u0135\3\2\2\2\67")
        buf.write("\u0138\3\2\2\29\u013a\3\2\2\2;\u013d\3\2\2\2=\u013f\3")
        buf.write("\2\2\2?\u0142\3\2\2\2A\u0144\3\2\2\2C\u0147\3\2\2\2E\u0149")
        buf.write("\3\2\2\2G\u014b\3\2\2\2I\u014e\3\2\2\2K\u0151\3\2\2\2")
        buf.write("M\u0154\3\2\2\2O\u0157\3\2\2\2Q\u015b\3\2\2\2S\u015d\3")
        buf.write("\2\2\2U\u0160\3\2\2\2W\u0162\3\2\2\2Y\u0165\3\2\2\2[\u0168")
        buf.write("\3\2\2\2]\u016c\3\2\2\2_\u016f\3\2\2\2a\u0173\3\2\2\2")
        buf.write("c\u0175\3\2\2\2e\u0177\3\2\2\2g\u0179\3\2\2\2i\u017b\3")
        buf.write("\2\2\2k\u017d\3\2\2\2m\u017f\3\2\2\2o\u0181\3\2\2\2q\u0183")
        buf.write("\3\2\2\2s\u0185\3\2\2\2u\u018a\3\2\2\2w\u0193\3\2\2\2")
        buf.write("y\u01a3\3\2\2\2{\u01a5\3\2\2\2}\u01ac\3\2\2\2\177\u01c5")
        buf.write("\3\2\2\2\u0081\u01d1\3\2\2\2\u0083\u01d5\3\2\2\2\u0085")
        buf.write("\u01d7\3\2\2\2\u0087\u01da\3\2\2\2\u0089\u01dd\3\2\2\2")
        buf.write("\u008b\u01e6\3\2\2\2\u008d\u01ef\3\2\2\2\u008f\u01fa\3")
        buf.write("\2\2\2\u0091\u0216\3\2\2\2\u0093\u0219\3\2\2\2\u0095\u021f")
        buf.write("\3\2\2\2\u0097\u022d\3\2\2\2\u0099\u0230\3\2\2\2\u009b")
        buf.write("\u0239\3\2\2\2\u009d\u023e\3\2\2\2\u009f\u00a4\5\5\3\2")
        buf.write("\u00a0\u00a1\5e\63\2\u00a1\u00a2\5u;\2\u00a2\u00a3\5g")
        buf.write("\64\2\u00a3\u00a5\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\4\3\2\2\2\u00a8\u00ac\t\2\2\2\u00a9\u00ab\t\3\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\6\3\2\2\2\u00ae\u00ac\3\2\2")
        buf.write("\2\u00af\u00b0\7D\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7")
        buf.write("f\2\2\u00b2\u00b3\7{\2\2\u00b3\b\3\2\2\2\u00b4\u00b5\7")
        buf.write("D\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7m\2\2\u00b9\n\3\2\2\2\u00ba\u00bb")
        buf.write("\7E\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7w\2\2\u00c1\u00c2\7g\2\2\u00c2\f\3\2\2\2\u00c3\u00c4")
        buf.write("\7F\2\2\u00c4\u00c5\7q\2\2\u00c5\16\3\2\2\2\u00c6\u00c7")
        buf.write("\7G\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7K\2\2\u00d0\u00d1\7h\2\2\u00d1\22\3\2\2\2\u00d2\u00d3")
        buf.write("\7G\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7f\2\2\u00d5\u00d6")
        buf.write("\7D\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7f\2\2\u00d8\u00d9")
        buf.write("\7{\2\2\u00d9\24\3\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de\7K\2\2\u00de\u00df")
        buf.write("\7h\2\2\u00df\26\3\2\2\2\u00e0\u00e1\7G\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7f\2\2\u00e3\u00e4\7H\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7t\2\2\u00e6\30\3\2\2\2\u00e7\u00e8")
        buf.write("\7G\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7f\2\2\u00ea\u00eb")
        buf.write("\7Y\2\2\u00eb\u00ec\7j\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\32\3\2\2\2\u00f0\u00f1")
        buf.write("\7H\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7t\2\2\u00f3\34")
        buf.write("\3\2\2\2\u00f4\u00f5\7H\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7p\2\2\u00fc\36")
        buf.write("\3\2\2\2\u00fd\u00fe\7K\2\2\u00fe\u00ff\7h\2\2\u00ff ")
        buf.write("\3\2\2\2\u0100\u0101\7R\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7o\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7v\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\"\3\2\2\2\u010a\u010b\7T\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7v\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7p\2\2\u0110$\3\2\2\2\u0111\u0112")
        buf.write("\7V\2\2\u0112\u0113\7j\2\2\u0113\u0114\7g\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115&\3\2\2\2\u0116\u0117\7X\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7t\2\2\u0119(\3\2\2\2\u011a\u011b")
        buf.write("\7Y\2\2\u011b\u011c\7j\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7n\2\2\u011e\u011f\7g\2\2\u011f*\3\2\2\2\u0120\u0121")
        buf.write("\7V\2\2\u0121\u0122\7t\2\2\u0122\u0123\7w\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124,\3\2\2\2\u0125\u0126\7H\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7n\2\2\u0128\u0129\7u\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a.\3\2\2\2\u012b\u012c\7G\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7f\2\2\u012e\u012f\7F\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\60\3\2\2\2\u0131\u0132\7?\2\2\u0132\62\3")
        buf.write("\2\2\2\u0133\u0134\7-\2\2\u0134\64\3\2\2\2\u0135\u0136")
        buf.write("\7-\2\2\u0136\u0137\7\60\2\2\u0137\66\3\2\2\2\u0138\u0139")
        buf.write("\7/\2\2\u01398\3\2\2\2\u013a\u013b\7/\2\2\u013b\u013c")
        buf.write("\7\60\2\2\u013c:\3\2\2\2\u013d\u013e\7,\2\2\u013e<\3\2")
        buf.write("\2\2\u013f\u0140\7,\2\2\u0140\u0141\7\60\2\2\u0141>\3")
        buf.write("\2\2\2\u0142\u0143\7\61\2\2\u0143@\3\2\2\2\u0144\u0145")
        buf.write("\7\61\2\2\u0145\u0146\7\60\2\2\u0146B\3\2\2\2\u0147\u0148")
        buf.write("\7\'\2\2\u0148D\3\2\2\2\u0149\u014a\7#\2\2\u014aF\3\2")
        buf.write("\2\2\u014b\u014c\7~\2\2\u014c\u014d\7~\2\2\u014dH\3\2")
        buf.write("\2\2\u014e\u014f\7(\2\2\u014f\u0150\7(\2\2\u0150J\3\2")
        buf.write("\2\2\u0151\u0152\7?\2\2\u0152\u0153\7?\2\2\u0153L\3\2")
        buf.write("\2\2\u0154\u0155\7#\2\2\u0155\u0156\7?\2\2\u0156N\3\2")
        buf.write("\2\2\u0157\u0158\7?\2\2\u0158\u0159\7\61\2\2\u0159\u015a")
        buf.write("\7?\2\2\u015aP\3\2\2\2\u015b\u015c\7>\2\2\u015cR\3\2\2")
        buf.write("\2\u015d\u015e\7>\2\2\u015e\u015f\7\60\2\2\u015fT\3\2")
        buf.write("\2\2\u0160\u0161\7@\2\2\u0161V\3\2\2\2\u0162\u0163\7@")
        buf.write("\2\2\u0163\u0164\7\60\2\2\u0164X\3\2\2\2\u0165\u0166\7")
        buf.write(">\2\2\u0166\u0167\7?\2\2\u0167Z\3\2\2\2\u0168\u0169\7")
        buf.write(">\2\2\u0169\u016a\7?\2\2\u016a\u016b\7\60\2\2\u016b\\")
        buf.write("\3\2\2\2\u016c\u016d\7@\2\2\u016d\u016e\7?\2\2\u016e^")
        buf.write("\3\2\2\2\u016f\u0170\7@\2\2\u0170\u0171\7?\2\2\u0171\u0172")
        buf.write("\7\60\2\2\u0172`\3\2\2\2\u0173\u0174\7*\2\2\u0174b\3\2")
        buf.write("\2\2\u0175\u0176\7+\2\2\u0176d\3\2\2\2\u0177\u0178\7]")
        buf.write("\2\2\u0178f\3\2\2\2\u0179\u017a\7_\2\2\u017ah\3\2\2\2")
        buf.write("\u017b\u017c\7<\2\2\u017cj\3\2\2\2\u017d\u017e\7\60\2")
        buf.write("\2\u017el\3\2\2\2\u017f\u0180\7.\2\2\u0180n\3\2\2\2\u0181")
        buf.write("\u0182\7=\2\2\u0182p\3\2\2\2\u0183\u0184\7}\2\2\u0184")
        buf.write("r\3\2\2\2\u0185\u0186\7\177\2\2\u0186t\3\2\2\2\u0187\u018b")
        buf.write("\5w<\2\u0188\u018b\5y=\2\u0189\u018b\5{>\2\u018a\u0187")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("v\3\2\2\2\u018c\u018e\t\4\2\2\u018d\u018f\t\5\2\2\u018e")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0194\t")
        buf.write("\5\2\2\u0193\u018c\3\2\2\2\u0193\u0192\3\2\2\2\u0194x")
        buf.write("\3\2\2\2\u0195\u0196\t\6\2\2\u0196\u0198\t\7\2\2\u0197")
        buf.write("\u0199\t\5\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u01a4\3")
        buf.write("\2\2\2\u019c\u019d\t\6\2\2\u019d\u019f\t\7\2\2\u019e\u01a0")
        buf.write("\t\b\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2")
        buf.write("\u01a3\u0195\3\2\2\2\u01a3\u019c\3\2\2\2\u01a4z\3\2\2")
        buf.write("\2\u01a5\u01a6\t\6\2\2\u01a6\u01a8\t\t\2\2\u01a7\u01a9")
        buf.write("\t\n\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab|\3\2\2\2\u01ac")
        buf.write("\u01ae\5u;\2\u01ad\u01af\t\13\2\2\u01ae\u01ad\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2\t")
        buf.write("\f\2\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01b5\5u;\2\u01b4\u01b3\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b8\7\60\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c3\3\2\2\2")
        buf.write("\u01b9\u01bb\5u;\2\u01ba\u01bc\t\13\2\2\u01bb\u01ba\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bf")
        buf.write("\t\f\2\2\u01be\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01c1\3\2\2\2\u01c0\u01c2\5u;\2\u01c1\u01c0\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01b9\3\2\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4~\3\2\2\2\u01c5\u01c9\7$\2\2")
        buf.write("\u01c6\u01c8\5\u0081A\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7$\2\2")
        buf.write("\u01cd\u01ce\b@\2\2\u01ce\u0080\3\2\2\2\u01cf\u01d2\5")
        buf.write("\u0083B\2\u01d0\u01d2\5\u0087D\2\u01d1\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2\u0082\3\2\2\2\u01d3\u01d6\n\r\2\2")
        buf.write("\u01d4\u01d6\5\u0085C\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6\u0084\3\2\2\2\u01d7\u01d8\7^\2\2\u01d8")
        buf.write("\u01d9\t\16\2\2\u01d9\u0086\3\2\2\2\u01da\u01db\7)\2\2")
        buf.write("\u01db\u01dc\7$\2\2\u01dc\u0088\3\2\2\2\u01dd\u01e3\5")
        buf.write("u;\2\u01de\u01df\5m\67\2\u01df\u01e0\5u;\2\u01e0\u01e2")
        buf.write("\3\2\2\2\u01e1\u01de\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u008a\3\2\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e6\u01ec\5}?\2\u01e7\u01e8\5m")
        buf.write("\67\2\u01e8\u01e9\5}?\2\u01e9\u01eb\3\2\2\2\u01ea\u01e7")
        buf.write("\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u008c\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ef\u01f5\5\177@\2\u01f0\u01f1\5m\67\2\u01f1\u01f2")
        buf.write("\5\177@\2\u01f2\u01f4\3\2\2\2\u01f3\u01f0\3\2\2\2\u01f4")
        buf.write("\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u008e\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01fb\5")
        buf.write("+\26\2\u01f9\u01fb\5-\27\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u0203\3\2\2\2\u01fc\u01ff\5m\67\2\u01fd")
        buf.write("\u0200\5+\26\2\u01fe\u0200\5-\27\2\u01ff\u01fd\3\2\2\2")
        buf.write("\u01ff\u01fe\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01fc\3")
        buf.write("\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0090\3\2\2\2\u0205\u0203\3\2\2\2\u0206")
        buf.write("\u0207\5q9\2\u0207\u0208\5\u0089E\2\u0208\u0209\5s:\2")
        buf.write("\u0209\u0217\3\2\2\2\u020a\u020b\5q9\2\u020b\u020c\5\u008b")
        buf.write("F\2\u020c\u020d\5s:\2\u020d\u0217\3\2\2\2\u020e\u020f")
        buf.write("\5q9\2\u020f\u0210\5\u008dG\2\u0210\u0211\5s:\2\u0211")
        buf.write("\u0217\3\2\2\2\u0212\u0213\5q9\2\u0213\u0214\5\u008fH")
        buf.write("\2\u0214\u0215\5s:\2\u0215\u0217\3\2\2\2\u0216\u0206\3")
        buf.write("\2\2\2\u0216\u020a\3\2\2\2\u0216\u020e\3\2\2\2\u0216\u0212")
        buf.write("\3\2\2\2\u0217\u0092\3\2\2\2\u0218\u021a\t\17\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\b")
        buf.write("J\3\2\u021e\u0094\3\2\2\2\u021f\u0220\7,\2\2\u0220\u0221")
        buf.write("\7,\2\2\u0221\u0225\3\2\2\2\u0222\u0224\13\2\2\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0228\u0229\7,\2\2\u0229\u022a\7,\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022c\bK\3\2\u022c\u0096\3\2\2\2\u022d")
        buf.write("\u022e\13\2\2\2\u022e\u022f\bL\4\2\u022f\u0098\3\2\2\2")
        buf.write("\u0230\u0234\7$\2\2\u0231\u0233\5\u0081A\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0237\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0237\u0238\bM\5\2\u0238\u009a\3\2\2\2\u0239\u023a\5")
        buf.write("\u0099M\2\u023a\u023b\7^\2\2\u023b\u023c\n\20\2\2\u023c")
        buf.write("\u023d\bN\6\2\u023d\u009c\3\2\2\2\u023e\u023f\13\2\2\2")
        buf.write("\u023f\u009e\3\2\2\2!\2\u00a6\u00ac\u018a\u0190\u0193")
        buf.write("\u019a\u01a1\u01a3\u01aa\u01ae\u01b1\u01b4\u01b7\u01bb")
        buf.write("\u01be\u01c1\u01c3\u01c9\u01d1\u01d5\u01e3\u01ec\u01f5")
        buf.write("\u01fa\u01ff\u0203\u0216\u021b\u0225\u0234\7\3@\2\b\2")
        buf.write("\2\3L\3\3M\4\3N\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY_ID = 1
    ID = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSEIF = 8
    ENDBODY = 9
    ENDIF = 10
    ENDFOR = 11
    ENDWHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    VAR = 19
    WHILE = 20
    TRUE = 21
    FALSE = 22
    ENDDO = 23
    ASSIGN = 24
    ADDOP = 25
    ADDOPDOT = 26
    SUBOP = 27
    SUBOPDOT = 28
    MULOP = 29
    MULOPDOT = 30
    DIVOP = 31
    DIVOPDOT = 32
    MODOP = 33
    NOTOP = 34
    OROP = 35
    ANDOP = 36
    EQUALOP = 37
    NOTEQUALOP = 38
    NOTEQUALOPFLOAT = 39
    LESSOP = 40
    LESSOPDOT = 41
    GREATEROP = 42
    GREATEROPDOT = 43
    LESSOREQUALOP = 44
    LESSOREQUALOPDOT = 45
    GREATEOREQUALOP = 46
    GREATEOREQUALOPDOT = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    COLON = 52
    DOT = 53
    COMMA = 54
    SEMI = 55
    LP = 56
    RP = 57
    INTLIT = 58
    FLOATLIT = 59
    STRINGLIT = 60
    ARRAY = 61
    WS = 62
    COMMENT = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    UNTERMINATED_COMMENT = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'='", "'+'", "'+.'", "'-'", 
            "'-.'", "'*'", "'*.'", "'/'", "'/.'", "'%'", "'!'", "'||'", 
            "'&&'", "'=='", "'!='", "'=/='", "'<'", "'<.'", "'>'", "'>.'", 
            "'<='", "'<=.'", "'>='", "'>=.'", "'('", "')'", "'['", "']'", 
            "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY_ID", "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "ASSIGN", "ADDOP", "ADDOPDOT", "SUBOP", "SUBOPDOT", 
            "MULOP", "MULOPDOT", "DIVOP", "DIVOPDOT", "MODOP", "NOTOP", 
            "OROP", "ANDOP", "EQUALOP", "NOTEQUALOP", "NOTEQUALOPFLOAT", 
            "LESSOP", "LESSOPDOT", "GREATEROP", "GREATEROPDOT", "LESSOREQUALOP", 
            "LESSOREQUALOPDOT", "GREATEOREQUALOP", "GREATEOREQUALOPDOT", 
            "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "LP", 
            "RP", "INTLIT", "FLOATLIT", "STRINGLIT", "ARRAY", "WS", "COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ARRAY_ID", "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "ASSIGN", "ADDOP", 
                  "ADDOPDOT", "SUBOP", "SUBOPDOT", "MULOP", "MULOPDOT", 
                  "DIVOP", "DIVOPDOT", "MODOP", "NOTOP", "OROP", "ANDOP", 
                  "EQUALOP", "NOTEQUALOP", "NOTEQUALOPFLOAT", "LESSOP", 
                  "LESSOPDOT", "GREATEROP", "GREATEROPDOT", "LESSOREQUALOP", 
                  "LESSOREQUALOPDOT", "GREATEOREQUALOP", "GREATEOREQUALOPDOT", 
                  "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", 
                  "LP", "RP", "INTLIT", "DEC", "HEX", "OCT", "FLOATLIT", 
                  "STRINGLIT", "STR_CHAR", "STR_CHAR_NORMAL", "ESC_SEQ", 
                  "STR_CHAR_QUOTE", "INTLIT_LIST", "FLOATLIT_LIST", "STRING_LIST", 
                  "BOOLEAN_LIST", "ARRAY", "WS", "COMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRINGLIT_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = self.text[1:-1];
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise IllegalEscape(self.text[1:])
     



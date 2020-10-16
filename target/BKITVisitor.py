# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids_list.
    def visitIds_list(self, ctx:BKITParser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#id_declare.
    def visitId_declare(self, ctx:BKITParser.Id_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_declare.
    def visitArray_declare(self, ctx:BKITParser.Array_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#type_list.
    def visitType_list(self, ctx:BKITParser.Type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#header_stm.
    def visitHeader_stm(self, ctx:BKITParser.Header_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramater_stm.
    def visitParamater_stm(self, ctx:BKITParser.Paramater_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramater_list.
    def visitParamater_list(self, ctx:BKITParser.Paramater_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_stm.
    def visitBody_stm(self, ctx:BKITParser.Body_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#id_var.
    def visitId_var(self, ctx:BKITParser.Id_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_statement.
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_if_statement.
    def visitElse_if_statement(self, ctx:BKITParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_statement.
    def visitElse_statement(self, ctx:BKITParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_condition.
    def visitFor_condition(self, ctx:BKITParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:BKITParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expressions.
    def visitExpressions(self, ctx:BKITParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sub_expression.
    def visitSub_expression(self, ctx:BKITParser.Sub_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_expression.
    def visitList_expression(self, ctx:BKITParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)



del BKITParser
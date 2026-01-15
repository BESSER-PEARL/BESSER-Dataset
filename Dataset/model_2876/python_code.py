from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class eol_statements_VariableDeclarationExpression(Expression):

    pass
class eol_statements_ModelDeclarationParameter:

    pass
class eol_statements_StringExpression:

    pass
class AnnotationStatement:

    pass
class eol_statements_ExecutableAnnotationStatement(AnnotationStatement):

    pass
class eol_statements_SimpleAnnotationStatement(AnnotationStatement):

    pass
class eol_statements_NameExpression(Expression):

    pass
class AssignmentStatement:

    pass
class eol_statements_SpecialAssignmentStatement(AssignmentStatement):

    pass
class eol_statements_FormalParameterExpression:

    pass
class SwitchCaseStatement:

    pass
class eol_statements_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class eol_statements_SwitchCaseDefaultStatement(SwitchCaseStatement):

    pass
class eol_statements_ExpressionOrStatementBlock:

    pass
class eol_statements_Expression(ABC):

    pass
class Statement:

    pass
class eol_statements_DeleteStatement(Statement):

    pass
class eol_statements_IfStatement(Statement):

    pass
class eol_statements_BreakAllStatement(Statement):

    pass
class eol_statements_AnnotationStatement(Statement):

    pass
class eol_statements_AbortStatement(Statement):

    pass
class eol_statements_WhileStatement(Statement):

    pass
class eol_statements_AssignmentStatement(Statement):

    pass
class eol_statements_ForStatement(Statement):

    pass
class eol_statements_ReturnStatement(Statement):

    pass
class eol_statements_SwitchCaseStatement(Statement):

    pass
class eol_statements_ModelDeclarationStatement(Statement):

    pass
class eol_statements_BreakStatement(Statement):

    pass
class eol_statements_ContinueStatement(Statement):

    pass
class eol_statements_ThrowStatement(Statement):

    pass
class eol_statements_SwitchStatement(Statement):

    pass
class eol_statements_ExpressionStatement(Statement):

    pass
class eol_statements_Statement(ABC):

    pass
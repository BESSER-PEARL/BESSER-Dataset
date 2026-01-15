from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_ReferenceExpression:

    pass
class model_ParameterDeclaration:

    pass
class model_ConstantDeclaration:

    pass
class model_VariableDeclaration:

    pass
class model_Expression:

    pass
class model_Branch:

    pass
class Statement:

    pass
class model_ConstantDeclarationStatement(Statement):

    pass
class model_AssignmentStatement(Statement):

    pass
class model_ForStatement(Statement):

    pass
class model_SwitchStatement(Statement):

    pass
class model_ExpressionStatement(Statement):

    pass
class model_ChoiceStatement(Statement):

    pass
class model_VariableDeclarationStatement(Statement):

    pass
class model_EmptyStatement(Statement):

    pass
class Action:

    pass
class model_Statement(Action):

    pass
class model_Action(ABC):

    pass
class model_Block(Action):

    pass
class FunctionDeclaration:

    pass
class model_ProcedureDeclaration(FunctionDeclaration):

    pass
class model_IfStatement(Statement):

    pass
class model_ReturnStatement(Statement):

    pass
class model_BreakStatement(Statement):

    pass
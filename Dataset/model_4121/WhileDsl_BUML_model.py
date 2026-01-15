####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
whileDsl_Model = Class(name="whileDsl::Model")
whileDsl_ForeachCommand = Class(name="whileDsl::ForeachCommand")
whileDsl_Function = Class(name="whileDsl::Function")
whileDsl_Definition = Class(name="whileDsl::Definition")
whileDsl_Input = Class(name="whileDsl::Input")
whileDsl_Commands = Class(name="whileDsl::Commands")
whileDsl_Output = Class(name="whileDsl::Output")
whileDsl_Command = Class(name="whileDsl::Command")
whileDsl_WhileCommand = Class(name="whileDsl::WhileCommand")
Command = Class(name="Command")
whileDsl_Expr = Class(name="whileDsl::Expr")
whileDsl_ForCommand = Class(name="whileDsl::ForCommand")
whileDsl_IfCommand = Class(name="whileDsl::IfCommand")
whileDsl_ExprEq = Class(name="whileDsl::ExprEq")
whileDsl_VarsCommand = Class(name="whileDsl::VarsCommand")
whileDsl_Vars = Class(name="whileDsl::Vars")
whileDsl_Exprs = Class(name="whileDsl::Exprs")
whileDsl_ExprSimple = Class(name="whileDsl::ExprSimple")
whileDsl_EObject = Class(name="whileDsl::EObject")
whileDsl_ExprSimpleWithLExpr = Class(name="whileDsl::ExprSimpleWithLExpr")
whileDsl_LExpr = Class(name="whileDsl::LExpr")
whileDsl_ExprSimpleWithExpr = Class(name="whileDsl::ExprSimpleWithExpr")
whileDsl_ExprSimpleWithSymbolLExpr = Class(name="whileDsl::ExprSimpleWithSymbolLExpr")
whileDsl_ExprAnd = Class(name="whileDsl::ExprAnd")
whileDsl_ExprOr = Class(name="whileDsl::ExprOr")
whileDsl_ExprNot = Class(name="whileDsl::ExprNot")
whileDsl_NopCommand = Class(name="whileDsl::NopCommand")

# whileDsl_Model class attributes and methods

# whileDsl_ForeachCommand class attributes and methods
whileDsl_ForeachCommand_expElement: Property = Property(name="expElement", type=StringType)
whileDsl_ForeachCommand.attributes={whileDsl_ForeachCommand_expElement}

# whileDsl_Function class attributes and methods
whileDsl_Function_functionName: Property = Property(name="functionName", type=StringType)
whileDsl_Function.attributes={whileDsl_Function_functionName}

# whileDsl_Definition class attributes and methods

# whileDsl_Input class attributes and methods
whileDsl_Input_variables: Property = Property(name="variables", type=StringType)
whileDsl_Input.attributes={whileDsl_Input_variables}

# whileDsl_Commands class attributes and methods

# whileDsl_Output class attributes and methods
whileDsl_Output_variables: Property = Property(name="variables", type=StringType)
whileDsl_Output.attributes={whileDsl_Output_variables}

# whileDsl_Command class attributes and methods

# whileDsl_WhileCommand class attributes and methods

# Command class attributes and methods

# whileDsl_Expr class attributes and methods

# whileDsl_ForCommand class attributes and methods

# whileDsl_IfCommand class attributes and methods

# whileDsl_ExprEq class attributes and methods

# whileDsl_VarsCommand class attributes and methods

# whileDsl_Vars class attributes and methods
whileDsl_Vars_variables: Property = Property(name="variables", type=StringType)
whileDsl_Vars.attributes={whileDsl_Vars_variables}

# whileDsl_Exprs class attributes and methods

# whileDsl_ExprSimple class attributes and methods
whileDsl_ExprSimple_term: Property = Property(name="term", type=StringType)
whileDsl_ExprSimple.attributes={whileDsl_ExprSimple_term}

# whileDsl_EObject class attributes and methods

# whileDsl_ExprSimpleWithLExpr class attributes and methods
whileDsl_ExprSimpleWithLExpr_operation: Property = Property(name="operation", type=StringType)
whileDsl_ExprSimpleWithLExpr.attributes={whileDsl_ExprSimpleWithLExpr_operation}

# whileDsl_LExpr class attributes and methods

# whileDsl_ExprSimpleWithExpr class attributes and methods
whileDsl_ExprSimpleWithExpr_operation: Property = Property(name="operation", type=StringType)
whileDsl_ExprSimpleWithExpr.attributes={whileDsl_ExprSimpleWithExpr_operation}

# whileDsl_ExprSimpleWithSymbolLExpr class attributes and methods
whileDsl_ExprSimpleWithSymbolLExpr_symbol: Property = Property(name="symbol", type=StringType)
whileDsl_ExprSimpleWithSymbolLExpr.attributes={whileDsl_ExprSimpleWithSymbolLExpr_symbol}

# whileDsl_ExprAnd class attributes and methods

# whileDsl_ExprOr class attributes and methods

# whileDsl_ExprNot class attributes and methods
whileDsl_ExprNot_negation: Property = Property(name="negation", type=BooleanType)
whileDsl_ExprNot.attributes={whileDsl_ExprNot_negation}

# whileDsl_NopCommand class attributes and methods

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="whileDsl_Function", type=whileDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Model", type=whileDsl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionDefinition1: BinaryAssociation = BinaryAssociation(
    name="functionDefinition1",
    ends={
        Property(name="whileDsl_Definition", type=whileDsl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Function2", type=whileDsl_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intput3: BinaryAssociation = BinaryAssociation(
    name="intput3",
    ends={
        Property(name="whileDsl_Input", type=whileDsl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Definition4", type=whileDsl_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="whileDsl_Commands", type=whileDsl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Definition6", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output7: BinaryAssociation = BinaryAssociation(
    name="output7",
    ends={
        Property(name="whileDsl_Output", type=whileDsl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Definition8", type=whileDsl_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands9: BinaryAssociation = BinaryAssociation(
    name="commands9",
    ends={
        Property(name="whileDsl_Command", type=whileDsl_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Commands10", type=whileDsl_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond11: BinaryAssociation = BinaryAssociation(
    name="cond11",
    ends={
        Property(name="whileDsl_Expr", type=whileDsl_WhileCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_WhileCommand", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="whileDsl_Commands14", type=whileDsl_WhileCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_WhileCommand13", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond15: BinaryAssociation = BinaryAssociation(
    name="cond15",
    ends={
        Property(name="whileDsl_Expr16", type=whileDsl_ForCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ForCommand", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body17: BinaryAssociation = BinaryAssociation(
    name="body17",
    ends={
        Property(name="whileDsl_Commands19", type=whileDsl_ForCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ForCommand18", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond20: BinaryAssociation = BinaryAssociation(
    name="cond20",
    ends={
        Property(name="whileDsl_Expr21", type=whileDsl_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_IfCommand", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody22: BinaryAssociation = BinaryAssociation(
    name="thenBody22",
    ends={
        Property(name="whileDsl_Commands24", type=whileDsl_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_IfCommand23", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody25: BinaryAssociation = BinaryAssociation(
    name="elseBody25",
    ends={
        Property(name="whileDsl_Commands27", type=whileDsl_IfCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_IfCommand26", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionsNot52: BinaryAssociation = BinaryAssociation(
    name="expressionsNot52",
    ends={
        Property(name="whileDsl_ExprOr53", type=whileDsl_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="whileDsl_ExprNot", type=whileDsl_ExprOr, multiplicity=Multiplicity(1, 1))
    }
)
expList28: BinaryAssociation = BinaryAssociation(
    name="expList28",
    ends={
        Property(name="whileDsl_Expr29", type=whileDsl_ForeachCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ForeachCommand", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body30: BinaryAssociation = BinaryAssociation(
    name="body30",
    ends={
        Property(name="whileDsl_Commands32", type=whileDsl_ForeachCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ForeachCommand31", type=whileDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables33: BinaryAssociation = BinaryAssociation(
    name="variables33",
    ends={
        Property(name="whileDsl_Vars", type=whileDsl_VarsCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_VarsCommand", type=whileDsl_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values34: BinaryAssociation = BinaryAssociation(
    name="values34",
    ends={
        Property(name="whileDsl_Exprs", type=whileDsl_VarsCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_VarsCommand35", type=whileDsl_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression36: BinaryAssociation = BinaryAssociation(
    name="expression36",
    ends={
        Property(name="whileDsl_EObject", type=whileDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprSimple", type=whileDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr37: BinaryAssociation = BinaryAssociation(
    name="lexpr37",
    ends={
        Property(name="whileDsl_LExpr", type=whileDsl_ExprSimpleWithLExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprSimpleWithLExpr", type=whileDsl_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr38: BinaryAssociation = BinaryAssociation(
    name="expr38",
    ends={
        Property(name="whileDsl_Expr39", type=whileDsl_ExprSimpleWithExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprSimpleWithExpr", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr40: BinaryAssociation = BinaryAssociation(
    name="lexpr40",
    ends={
        Property(name="whileDsl_LExpr41", type=whileDsl_ExprSimpleWithSymbolLExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprSimpleWithSymbolLExpr", type=whileDsl_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions42: BinaryAssociation = BinaryAssociation(
    name="expressions42",
    ends={
        Property(name="whileDsl_Expr44", type=whileDsl_LExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_LExpr43", type=whileDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions45: BinaryAssociation = BinaryAssociation(
    name="expressions45",
    ends={
        Property(name="whileDsl_Expr47", type=whileDsl_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Exprs46", type=whileDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="whileDsl_EObject50", type=whileDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_Expr49", type=whileDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionsOr51: BinaryAssociation = BinaryAssociation(
    name="expressionsOr51",
    ends={
        Property(name="whileDsl_ExprOr", type=whileDsl_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprAnd", type=whileDsl_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionEq54: BinaryAssociation = BinaryAssociation(
    name="expressionEq54",
    ends={
        Property(name="whileDsl_ExprEq", type=whileDsl_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprNot55", type=whileDsl_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprLSimple56: BinaryAssociation = BinaryAssociation(
    name="exprLSimple56",
    ends={
        Property(name="whileDsl_ExprSimple58", type=whileDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprEq57", type=whileDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprRSimple59: BinaryAssociation = BinaryAssociation(
    name="exprRSimple59",
    ends={
        Property(name="whileDsl_ExprSimple61", type=whileDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprEq60", type=whileDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr62: BinaryAssociation = BinaryAssociation(
    name="expr62",
    ends={
        Property(name="whileDsl_Expr64", type=whileDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileDsl_ExprEq63", type=whileDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_whileDsl_ForeachCommand_Command = Generalization(general=Command, specific=whileDsl_ForeachCommand)
gen_whileDsl_WhileCommand_Command = Generalization(general=Command, specific=whileDsl_WhileCommand)
gen_whileDsl_ForCommand_Command = Generalization(general=Command, specific=whileDsl_ForCommand)
gen_whileDsl_IfCommand_Command = Generalization(general=Command, specific=whileDsl_IfCommand)
gen_whileDsl_VarsCommand_Command = Generalization(general=Command, specific=whileDsl_VarsCommand)
gen_whileDsl_NopCommand_Command = Generalization(general=Command, specific=whileDsl_NopCommand)

# Domain Model
domain_model = DomainModel(
    name="whileDsl",
    types={whileDsl_Model, whileDsl_ForeachCommand, whileDsl_Function, whileDsl_Definition, whileDsl_Input, whileDsl_Commands, whileDsl_Output, whileDsl_Command, whileDsl_WhileCommand, Command, whileDsl_Expr, whileDsl_ForCommand, whileDsl_IfCommand, whileDsl_ExprEq, whileDsl_VarsCommand, whileDsl_Vars, whileDsl_Exprs, whileDsl_ExprSimple, whileDsl_EObject, whileDsl_ExprSimpleWithLExpr, whileDsl_LExpr, whileDsl_ExprSimpleWithExpr, whileDsl_ExprSimpleWithSymbolLExpr, whileDsl_ExprAnd, whileDsl_ExprOr, whileDsl_ExprNot, whileDsl_NopCommand},
    associations={program0, functionDefinition1, intput3, body5, output7, commands9, cond11, body12, cond15, body17, cond20, thenBody22, elseBody25, expressionsNot52, expList28, body30, variables33, values34, expression36, lexpr37, expr38, lexpr40, expressions42, expressions45, expression48, expressionsOr51, expressionEq54, exprLSimple56, exprRSimple59, expr62},
    generalizations={gen_whileDsl_ForeachCommand_Command, gen_whileDsl_WhileCommand_Command, gen_whileDsl_ForCommand_Command, gen_whileDsl_IfCommand_Command, gen_whileDsl_VarsCommand_Command, gen_whileDsl_NopCommand_Command},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
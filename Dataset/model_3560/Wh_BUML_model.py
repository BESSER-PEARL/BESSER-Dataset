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
wh_Model = Class(name="wh::Model")
wh_Program = Class(name="wh::Program")
wh_Function = Class(name="wh::Function")
wh_Definition = Class(name="wh::Definition")
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")
wh_Command = Class(name="wh::Command")
wh_EObject = Class(name="wh::EObject")
wh_Nop = Class(name="wh::Nop")
wh_Assign = Class(name="wh::Assign")
wh_Vars = Class(name="wh::Vars")
wh_Exprs = Class(name="wh::Exprs")
wh_While = Class(name="wh::While")
wh_Expr = Class(name="wh::Expr")
wh_For = Class(name="wh::For")
wh_If = Class(name="wh::If")
wh_LExpr = Class(name="wh::LExpr")
wh_Foreach = Class(name="wh::Foreach")
wh_ExprAnd = Class(name="wh::ExprAnd")
wh_ExprSimple = Class(name="wh::ExprSimple")
wh_ExprOr = Class(name="wh::ExprOr")
wh_ExprNot = Class(name="wh::ExprNot")
wh_ExprEq = Class(name="wh::ExprEq")

# wh_Model class attributes and methods

# wh_Program class attributes and methods

# wh_Function class attributes and methods
wh_Function_fname: Property = Property(name="fname", type=StringType)
wh_Function.attributes={wh_Function_fname}

# wh_Definition class attributes and methods

# wh_Input class attributes and methods
wh_Input_params: Property = Property(name="params", type=StringType)
wh_Input.attributes={wh_Input_params}

# wh_Commands class attributes and methods

# wh_Output class attributes and methods
wh_Output_r_values: Property = Property(name="r_values", type=StringType)
wh_Output.attributes={wh_Output_r_values}

# wh_Command class attributes and methods

# wh_EObject class attributes and methods

# wh_Nop class attributes and methods
wh_Nop_nop: Property = Property(name="nop", type=StringType)
wh_Nop.attributes={wh_Nop_nop}

# wh_Assign class attributes and methods

# wh_Vars class attributes and methods
wh_Vars_variables: Property = Property(name="variables", type=StringType)
wh_Vars.attributes={wh_Vars_variables}

# wh_Exprs class attributes and methods

# wh_While class attributes and methods

# wh_Expr class attributes and methods

# wh_For class attributes and methods

# wh_If class attributes and methods

# wh_LExpr class attributes and methods

# wh_Foreach class attributes and methods

# wh_ExprAnd class attributes and methods

# wh_ExprSimple class attributes and methods
wh_ExprSimple_sym: Property = Property(name="sym", type=StringType)
wh_ExprSimple_nil: Property = Property(name="nil", type=StringType)
wh_ExprSimple_variable: Property = Property(name="variable", type=StringType)
wh_ExprSimple.attributes={wh_ExprSimple_nil, wh_ExprSimple_variable, wh_ExprSimple_sym}

# wh_ExprOr class attributes and methods

# wh_ExprNot class attributes and methods
wh_ExprNot_hasNot: Property = Property(name="hasNot", type=StringType)
wh_ExprNot.attributes={wh_ExprNot_hasNot}

# wh_ExprEq class attributes and methods
wh_ExprEq_sym: Property = Property(name="sym", type=StringType)
wh_ExprEq.attributes={wh_ExprEq_sym}

# Relationships
text0: BinaryAssociation = BinaryAssociation(
    name="text0",
    ends={
        Property(name="wh_Program", type=wh_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Model", type=wh_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions1: BinaryAssociation = BinaryAssociation(
    name="functions1",
    ends={
        Property(name="wh_Function", type=wh_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Program2", type=wh_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition3: BinaryAssociation = BinaryAssociation(
    name="definition3",
    ends={
        Property(name="wh_Definition", type=wh_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Function4", type=wh_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs5: BinaryAssociation = BinaryAssociation(
    name="inputs5",
    ends={
        Property(name="wh_Input", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition6", type=wh_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands7: BinaryAssociation = BinaryAssociation(
    name="commands7",
    ends={
        Property(name="wh_Commands", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition8", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs9: BinaryAssociation = BinaryAssociation(
    name="outputs9",
    ends={
        Property(name="wh_Output", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition10", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
command11: BinaryAssociation = BinaryAssociation(
    name="command11",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands12", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command13: BinaryAssociation = BinaryAssociation(
    name="command13",
    ends={
        Property(name="wh_EObject", type=wh_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Command14", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars15: BinaryAssociation = BinaryAssociation(
    name="vars15",
    ends={
        Property(name="wh_Vars", type=wh_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Assign", type=wh_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs16: BinaryAssociation = BinaryAssociation(
    name="exprs16",
    ends={
        Property(name="wh_Exprs", type=wh_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Assign17", type=wh_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond18: BinaryAssociation = BinaryAssociation(
    name="cond18",
    ends={
        Property(name="wh_Expr", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands19: BinaryAssociation = BinaryAssociation(
    name="commands19",
    ends={
        Property(name="wh_Commands21", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While20", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond22: BinaryAssociation = BinaryAssociation(
    name="cond22",
    ends={
        Property(name="wh_Expr23", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands24: BinaryAssociation = BinaryAssociation(
    name="commands24",
    ends={
        Property(name="wh_Commands26", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For25", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond27: BinaryAssociation = BinaryAssociation(
    name="cond27",
    ends={
        Property(name="wh_Expr28", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cons_exp48: BinaryAssociation = BinaryAssociation(
    name="cons_exp48",
    ends={
        Property(name="wh_LExpr", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple", type=wh_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_commands29: BinaryAssociation = BinaryAssociation(
    name="if_commands29",
    ends={
        Property(name="wh_Commands31", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If30", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else_commands32: BinaryAssociation = BinaryAssociation(
    name="else_commands32",
    ends={
        Property(name="wh_Commands34", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If33", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond35: BinaryAssociation = BinaryAssociation(
    name="cond35",
    ends={
        Property(name="wh_Expr36", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ens37: BinaryAssociation = BinaryAssociation(
    name="ens37",
    ends={
        Property(name="wh_Expr39", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach38", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands40: BinaryAssociation = BinaryAssociation(
    name="commands40",
    ends={
        Property(name="wh_Commands42", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach41", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr43: BinaryAssociation = BinaryAssociation(
    name="expr43",
    ends={
        Property(name="wh_Expr45", type=wh_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Exprs44", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr_and46: BinaryAssociation = BinaryAssociation(
    name="expr_and46",
    ends={
        Property(name="wh_ExprAnd", type=wh_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Expr47", type=wh_ExprAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list_exp49: BinaryAssociation = BinaryAssociation(
    name="list_exp49",
    ends={
        Property(name="wh_LExpr51", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple50", type=wh_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hd_expr52: BinaryAssociation = BinaryAssociation(
    name="hd_expr52",
    ends={
        Property(name="wh_Expr54", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple53", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tl_expr55: BinaryAssociation = BinaryAssociation(
    name="tl_expr55",
    ends={
        Property(name="wh_Expr57", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple56", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr_or58: BinaryAssociation = BinaryAssociation(
    name="expr_or58",
    ends={
        Property(name="wh_ExprOr", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd59", type=wh_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr_not60: BinaryAssociation = BinaryAssociation(
    name="expr_not60",
    ends={
        Property(name="wh_ExprNot", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr61", type=wh_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr73: BinaryAssociation = BinaryAssociation(
    name="expr73",
    ends={
        Property(name="wh_Expr75", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq74", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr_eq62: BinaryAssociation = BinaryAssociation(
    name="expr_eq62",
    ends={
        Property(name="wh_ExprEq", type=wh_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprNot63", type=wh_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr76: BinaryAssociation = BinaryAssociation(
    name="expr76",
    ends={
        Property(name="wh_Expr78", type=wh_LExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_LExpr77", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr_left64: BinaryAssociation = BinaryAssociation(
    name="expr_left64",
    ends={
        Property(name="wh_ExprSimple66", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq65", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr_right67: BinaryAssociation = BinaryAssociation(
    name="expr_right67",
    ends={
        Property(name="wh_ExprSimple69", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq68", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr70: BinaryAssociation = BinaryAssociation(
    name="lexpr70",
    ends={
        Property(name="wh_LExpr72", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq71", type=wh_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Model, wh_Program, wh_Function, wh_Definition, wh_Input, wh_Commands, wh_Output, wh_Command, wh_EObject, wh_Nop, wh_Assign, wh_Vars, wh_Exprs, wh_While, wh_Expr, wh_For, wh_If, wh_LExpr, wh_Foreach, wh_ExprAnd, wh_ExprSimple, wh_ExprOr, wh_ExprNot, wh_ExprEq},
    associations={text0, functions1, definition3, inputs5, commands7, outputs9, command11, command13, vars15, exprs16, cond18, commands19, cond22, commands24, cond27, cons_exp48, if_commands29, else_commands32, cond35, ens37, commands40, expr43, expr_and46, list_exp49, hd_expr52, tl_expr55, expr_or58, expr_not60, expr73, expr_eq62, expr76, expr_left64, expr_right67, lexpr70},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
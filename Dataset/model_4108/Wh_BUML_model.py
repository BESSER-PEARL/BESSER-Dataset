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
wh_Wh = Class(name="wh::Wh")
wh_Program = Class(name="wh::Program")
wh_Foreach = Class(name="wh::Foreach")
wh_Expr = Class(name="wh::Expr")
wh_For = Class(name="wh::For")
wh_While = Class(name="wh::While")
wh_If = Class(name="wh::If")
wh_Definition = Class(name="wh::Definition")
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")
wh_Command = Class(name="wh::Command")
wh_EObject = Class(name="wh::EObject")
wh_ExprAnd = Class(name="wh::ExprAnd")
wh_ExprOr = Class(name="wh::ExprOr")
wh_ExprNot = Class(name="wh::ExprNot")
wh_ExprEq = Class(name="wh::ExprEq")
wh_Nop = Class(name="wh::Nop")
wh_Affect = Class(name="wh::Affect")
wh_Vars = Class(name="wh::Vars")
wh_Exprs = Class(name="wh::Exprs")
wh_ExprSimple = Class(name="wh::ExprSimple")
wh_Cons = Class(name="wh::Cons")
wh_ListExpr = Class(name="wh::ListExpr")

# wh_Wh class attributes and methods

# wh_Program class attributes and methods
wh_Program_name: Property = Property(name="name", type=StringType)
wh_Program.attributes={wh_Program_name}

# wh_Foreach class attributes and methods

# wh_Expr class attributes and methods

# wh_For class attributes and methods

# wh_While class attributes and methods

# wh_If class attributes and methods

# wh_Definition class attributes and methods

# wh_Input class attributes and methods
wh_Input_vars: Property = Property(name="vars", type=StringType)
wh_Input.attributes={wh_Input_vars}

# wh_Commands class attributes and methods

# wh_Output class attributes and methods
wh_Output_vars: Property = Property(name="vars", type=StringType)
wh_Output.attributes={wh_Output_vars}

# wh_Command class attributes and methods

# wh_EObject class attributes and methods

# wh_ExprAnd class attributes and methods

# wh_ExprOr class attributes and methods

# wh_ExprNot class attributes and methods
wh_ExprNot_not: Property = Property(name="not", type=StringType)
wh_ExprNot.attributes={wh_ExprNot_not}

# wh_ExprEq class attributes and methods

# wh_Nop class attributes and methods
wh_Nop_nop: Property = Property(name="nop", type=StringType)
wh_Nop.attributes={wh_Nop_nop}

# wh_Affect class attributes and methods

# wh_Vars class attributes and methods
wh_Vars_vars: Property = Property(name="vars", type=StringType)
wh_Vars.attributes={wh_Vars_vars}

# wh_Exprs class attributes and methods

# wh_ExprSimple class attributes and methods
wh_ExprSimple_str: Property = Property(name="str", type=StringType)
wh_ExprSimple_strSymb: Property = Property(name="strSymb", type=StringType)
wh_ExprSimple.attributes={wh_ExprSimple_str, wh_ExprSimple_strSymb}

# wh_Cons class attributes and methods

# wh_ListExpr class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wh_Program", type=wh_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Wh", type=wh_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd11: BinaryAssociation = BinaryAssociation(
    name="cmd11",
    ends={
        Property(name="wh_EObject", type=wh_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Command12", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr113: BinaryAssociation = BinaryAssociation(
    name="expr113",
    ends={
        Property(name="wh_Expr", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr214: BinaryAssociation = BinaryAssociation(
    name="expr214",
    ends={
        Property(name="wh_Expr16", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach15", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds17: BinaryAssociation = BinaryAssociation(
    name="cmds17",
    ends={
        Property(name="wh_Commands19", type=wh_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Foreach18", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr20: BinaryAssociation = BinaryAssociation(
    name="expr20",
    ends={
        Property(name="wh_Expr21", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds22: BinaryAssociation = BinaryAssociation(
    name="cmds22",
    ends={
        Property(name="wh_Commands24", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For23", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr25: BinaryAssociation = BinaryAssociation(
    name="expr25",
    ends={
        Property(name="wh_Expr26", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds27: BinaryAssociation = BinaryAssociation(
    name="cmds27",
    ends={
        Property(name="wh_Commands29", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While28", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr30: BinaryAssociation = BinaryAssociation(
    name="expr30",
    ends={
        Property(name="wh_Expr31", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsTrue32: BinaryAssociation = BinaryAssociation(
    name="cmdsTrue32",
    ends={
        Property(name="wh_Commands34", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If33", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsFalse35: BinaryAssociation = BinaryAssociation(
    name="cmdsFalse35",
    ends={
        Property(name="wh_Commands37", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If36", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition1: BinaryAssociation = BinaryAssociation(
    name="definition1",
    ends={
        Property(name="wh_Definition", type=wh_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Program2", type=wh_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="wh_Input", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition4", type=wh_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
command5: BinaryAssociation = BinaryAssociation(
    name="command5",
    ends={
        Property(name="wh_Commands", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition6", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output7: BinaryAssociation = BinaryAssociation(
    name="output7",
    ends={
        Property(name="wh_Output", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition8", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands9: BinaryAssociation = BinaryAssociation(
    name="commands9",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands10", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listExpr48: BinaryAssociation = BinaryAssociation(
    name="listExpr48",
    ends={
        Property(name="wh_ListExpr", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple49", type=wh_ListExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprHd50: BinaryAssociation = BinaryAssociation(
    name="exprHd50",
    ends={
        Property(name="wh_Expr52", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple51", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprTl53: BinaryAssociation = BinaryAssociation(
    name="exprTl53",
    ends={
        Property(name="wh_Expr55", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple54", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list56: BinaryAssociation = BinaryAssociation(
    name="list56",
    ends={
        Property(name="wh_ListExpr58", type=wh_Cons, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Cons57", type=wh_ListExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs59: BinaryAssociation = BinaryAssociation(
    name="exprs59",
    ends={
        Property(name="wh_Expr61", type=wh_ListExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ListExpr60", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprOr162: BinaryAssociation = BinaryAssociation(
    name="exprOr162",
    ends={
        Property(name="wh_ExprOr", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd", type=wh_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprOrX63: BinaryAssociation = BinaryAssociation(
    name="exprOrX63",
    ends={
        Property(name="wh_ExprOr65", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd64", type=wh_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprNot166: BinaryAssociation = BinaryAssociation(
    name="exprNot166",
    ends={
        Property(name="wh_ExprNot", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr67", type=wh_ExprNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprNotX68: BinaryAssociation = BinaryAssociation(
    name="exprNotX68",
    ends={
        Property(name="wh_ExprNot70", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr69", type=wh_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr71: BinaryAssociation = BinaryAssociation(
    name="expr71",
    ends={
        Property(name="wh_ExprEq", type=wh_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprNot72", type=wh_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars38: BinaryAssociation = BinaryAssociation(
    name="vars38",
    ends={
        Property(name="wh_Vars", type=wh_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Affect", type=wh_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp39: BinaryAssociation = BinaryAssociation(
    name="exp39",
    ends={
        Property(name="wh_Exprs", type=wh_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Affect40", type=wh_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs41: BinaryAssociation = BinaryAssociation(
    name="exprs41",
    ends={
        Property(name="wh_Expr43", type=wh_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Exprs42", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr44: BinaryAssociation = BinaryAssociation(
    name="expr44",
    ends={
        Property(name="wh_EObject46", type=wh_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Expr45", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cons47: BinaryAssociation = BinaryAssociation(
    name="cons47",
    ends={
        Property(name="wh_Cons", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple", type=wh_Cons, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSimp173: BinaryAssociation = BinaryAssociation(
    name="exprSimp173",
    ends={
        Property(name="wh_ExprSimple75", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq74", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSimp276: BinaryAssociation = BinaryAssociation(
    name="exprSimp276",
    ends={
        Property(name="wh_ExprSimple78", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq77", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr79: BinaryAssociation = BinaryAssociation(
    name="expr79",
    ends={
        Property(name="wh_Expr81", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq80", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Wh, wh_Program, wh_Foreach, wh_Expr, wh_For, wh_While, wh_If, wh_Definition, wh_Input, wh_Commands, wh_Output, wh_Command, wh_EObject, wh_ExprAnd, wh_ExprOr, wh_ExprNot, wh_ExprEq, wh_Nop, wh_Affect, wh_Vars, wh_Exprs, wh_ExprSimple, wh_Cons, wh_ListExpr},
    associations={elements0, cmd11, expr113, expr214, cmds17, expr20, cmds22, expr25, cmds27, expr30, cmdsTrue32, cmdsFalse35, definition1, input3, command5, output7, commands9, listExpr48, exprHd50, exprTl53, list56, exprs59, exprOr162, exprOrX63, exprNot166, exprNotX68, expr71, vars38, exp39, exprs41, expr44, cons47, exprSimp173, exprSimp276, expr79},
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
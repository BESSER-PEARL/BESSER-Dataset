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
while_l_Wh = Class(name="while::l::Wh")
while_l_Program = Class(name="while::l::Program")
while_l_For = Class(name="while::l::For")
while_l_Function = Class(name="while::l::Function")
while_l_Definition = Class(name="while::l::Definition")
while_l_Input = Class(name="while::l::Input")
while_l_Commands = Class(name="while::l::Commands")
while_l_Output = Class(name="while::l::Output")
while_l_Command = Class(name="while::l::Command")
while_l_EObject = Class(name="while::l::EObject")
while_l_If = Class(name="while::l::If")
while_l_Expr = Class(name="while::l::Expr")
while_l_Nop = Class(name="while::l::Nop")
while_l_Affect = Class(name="while::l::Affect")
while_l_ExprTl = Class(name="while::l::ExprTl")
while_l_ExprSym = Class(name="while::l::ExprSym")
while_l_While = Class(name="while::l::While")
while_l_ExprEq = Class(name="while::l::ExprEq")
while_l_ExprSimple = Class(name="while::l::ExprSimple")
while_l_ExprAnd = Class(name="while::l::ExprAnd")
while_l_ExprOr = Class(name="while::l::ExprOr")
while_l_ExprCons = Class(name="while::l::ExprCons")
while_l_ExprList = Class(name="while::l::ExprList")
while_l_ExprHd = Class(name="while::l::ExprHd")
while_l_ExprNot = Class(name="while::l::ExprNot")

# while_l_Wh class attributes and methods

# while_l_Program class attributes and methods

# while_l_For class attributes and methods

# while_l_Function class attributes and methods
while_l_Function_name: Property = Property(name="name", type=StringType)
while_l_Function.attributes={while_l_Function_name}

# while_l_Definition class attributes and methods

# while_l_Input class attributes and methods
while_l_Input_vars: Property = Property(name="vars", type=StringType)
while_l_Input.attributes={while_l_Input_vars}

# while_l_Commands class attributes and methods

# while_l_Output class attributes and methods
while_l_Output_vars: Property = Property(name="vars", type=StringType)
while_l_Output.attributes={while_l_Output_vars}

# while_l_Command class attributes and methods

# while_l_EObject class attributes and methods

# while_l_If class attributes and methods

# while_l_Expr class attributes and methods

# while_l_Nop class attributes and methods
while_l_Nop_nop: Property = Property(name="nop", type=StringType)
while_l_Nop.attributes={while_l_Nop_nop}

# while_l_Affect class attributes and methods
while_l_Affect_vars: Property = Property(name="vars", type=StringType)
while_l_Affect.attributes={while_l_Affect_vars}

# while_l_ExprTl class attributes and methods

# while_l_ExprSym class attributes and methods
while_l_ExprSym_arg1: Property = Property(name="arg1", type=StringType)
while_l_ExprSym.attributes={while_l_ExprSym_arg1}

# while_l_While class attributes and methods

# while_l_ExprEq class attributes and methods

# while_l_ExprSimple class attributes and methods
while_l_ExprSimple_str: Property = Property(name="str", type=StringType)
while_l_ExprSimple_varSimple: Property = Property(name="varSimple", type=StringType)
while_l_ExprSimple_sym: Property = Property(name="sym", type=StringType)
while_l_ExprSimple_nameFunction: Property = Property(name="nameFunction", type=StringType)
while_l_ExprSimple.attributes={while_l_ExprSimple_sym, while_l_ExprSimple_varSimple, while_l_ExprSimple_str, while_l_ExprSimple_nameFunction}

# while_l_ExprAnd class attributes and methods

# while_l_ExprOr class attributes and methods

# while_l_ExprCons class attributes and methods

# while_l_ExprList class attributes and methods

# while_l_ExprHd class attributes and methods

# while_l_ExprNot class attributes and methods

# Relationships
exprs22: BinaryAssociation = BinaryAssociation(
    name="exprs22",
    ends={
        Property(name="while_l_Expr23", type=while_l_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Affect", type=while_l_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr24: BinaryAssociation = BinaryAssociation(
    name="expr24",
    ends={
        Property(name="while_l_Expr25", type=while_l_For, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_For", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds26: BinaryAssociation = BinaryAssociation(
    name="cmds26",
    ends={
        Property(name="while_l_Commands28", type=while_l_For, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_For27", type=while_l_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="while_l_Program", type=while_l_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Wh", type=while_l_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions1: BinaryAssociation = BinaryAssociation(
    name="functions1",
    ends={
        Property(name="while_l_Function", type=while_l_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Program2", type=while_l_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition3: BinaryAssociation = BinaryAssociation(
    name="definition3",
    ends={
        Property(name="while_l_Definition", type=while_l_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Function4", type=while_l_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
    ends={
        Property(name="while_l_Input", type=while_l_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Definition6", type=while_l_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands7: BinaryAssociation = BinaryAssociation(
    name="commands7",
    ends={
        Property(name="while_l_Commands", type=while_l_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Definition8", type=while_l_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output9: BinaryAssociation = BinaryAssociation(
    name="output9",
    ends={
        Property(name="while_l_Output", type=while_l_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Definition10", type=while_l_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands11: BinaryAssociation = BinaryAssociation(
    name="commands11",
    ends={
        Property(name="while_l_Command", type=while_l_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Commands12", type=while_l_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd13: BinaryAssociation = BinaryAssociation(
    name="cmd13",
    ends={
        Property(name="while_l_EObject", type=while_l_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Command14", type=while_l_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr15: BinaryAssociation = BinaryAssociation(
    name="expr15",
    ends={
        Property(name="while_l_Expr", type=while_l_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_If", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands116: BinaryAssociation = BinaryAssociation(
    name="commands116",
    ends={
        Property(name="while_l_Commands18", type=while_l_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_If17", type=while_l_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands219: BinaryAssociation = BinaryAssociation(
    name="commands219",
    ends={
        Property(name="while_l_Commands21", type=while_l_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_If20", type=while_l_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg60: BinaryAssociation = BinaryAssociation(
    name="arg60",
    ends={
        Property(name="while_l_Expr61", type=while_l_ExprTl, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprTl", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg262: BinaryAssociation = BinaryAssociation(
    name="arg262",
    ends={
        Property(name="while_l_Expr63", type=while_l_ExprSym, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprSym", type=while_l_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr29: BinaryAssociation = BinaryAssociation(
    name="expr29",
    ends={
        Property(name="while_l_Expr30", type=while_l_While, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_While", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds31: BinaryAssociation = BinaryAssociation(
    name="cmds31",
    ends={
        Property(name="while_l_Commands33", type=while_l_While, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_While32", type=while_l_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr34: BinaryAssociation = BinaryAssociation(
    name="expr34",
    ends={
        Property(name="while_l_EObject36", type=while_l_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Expr35", type=while_l_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprEq37: BinaryAssociation = BinaryAssociation(
    name="exprEq37",
    ends={
        Property(name="while_l_ExprEq", type=while_l_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_Expr38", type=while_l_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars39: BinaryAssociation = BinaryAssociation(
    name="vars39",
    ends={
        Property(name="while_l_Input40", type=while_l_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprSimple", type=while_l_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg141: BinaryAssociation = BinaryAssociation(
    name="arg141",
    ends={
        Property(name="while_l_ExprSimple42", type=while_l_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprAnd", type=while_l_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg243: BinaryAssociation = BinaryAssociation(
    name="arg243",
    ends={
        Property(name="while_l_Expr45", type=while_l_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprAnd44", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg146: BinaryAssociation = BinaryAssociation(
    name="arg146",
    ends={
        Property(name="while_l_ExprSimple47", type=while_l_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprOr", type=while_l_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg248: BinaryAssociation = BinaryAssociation(
    name="arg248",
    ends={
        Property(name="while_l_Expr50", type=while_l_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprOr49", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg151: BinaryAssociation = BinaryAssociation(
    name="arg151",
    ends={
        Property(name="while_l_Expr52", type=while_l_ExprCons, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprCons", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg253: BinaryAssociation = BinaryAssociation(
    name="arg253",
    ends={
        Property(name="while_l_Expr55", type=while_l_ExprCons, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprCons54", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg56: BinaryAssociation = BinaryAssociation(
    name="arg56",
    ends={
        Property(name="while_l_Expr57", type=while_l_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprList", type=while_l_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg58: BinaryAssociation = BinaryAssociation(
    name="arg58",
    ends={
        Property(name="while_l_Expr59", type=while_l_ExprHd, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprHd", type=while_l_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg164: BinaryAssociation = BinaryAssociation(
    name="arg164",
    ends={
        Property(name="while_l_ExprEq65", type=while_l_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprNot", type=while_l_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg166: BinaryAssociation = BinaryAssociation(
    name="arg166",
    ends={
        Property(name="while_l_ExprSimple68", type=while_l_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprEq67", type=while_l_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg269: BinaryAssociation = BinaryAssociation(
    name="arg269",
    ends={
        Property(name="while_l_ExprSimple71", type=while_l_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="while_l_ExprEq70", type=while_l_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="while_l",
    types={while_l_Wh, while_l_Program, while_l_For, while_l_Function, while_l_Definition, while_l_Input, while_l_Commands, while_l_Output, while_l_Command, while_l_EObject, while_l_If, while_l_Expr, while_l_Nop, while_l_Affect, while_l_ExprTl, while_l_ExprSym, while_l_While, while_l_ExprEq, while_l_ExprSimple, while_l_ExprAnd, while_l_ExprOr, while_l_ExprCons, while_l_ExprList, while_l_ExprHd, while_l_ExprNot},
    associations={exprs22, expr24, cmds26, elements0, functions1, definition3, input5, commands7, output9, commands11, cmd13, expr15, commands116, commands219, arg60, arg262, expr29, cmds31, expr34, exprEq37, vars39, arg141, arg243, arg146, arg248, arg151, arg253, arg56, arg58, arg164, arg166, arg269},
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
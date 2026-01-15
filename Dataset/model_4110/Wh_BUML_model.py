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
wh_Command = Class(name="wh::Command")
wh_EObject = Class(name="wh::EObject")
wh_If = Class(name="wh::If")
wh_Expr = Class(name="wh::Expr")
wh_Nop = Class(name="wh::Nop")
wh_Affect = Class(name="wh::Affect")
wh_Wh = Class(name="wh::Wh")
wh_Program = Class(name="wh::Program")
wh_Function = Class(name="wh::Function")
wh_Definition = Class(name="wh::Definition")
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")
wh_ExprOr = Class(name="wh::ExprOr")
wh_ExprCons = Class(name="wh::ExprCons")
wh_ExprList = Class(name="wh::ExprList")
wh_ExprHd = Class(name="wh::ExprHd")
wh_ExprTl = Class(name="wh::ExprTl")
wh_For = Class(name="wh::For")
wh_While = Class(name="wh::While")
wh_ExprSimple = Class(name="wh::ExprSimple")
Expr = Class(name="Expr")
wh_ExprAnd = Class(name="wh::ExprAnd")
wh_ExprSym = Class(name="wh::ExprSym")
wh_ExprNot = Class(name="wh::ExprNot")
wh_ExprEq = Class(name="wh::ExprEq")

# wh_Command class attributes and methods

# wh_EObject class attributes and methods

# wh_If class attributes and methods

# wh_Expr class attributes and methods

# wh_Nop class attributes and methods
wh_Nop_nop: Property = Property(name="nop", type=StringType)
wh_Nop.attributes={wh_Nop_nop}

# wh_Affect class attributes and methods
wh_Affect_vars: Property = Property(name="vars", type=StringType)
wh_Affect.attributes={wh_Affect_vars}

# wh_Wh class attributes and methods

# wh_Program class attributes and methods

# wh_Function class attributes and methods
wh_Function_name: Property = Property(name="name", type=StringType)
wh_Function.attributes={wh_Function_name}

# wh_Definition class attributes and methods

# wh_Input class attributes and methods
wh_Input_vars: Property = Property(name="vars", type=StringType)
wh_Input.attributes={wh_Input_vars}

# wh_Commands class attributes and methods

# wh_Output class attributes and methods
wh_Output_vars: Property = Property(name="vars", type=StringType)
wh_Output.attributes={wh_Output_vars}

# wh_ExprOr class attributes and methods

# wh_ExprCons class attributes and methods

# wh_ExprList class attributes and methods

# wh_ExprHd class attributes and methods

# wh_ExprTl class attributes and methods

# wh_For class attributes and methods

# wh_While class attributes and methods

# wh_ExprSimple class attributes and methods
wh_ExprSimple_str: Property = Property(name="str", type=StringType)
wh_ExprSimple_varSimple: Property = Property(name="varSimple", type=StringType)
wh_ExprSimple_sym: Property = Property(name="sym", type=StringType)
wh_ExprSimple.attributes={wh_ExprSimple_sym, wh_ExprSimple_varSimple, wh_ExprSimple_str}

# Expr class attributes and methods

# wh_ExprAnd class attributes and methods

# wh_ExprSym class attributes and methods
wh_ExprSym_arg1: Property = Property(name="arg1", type=StringType)
wh_ExprSym.attributes={wh_ExprSym_arg1}

# wh_ExprNot class attributes and methods

# wh_ExprEq class attributes and methods

# Relationships
commands11: BinaryAssociation = BinaryAssociation(
    name="commands11",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands12", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd13: BinaryAssociation = BinaryAssociation(
    name="cmd13",
    ends={
        Property(name="wh_EObject", type=wh_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Command14", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr15: BinaryAssociation = BinaryAssociation(
    name="expr15",
    ends={
        Property(name="wh_Expr", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands116: BinaryAssociation = BinaryAssociation(
    name="commands116",
    ends={
        Property(name="wh_Commands18", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If17", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands219: BinaryAssociation = BinaryAssociation(
    name="commands219",
    ends={
        Property(name="wh_Commands21", type=wh_If, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_If20", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wh_Program", type=wh_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Wh", type=wh_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
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
output9: BinaryAssociation = BinaryAssociation(
    name="output9",
    ends={
        Property(name="wh_Output", type=wh_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Definition10", type=wh_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg238: BinaryAssociation = BinaryAssociation(
    name="arg238",
    ends={
        Property(name="wh_ExprAnd39", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="wh_Expr40", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1))
    }
)
arg141: BinaryAssociation = BinaryAssociation(
    name="arg141",
    ends={
        Property(name="wh_ExprSimple42", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg243: BinaryAssociation = BinaryAssociation(
    name="arg243",
    ends={
        Property(name="wh_Expr45", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr44", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg46: BinaryAssociation = BinaryAssociation(
    name="arg46",
    ends={
        Property(name="wh_Expr47", type=wh_ExprCons, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprCons", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg48: BinaryAssociation = BinaryAssociation(
    name="arg48",
    ends={
        Property(name="wh_Expr49", type=wh_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprList", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg50: BinaryAssociation = BinaryAssociation(
    name="arg50",
    ends={
        Property(name="wh_Expr51", type=wh_ExprHd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprHd", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs22: BinaryAssociation = BinaryAssociation(
    name="exprs22",
    ends={
        Property(name="wh_Expr23", type=wh_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Affect", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg52: BinaryAssociation = BinaryAssociation(
    name="arg52",
    ends={
        Property(name="wh_Expr53", type=wh_ExprTl, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprTl", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr24: BinaryAssociation = BinaryAssociation(
    name="expr24",
    ends={
        Property(name="wh_Expr25", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds26: BinaryAssociation = BinaryAssociation(
    name="cmds26",
    ends={
        Property(name="wh_Commands28", type=wh_For, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_For27", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr29: BinaryAssociation = BinaryAssociation(
    name="expr29",
    ends={
        Property(name="wh_Expr30", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds31: BinaryAssociation = BinaryAssociation(
    name="cmds31",
    ends={
        Property(name="wh_Commands33", type=wh_While, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_While32", type=wh_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr35: BinaryAssociation = BinaryAssociation(
    name="expr35",
    ends={
        Property(name="wh_Expr36", type=wh_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Expr34", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg137: BinaryAssociation = BinaryAssociation(
    name="arg137",
    ends={
        Property(name="wh_ExprSimple", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg254: BinaryAssociation = BinaryAssociation(
    name="arg254",
    ends={
        Property(name="wh_Expr55", type=wh_ExprSym, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSym", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg156: BinaryAssociation = BinaryAssociation(
    name="arg156",
    ends={
        Property(name="wh_ExprEq", type=wh_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprNot", type=wh_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg157: BinaryAssociation = BinaryAssociation(
    name="arg157",
    ends={
        Property(name="wh_ExprSimple59", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq58", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg260: BinaryAssociation = BinaryAssociation(
    name="arg260",
    ends={
        Property(name="wh_ExprSimple62", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq61", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_wh_ExprOr_Expr = Generalization(general=Expr, specific=wh_ExprOr)
gen_wh_ExprCons_Expr = Generalization(general=Expr, specific=wh_ExprCons)
gen_wh_ExprList_Expr = Generalization(general=Expr, specific=wh_ExprList)
gen_wh_ExprHd_Expr = Generalization(general=Expr, specific=wh_ExprHd)
gen_wh_ExprTl_Expr = Generalization(general=Expr, specific=wh_ExprTl)
gen_wh_ExprSimple_Expr = Generalization(general=Expr, specific=wh_ExprSimple)
gen_wh_ExprAnd_Expr = Generalization(general=Expr, specific=wh_ExprAnd)
gen_wh_ExprSym_Expr = Generalization(general=Expr, specific=wh_ExprSym)
gen_wh_ExprNot_Expr = Generalization(general=Expr, specific=wh_ExprNot)
gen_wh_ExprEq_Expr = Generalization(general=Expr, specific=wh_ExprEq)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Command, wh_EObject, wh_If, wh_Expr, wh_Nop, wh_Affect, wh_Wh, wh_Program, wh_Function, wh_Definition, wh_Input, wh_Commands, wh_Output, wh_ExprOr, wh_ExprCons, wh_ExprList, wh_ExprHd, wh_ExprTl, wh_For, wh_While, wh_ExprSimple, Expr, wh_ExprAnd, wh_ExprSym, wh_ExprNot, wh_ExprEq},
    associations={commands11, cmd13, expr15, commands116, commands219, elements0, functions1, definition3, input5, commands7, output9, arg238, arg141, arg243, arg46, arg48, arg50, exprs22, arg52, expr24, cmds26, expr29, cmds31, expr35, arg137, arg254, arg156, arg157, arg260},
    generalizations={gen_wh_ExprOr_Expr, gen_wh_ExprCons_Expr, gen_wh_ExprList_Expr, gen_wh_ExprHd_Expr, gen_wh_ExprTl_Expr, gen_wh_ExprSimple_Expr, gen_wh_ExprAnd_Expr, gen_wh_ExprSym_Expr, gen_wh_ExprNot_Expr, gen_wh_ExprEq_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
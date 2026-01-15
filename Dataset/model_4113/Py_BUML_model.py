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
py_Program = Class(name="py::Program")
py_FunctionP = Class(name="py::FunctionP")
py_Definition = Class(name="py::Definition")
py_Input = Class(name="py::Input")
py_Commands = Class(name="py::Commands")
py_Output = Class(name="py::Output")
py_Command = Class(name="py::Command")
py_EObject = Class(name="py::EObject")
py_If = Class(name="py::If")
py_Expr = Class(name="py::Expr")
py_Wh = Class(name="py::Wh")
py_Foreach = Class(name="py::Foreach")
py_While = Class(name="py::While")
py_ExprSimple = Class(name="py::ExprSimple")
py_ExprAnd = Class(name="py::ExprAnd")
py_ExprOr = Class(name="py::ExprOr")
py_ExprCons = Class(name="py::ExprCons")
py_LExpr = Class(name="py::LExpr")
py_Nop = Class(name="py::Nop")
py_Affect = Class(name="py::Affect")
py_For = Class(name="py::For")
py_ExprHd = Class(name="py::ExprHd")
py_ExprTl = Class(name="py::ExprTl")
py_ExprSym = Class(name="py::ExprSym")
py_ExprNot = Class(name="py::ExprNot")
py_ExprEq = Class(name="py::ExprEq")
py_ExprList = Class(name="py::ExprList")

# py_Program class attributes and methods

# py_FunctionP class attributes and methods
py_FunctionP_name: Property = Property(name="name", type=StringType)
py_FunctionP.attributes={py_FunctionP_name}

# py_Definition class attributes and methods

# py_Input class attributes and methods
py_Input_vars: Property = Property(name="vars", type=StringType)
py_Input.attributes={py_Input_vars}

# py_Commands class attributes and methods

# py_Output class attributes and methods
py_Output_vars: Property = Property(name="vars", type=StringType)
py_Output.attributes={py_Output_vars}

# py_Command class attributes and methods

# py_EObject class attributes and methods

# py_If class attributes and methods

# py_Expr class attributes and methods

# py_Wh class attributes and methods

# py_Foreach class attributes and methods
py_Foreach_var: Property = Property(name="var", type=StringType)
py_Foreach.attributes={py_Foreach_var}

# py_While class attributes and methods

# py_ExprSimple class attributes and methods
py_ExprSimple_str: Property = Property(name="str", type=StringType)
py_ExprSimple_varSimple: Property = Property(name="varSimple", type=StringType)
py_ExprSimple_sym: Property = Property(name="sym", type=StringType)
py_ExprSimple.attributes={py_ExprSimple_str, py_ExprSimple_varSimple, py_ExprSimple_sym}

# py_ExprAnd class attributes and methods

# py_ExprOr class attributes and methods

# py_ExprCons class attributes and methods

# py_LExpr class attributes and methods

# py_Nop class attributes and methods
py_Nop_nop: Property = Property(name="nop", type=StringType)
py_Nop.attributes={py_Nop_nop}

# py_Affect class attributes and methods
py_Affect_vars: Property = Property(name="vars", type=StringType)
py_Affect.attributes={py_Affect_vars}

# py_For class attributes and methods

# py_ExprHd class attributes and methods

# py_ExprTl class attributes and methods

# py_ExprSym class attributes and methods
py_ExprSym_arg1: Property = Property(name="arg1", type=StringType)
py_ExprSym.attributes={py_ExprSym_arg1}

# py_ExprNot class attributes and methods

# py_ExprEq class attributes and methods

# py_ExprList class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="py_Program", type=py_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Wh", type=py_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions1: BinaryAssociation = BinaryAssociation(
    name="functions1",
    ends={
        Property(name="py_FunctionP", type=py_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Program2", type=py_FunctionP, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition3: BinaryAssociation = BinaryAssociation(
    name="definition3",
    ends={
        Property(name="py_Definition", type=py_FunctionP, multiplicity=Multiplicity(1, 1)),
        Property(name="py_FunctionP4", type=py_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
    ends={
        Property(name="py_Input", type=py_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Definition6", type=py_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands7: BinaryAssociation = BinaryAssociation(
    name="commands7",
    ends={
        Property(name="py_Commands", type=py_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Definition8", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output9: BinaryAssociation = BinaryAssociation(
    name="output9",
    ends={
        Property(name="py_Output", type=py_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Definition10", type=py_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands11: BinaryAssociation = BinaryAssociation(
    name="commands11",
    ends={
        Property(name="py_Command", type=py_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Commands12", type=py_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd13: BinaryAssociation = BinaryAssociation(
    name="cmd13",
    ends={
        Property(name="py_EObject", type=py_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Command14", type=py_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr15: BinaryAssociation = BinaryAssociation(
    name="expr15",
    ends={
        Property(name="py_Expr", type=py_If, multiplicity=Multiplicity(1, 1)),
        Property(name="py_If", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr24: BinaryAssociation = BinaryAssociation(
    name="expr24",
    ends={
        Property(name="py_Expr25", type=py_For, multiplicity=Multiplicity(1, 1)),
        Property(name="py_For", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds26: BinaryAssociation = BinaryAssociation(
    name="cmds26",
    ends={
        Property(name="py_Commands28", type=py_For, multiplicity=Multiplicity(1, 1)),
        Property(name="py_For27", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr229: BinaryAssociation = BinaryAssociation(
    name="expr229",
    ends={
        Property(name="py_Expr30", type=py_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Foreach", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmd31: BinaryAssociation = BinaryAssociation(
    name="cmd31",
    ends={
        Property(name="py_Commands33", type=py_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Foreach32", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr34: BinaryAssociation = BinaryAssociation(
    name="expr34",
    ends={
        Property(name="py_Expr35", type=py_While, multiplicity=Multiplicity(1, 1)),
        Property(name="py_While", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds36: BinaryAssociation = BinaryAssociation(
    name="cmds36",
    ends={
        Property(name="py_Commands38", type=py_While, multiplicity=Multiplicity(1, 1)),
        Property(name="py_While37", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr39: BinaryAssociation = BinaryAssociation(
    name="expr39",
    ends={
        Property(name="py_EObject41", type=py_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Expr40", type=py_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg142: BinaryAssociation = BinaryAssociation(
    name="arg142",
    ends={
        Property(name="py_ExprSimple", type=py_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprAnd", type=py_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg243: BinaryAssociation = BinaryAssociation(
    name="arg243",
    ends={
        Property(name="py_Expr45", type=py_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprAnd44", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg146: BinaryAssociation = BinaryAssociation(
    name="arg146",
    ends={
        Property(name="py_ExprSimple47", type=py_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprOr", type=py_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg248: BinaryAssociation = BinaryAssociation(
    name="arg248",
    ends={
        Property(name="py_Expr50", type=py_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprOr49", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands116: BinaryAssociation = BinaryAssociation(
    name="commands116",
    ends={
        Property(name="py_Commands18", type=py_If, multiplicity=Multiplicity(1, 1)),
        Property(name="py_If17", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands219: BinaryAssociation = BinaryAssociation(
    name="commands219",
    ends={
        Property(name="py_Commands21", type=py_If, multiplicity=Multiplicity(1, 1)),
        Property(name="py_If20", type=py_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs22: BinaryAssociation = BinaryAssociation(
    name="exprs22",
    ends={
        Property(name="py_Expr23", type=py_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="py_Affect", type=py_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg57: BinaryAssociation = BinaryAssociation(
    name="arg57",
    ends={
        Property(name="py_Expr58", type=py_ExprHd, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprHd", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg59: BinaryAssociation = BinaryAssociation(
    name="arg59",
    ends={
        Property(name="py_Expr60", type=py_ExprTl, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprTl", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg261: BinaryAssociation = BinaryAssociation(
    name="arg261",
    ends={
        Property(name="py_Expr62", type=py_ExprSym, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprSym", type=py_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg163: BinaryAssociation = BinaryAssociation(
    name="arg163",
    ends={
        Property(name="py_Expr64", type=py_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprNot", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg165: BinaryAssociation = BinaryAssociation(
    name="arg165",
    ends={
        Property(name="py_ExprSimple66", type=py_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprEq", type=py_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg267: BinaryAssociation = BinaryAssociation(
    name="arg267",
    ends={
        Property(name="py_Expr69", type=py_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprEq68", type=py_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr51: BinaryAssociation = BinaryAssociation(
    name="lexpr51",
    ends={
        Property(name="py_LExpr", type=py_ExprCons, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprCons", type=py_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr52: BinaryAssociation = BinaryAssociation(
    name="lexpr52",
    ends={
        Property(name="py_Expr54", type=py_LExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="py_LExpr53", type=py_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg55: BinaryAssociation = BinaryAssociation(
    name="arg55",
    ends={
        Property(name="py_Expr56", type=py_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="py_ExprList", type=py_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="py",
    types={py_Program, py_FunctionP, py_Definition, py_Input, py_Commands, py_Output, py_Command, py_EObject, py_If, py_Expr, py_Wh, py_Foreach, py_While, py_ExprSimple, py_ExprAnd, py_ExprOr, py_ExprCons, py_LExpr, py_Nop, py_Affect, py_For, py_ExprHd, py_ExprTl, py_ExprSym, py_ExprNot, py_ExprEq, py_ExprList},
    associations={elements0, functions1, definition3, input5, commands7, output9, commands11, cmd13, expr15, expr24, cmds26, expr229, cmd31, expr34, cmds36, expr39, arg142, arg243, arg146, arg248, commands116, commands219, exprs22, arg57, arg59, arg261, arg163, arg165, arg267, lexpr51, lexpr52, arg55},
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
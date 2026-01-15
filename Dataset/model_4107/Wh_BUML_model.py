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
wh_Command = Class(name="wh::Command")
wh_EObject = Class(name="wh::EObject")
wh_Nop = Class(name="wh::Nop")
wh_Affect = Class(name="wh::Affect")
wh_Vars = Class(name="wh::Vars")
wh_Exprs = Class(name="wh::Exprs")
wh_Expr = Class(name="wh::Expr")
wh_ExprSimple = Class(name="wh::ExprSimple")
wh_Cons = Class(name="wh::Cons")
wh_ListExpr = Class(name="wh::ListExpr")
wh_Definition = Class(name="wh::Definition")
wh_Input = Class(name="wh::Input")
wh_Commands = Class(name="wh::Commands")
wh_Output = Class(name="wh::Output")
wh_ExprEq = Class(name="wh::ExprEq")
wh_ExprAnd = Class(name="wh::ExprAnd")
wh_ExprOr = Class(name="wh::ExprOr")
wh_ExprNot = Class(name="wh::ExprNot")

# wh_Wh class attributes and methods

# wh_Program class attributes and methods
wh_Program_name: Property = Property(name="name", type=StringType)
wh_Program.attributes={wh_Program_name}

# wh_Command class attributes and methods

# wh_EObject class attributes and methods

# wh_Nop class attributes and methods
wh_Nop_nop: Property = Property(name="nop", type=StringType)
wh_Nop.attributes={wh_Nop_nop}

# wh_Affect class attributes and methods

# wh_Vars class attributes and methods
wh_Vars_vars: Property = Property(name="vars", type=StringType)
wh_Vars.attributes={wh_Vars_vars}

# wh_Exprs class attributes and methods

# wh_Expr class attributes and methods

# wh_ExprSimple class attributes and methods
wh_ExprSimple_str: Property = Property(name="str", type=StringType)
wh_ExprSimple.attributes={wh_ExprSimple_str}

# wh_Cons class attributes and methods

# wh_ListExpr class attributes and methods

# wh_Definition class attributes and methods

# wh_Input class attributes and methods
wh_Input_vars: Property = Property(name="vars", type=StringType)
wh_Input.attributes={wh_Input_vars}

# wh_Commands class attributes and methods

# wh_Output class attributes and methods
wh_Output_vars: Property = Property(name="vars", type=StringType)
wh_Output.attributes={wh_Output_vars}

# wh_ExprEq class attributes and methods

# wh_ExprAnd class attributes and methods

# wh_ExprOr class attributes and methods

# wh_ExprNot class attributes and methods
wh_ExprNot_not: Property = Property(name="not", type=StringType)
wh_ExprNot.attributes={wh_ExprNot_not}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wh_Program", type=wh_Wh, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Wh", type=wh_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands9: BinaryAssociation = BinaryAssociation(
    name="commands9",
    ends={
        Property(name="wh_Command", type=wh_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Commands10", type=wh_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd11: BinaryAssociation = BinaryAssociation(
    name="cmd11",
    ends={
        Property(name="wh_EObject", type=wh_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Command12", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars13: BinaryAssociation = BinaryAssociation(
    name="vars13",
    ends={
        Property(name="wh_Vars", type=wh_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Affect", type=wh_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp14: BinaryAssociation = BinaryAssociation(
    name="exp14",
    ends={
        Property(name="wh_Exprs", type=wh_Affect, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Affect15", type=wh_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs16: BinaryAssociation = BinaryAssociation(
    name="exprs16",
    ends={
        Property(name="wh_Expr", type=wh_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Exprs17", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr18: BinaryAssociation = BinaryAssociation(
    name="expr18",
    ends={
        Property(name="wh_EObject20", type=wh_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Expr19", type=wh_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cons21: BinaryAssociation = BinaryAssociation(
    name="cons21",
    ends={
        Property(name="wh_Cons", type=wh_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprSimple", type=wh_Cons, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list22: BinaryAssociation = BinaryAssociation(
    name="list22",
    ends={
        Property(name="wh_ListExpr", type=wh_Cons, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_Cons23", type=wh_ListExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
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
exprNotX33: BinaryAssociation = BinaryAssociation(
    name="exprNotX33",
    ends={
        Property(name="wh_ExprNot35", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr34", type=wh_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr36: BinaryAssociation = BinaryAssociation(
    name="expr36",
    ends={
        Property(name="wh_ExprEq", type=wh_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprNot37", type=wh_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSimp138: BinaryAssociation = BinaryAssociation(
    name="exprSimp138",
    ends={
        Property(name="wh_ExprSimple40", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq39", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSimp241: BinaryAssociation = BinaryAssociation(
    name="exprSimp241",
    ends={
        Property(name="wh_ExprSimple43", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq42", type=wh_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr44: BinaryAssociation = BinaryAssociation(
    name="expr44",
    ends={
        Property(name="wh_Expr46", type=wh_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprEq45", type=wh_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs24: BinaryAssociation = BinaryAssociation(
    name="exprs24",
    ends={
        Property(name="wh_Expr26", type=wh_ListExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ListExpr25", type=wh_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprOr127: BinaryAssociation = BinaryAssociation(
    name="exprOr127",
    ends={
        Property(name="wh_ExprOr", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd", type=wh_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprOrX28: BinaryAssociation = BinaryAssociation(
    name="exprOrX28",
    ends={
        Property(name="wh_ExprOr30", type=wh_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprAnd29", type=wh_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprNot131: BinaryAssociation = BinaryAssociation(
    name="exprNot131",
    ends={
        Property(name="wh_ExprNot", type=wh_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="wh_ExprOr32", type=wh_ExprNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="wh",
    types={wh_Wh, wh_Program, wh_Command, wh_EObject, wh_Nop, wh_Affect, wh_Vars, wh_Exprs, wh_Expr, wh_ExprSimple, wh_Cons, wh_ListExpr, wh_Definition, wh_Input, wh_Commands, wh_Output, wh_ExprEq, wh_ExprAnd, wh_ExprOr, wh_ExprNot},
    associations={elements0, commands9, cmd11, vars13, exp14, exprs16, expr18, cons21, list22, definition1, input3, command5, output7, exprNotX33, expr36, exprSimp138, exprSimp241, expr44, exprs24, exprOr127, exprOrX28, exprNot131},
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
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
langage_while_Model = Class(name="langage::while::Model")
langage_while_Program = Class(name="langage::while::Program")
langage_while_Function = Class(name="langage::while::Function")
langage_while_SYMB = Class(name="langage::while::SYMB")
langage_while_Definition = Class(name="langage::while::Definition")
langage_while_Input = Class(name="langage::while::Input")
langage_while_Commands = Class(name="langage::while::Commands")
langage_while_Output = Class(name="langage::while::Output")
langage_while_Assign = Class(name="langage::while::Assign")
langage_while_While = Class(name="langage::while::While")
langage_while_For = Class(name="langage::while::For")
langage_while_If = Class(name="langage::while::If")
langage_while_Foreach = Class(name="langage::while::Foreach")
langage_while_Ifconfort = Class(name="langage::while::Ifconfort")
langage_while_Vars = Class(name="langage::while::Vars")
langage_while_Exprs = Class(name="langage::while::Exprs")
langage_while_Expr = Class(name="langage::while::Expr")
langage_while_VAR = Class(name="langage::while::VAR")
langage_while_Command = Class(name="langage::while::Command")
langage_while_ExprSimple = Class(name="langage::while::ExprSimple")
langage_while_ExprAnd = Class(name="langage::while::ExprAnd")
langage_while_LExpr = Class(name="langage::while::LExpr")
langage_while_ExprOr = Class(name="langage::while::ExprOr")
langage_while_ExprNot = Class(name="langage::while::ExprNot")
langage_while_ExprEq = Class(name="langage::while::ExprEq")

# langage_while_Model class attributes and methods

# langage_while_Program class attributes and methods
langage_while_Program_u: Property = Property(name="u", type=StringType)
langage_while_Program.attributes={langage_while_Program_u}

# langage_while_Function class attributes and methods

# langage_while_SYMB class attributes and methods
langage_while_SYMB_bs: Property = Property(name="bs", type=StringType)
langage_while_SYMB_cf: Property = Property(name="cf", type=StringType)
langage_while_SYMB.attributes={langage_while_SYMB_cf, langage_while_SYMB_bs}

# langage_while_Definition class attributes and methods

# langage_while_Input class attributes and methods

# langage_while_Commands class attributes and methods

# langage_while_Output class attributes and methods

# langage_while_Assign class attributes and methods

# langage_while_While class attributes and methods

# langage_while_For class attributes and methods

# langage_while_If class attributes and methods

# langage_while_Foreach class attributes and methods

# langage_while_Ifconfort class attributes and methods

# langage_while_Vars class attributes and methods

# langage_while_Exprs class attributes and methods

# langage_while_Expr class attributes and methods

# langage_while_VAR class attributes and methods
langage_while_VAR_bv: Property = Property(name="bv", type=StringType)
langage_while_VAR_cf: Property = Property(name="cf", type=StringType)
langage_while_VAR.attributes={langage_while_VAR_cf, langage_while_VAR_bv}

# langage_while_Command class attributes and methods
langage_while_Command_nop: Property = Property(name="nop", type=StringType)
langage_while_Command.attributes={langage_while_Command_nop}

# langage_while_ExprSimple class attributes and methods
langage_while_ExprSimple_nil: Property = Property(name="nil", type=StringType)
langage_while_ExprSimple_mot: Property = Property(name="mot", type=StringType)
langage_while_ExprSimple.attributes={langage_while_ExprSimple_nil, langage_while_ExprSimple_mot}

# langage_while_ExprAnd class attributes and methods

# langage_while_LExpr class attributes and methods

# langage_while_ExprOr class attributes and methods

# langage_while_ExprNot class attributes and methods

# langage_while_ExprEq class attributes and methods

# Relationships
nn0: BinaryAssociation = BinaryAssociation(
    name="nn0",
    ends={
        Property(name="langage_while_Program", type=langage_while_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Model", type=langage_while_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
f1: BinaryAssociation = BinaryAssociation(
    name="f1",
    ends={
        Property(name="langage_while_Function", type=langage_while_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Program2", type=langage_while_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pp4: BinaryAssociation = BinaryAssociation(
    name="pp4",
    ends={
        Property(name="langage_while_Program5", type=langage_while_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Program3", type=langage_while_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name6: BinaryAssociation = BinaryAssociation(
    name="name6",
    ends={
        Property(name="langage_while_SYMB", type=langage_while_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Function7", type=langage_while_SYMB, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def8: BinaryAssociation = BinaryAssociation(
    name="def8",
    ends={
        Property(name="langage_while_Definition", type=langage_while_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Function9", type=langage_while_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in10: BinaryAssociation = BinaryAssociation(
    name="in10",
    ends={
        Property(name="langage_while_Input", type=langage_while_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Definition11", type=langage_while_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com12: BinaryAssociation = BinaryAssociation(
    name="com12",
    ends={
        Property(name="langage_while_Commands", type=langage_while_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Definition13", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out14: BinaryAssociation = BinaryAssociation(
    name="out14",
    ends={
        Property(name="langage_while_Output", type=langage_while_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Definition15", type=langage_while_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign23: BinaryAssociation = BinaryAssociation(
    name="assign23",
    ends={
        Property(name="langage_while_Assign", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command24", type=langage_while_Assign, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wh25: BinaryAssociation = BinaryAssociation(
    name="wh25",
    ends={
        Property(name="langage_while_While", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command26", type=langage_while_While, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for27: BinaryAssociation = BinaryAssociation(
    name="for27",
    ends={
        Property(name="langage_while_For", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command28", type=langage_while_For, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if29: BinaryAssociation = BinaryAssociation(
    name="if29",
    ends={
        Property(name="langage_while_If", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command30", type=langage_while_If, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fore31: BinaryAssociation = BinaryAssociation(
    name="fore31",
    ends={
        Property(name="langage_while_Foreach", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command32", type=langage_while_Foreach, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifc33: BinaryAssociation = BinaryAssociation(
    name="ifc33",
    ends={
        Property(name="langage_while_Ifconfort", type=langage_while_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Command34", type=langage_while_Ifconfort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vs35: BinaryAssociation = BinaryAssociation(
    name="vs35",
    ends={
        Property(name="langage_while_Vars", type=langage_while_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Assign36", type=langage_while_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex37: BinaryAssociation = BinaryAssociation(
    name="ex37",
    ends={
        Property(name="langage_while_Exprs", type=langage_while_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Assign38", type=langage_while_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex39: BinaryAssociation = BinaryAssociation(
    name="ex39",
    ends={
        Property(name="langage_while_Expr", type=langage_while_While, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_While40", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c41: BinaryAssociation = BinaryAssociation(
    name="c41",
    ends={
        Property(name="langage_while_Commands43", type=langage_while_While, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_While42", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex44: BinaryAssociation = BinaryAssociation(
    name="ex44",
    ends={
        Property(name="langage_while_Expr46", type=langage_while_For, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_For45", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c47: BinaryAssociation = BinaryAssociation(
    name="c47",
    ends={
        Property(name="langage_while_Commands49", type=langage_while_For, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_For48", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex50: BinaryAssociation = BinaryAssociation(
    name="ex50",
    ends={
        Property(name="langage_while_Expr52", type=langage_while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_If51", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v16: BinaryAssociation = BinaryAssociation(
    name="v16",
    ends={
        Property(name="langage_while_VAR", type=langage_while_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Input17", type=langage_while_VAR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ex68: BinaryAssociation = BinaryAssociation(
    name="ex68",
    ends={
        Property(name="langage_while_Expr70", type=langage_while_Ifconfort, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Ifconfort69", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v18: BinaryAssociation = BinaryAssociation(
    name="v18",
    ends={
        Property(name="langage_while_VAR20", type=langage_while_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Output19", type=langage_while_VAR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c71: BinaryAssociation = BinaryAssociation(
    name="c71",
    ends={
        Property(name="langage_while_Commands73", type=langage_while_Ifconfort, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Ifconfort72", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c21: BinaryAssociation = BinaryAssociation(
    name="c21",
    ends={
        Property(name="langage_while_Command", type=langage_while_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Commands22", type=langage_while_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vs74: BinaryAssociation = BinaryAssociation(
    name="vs74",
    ends={
        Property(name="langage_while_VAR76", type=langage_while_Vars, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Vars75", type=langage_while_VAR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ex77: BinaryAssociation = BinaryAssociation(
    name="ex77",
    ends={
        Property(name="langage_while_Expr79", type=langage_while_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Exprs78", type=langage_while_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exs80: BinaryAssociation = BinaryAssociation(
    name="exs80",
    ends={
        Property(name="langage_while_ExprSimple", type=langage_while_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Expr81", type=langage_while_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exa82: BinaryAssociation = BinaryAssociation(
    name="exa82",
    ends={
        Property(name="langage_while_ExprAnd", type=langage_while_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Expr83", type=langage_while_ExprAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v84: BinaryAssociation = BinaryAssociation(
    name="v84",
    ends={
        Property(name="langage_while_VAR86", type=langage_while_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprSimple85", type=langage_while_VAR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sym87: BinaryAssociation = BinaryAssociation(
    name="sym87",
    ends={
        Property(name="langage_while_SYMB89", type=langage_while_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprSimple88", type=langage_while_SYMB, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lex90: BinaryAssociation = BinaryAssociation(
    name="lex90",
    ends={
        Property(name="langage_while_LExpr", type=langage_while_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprSimple91", type=langage_while_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex92: BinaryAssociation = BinaryAssociation(
    name="ex92",
    ends={
        Property(name="langage_while_Expr94", type=langage_while_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprSimple93", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e95: BinaryAssociation = BinaryAssociation(
    name="e95",
    ends={
        Property(name="langage_while_Expr97", type=langage_while_LExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_LExpr96", type=langage_while_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exo198: BinaryAssociation = BinaryAssociation(
    name="exo198",
    ends={
        Property(name="langage_while_ExprOr", type=langage_while_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprAnd99", type=langage_while_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exo2100: BinaryAssociation = BinaryAssociation(
    name="exo2100",
    ends={
        Property(name="langage_while_ExprOr102", type=langage_while_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprAnd101", type=langage_while_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ct53: BinaryAssociation = BinaryAssociation(
    name="ct53",
    ends={
        Property(name="langage_while_Commands55", type=langage_while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_If54", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ce56: BinaryAssociation = BinaryAssociation(
    name="ce56",
    ends={
        Property(name="langage_while_Commands58", type=langage_while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_If57", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exn1103: BinaryAssociation = BinaryAssociation(
    name="exn1103",
    ends={
        Property(name="langage_while_ExprNot", type=langage_while_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprOr104", type=langage_while_ExprNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex159: BinaryAssociation = BinaryAssociation(
    name="ex159",
    ends={
        Property(name="langage_while_Expr61", type=langage_while_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Foreach60", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex262: BinaryAssociation = BinaryAssociation(
    name="ex262",
    ends={
        Property(name="langage_while_Expr64", type=langage_while_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Foreach63", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c65: BinaryAssociation = BinaryAssociation(
    name="c65",
    ends={
        Property(name="langage_while_Commands67", type=langage_while_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_Foreach66", type=langage_while_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exS1113: BinaryAssociation = BinaryAssociation(
    name="exS1113",
    ends={
        Property(name="langage_while_ExprEq114", type=langage_while_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="langage_while_ExprSimple115", type=langage_while_ExprEq, multiplicity=Multiplicity(1, 1))
    }
)
exS2116: BinaryAssociation = BinaryAssociation(
    name="exS2116",
    ends={
        Property(name="langage_while_ExprSimple118", type=langage_while_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprEq117", type=langage_while_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex119: BinaryAssociation = BinaryAssociation(
    name="ex119",
    ends={
        Property(name="langage_while_Expr121", type=langage_while_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprEq120", type=langage_while_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exn2105: BinaryAssociation = BinaryAssociation(
    name="exn2105",
    ends={
        Property(name="langage_while_ExprNot107", type=langage_while_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprOr106", type=langage_while_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exQ1108: BinaryAssociation = BinaryAssociation(
    name="exQ1108",
    ends={
        Property(name="langage_while_ExprEq", type=langage_while_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprNot109", type=langage_while_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exQ2110: BinaryAssociation = BinaryAssociation(
    name="exQ2110",
    ends={
        Property(name="langage_while_ExprEq112", type=langage_while_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="langage_while_ExprNot111", type=langage_while_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="langage_while",
    types={langage_while_Model, langage_while_Program, langage_while_Function, langage_while_SYMB, langage_while_Definition, langage_while_Input, langage_while_Commands, langage_while_Output, langage_while_Assign, langage_while_While, langage_while_For, langage_while_If, langage_while_Foreach, langage_while_Ifconfort, langage_while_Vars, langage_while_Exprs, langage_while_Expr, langage_while_VAR, langage_while_Command, langage_while_ExprSimple, langage_while_ExprAnd, langage_while_LExpr, langage_while_ExprOr, langage_while_ExprNot, langage_while_ExprEq},
    associations={nn0, f1, pp4, name6, def8, in10, com12, out14, assign23, wh25, for27, if29, fore31, ifc33, vs35, ex37, ex39, c41, ex44, c47, ex50, v16, ex68, v18, c71, c21, vs74, ex77, exs80, exa82, v84, sym87, lex90, ex92, e95, exo198, exo2100, ct53, ce56, exn1103, ex159, ex262, c65, exS1113, exS2116, ex119, exn2105, exQ1108, exQ2110},
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
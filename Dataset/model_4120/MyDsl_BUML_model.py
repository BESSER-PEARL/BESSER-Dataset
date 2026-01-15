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
myDsl_Model = Class(name="myDsl::Model")
myDsl_Function = Class(name="myDsl::Function")
myDsl_Definiton = Class(name="myDsl::Definiton")
myDsl_Command = Class(name="myDsl::Command")
myDsl_Vars = Class(name="myDsl::Vars")
myDsl_Exprs = Class(name="myDsl::Exprs")
myDsl_Expr = Class(name="myDsl::Expr")
myDsl_Input = Class(name="myDsl::Input")
myDsl_Commands = Class(name="myDsl::Commands")
myDsl_Output = Class(name="myDsl::Output")
myDsl_Eq = Class(name="myDsl::Eq")
myDsl_EObject = Class(name="myDsl::EObject")
myDsl_Lexpr = Class(name="myDsl::Lexpr")
myDsl_ExprSimple = Class(name="myDsl::ExprSimple")
myDsl_And = Class(name="myDsl::And")
myDsl_ExprTerm = Class(name="myDsl::ExprTerm")
myDsl_Or = Class(name="myDsl::Or")
myDsl_Not = Class(name="myDsl::Not")

# myDsl_Model class attributes and methods

# myDsl_Function class attributes and methods
myDsl_Function_funName: Property = Property(name="funName", type=StringType)
myDsl_Function.attributes={myDsl_Function_funName}

# myDsl_Definiton class attributes and methods

# myDsl_Command class attributes and methods
myDsl_Command_nom: Property = Property(name="nom", type=StringType)
myDsl_Command.attributes={myDsl_Command_nom}

# myDsl_Vars class attributes and methods
myDsl_Vars_v1: Property = Property(name="v1", type=StringType)
myDsl_Vars_v2: Property = Property(name="v2", type=StringType)
myDsl_Vars.attributes={myDsl_Vars_v2, myDsl_Vars_v1}

# myDsl_Exprs class attributes and methods

# myDsl_Expr class attributes and methods

# myDsl_Input class attributes and methods
myDsl_Input_v: Property = Property(name="v", type=StringType)
myDsl_Input_v2: Property = Property(name="v2", type=StringType)
myDsl_Input.attributes={myDsl_Input_v2, myDsl_Input_v}

# myDsl_Commands class attributes and methods

# myDsl_Output class attributes and methods
myDsl_Output_v: Property = Property(name="v", type=StringType)
myDsl_Output_v2: Property = Property(name="v2", type=StringType)
myDsl_Output.attributes={myDsl_Output_v, myDsl_Output_v2}

# myDsl_Eq class attributes and methods

# myDsl_EObject class attributes and methods

# myDsl_Lexpr class attributes and methods

# myDsl_ExprSimple class attributes and methods
myDsl_ExprSimple_mot: Property = Property(name="mot", type=StringType)
myDsl_ExprSimple.attributes={myDsl_ExprSimple_mot}

# myDsl_And class attributes and methods

# myDsl_ExprTerm class attributes and methods
myDsl_ExprTerm_termVar: Property = Property(name="termVar", type=StringType)
myDsl_ExprTerm_termSym: Property = Property(name="termSym", type=StringType)
myDsl_ExprTerm.attributes={myDsl_ExprTerm_termVar, myDsl_ExprTerm_termSym}

# myDsl_Or class attributes and methods

# myDsl_Not class attributes and methods
myDsl_Not_non: Property = Property(name="non", type=StringType)
myDsl_Not.attributes={myDsl_Not_non}

# Relationships
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="myDsl_Function", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c9: BinaryAssociation = BinaryAssociation(
    name="c9",
    ends={
        Property(name="myDsl_Command", type=myDsl_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commands10", type=myDsl_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp11: BinaryAssociation = BinaryAssociation(
    name="exp11",
    ends={
        Property(name="myDsl_Expr", type=myDsl_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Exprs", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expL12: BinaryAssociation = BinaryAssociation(
    name="expL12",
    ends={
        Property(name="myDsl_Expr14", type=myDsl_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Exprs13", type=myDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varL15: BinaryAssociation = BinaryAssociation(
    name="varL15",
    ends={
        Property(name="myDsl_Vars", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command16", type=myDsl_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expL17: BinaryAssociation = BinaryAssociation(
    name="expL17",
    ends={
        Property(name="myDsl_Exprs19", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command18", type=myDsl_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp20: BinaryAssociation = BinaryAssociation(
    name="exp20",
    ends={
        Property(name="myDsl_Expr22", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command21", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c123: BinaryAssociation = BinaryAssociation(
    name="c123",
    ends={
        Property(name="myDsl_Commands25", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command24", type=myDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp126: BinaryAssociation = BinaryAssociation(
    name="exp126",
    ends={
        Property(name="myDsl_Expr28", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command27", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp229: BinaryAssociation = BinaryAssociation(
    name="exp229",
    ends={
        Property(name="myDsl_Expr31", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command30", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c232: BinaryAssociation = BinaryAssociation(
    name="c232",
    ends={
        Property(name="myDsl_Commands34", type=myDsl_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Command33", type=myDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def1: BinaryAssociation = BinaryAssociation(
    name="def1",
    ends={
        Property(name="myDsl_Definiton", type=myDsl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Function2", type=myDsl_Definiton, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputVars3: BinaryAssociation = BinaryAssociation(
    name="inputVars3",
    ends={
        Property(name="myDsl_Input", type=myDsl_Definiton, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Definiton4", type=myDsl_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandList5: BinaryAssociation = BinaryAssociation(
    name="commandList5",
    ends={
        Property(name="myDsl_Commands", type=myDsl_Definiton, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Definiton6", type=myDsl_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputVars7: BinaryAssociation = BinaryAssociation(
    name="outputVars7",
    ends={
        Property(name="myDsl_Output", type=myDsl_Definiton, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Definiton8", type=myDsl_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expNon248: BinaryAssociation = BinaryAssociation(
    name="expNon248",
    ends={
        Property(name="myDsl_Not50", type=myDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Or49", type=myDsl_Not, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expEq51: BinaryAssociation = BinaryAssociation(
    name="expEq51",
    ends={
        Property(name="myDsl_Eq", type=myDsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Not52", type=myDsl_Eq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprEq153: BinaryAssociation = BinaryAssociation(
    name="exprEq153",
    ends={
        Property(name="myDsl_EObject", type=myDsl_Eq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Eq54", type=myDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprEq255: BinaryAssociation = BinaryAssociation(
    name="exprEq255",
    ends={
        Property(name="myDsl_EObject57", type=myDsl_Eq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Eq56", type=myDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp58: BinaryAssociation = BinaryAssociation(
    name="exp58",
    ends={
        Property(name="myDsl_EObject60", type=myDsl_Eq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Eq59", type=myDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr61: BinaryAssociation = BinaryAssociation(
    name="lexpr61",
    ends={
        Property(name="myDsl_Lexpr", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple62", type=myDsl_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr63: BinaryAssociation = BinaryAssociation(
    name="expr63",
    ends={
        Property(name="myDsl_Expr65", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple64", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp66: BinaryAssociation = BinaryAssociation(
    name="exp66",
    ends={
        Property(name="myDsl_Expr68", type=myDsl_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Lexpr67", type=myDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprSimple35: BinaryAssociation = BinaryAssociation(
    name="exprSimple35",
    ends={
        Property(name="myDsl_ExprSimple", type=myDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expr36", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expEt37: BinaryAssociation = BinaryAssociation(
    name="expEt37",
    ends={
        Property(name="myDsl_And", type=myDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expr38", type=myDsl_And, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expTerminale39: BinaryAssociation = BinaryAssociation(
    name="expTerminale39",
    ends={
        Property(name="myDsl_ExprTerm", type=myDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expr40", type=myDsl_ExprTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expOu41: BinaryAssociation = BinaryAssociation(
    name="expOu41",
    ends={
        Property(name="myDsl_Or", type=myDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_And42", type=myDsl_Or, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expOu243: BinaryAssociation = BinaryAssociation(
    name="expOu243",
    ends={
        Property(name="myDsl_Or45", type=myDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_And44", type=myDsl_Or, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expNon46: BinaryAssociation = BinaryAssociation(
    name="expNon46",
    ends={
        Property(name="myDsl_Not", type=myDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Or47", type=myDsl_Not, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Function, myDsl_Definiton, myDsl_Command, myDsl_Vars, myDsl_Exprs, myDsl_Expr, myDsl_Input, myDsl_Commands, myDsl_Output, myDsl_Eq, myDsl_EObject, myDsl_Lexpr, myDsl_ExprSimple, myDsl_And, myDsl_ExprTerm, myDsl_Or, myDsl_Not},
    associations={model0, c9, exp11, expL12, varL15, expL17, exp20, c123, exp126, exp229, c232, def1, inputVars3, commandList5, outputVars7, expNon248, expEq51, exprEq153, exprEq255, exp58, lexpr61, expr63, exp66, exprSimple35, expEt37, expTerminale39, expOu41, expOu243, expNon46},
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
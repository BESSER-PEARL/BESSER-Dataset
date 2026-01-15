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
miniOCL_RootCS = Class(name="miniOCL::RootCS")
miniOCL_ClassCS = Class(name="miniOCL::ClassCS")
miniOCL_PathNameCS = Class(name="miniOCL::PathNameCS")
miniOCL_PropertyCS = Class(name="miniOCL::PropertyCS")
miniOCL_OperationCS = Class(name="miniOCL::OperationCS")
miniOCL_ParameterCS = Class(name="miniOCL::ParameterCS")
miniOCL_ExpCS = Class(name="miniOCL::ExpCS")
miniOCL_PackageCS = Class(name="miniOCL::PackageCS")
miniOCL_ConstraintCS = Class(name="miniOCL::ConstraintCS")
miniOCL_InvariantCS = Class(name="miniOCL::InvariantCS")
miniOCL_LogicExpCS = Class(name="miniOCL::LogicExpCS")
ExpCS = Class(name="ExpCS")
miniOCL_CallExpCS = Class(name="miniOCL::CallExpCS")
LogicExpCS = Class(name="LogicExpCS")
miniOCL_NameExpCS = Class(name="miniOCL::NameExpCS")
miniOCL_PrimaryExpCS = Class(name="miniOCL::PrimaryExpCS")
CallExpCS = Class(name="CallExpCS")
PrimaryExpCS = Class(name="PrimaryExpCS")
miniOCL_RoundedBracketClauseCS = Class(name="miniOCL::RoundedBracketClauseCS")
miniOCL_StringLiteralExpCS = Class(name="miniOCL::StringLiteralExpCS")
miniOCL_BooleanLiteralExpCS = Class(name="miniOCL::BooleanLiteralExpCS")
miniOCL_PathElementCS = Class(name="miniOCL::PathElementCS")
miniOCL_BooleanExpCS = Class(name="miniOCL::BooleanExpCS")
BooleanLiteralExpCS = Class(name="BooleanLiteralExpCS")
miniOCL_LiteralExpCS = Class(name="miniOCL::LiteralExpCS")
miniOCL_IntLiteralExpCS = Class(name="miniOCL::IntLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")

# miniOCL_RootCS class attributes and methods

# miniOCL_ClassCS class attributes and methods
miniOCL_ClassCS_name: Property = Property(name="name", type=StringType)
miniOCL_ClassCS.attributes={miniOCL_ClassCS_name}

# miniOCL_PathNameCS class attributes and methods

# miniOCL_PropertyCS class attributes and methods
miniOCL_PropertyCS_name: Property = Property(name="name", type=StringType)
miniOCL_PropertyCS.attributes={miniOCL_PropertyCS_name}

# miniOCL_OperationCS class attributes and methods
miniOCL_OperationCS_name: Property = Property(name="name", type=StringType)
miniOCL_OperationCS.attributes={miniOCL_OperationCS_name}

# miniOCL_ParameterCS class attributes and methods
miniOCL_ParameterCS_name: Property = Property(name="name", type=StringType)
miniOCL_ParameterCS.attributes={miniOCL_ParameterCS_name}

# miniOCL_ExpCS class attributes and methods

# miniOCL_PackageCS class attributes and methods
miniOCL_PackageCS_name: Property = Property(name="name", type=StringType)
miniOCL_PackageCS.attributes={miniOCL_PackageCS_name}

# miniOCL_ConstraintCS class attributes and methods

# miniOCL_InvariantCS class attributes and methods

# miniOCL_LogicExpCS class attributes and methods
miniOCL_LogicExpCS_op: Property = Property(name="op", type=StringType)
miniOCL_LogicExpCS.attributes={miniOCL_LogicExpCS_op}

# ExpCS class attributes and methods

# miniOCL_CallExpCS class attributes and methods

# LogicExpCS class attributes and methods

# miniOCL_NameExpCS class attributes and methods

# miniOCL_PrimaryExpCS class attributes and methods

# CallExpCS class attributes and methods

# PrimaryExpCS class attributes and methods

# miniOCL_RoundedBracketClauseCS class attributes and methods

# miniOCL_StringLiteralExpCS class attributes and methods
miniOCL_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
miniOCL_StringLiteralExpCS.attributes={miniOCL_StringLiteralExpCS_stringSymbol}

# miniOCL_BooleanLiteralExpCS class attributes and methods

# miniOCL_PathElementCS class attributes and methods
miniOCL_PathElementCS_pathName: Property = Property(name="pathName", type=StringType)
miniOCL_PathElementCS.attributes={miniOCL_PathElementCS_pathName}

# miniOCL_BooleanExpCS class attributes and methods
miniOCL_BooleanExpCS_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
miniOCL_BooleanExpCS.attributes={miniOCL_BooleanExpCS_boolSymbol}

# BooleanLiteralExpCS class attributes and methods

# miniOCL_LiteralExpCS class attributes and methods

# miniOCL_IntLiteralExpCS class attributes and methods
miniOCL_IntLiteralExpCS_intSymbol: Property = Property(name="intSymbol", type=IntegerType)
miniOCL_IntLiteralExpCS.attributes={miniOCL_IntLiteralExpCS_intSymbol}

# LiteralExpCS class attributes and methods

# Relationships
contraints1: BinaryAssociation = BinaryAssociation(
    name="contraints1",
    ends={
        Property(name="miniOCL_RootCS2", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="miniOCL_ConstraintCS", type=miniOCL_RootCS, multiplicity=Multiplicity(1, 1))
    }
)
packages4: BinaryAssociation = BinaryAssociation(
    name="packages4",
    ends={
        Property(name="miniOCL_PackageCS5", type=miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PackageCS3", type=miniOCL_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes6: BinaryAssociation = BinaryAssociation(
    name="classes6",
    ends={
        Property(name="miniOCL_ClassCS", type=miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PackageCS7", type=miniOCL_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends8: BinaryAssociation = BinaryAssociation(
    name="extends8",
    ends={
        Property(name="miniOCL_PathNameCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS9", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="miniOCL_PropertyCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS11", type=miniOCL_PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations12: BinaryAssociation = BinaryAssociation(
    name="operations12",
    ends={
        Property(name="miniOCL_OperationCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS13", type=miniOCL_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef14: BinaryAssociation = BinaryAssociation(
    name="typeRef14",
    ends={
        Property(name="miniOCL_PathNameCS16", type=miniOCL_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PropertyCS15", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params17: BinaryAssociation = BinaryAssociation(
    name="params17",
    ends={
        Property(name="miniOCL_ParameterCS", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS18", type=miniOCL_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultRef19: BinaryAssociation = BinaryAssociation(
    name="resultRef19",
    ends={
        Property(name="miniOCL_PathNameCS21", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS20", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body22: BinaryAssociation = BinaryAssociation(
    name="body22",
    ends={
        Property(name="miniOCL_ExpCS", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS23", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef24: BinaryAssociation = BinaryAssociation(
    name="typeRef24",
    ends={
        Property(name="miniOCL_PathNameCS26", type=miniOCL_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ParameterCS25", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="miniOCL_PackageCS", type=miniOCL_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_RootCS", type=miniOCL_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef27: BinaryAssociation = BinaryAssociation(
    name="typeRef27",
    ends={
        Property(name="miniOCL_PathNameCS29", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ConstraintCS28", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants30: BinaryAssociation = BinaryAssociation(
    name="invariants30",
    ends={
        Property(name="miniOCL_InvariantCS", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ConstraintCS31", type=miniOCL_InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp32: BinaryAssociation = BinaryAssociation(
    name="exp32",
    ends={
        Property(name="miniOCL_ExpCS34", type=miniOCL_InvariantCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_InvariantCS33", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="miniOCL_LogicExpCS", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LogicExpCS35", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="miniOCL_CallExpCS", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LogicExpCS38", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="miniOCL_CallExpCS41", type=miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_CallExpCS39", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameExp42: BinaryAssociation = BinaryAssociation(
    name="nameExp42",
    ends={
        Property(name="miniOCL_NameExpCS", type=miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_CallExpCS43", type=miniOCL_NameExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName44: BinaryAssociation = BinaryAssociation(
    name="expName44",
    ends={
        Property(name="miniOCL_PathNameCS46", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS45", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets47: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets47",
    ends={
        Property(name="miniOCL_RoundedBracketClauseCS", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS48", type=miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callExp49: BinaryAssociation = BinaryAssociation(
    name="callExp49",
    ends={
        Property(name="miniOCL_CallExpCS51", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS50", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args52: BinaryAssociation = BinaryAssociation(
    name="args52",
    ends={
        Property(name="miniOCL_ExpCS54", type=miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_RoundedBracketClauseCS53", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path55: BinaryAssociation = BinaryAssociation(
    name="path55",
    ends={
        Property(name="miniOCL_PathElementCS", type=miniOCL_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PathNameCS56", type=miniOCL_PathElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_miniOCL_LogicExpCS_ExpCS = Generalization(general=ExpCS, specific=miniOCL_LogicExpCS)
gen_miniOCL_CallExpCS_LogicExpCS = Generalization(general=LogicExpCS, specific=miniOCL_CallExpCS)
gen_miniOCL_PrimaryExpCS_CallExpCS = Generalization(general=CallExpCS, specific=miniOCL_PrimaryExpCS)
gen_miniOCL_NameExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=miniOCL_NameExpCS)
gen_miniOCL_StringLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_StringLiteralExpCS)
gen_miniOCL_BooleanLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_BooleanLiteralExpCS)
gen_miniOCL_BooleanExpCS_BooleanLiteralExpCS = Generalization(general=BooleanLiteralExpCS, specific=miniOCL_BooleanExpCS)
gen_miniOCL_LiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=miniOCL_LiteralExpCS)
gen_miniOCL_IntLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_IntLiteralExpCS)

# Domain Model
domain_model = DomainModel(
    name="miniOCL",
    types={miniOCL_RootCS, miniOCL_ClassCS, miniOCL_PathNameCS, miniOCL_PropertyCS, miniOCL_OperationCS, miniOCL_ParameterCS, miniOCL_ExpCS, miniOCL_PackageCS, miniOCL_ConstraintCS, miniOCL_InvariantCS, miniOCL_LogicExpCS, ExpCS, miniOCL_CallExpCS, LogicExpCS, miniOCL_NameExpCS, miniOCL_PrimaryExpCS, CallExpCS, PrimaryExpCS, miniOCL_RoundedBracketClauseCS, miniOCL_StringLiteralExpCS, miniOCL_BooleanLiteralExpCS, miniOCL_PathElementCS, miniOCL_BooleanExpCS, BooleanLiteralExpCS, miniOCL_LiteralExpCS, miniOCL_IntLiteralExpCS, LiteralExpCS},
    associations={contraints1, packages4, classes6, extends8, properties10, operations12, typeRef14, params17, resultRef19, body22, typeRef24, packages0, typeRef27, invariants30, exp32, left36, right37, source40, nameExp42, expName44, roundedBrackets47, callExp49, args52, path55},
    generalizations={gen_miniOCL_LogicExpCS_ExpCS, gen_miniOCL_CallExpCS_LogicExpCS, gen_miniOCL_PrimaryExpCS_CallExpCS, gen_miniOCL_NameExpCS_PrimaryExpCS, gen_miniOCL_StringLiteralExpCS_LiteralExpCS, gen_miniOCL_BooleanLiteralExpCS_LiteralExpCS, gen_miniOCL_BooleanExpCS_BooleanLiteralExpCS, gen_miniOCL_LiteralExpCS_PrimaryExpCS, gen_miniOCL_IntLiteralExpCS_LiteralExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
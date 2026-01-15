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
boolExpEnv_Fals = Class(name="boolExpEnv::Fals")
boolExpEnv_Not = Class(name="boolExpEnv::Not")
boolExpEnv_Exp = Class(name="boolExpEnv::Exp", is_abstract=True)
boolExpEnv_BinExp = Class(name="boolExpEnv::BinExp", is_abstract=True)
Exp = Class(name="Exp")
boolExpEnv_Lit = Class(name="boolExpEnv::Lit", is_abstract=True)
boolExpEnv_Tru = Class(name="boolExpEnv::Tru")
Lit = Class(name="Lit")
boolExpEnv_And = Class(name="boolExpEnv::And")
BinExp = Class(name="BinExp")
boolExpEnv_Or = Class(name="boolExpEnv::Or")
boolExpEnv_VarRef = Class(name="boolExpEnv::VarRef")

# boolExpEnv_Fals class attributes and methods

# boolExpEnv_Not class attributes and methods

# boolExpEnv_Exp class attributes and methods

# boolExpEnv_BinExp class attributes and methods

# Exp class attributes and methods

# boolExpEnv_Lit class attributes and methods

# boolExpEnv_Tru class attributes and methods

# Lit class attributes and methods

# boolExpEnv_And class attributes and methods

# BinExp class attributes and methods

# boolExpEnv_Or class attributes and methods

# boolExpEnv_VarRef class attributes and methods
boolExpEnv_VarRef_name: Property = Property(name="name", type=StringType)
boolExpEnv_VarRef.attributes={boolExpEnv_VarRef_name}

# Relationships
lhs0: BinaryAssociation = BinaryAssociation(
    name="lhs0",
    ends={
        Property(name="boolExpEnv_Exp", type=boolExpEnv_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolExpEnv_BinExp", type=boolExpEnv_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs1: BinaryAssociation = BinaryAssociation(
    name="rhs1",
    ends={
        Property(name="boolExpEnv_Exp3", type=boolExpEnv_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolExpEnv_BinExp2", type=boolExpEnv_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp4: BinaryAssociation = BinaryAssociation(
    name="exp4",
    ends={
        Property(name="boolExpEnv_Exp5", type=boolExpEnv_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="boolExpEnv_Not", type=boolExpEnv_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_boolExpEnv_Fals_Lit = Generalization(general=Lit, specific=boolExpEnv_Fals)
gen_boolExpEnv_Not_Exp = Generalization(general=Exp, specific=boolExpEnv_Not)
gen_boolExpEnv_BinExp_Exp = Generalization(general=Exp, specific=boolExpEnv_BinExp)
gen_boolExpEnv_Lit_Exp = Generalization(general=Exp, specific=boolExpEnv_Lit)
gen_boolExpEnv_Tru_Lit = Generalization(general=Lit, specific=boolExpEnv_Tru)
gen_boolExpEnv_And_BinExp = Generalization(general=BinExp, specific=boolExpEnv_And)
gen_boolExpEnv_Or_BinExp = Generalization(general=BinExp, specific=boolExpEnv_Or)
gen_boolExpEnv_VarRef_Exp = Generalization(general=Exp, specific=boolExpEnv_VarRef)

# Domain Model
domain_model = DomainModel(
    name="boolExpEnv",
    types={boolExpEnv_Fals, boolExpEnv_Not, boolExpEnv_Exp, boolExpEnv_BinExp, Exp, boolExpEnv_Lit, boolExpEnv_Tru, Lit, boolExpEnv_And, BinExp, boolExpEnv_Or, boolExpEnv_VarRef},
    associations={lhs0, rhs1, exp4},
    generalizations={gen_boolExpEnv_Fals_Lit, gen_boolExpEnv_Not_Exp, gen_boolExpEnv_BinExp_Exp, gen_boolExpEnv_Lit_Exp, gen_boolExpEnv_Tru_Lit, gen_boolExpEnv_And_BinExp, gen_boolExpEnv_Or_BinExp, gen_boolExpEnv_VarRef_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
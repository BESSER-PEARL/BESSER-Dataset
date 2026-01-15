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
boolexp_Lit = Class(name="boolexp::Lit", is_abstract=True)
boolexp_Tru = Class(name="boolexp::Tru")
Lit = Class(name="Lit")
boolexp_Fals = Class(name="boolexp::Fals")
boolexp_Not = Class(name="boolexp::Not")
boolexp_And = Class(name="boolexp::And")
BinExp = Class(name="BinExp")
boolexp_Or = Class(name="boolexp::Or")
boolexp_Exp = Class(name="boolexp::Exp", is_abstract=True)
boolexp_BinExp = Class(name="boolexp::BinExp", is_abstract=True)
Exp = Class(name="Exp")

# boolexp_Lit class attributes and methods

# boolexp_Tru class attributes and methods

# Lit class attributes and methods

# boolexp_Fals class attributes and methods

# boolexp_Not class attributes and methods

# boolexp_And class attributes and methods

# BinExp class attributes and methods

# boolexp_Or class attributes and methods

# boolexp_Exp class attributes and methods

# boolexp_BinExp class attributes and methods

# Exp class attributes and methods

# Relationships
lhs0: BinaryAssociation = BinaryAssociation(
    name="lhs0",
    ends={
        Property(name="boolexp_Exp", type=boolexp_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolexp_BinExp", type=boolexp_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs1: BinaryAssociation = BinaryAssociation(
    name="rhs1",
    ends={
        Property(name="boolexp_Exp3", type=boolexp_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolexp_BinExp2", type=boolexp_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp4: BinaryAssociation = BinaryAssociation(
    name="exp4",
    ends={
        Property(name="boolexp_Exp5", type=boolexp_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="boolexp_Not", type=boolexp_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_boolexp_Lit_Exp = Generalization(general=Exp, specific=boolexp_Lit)
gen_boolexp_Tru_Lit = Generalization(general=Lit, specific=boolexp_Tru)
gen_boolexp_Fals_Lit = Generalization(general=Lit, specific=boolexp_Fals)
gen_boolexp_Not_Exp = Generalization(general=Exp, specific=boolexp_Not)
gen_boolexp_And_BinExp = Generalization(general=BinExp, specific=boolexp_And)
gen_boolexp_Or_BinExp = Generalization(general=BinExp, specific=boolexp_Or)
gen_boolexp_BinExp_Exp = Generalization(general=Exp, specific=boolexp_BinExp)

# Domain Model
domain_model = DomainModel(
    name="boolexp",
    types={boolexp_Lit, boolexp_Tru, Lit, boolexp_Fals, boolexp_Not, boolexp_And, BinExp, boolexp_Or, boolexp_Exp, boolexp_BinExp, Exp},
    associations={lhs0, rhs1, exp4},
    generalizations={gen_boolexp_Lit_Exp, gen_boolexp_Tru_Lit, gen_boolexp_Fals_Lit, gen_boolexp_Not_Exp, gen_boolexp_And_BinExp, gen_boolexp_Or_BinExp, gen_boolexp_BinExp_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
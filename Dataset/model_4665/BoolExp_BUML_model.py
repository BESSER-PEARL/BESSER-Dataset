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
boolexp_Exp = Class(name="boolexp::Exp", is_abstract=True)
boolexp_BinaryExp = Class(name="boolexp::BinaryExp", is_abstract=True)
Exp = Class(name="Exp")
boolexp_Lit = Class(name="boolexp::Lit", is_abstract=True)
boolexp_And = Class(name="boolexp::And")
BinaryExp = Class(name="BinaryExp")
boolexp_Or = Class(name="boolexp::Or")
boolexp_Tru = Class(name="boolexp::Tru")
Lit = Class(name="Lit")
boolexp_Fals = Class(name="boolexp::Fals")

# boolexp_Exp class attributes and methods

# boolexp_BinaryExp class attributes and methods

# Exp class attributes and methods

# boolexp_Lit class attributes and methods

# boolexp_And class attributes and methods

# BinaryExp class attributes and methods

# boolexp_Or class attributes and methods

# boolexp_Tru class attributes and methods

# Lit class attributes and methods

# boolexp_Fals class attributes and methods

# Relationships
lhs0: BinaryAssociation = BinaryAssociation(
    name="lhs0",
    ends={
        Property(name="boolexp_Exp", type=boolexp_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolexp_BinaryExp", type=boolexp_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs1: BinaryAssociation = BinaryAssociation(
    name="rhs1",
    ends={
        Property(name="boolexp_Exp3", type=boolexp_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="boolexp_BinaryExp2", type=boolexp_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_boolexp_BinaryExp_Exp = Generalization(general=Exp, specific=boolexp_BinaryExp)
gen_boolexp_Lit_Exp = Generalization(general=Exp, specific=boolexp_Lit)
gen_boolexp_And_BinaryExp = Generalization(general=BinaryExp, specific=boolexp_And)
gen_boolexp_Or_BinaryExp = Generalization(general=BinaryExp, specific=boolexp_Or)
gen_boolexp_Tru_Lit = Generalization(general=Lit, specific=boolexp_Tru)
gen_boolexp_Fals_Lit = Generalization(general=Lit, specific=boolexp_Fals)

# Domain Model
domain_model = DomainModel(
    name="boolexp",
    types={boolexp_Exp, boolexp_BinaryExp, Exp, boolexp_Lit, boolexp_And, BinaryExp, boolexp_Or, boolexp_Tru, Lit, boolexp_Fals},
    associations={lhs0, rhs1},
    generalizations={gen_boolexp_BinaryExp_Exp, gen_boolexp_Lit_Exp, gen_boolexp_And_BinaryExp, gen_boolexp_Or_BinaryExp, gen_boolexp_Tru_Lit, gen_boolexp_Fals_Lit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
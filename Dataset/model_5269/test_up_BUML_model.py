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
testup_AUp = Class(name="testup::AUp")
testup_B = Class(name="testup::B")
testup_D = Class(name="testup::D")
testup_E = Class(name="testup::E")
AUp = Class(name="AUp")
testup_F = Class(name="testup::F")
E = Class(name="E")
G = Class(name="G")
testup_G = Class(name="testup::G")

# testup_AUp class attributes and methods

# testup_B class attributes and methods
testup_B_newAttribute: Property = Property(name="newAttribute", type=StringType)
testup_B.attributes={testup_B_newAttribute}

# testup_D class attributes and methods
testup_D_newAttribute: Property = Property(name="newAttribute", type=StringType)
testup_D.attributes={testup_D_newAttribute}

# testup_E class attributes and methods
testup_E_newAttribute: Property = Property(name="newAttribute", type=StringType)
testup_E.attributes={testup_E_newAttribute}

# AUp class attributes and methods

# testup_F class attributes and methods

# E class attributes and methods

# G class attributes and methods

# testup_G class attributes and methods

# Relationships
aup0: BinaryAssociation = BinaryAssociation(
    name="aup0",
    ends={
        Property(name="testup_AUp", type=testup_B, multiplicity=Multiplicity(1, 1)),
        Property(name="testup_B", type=testup_AUp, multiplicity=Multiplicity(0, 1))
    }
)
aup1: BinaryAssociation = BinaryAssociation(
    name="aup1",
    ends={
        Property(name="testup_AUp2", type=testup_D, multiplicity=Multiplicity(1, 1)),
        Property(name="testup_D", type=testup_AUp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_testup_E_AUp = Generalization(general=AUp, specific=testup_E)
gen_testup_F_E = Generalization(general=E, specific=testup_F)
gen_testup_F_G = Generalization(general=G, specific=testup_F)

# Domain Model
domain_model = DomainModel(
    name="testup",
    types={testup_AUp, testup_B, testup_D, testup_E, AUp, testup_F, E, G, testup_G},
    associations={aup0, aup1},
    generalizations={gen_testup_E_AUp, gen_testup_F_E, gen_testup_F_G},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
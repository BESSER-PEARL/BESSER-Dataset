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
testmerge_A3 = Class(name="testmerge::A3")
SuperA3 = Class(name="SuperA3")
testmerge_B3 = Class(name="testmerge::B3")
testmerge_SuperA3 = Class(name="testmerge::SuperA3")

# testmerge_A3 class attributes and methods

# SuperA3 class attributes and methods

# testmerge_B3 class attributes and methods
testmerge_B3_m_getA: Method = Method(name="getA", parameters={Parameter(name='paramB')}, type=StringType)
testmerge_B3.methods={testmerge_B3_m_getA}

# testmerge_SuperA3 class attributes and methods

# Relationships
toB30: BinaryAssociation = BinaryAssociation(
    name="toB30",
    ends={
        Property(name="B3", type=testmerge_A3, multiplicity=Multiplicity(1, 1)),
        Property(name="toA3", type=testmerge_B3, multiplicity=Multiplicity(0, 1))
    }
)
toA31: BinaryAssociation = BinaryAssociation(
    name="toA31",
    ends={
        Property(name="A3", type=testmerge_B3, multiplicity=Multiplicity(1, 1)),
        Property(name="toB3", type=testmerge_A3, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testmerge_A3_SuperA3 = Generalization(general=SuperA3, specific=testmerge_A3)

# Domain Model
domain_model = DomainModel(
    name="testmerge",
    types={testmerge_A3, SuperA3, testmerge_B3, testmerge_SuperA3},
    associations={toB30, toA31},
    generalizations={gen_testmerge_A3_SuperA3},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
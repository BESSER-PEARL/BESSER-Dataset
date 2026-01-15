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
Named = Class(name="Named")
tests_TypeB = Class(name="tests::TypeB")
tests_TypeA = Class(name="tests::TypeA")
tests_Root = Class(name="tests::Root")
tests_Named = Class(name="tests::Named", is_abstract=True)

# Named class attributes and methods

# tests_TypeB class attributes and methods

# tests_TypeA class attributes and methods

# tests_Root class attributes and methods

# tests_Named class attributes and methods
tests_Named_name: Property = Property(name="name", type=StringType)
tests_Named.attributes={tests_Named_name}

# Relationships
someAs0: BinaryAssociation = BinaryAssociation(
    name="someAs0",
    ends={
        Property(name="tests_TypeB", type=tests_TypeA, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TypeA", type=tests_TypeB, multiplicity=Multiplicity(0, 9999))
    }
)
allAs4: BinaryAssociation = BinaryAssociation(
    name="allAs4",
    ends={
        Property(name="tests_TypeA5", type=tests_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_Root", type=tests_TypeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allBs6: BinaryAssociation = BinaryAssociation(
    name="allBs6",
    ends={
        Property(name="tests_TypeB8", type=tests_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_Root7", type=tests_TypeB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
someAs1: BinaryAssociation = BinaryAssociation(
    name="someAs1",
    ends={
        Property(name="tests_TypeA3", type=tests_TypeB, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TypeB2", type=tests_TypeA, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tests_TypeA_Named = Generalization(general=Named, specific=tests_TypeA)
gen_tests_TypeB_Named = Generalization(general=Named, specific=tests_TypeB)
gen_tests_Root_Named = Generalization(general=Named, specific=tests_Root)

# Domain Model
domain_model = DomainModel(
    name="tests",
    types={Named, tests_TypeB, tests_TypeA, tests_Root, tests_Named},
    associations={someAs0, allAs4, allBs6, someAs1},
    generalizations={gen_tests_TypeA_Named, gen_tests_TypeB_Named, gen_tests_Root_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
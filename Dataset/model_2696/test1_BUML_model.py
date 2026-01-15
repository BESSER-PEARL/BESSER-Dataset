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
test1_ConceptA = Class(name="test1::ConceptA")
test1_ConceptC = Class(name="test1::ConceptC")
test1_ConceptB = Class(name="test1::ConceptB")
ConceptA = Class(name="ConceptA")

# test1_ConceptA class attributes and methods

# test1_ConceptC class attributes and methods
test1_ConceptC_cool: Property = Property(name="cool", type=BooleanType)
test1_ConceptC_nbr: Property = Property(name="nbr", type=IntegerType)
test1_ConceptC.attributes={test1_ConceptC_nbr, test1_ConceptC_cool}

# test1_ConceptB class attributes and methods

# ConceptA class attributes and methods

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="test1_ConceptC", type=test1_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="test1_ConceptA", type=test1_ConceptC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test1_ConceptB_ConceptA = Generalization(general=ConceptA, specific=test1_ConceptB)

# Domain Model
domain_model = DomainModel(
    name="test1",
    types={test1_ConceptA, test1_ConceptC, test1_ConceptB, ConceptA},
    associations={cs0},
    generalizations={gen_test1_ConceptB_ConceptA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
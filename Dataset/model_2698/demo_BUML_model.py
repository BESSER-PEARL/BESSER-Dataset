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
democea_ConceptC = Class(name="democea::ConceptC")
democea_ConceptA = Class(name="democea::ConceptA")
democea_ConceptB = Class(name="democea::ConceptB")
ConceptA = Class(name="ConceptA")

# democea_ConceptC class attributes and methods
democea_ConceptC_value: Property = Property(name="value", type=IntegerType)
democea_ConceptC.attributes={democea_ConceptC_value}

# democea_ConceptA class attributes and methods

# democea_ConceptB class attributes and methods

# ConceptA class attributes and methods

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="democea_ConceptC", type=democea_ConceptB, multiplicity=Multiplicity(1, 1)),
        Property(name="democea_ConceptB", type=democea_ConceptC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="democea_ConceptB3", type=democea_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="democea_ConceptC2", type=democea_ConceptB, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_democea_ConceptB_ConceptA = Generalization(general=ConceptA, specific=democea_ConceptB)

# Domain Model
domain_model = DomainModel(
    name="democea",
    types={democea_ConceptC, democea_ConceptA, democea_ConceptB, ConceptA},
    associations={cs0, b1},
    generalizations={gen_democea_ConceptB_ConceptA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
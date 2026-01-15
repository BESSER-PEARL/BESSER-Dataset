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
test1_StringToIntegerMapEntry = Class(name="test1::StringToIntegerMapEntry")

# test1_ConceptA class attributes and methods

# test1_StringToIntegerMapEntry class attributes and methods
test1_StringToIntegerMapEntry_key: Property = Property(name="key", type=StringType)
test1_StringToIntegerMapEntry_value: Property = Property(name="value", type=StringType)
test1_StringToIntegerMapEntry.attributes={test1_StringToIntegerMapEntry_key, test1_StringToIntegerMapEntry_value}

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="test1_StringToIntegerMapEntry", type=test1_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="test1_ConceptA", type=test1_StringToIntegerMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test1",
    types={test1_ConceptA, test1_StringToIntegerMapEntry},
    associations={cs0},
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
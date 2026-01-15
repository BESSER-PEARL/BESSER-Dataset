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
b_Model = Class(name="b::Model")
b_B = Class(name="b::B")
b_Y = Class(name="b::Y")

# b_Model class attributes and methods

# b_B class attributes and methods
b_B_id: Property = Property(name="id", type=StringType)
b_B.attributes={b_B_id}

# b_Y class attributes and methods
b_Y_label: Property = Property(name="label", type=StringType)
b_Y_info: Property = Property(name="info", type=StringType)
b_Y.attributes={b_Y_label, b_Y_info}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="b_B", type=b_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Model", type=b_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y1: BinaryAssociation = BinaryAssociation(
    name="y1",
    ends={
        Property(name="b_Y", type=b_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Model2", type=b_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_Model, b_B, b_Y},
    associations={b0, y1},
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
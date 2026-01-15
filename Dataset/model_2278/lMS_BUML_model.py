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
lMS_LMS = Class(name="lMS::LMS")
lMS_Course = Class(name="lMS::Course")

# lMS_LMS class attributes and methods
lMS_LMS_description: Property = Property(name="description", type=StringType)
lMS_LMS.attributes={lMS_LMS_description}

# lMS_Course class attributes and methods
lMS_Course_name: Property = Property(name="name", type=StringType)
lMS_Course.attributes={lMS_Course_name}

# Relationships
course0: BinaryAssociation = BinaryAssociation(
    name="course0",
    ends={
        Property(name="lMS_Course", type=lMS_LMS, multiplicity=Multiplicity(1, 1)),
        Property(name="lMS_LMS", type=lMS_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="lMS",
    types={lMS_LMS, lMS_Course},
    associations={course0},
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
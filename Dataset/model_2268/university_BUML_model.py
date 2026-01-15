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
university_CourseCatalog = Class(name="university::CourseCatalog")
university_Course = Class(name="university::Course")

# university_CourseCatalog class attributes and methods

# university_Course class attributes and methods
university_Course_id: Property = Property(name="id", type=StringType)
university_Course_name: Property = Property(name="name", type=StringType)
university_Course_etcs: Property = Property(name="etcs", type=IntegerType)
university_Course.attributes={university_Course_name, university_Course_etcs, university_Course_id}

# Relationships
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="university_Course", type=university_CourseCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="university_CourseCatalog", type=university_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_CourseCatalog, university_Course},
    associations={courses0},
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
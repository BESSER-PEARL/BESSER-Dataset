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
university_Staff = Class(name="university::Staff")
university_Professor = Class(name="university::Professor")
university_Assistant = Class(name="university::Assistant")
Person = Class(name="Person")
university_Person = Class(name="university::Person", is_abstract=True)
university_Address = Class(name="university::Address")

# university_CourseCatalog class attributes and methods

# university_Course class attributes and methods
university_Course_id: Property = Property(name="id", type=StringType)
university_Course_name: Property = Property(name="name", type=StringType)
university_Course_etcs: Property = Property(name="etcs", type=IntegerType)
university_Course.attributes={university_Course_etcs, university_Course_id, university_Course_name}

# university_Staff class attributes and methods
university_Staff_staff: Property = Property(name="staff", type=StringType)
university_Staff.attributes={university_Staff_staff}

# university_Professor class attributes and methods

# university_Assistant class attributes and methods

# Person class attributes and methods

# university_Person class attributes and methods
university_Person_name: Property = Property(name="name", type=StringType)
university_Person.attributes={university_Person_name}

# university_Address class attributes and methods

# Relationships
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="university_Course", type=university_CourseCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="university_CourseCatalog", type=university_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
professors1: BinaryAssociation = BinaryAssociation(
    name="professors1",
    ends={
        Property(name="university_Professor", type=university_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Staff", type=university_Professor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assistants2: BinaryAssociation = BinaryAssociation(
    name="assistants2",
    ends={
        Property(name="university_Assistant", type=university_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Staff3", type=university_Assistant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addresses4: BinaryAssociation = BinaryAssociation(
    name="addresses4",
    ends={
        Property(name="university_Address", type=university_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Person", type=university_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_university_Professor_Person = Generalization(general=Person, specific=university_Professor)
gen_university_Assistant_Person = Generalization(general=Person, specific=university_Assistant)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_CourseCatalog, university_Course, university_Staff, university_Professor, university_Assistant, Person, university_Person, university_Address},
    associations={courses0, professors1, assistants2, addresses4},
    generalizations={gen_university_Professor_Person, gen_university_Assistant_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
school_School = Class(name="school::School")
school_Pupil = Class(name="school::Pupil")
school_Book = Class(name="school::Book")
school_SpecialBook = Class(name="school::SpecialBook")
Book = Class(name="Book")

# school_School class attributes and methods

# school_Pupil class attributes and methods
school_Pupil_name: Property = Property(name="name", type=StringType)
school_Pupil.attributes={school_Pupil_name}

# school_Book class attributes and methods

# school_SpecialBook class attributes and methods

# Book class attributes and methods

# Relationships
pupils0: BinaryAssociation = BinaryAssociation(
    name="pupils0",
    ends={
        Property(name="school_Pupil", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School", type=school_Pupil, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readBooks1: BinaryAssociation = BinaryAssociation(
    name="readBooks1",
    ends={
        Property(name="school_Book", type=school_Pupil, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Pupil2", type=school_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_school_SpecialBook_Book = Generalization(general=Book, specific=school_SpecialBook)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_School, school_Pupil, school_Book, school_SpecialBook, Book},
    associations={pupils0, readBooks1},
    generalizations={gen_school_SpecialBook_Book},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
test_Library = Class(name="test::Library")
test_Writer = Class(name="test::Writer")
test_Book = Class(name="test::Book")

# test_Library class attributes and methods
test_Library_name: Property = Property(name="name", type=StringType)
test_Library.attributes={test_Library_name}

# test_Writer class attributes and methods
test_Writer_firstName: Property = Property(name="firstName", type=StringType)
test_Writer_BirthDate: Property = Property(name="BirthDate", type=DateType)
test_Writer_Pseudonym: Property = Property(name="Pseudonym", type=BooleanType)
test_Writer_lastName: Property = Property(name="lastName", type=StringType)
test_Writer_EMail: Property = Property(name="EMail", type=StringType)
test_Writer_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
test_Writer.attributes={test_Writer_Pseudonym, test_Writer_lastName, test_Writer_BirthDate, test_Writer_firstName, test_Writer_EMail}
test_Writer.methods={test_Writer_m_validate}

# test_Book class attributes and methods
test_Book_title: Property = Property(name="title", type=StringType)
test_Book_pages: Property = Property(name="pages", type=IntegerType)
test_Book.attributes={test_Book_title, test_Book_pages}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="Writer", type=test_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=test_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="test_Book", type=test_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Library", type=test_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="Book", type=test_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=test_Book, multiplicity=Multiplicity(0, 9999))
    }
)
library3: BinaryAssociation = BinaryAssociation(
    name="library3",
    ends={
        Property(name="Library", type=test_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers4", type=test_Library, multiplicity=Multiplicity(0, 1))
    }
)
writers5: BinaryAssociation = BinaryAssociation(
    name="writers5",
    ends={
        Property(name="Writer6", type=test_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=test_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Library, test_Writer, test_Book},
    associations={writers0, books1, books2, library3, writers5},
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
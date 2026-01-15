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

# Enumerations
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="Biography"),
			EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ScienceFiction")
    }
)

# Classes
library_Library = Class(name="library::Library")
library_Book = Class(name="library::Book")
Writer = Class(name="Writer")
library_people_Writer = Class(name="library::people::Writer")
people_library_Book = Class(name="people::library::Book")
people_library_Car = Class(name="people::library::Car")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_m_reserve: Method = Method(name="reserve", parameters={Parameter(name='books')})
library_Library.attributes={library_Library_name}
library_Library.methods={library_Library_m_reserve}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_title, library_Book_pages, library_Book_category}

# Writer class attributes and methods

# library_people_Writer class attributes and methods
library_people_Writer_name: Property = Property(name="name", type=StringType)
library_people_Writer.attributes={library_people_Writer_name}

# people_library_Book class attributes and methods

# people_library_Car class attributes and methods

# Relationships
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="Writer2", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="people", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Writer", type=Writer, multiplicity=Multiplicity(0, 1))
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="Book", type=library_people_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=people_library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
car6: BinaryAssociation = BinaryAssociation(
    name="car6",
    ends={
        Property(name="people_library_Car", type=library_people_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_people_Writer", type=people_library_Car, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Book, Writer, library_people_Writer, people_library_Book, people_library_Car, BookCategory},
    associations={writers1, author0, books3, books5, car6},
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
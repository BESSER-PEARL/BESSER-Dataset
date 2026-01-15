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
            EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biography"),
			EnumerationLiteral(name="IT")
    }
)

# Classes
library_Person = Class(name="library::Person")
library_Book = Class(name="library::Book")
Person = Class(name="Person")
library_Writer = Class(name="library::Writer")
library_Library = Class(name="library::Library")

# library_Person class attributes and methods

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_category, library_Book_pages, library_Book_title}

# Person class attributes and methods

# library_Writer class attributes and methods

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_site: Property = Property(name="site", type=StringType)
library_Library.attributes={library_Library_site, library_Library_name}

# Relationships
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="library_Library3", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
employees4: BinaryAssociation = BinaryAssociation(
    name="employees4",
    ends={
        Property(name="hr.ecorePerson", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library", type=library_Person, multiplicity=Multiplicity(0, 9999))
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Writer_Person = Generalization(general=Person, specific=library_Writer)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Person, library_Book, Person, library_Writer, library_Library, BookCategory},
    associations={books2, employees4, books5, author0, writers1},
    generalizations={gen_library_Writer_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
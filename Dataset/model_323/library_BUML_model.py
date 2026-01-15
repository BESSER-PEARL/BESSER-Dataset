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
            EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biographie"),
			EnumerationLiteral(name="Mistery")
    }
)

# Classes
library_Employee = Class(name="library::Employee")
library_Book = Class(name="library::Book")
library_Library = Class(name="library::Library")
library__cPfS4h9KEeeOINGRvT6ccg = Class(name="library::::cPfS4h9KEeeOINGRvT6ccg")
library__cPfTBB9KEeeOINGRvT6ccg = Class(name="library::::cPfTBB9KEeeOINGRvT6ccg")
library__cPfTDx9KEeeOINGRvT6ccg = Class(name="library::::cPfTDx9KEeeOINGRvT6ccg")
library_Writer = Class(name="library::Writer")

# library_Employee class attributes and methods
library_Employee_name: Property = Property(name="name", type=StringType)
library_Employee_age: Property = Property(name="age", type=IntegerType)
library_Employee.attributes={library_Employee_age, library_Employee_name}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_title, library_Book_category, library_Book_pages}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_address: Property = Property(name="address", type=StringType)
library_Library.attributes={library_Library_address, library_Library_name}

# library__cPfS4h9KEeeOINGRvT6ccg class attributes and methods

# library__cPfTBB9KEeeOINGRvT6ccg class attributes and methods

# library__cPfTDx9KEeeOINGRvT6ccg class attributes and methods

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="library__cPfS4h9KEeeOINGRvT6ccg", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library__cPfS4h9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library__cPfTBB9KEeeOINGRvT6ccg", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library__cPfTBB9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="library__cPfTDx9KEeeOINGRvT6ccg", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library__cPfTDx9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="library__cPfTDx9KEeeOINGRvT6ccg6", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer", type=library__cPfTDx9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999))
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="library__cPfTBB9KEeeOINGRvT6ccg8", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library__cPfTBB9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Employee, library_Book, library_Library, library__cPfS4h9KEeeOINGRvT6ccg, library__cPfTBB9KEeeOINGRvT6ccg, library__cPfTDx9KEeeOINGRvT6ccg, library_Writer, BookCategory},
    associations={employees0, writers1, books3, books5, authors7},
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
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
library__cPfS4h9KEeeOINGRvT6ccg = Class(name="library::::cPfS4h9KEeeOINGRvT6ccg")
library_Employee = Class(name="library::Employee")
library_Library = Class(name="library::Library")
library__cPfTBB9KEeeOINGRvT6ccg = Class(name="library::::cPfTBB9KEeeOINGRvT6ccg")
library__cPfTDx9KEeeOINGRvT6ccg = Class(name="library::::cPfTDx9KEeeOINGRvT6ccg")
library_Writer = Class(name="library::Writer")
library_Book = Class(name="library::Book")

# library__cPfS4h9KEeeOINGRvT6ccg class attributes and methods

# library_Employee class attributes and methods
library_Employee_name: Property = Property(name="name", type=StringType)
library_Employee_age: Property = Property(name="age", type=IntegerType)
library_Employee.attributes={library_Employee_name, library_Employee_age}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_address: Property = Property(name="address", type=StringType)
library_Library_ages: Property = Property(name="ages", type=IntegerType)
library_Library.attributes={library_Library_name, library_Library_ages, library_Library_address}

# library__cPfTBB9KEeeOINGRvT6ccg class attributes and methods

# library__cPfTDx9KEeeOINGRvT6ccg class attributes and methods

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Book class attributes and methods
library_Book_category: Property = Property(name="category", type=StringType)
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book.attributes={library_Book_category, library_Book_pages, library_Book_title}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="library__cPfS4h9KEeeOINGRvT6ccg", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library__cPfS4h9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors10: BinaryAssociation = BinaryAssociation(
    name="authors10",
    ends={
        Property(name="library__cPfTBB9KEeeOINGRvT6ccg11", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library__cPfTBB9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999))
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
moreThan205: BinaryAssociation = BinaryAssociation(
    name="moreThan205",
    ends={
        Property(name="library__cPfS4h9KEeeOINGRvT6ccg7", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library6", type=library__cPfS4h9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books8: BinaryAssociation = BinaryAssociation(
    name="books8",
    ends={
        Property(name="library__cPfTDx9KEeeOINGRvT6ccg9", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer", type=library__cPfTDx9KEeeOINGRvT6ccg, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library__cPfS4h9KEeeOINGRvT6ccg, library_Employee, library_Library, library__cPfTBB9KEeeOINGRvT6ccg, library__cPfTDx9KEeeOINGRvT6ccg, library_Writer, library_Book, BookCategory},
    associations={employees0, authors10, writers1, books3, moreThan205, books8},
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
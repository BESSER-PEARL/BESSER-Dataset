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
			EnumerationLiteral(name="Biography")
    }
)

# Classes
libraryModel_Library = Class(name="libraryModel::Library")
libraryModel_Writer = Class(name="libraryModel::Writer")
libraryModel_Book = Class(name="libraryModel::Book")

# libraryModel_Library class attributes and methods
libraryModel_Library_name: Property = Property(name="name", type=StringType)
libraryModel_Library.attributes={libraryModel_Library_name}

# libraryModel_Writer class attributes and methods
libraryModel_Writer_name: Property = Property(name="name", type=StringType)
libraryModel_Writer.attributes={libraryModel_Writer_name}

# libraryModel_Book class attributes and methods
libraryModel_Book_title: Property = Property(name="title", type=StringType)
libraryModel_Book_pages: Property = Property(name="pages", type=IntegerType)
libraryModel_Book_category: Property = Property(name="category", type=StringType)
libraryModel_Book.attributes={libraryModel_Book_pages, libraryModel_Book_category, libraryModel_Book_title}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="libraryModel_Writer", type=libraryModel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryModel_Library", type=libraryModel_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="libraryModel_Book", type=libraryModel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryModel_Library2", type=libraryModel_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="Book", type=libraryModel_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=libraryModel_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author4: BinaryAssociation = BinaryAssociation(
    name="author4",
    ends={
        Property(name="Writer", type=libraryModel_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=libraryModel_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="libraryModel",
    types={libraryModel_Library, libraryModel_Writer, libraryModel_Book, BookCategory},
    associations={writers0, books1, books3, author4},
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
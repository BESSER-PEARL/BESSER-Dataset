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
library_Library = Class(name="library::Library")
library_Writer = Class(name="library::Writer")
library_Review = Class(name="library::Review")
library_Book = Class(name="library::Book")
library_Opinion = Class(name="library::Opinion")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Review class attributes and methods
library_Review_title: Property = Property(name="title", type=StringType)
library_Review_positive: Property = Property(name="positive", type=BooleanType)
library_Review.attributes={library_Review_title, library_Review_positive}

# library_Book class attributes and methods
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book_title: Property = Property(name="title", type=StringType)
library_Book.attributes={library_Book_pages, library_Book_category, library_Book_title}

# library_Opinion class attributes and methods
library_Opinion_text: Property = Property(name="text", type=StringType)
library_Opinion_context: Property = Property(name="context", type=StringType)
library_Opinion.attributes={library_Opinion_text, library_Opinion_context}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author5: BinaryAssociation = BinaryAssociation(
    name="author5",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
reviews6: BinaryAssociation = BinaryAssociation(
    name="reviews6",
    ends={
        Property(name="Review", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=library_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="Book8", type=library_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews", type=library_Book, multiplicity=Multiplicity(1, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
opinions4: BinaryAssociation = BinaryAssociation(
    name="opinions4",
    ends={
        Property(name="Opinion", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writer", type=library_Opinion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writer9: BinaryAssociation = BinaryAssociation(
    name="writer9",
    ends={
        Property(name="Writer10", type=library_Opinion, multiplicity=Multiplicity(1, 1)),
        Property(name="opinions", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
book11: BinaryAssociation = BinaryAssociation(
    name="book11",
    ends={
        Property(name="library_Book12", type=library_Opinion, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Opinion", type=library_Book, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Writer, library_Review, library_Book, library_Opinion, BookCategory},
    associations={writers0, author5, reviews6, book7, books1, books3, opinions4, writer9, book11},
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
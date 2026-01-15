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
elements_Book = Class(name="elements::Book")
elements_Writer = Class(name="elements::Writer")
Person = Class(name="Person")
elements_EObject = Class(name="elements::EObject")

# elements_Book class attributes and methods
elements_Book_title: Property = Property(name="title", type=StringType)
elements_Book_pages: Property = Property(name="pages", type=StringType)
elements_Book_category: Property = Property(name="category", type=StringType)
elements_Book_uuid: Property = Property(name="uuid", type=StringType)
elements_Book.attributes={elements_Book_pages, elements_Book_category, elements_Book_title, elements_Book_uuid}

# elements_Writer class attributes and methods

# Person class attributes and methods

# elements_EObject class attributes and methods

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="elements_EObject", type=elements_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="elements_Book", type=elements_EObject, multiplicity=Multiplicity(1, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="elements_EObject2", type=elements_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="elements_Writer", type=elements_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_elements_Writer_Person = Generalization(general=Person, specific=elements_Writer)

# Domain Model
domain_model = DomainModel(
    name="elements",
    types={elements_Book, elements_Writer, Person, elements_EObject, BookCategory},
    associations={author0, books1},
    generalizations={gen_elements_Writer_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
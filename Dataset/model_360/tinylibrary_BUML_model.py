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
			EnumerationLiteral(name="Computing")
    }
)

# Classes
tinylibrary_Library = Class(name="tinylibrary::Library")
tinylibrary_Book = Class(name="tinylibrary::Book")
tinylibrary_Employee = Class(name="tinylibrary::Employee")
tinylibrary_Writer = Class(name="tinylibrary::Writer")
tinylibrary_Person = Class(name="tinylibrary::Person", is_abstract=True)
Person = Class(name="Person")

# tinylibrary_Library class attributes and methods

# tinylibrary_Book class attributes and methods
tinylibrary_Book_isbn: Property = Property(name="isbn", type=StringType)
tinylibrary_Book_title: Property = Property(name="title", type=StringType)
tinylibrary_Book_category: Property = Property(name="category", type=StringType)
tinylibrary_Book_pages: Property = Property(name="pages", type=StringType)
tinylibrary_Book_published: Property = Property(name="published", type=DateType)
tinylibrary_Book_damaged: Property = Property(name="damaged", type=StringType)
tinylibrary_Book.attributes={tinylibrary_Book_damaged, tinylibrary_Book_isbn, tinylibrary_Book_category, tinylibrary_Book_pages, tinylibrary_Book_title, tinylibrary_Book_published}

# tinylibrary_Employee class attributes and methods

# tinylibrary_Writer class attributes and methods

# tinylibrary_Person class attributes and methods
tinylibrary_Person_firstName: Property = Property(name="firstName", type=StringType)
tinylibrary_Person_lastName: Property = Property(name="lastName", type=StringType)
tinylibrary_Person_name: Property = Property(name="name", type=StringType)
tinylibrary_Person.attributes={tinylibrary_Person_name, tinylibrary_Person_firstName, tinylibrary_Person_lastName}

# Person class attributes and methods

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="tinylibrary_Book", type=tinylibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tinylibrary_Library", type=tinylibrary_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="tinylibrary_Employee", type=tinylibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tinylibrary_Library2", type=tinylibrary_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers3: BinaryAssociation = BinaryAssociation(
    name="writers3",
    ends={
        Property(name="tinylibrary_Writer", type=tinylibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tinylibrary_Library4", type=tinylibrary_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="Book", type=tinylibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=tinylibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
manager7: BinaryAssociation = BinaryAssociation(
    name="manager7",
    ends={
        Property(name="Employee", type=tinylibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="managed", type=tinylibrary_Employee, multiplicity=Multiplicity(0, 1))
    }
)
managed9: BinaryAssociation = BinaryAssociation(
    name="managed9",
    ends={
        Property(name="Employee10", type=tinylibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=tinylibrary_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Writer", type=tinylibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=tinylibrary_Writer, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_tinylibrary_Writer_Person = Generalization(general=Person, specific=tinylibrary_Writer)
gen_tinylibrary_Employee_Person = Generalization(general=Person, specific=tinylibrary_Employee)

# Domain Model
domain_model = DomainModel(
    name="tinylibrary",
    types={tinylibrary_Library, tinylibrary_Book, tinylibrary_Employee, tinylibrary_Writer, tinylibrary_Person, Person, BookCategory},
    associations={books0, employees1, writers3, books5, manager7, managed9, authors11},
    generalizations={gen_tinylibrary_Writer_Person, gen_tinylibrary_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
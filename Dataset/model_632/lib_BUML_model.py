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
library_Library = Class(name="library::Library")
library_Person = Class(name="library::Person")
library_Author = Class(name="library::Author")
library_Book = Class(name="library::Book")
library_UoD = Class(name="library::UoD")
AbstractPerson = Class(name="AbstractPerson")
library_AbstractPerson = Class(name="library::AbstractPerson", is_abstract=True)
library_Loan = Class(name="library::Loan")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Person class attributes and methods

# library_Author class attributes and methods

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_isbn: Property = Property(name="isbn", type=StringType)
library_Book.attributes={library_Book_isbn, library_Book_title}

# library_UoD class attributes and methods

# AbstractPerson class attributes and methods

# library_AbstractPerson class attributes and methods
library_AbstractPerson_name: Property = Property(name="name", type=StringType)
library_AbstractPerson_m_getFirstName: Method = Method(name="getFirstName", parameters={}, type=StringType)
library_AbstractPerson_m_getLastName: Method = Method(name="getLastName", parameters={}, type=StringType)
library_AbstractPerson.attributes={library_AbstractPerson_name}
library_AbstractPerson.methods={library_AbstractPerson_m_getLastName, library_AbstractPerson_m_getFirstName}

# library_Loan class attributes and methods

# Relationships
allLibraries0: BinaryAssociation = BinaryAssociation(
    name="allLibraries0",
    ends={
        Property(name="library_Library", type=library_UoD, multiplicity=Multiplicity(1, 1)),
        Property(name="library_UoD", type=library_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allPersons1: BinaryAssociation = BinaryAssociation(
    name="allPersons1",
    ends={
        Property(name="library_Person", type=library_UoD, multiplicity=Multiplicity(1, 1)),
        Property(name="library_UoD2", type=library_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAuthors3: BinaryAssociation = BinaryAssociation(
    name="allAuthors3",
    ends={
        Property(name="library_Author", type=library_UoD, multiplicity=Multiplicity(1, 1)),
        Property(name="library_UoD4", type=library_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author5: BinaryAssociation = BinaryAssociation(
    name="author5",
    ends={
        Property(name="library_Author6", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library_Author, multiplicity=Multiplicity(0, 1))
    }
)
loans10: BinaryAssociation = BinaryAssociation(
    name="loans10",
    ends={
        Property(name="library_Library11", type=library_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="library_Loan", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
borrower12: BinaryAssociation = BinaryAssociation(
    name="borrower12",
    ends={
        Property(name="library_Person14", type=library_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Loan13", type=library_Person, multiplicity=Multiplicity(0, 1))
    }
)
book15: BinaryAssociation = BinaryAssociation(
    name="book15",
    ends={
        Property(name="library_Book17", type=library_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Loan16", type=library_Book, multiplicity=Multiplicity(0, 1))
    }
)
books7: BinaryAssociation = BinaryAssociation(
    name="books7",
    ends={
        Property(name="library_Book9", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library8", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Person_AbstractPerson = Generalization(general=AbstractPerson, specific=library_Person)
gen_library_Author_AbstractPerson = Generalization(general=AbstractPerson, specific=library_Author)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Person, library_Author, library_Book, library_UoD, AbstractPerson, library_AbstractPerson, library_Loan},
    associations={allLibraries0, allPersons1, allAuthors3, author5, loans10, borrower12, book15, books7},
    generalizations={gen_library_Person_AbstractPerson, gen_library_Author_AbstractPerson},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
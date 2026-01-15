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
Addressable = Class(name="Addressable")
library_Writer = Class(name="library::Writer")
library_Employee = Class(name="library::Employee")
library_Borrower = Class(name="library::Borrower")
library_Item = Class(name="library::Item", is_abstract=True)
library_Person = Class(name="library::Person")
Lendable = Class(name="Lendable")
library_Addressable = Class(name="library::Addressable", is_abstract=True)
Person = Class(name="Person")
library_IncBook = Class(name="library::IncBook")
library_Lendable = Class(name="library::Lendable", is_abstract=True)
CirculatingItem = Class(name="CirculatingItem")
library_CirculatingItem = Class(name="library::CirculatingItem", is_abstract=True)
Item = Class(name="Item")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# Addressable class attributes and methods

# library_Writer class attributes and methods

# library_Employee class attributes and methods

# library_Borrower class attributes and methods

# library_Item class attributes and methods
library_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
library_Item.attributes={library_Item_publicationDate}

# library_Person class attributes and methods
library_Person_firstName: Property = Property(name="firstName", type=StringType)
library_Person_lastName: Property = Property(name="lastName", type=StringType)
library_Person.attributes={library_Person_firstName, library_Person_lastName}

# Lendable class attributes and methods

# library_Addressable class attributes and methods
library_Addressable_address: Property = Property(name="address", type=StringType)
library_Addressable.attributes={library_Addressable_address}

# Person class attributes and methods

# library_IncBook class attributes and methods
library_IncBook_title: Property = Property(name="title", type=StringType)
library_IncBook_pages: Property = Property(name="pages", type=IntegerType)
library_IncBook.attributes={library_IncBook_title, library_IncBook_pages}

# library_Lendable class attributes and methods
library_Lendable_copies: Property = Property(name="copies", type=IntegerType)
library_Lendable.attributes={library_Lendable_copies}

# CirculatingItem class attributes and methods

# library_CirculatingItem class attributes and methods

# Item class attributes and methods

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="library_Employee", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers3: BinaryAssociation = BinaryAssociation(
    name="borrowers3",
    ends={
        Property(name="library_Borrower", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_Borrower, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stock5: BinaryAssociation = BinaryAssociation(
    name="stock5",
    ends={
        Property(name="library_Item", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library6", type=library_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers10: BinaryAssociation = BinaryAssociation(
    name="borrowers10",
    ends={
        Property(name="Borrower", type=library_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowing", type=library_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
books7: BinaryAssociation = BinaryAssociation(
    name="books7",
    ends={
        Property(name="IncBook", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=library_IncBook, multiplicity=Multiplicity(0, 9999))
    }
)
borrowing8: BinaryAssociation = BinaryAssociation(
    name="borrowing8",
    ends={
        Property(name="Lendable", type=library_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowers", type=library_Lendable, multiplicity=Multiplicity(0, 9999))
    }
)
authors9: BinaryAssociation = BinaryAssociation(
    name="authors9",
    ends={
        Property(name="Writer", type=library_IncBook, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_library_Library_Addressable = Generalization(general=Addressable, specific=library_Library)
gen_library_Person_Addressable = Generalization(general=Addressable, specific=library_Person)
gen_library_CirculatingItem_Lendable = Generalization(general=Lendable, specific=library_CirculatingItem)
gen_library_Employee_Person = Generalization(general=Person, specific=library_Employee)
gen_library_Writer_Person = Generalization(general=Person, specific=library_Writer)
gen_library_Borrower_Person = Generalization(general=Person, specific=library_Borrower)
gen_library_IncBook_CirculatingItem = Generalization(general=CirculatingItem, specific=library_IncBook)
gen_library_CirculatingItem_Item = Generalization(general=Item, specific=library_CirculatingItem)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, Addressable, library_Writer, library_Employee, library_Borrower, library_Item, library_Person, Lendable, library_Addressable, Person, library_IncBook, library_Lendable, CirculatingItem, library_CirculatingItem, Item},
    associations={writers0, employees1, borrowers3, stock5, borrowers10, books7, borrowing8, authors9},
    generalizations={gen_library_Library_Addressable, gen_library_Person_Addressable, gen_library_CirculatingItem_Lendable, gen_library_Employee_Person, gen_library_Writer_Person, gen_library_Borrower_Person, gen_library_IncBook_CirculatingItem, gen_library_CirculatingItem_Item},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
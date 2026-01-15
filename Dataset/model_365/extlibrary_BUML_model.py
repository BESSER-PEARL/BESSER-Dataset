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
extlibrary_Book = Class(name="extlibrary::Book")
CirculatingItem = Class(name="CirculatingItem")
extlibrary_Writer = Class(name="extlibrary::Writer")
Person = Class(name="Person")
extlibrary_VideoCassette = Class(name="extlibrary::VideoCassette")
Addressable = Class(name="Addressable")
extlibrary_Employee = Class(name="extlibrary::Employee")
extlibrary_Addressable = Class(name="extlibrary::Addressable", is_abstract=True)
extlibrary_Item = Class(name="extlibrary::Item", is_abstract=True)
extlibrary_Lendable = Class(name="extlibrary::Lendable", is_abstract=True)
extlibrary_Borrower = Class(name="extlibrary::Borrower")
extlibrary_CirculatingItem = Class(name="extlibrary::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
extlibrary_Periodical = Class(name="extlibrary::Periodical", is_abstract=True)
extlibrary_AudioVisualItem = Class(name="extlibrary::AudioVisualItem", is_abstract=True)
extlibrary_BookOnTape = Class(name="extlibrary::BookOnTape")
AudioVisualItem = Class(name="AudioVisualItem")
extlibrary_Person = Class(name="extlibrary::Person")

# extlibrary_Book class attributes and methods
extlibrary_Book_title: Property = Property(name="title", type=StringType)
extlibrary_Book_pages: Property = Property(name="pages", type=IntegerType)
extlibrary_Book_category: Property = Property(name="category", type=StringType)
extlibrary_Book.attributes={extlibrary_Book_pages, extlibrary_Book_category, extlibrary_Book_title}

# CirculatingItem class attributes and methods

# extlibrary_Writer class attributes and methods
extlibrary_Writer_name: Property = Property(name="name", type=StringType)
extlibrary_Writer.attributes={extlibrary_Writer_name}

# Person class attributes and methods

# extlibrary_VideoCassette class attributes and methods

# Addressable class attributes and methods

# extlibrary_Employee class attributes and methods

# extlibrary_Addressable class attributes and methods
extlibrary_Addressable_address: Property = Property(name="address", type=StringType)
extlibrary_Addressable.attributes={extlibrary_Addressable_address}

# extlibrary_Item class attributes and methods
extlibrary_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
extlibrary_Item.attributes={extlibrary_Item_publicationDate}

# extlibrary_Lendable class attributes and methods
extlibrary_Lendable_copies: Property = Property(name="copies", type=IntegerType)
extlibrary_Lendable.attributes={extlibrary_Lendable_copies}

# extlibrary_Borrower class attributes and methods

# extlibrary_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# extlibrary_Periodical class attributes and methods
extlibrary_Periodical_title: Property = Property(name="title", type=StringType)
extlibrary_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
extlibrary_Periodical.attributes={extlibrary_Periodical_title, extlibrary_Periodical_issuesPerYear}

# extlibrary_AudioVisualItem class attributes and methods
extlibrary_AudioVisualItem_title: Property = Property(name="title", type=StringType)
extlibrary_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
extlibrary_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
extlibrary_AudioVisualItem.attributes={extlibrary_AudioVisualItem_minutesLength, extlibrary_AudioVisualItem_damaged, extlibrary_AudioVisualItem_title}

# extlibrary_BookOnTape class attributes and methods

# AudioVisualItem class attributes and methods

# extlibrary_Person class attributes and methods
extlibrary_Person_firstName: Property = Property(name="firstName", type=StringType)
extlibrary_Person_lastName: Property = Property(name="lastName", type=StringType)
extlibrary_Person.attributes={extlibrary_Person_lastName, extlibrary_Person_firstName}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=extlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1))
    }
)
author4: BinaryAssociation = BinaryAssociation(
    name="author4",
    ends={
        Property(name="extlibrary_Writer", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape5", type=extlibrary_Writer, multiplicity=Multiplicity(0, 1))
    }
)
cast6: BinaryAssociation = BinaryAssociation(
    name="cast6",
    ends={
        Property(name="extlibrary_Person7", type=extlibrary_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_VideoCassette", type=extlibrary_Person, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed8: BinaryAssociation = BinaryAssociation(
    name="borrowed8",
    ends={
        Property(name="Lendable", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowers", type=extlibrary_Lendable, multiplicity=Multiplicity(0, 9999))
    }
)
manager10: BinaryAssociation = BinaryAssociation(
    name="manager10",
    ends={
        Property(name="extlibrary_Employee", type=extlibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Employee9", type=extlibrary_Employee, multiplicity=Multiplicity(0, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="Book", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=extlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
borrowers2: BinaryAssociation = BinaryAssociation(
    name="borrowers2",
    ends={
        Property(name="Borrower", type=extlibrary_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowed", type=extlibrary_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
reader3: BinaryAssociation = BinaryAssociation(
    name="reader3",
    ends={
        Property(name="extlibrary_Person", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape", type=extlibrary_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extlibrary_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_Book)
gen_extlibrary_Writer_Person = Generalization(general=Person, specific=extlibrary_Writer)
gen_extlibrary_VideoCassette_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_VideoCassette)
gen_extlibrary_Borrower_Person = Generalization(general=Person, specific=extlibrary_Borrower)
gen_extlibrary_Person_Addressable = Generalization(general=Addressable, specific=extlibrary_Person)
gen_extlibrary_Employee_Person = Generalization(general=Person, specific=extlibrary_Employee)
gen_extlibrary_CirculatingItem_Item = Generalization(general=Item, specific=extlibrary_CirculatingItem)
gen_extlibrary_CirculatingItem_Lendable = Generalization(general=Lendable, specific=extlibrary_CirculatingItem)
gen_extlibrary_Periodical_Item = Generalization(general=Item, specific=extlibrary_Periodical)
gen_extlibrary_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_AudioVisualItem)
gen_extlibrary_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_BookOnTape)

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary_Book, CirculatingItem, extlibrary_Writer, Person, extlibrary_VideoCassette, Addressable, extlibrary_Employee, extlibrary_Addressable, extlibrary_Item, extlibrary_Lendable, extlibrary_Borrower, extlibrary_CirculatingItem, Item, Lendable, extlibrary_Periodical, extlibrary_AudioVisualItem, extlibrary_BookOnTape, AudioVisualItem, extlibrary_Person, BookCategory},
    associations={author0, author4, cast6, borrowed8, manager10, books1, borrowers2, reader3},
    generalizations={gen_extlibrary_Book_CirculatingItem, gen_extlibrary_Writer_Person, gen_extlibrary_VideoCassette_AudioVisualItem, gen_extlibrary_Borrower_Person, gen_extlibrary_Person_Addressable, gen_extlibrary_Employee_Person, gen_extlibrary_CirculatingItem_Item, gen_extlibrary_CirculatingItem_Lendable, gen_extlibrary_Periodical_Item, gen_extlibrary_AudioVisualItem_CirculatingItem, gen_extlibrary_BookOnTape_AudioVisualItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
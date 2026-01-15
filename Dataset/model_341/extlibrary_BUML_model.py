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
extlibrary_Employee = Class(name="extlibrary::Employee")
extlibrary_Borrower = Class(name="extlibrary::Borrower")
extlibrary_Item = Class(name="extlibrary::Item", is_abstract=True)
extlibrary_Writer = Class(name="extlibrary::Writer")
extlibrary_Library = Class(name="extlibrary::Library")
Addressable = Class(name="Addressable")
extlibrary_Lendable = Class(name="extlibrary::Lendable", is_abstract=True)
extlibrary_CirculatingItem = Class(name="extlibrary::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
extlibrary_Periodical = Class(name="extlibrary::Periodical", is_abstract=True)
extlibrary_AudioVisualItem = Class(name="extlibrary::AudioVisualItem", is_abstract=True)
Person = Class(name="Person")
extlibrary_Addressable = Class(name="extlibrary::Addressable", is_abstract=True)
extlibrary_BookOnTape = Class(name="extlibrary::BookOnTape")
AudioVisualItem = Class(name="AudioVisualItem")
extlibrary_Person = Class(name="extlibrary::Person")
extlibrary_VideoCassette = Class(name="extlibrary::VideoCassette")

# extlibrary_Book class attributes and methods
extlibrary_Book_title: Property = Property(name="title", type=StringType)
extlibrary_Book_pages: Property = Property(name="pages", type=IntegerType)
extlibrary_Book_category: Property = Property(name="category", type=StringType)
extlibrary_Book.attributes={extlibrary_Book_category, extlibrary_Book_title, extlibrary_Book_pages}

# CirculatingItem class attributes and methods

# extlibrary_Employee class attributes and methods

# extlibrary_Borrower class attributes and methods

# extlibrary_Item class attributes and methods
extlibrary_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
extlibrary_Item.attributes={extlibrary_Item_publicationDate}

# extlibrary_Writer class attributes and methods
extlibrary_Writer_name: Property = Property(name="name", type=StringType)
extlibrary_Writer.attributes={extlibrary_Writer_name}

# extlibrary_Library class attributes and methods
extlibrary_Library_name: Property = Property(name="name", type=StringType)
extlibrary_Library_people: Property = Property(name="people", type=StringType)
extlibrary_Library.attributes={extlibrary_Library_name, extlibrary_Library_people}

# Addressable class attributes and methods

# extlibrary_Lendable class attributes and methods
extlibrary_Lendable_copies: Property = Property(name="copies", type=IntegerType)
extlibrary_Lendable.attributes={extlibrary_Lendable_copies}

# extlibrary_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# extlibrary_Periodical class attributes and methods
extlibrary_Periodical_title: Property = Property(name="title", type=StringType)
extlibrary_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
extlibrary_Periodical.attributes={extlibrary_Periodical_issuesPerYear, extlibrary_Periodical_title}

# extlibrary_AudioVisualItem class attributes and methods
extlibrary_AudioVisualItem_title: Property = Property(name="title", type=StringType)
extlibrary_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
extlibrary_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
extlibrary_AudioVisualItem.attributes={extlibrary_AudioVisualItem_damaged, extlibrary_AudioVisualItem_title, extlibrary_AudioVisualItem_minutesLength}

# Person class attributes and methods

# extlibrary_Addressable class attributes and methods
extlibrary_Addressable_address: Property = Property(name="address", type=StringType)
extlibrary_Addressable.attributes={extlibrary_Addressable_address}

# extlibrary_BookOnTape class attributes and methods

# AudioVisualItem class attributes and methods

# extlibrary_Person class attributes and methods
extlibrary_Person_lastName: Property = Property(name="lastName", type=StringType)
extlibrary_Person_firstName: Property = Property(name="firstName", type=StringType)
extlibrary_Person.attributes={extlibrary_Person_lastName, extlibrary_Person_firstName}

# extlibrary_VideoCassette class attributes and methods

# Relationships
writers2: BinaryAssociation = BinaryAssociation(
    name="writers2",
    ends={
        Property(name="extlibrary_Writer", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library", type=extlibrary_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="extlibrary_Employee", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library4", type=extlibrary_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers5: BinaryAssociation = BinaryAssociation(
    name="borrowers5",
    ends={
        Property(name="extlibrary_Borrower", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library6", type=extlibrary_Borrower, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stock7: BinaryAssociation = BinaryAssociation(
    name="stock7",
    ends={
        Property(name="extlibrary_Item", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library8", type=extlibrary_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books9: BinaryAssociation = BinaryAssociation(
    name="books9",
    ends={
        Property(name="extlibrary_Book", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library10", type=extlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
branches12: BinaryAssociation = BinaryAssociation(
    name="branches12",
    ends={
        Property(name="14", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=extlibrary_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="1", type=extlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1))
    }
)
borrowers22: BinaryAssociation = BinaryAssociation(
    name="borrowers22",
    ends={
        Property(name="24", type=extlibrary_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=extlibrary_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
parentBranch16: BinaryAssociation = BinaryAssociation(
    name="parentBranch16",
    ends={
        Property(name="18", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=extlibrary_Library, multiplicity=Multiplicity(0, 1))
    }
)
books19: BinaryAssociation = BinaryAssociation(
    name="books19",
    ends={
        Property(name="21", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=extlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
manager35: BinaryAssociation = BinaryAssociation(
    name="manager35",
    ends={
        Property(name="extlibrary_Employee36", type=extlibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Employee34", type=extlibrary_Employee, multiplicity=Multiplicity(0, 1))
    }
)
reader25: BinaryAssociation = BinaryAssociation(
    name="reader25",
    ends={
        Property(name="extlibrary_Person", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape", type=extlibrary_Person, multiplicity=Multiplicity(0, 1))
    }
)
author26: BinaryAssociation = BinaryAssociation(
    name="author26",
    ends={
        Property(name="extlibrary_Writer28", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape27", type=extlibrary_Writer, multiplicity=Multiplicity(0, 1))
    }
)
cast29: BinaryAssociation = BinaryAssociation(
    name="cast29",
    ends={
        Property(name="extlibrary_Person30", type=extlibrary_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_VideoCassette", type=extlibrary_Person, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed31: BinaryAssociation = BinaryAssociation(
    name="borrowed31",
    ends={
        Property(name="33", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="32", type=extlibrary_Lendable, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_extlibrary_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_Book)
gen_extlibrary_Library_Addressable = Generalization(general=Addressable, specific=extlibrary_Library)
gen_extlibrary_CirculatingItem_Item = Generalization(general=Item, specific=extlibrary_CirculatingItem)
gen_extlibrary_CirculatingItem_Lendable = Generalization(general=Lendable, specific=extlibrary_CirculatingItem)
gen_extlibrary_Periodical_Item = Generalization(general=Item, specific=extlibrary_Periodical)
gen_extlibrary_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_AudioVisualItem)
gen_extlibrary_Writer_Person = Generalization(general=Person, specific=extlibrary_Writer)
gen_extlibrary_Employee_Person = Generalization(general=Person, specific=extlibrary_Employee)
gen_extlibrary_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_BookOnTape)
gen_extlibrary_VideoCassette_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_VideoCassette)
gen_extlibrary_Borrower_Person = Generalization(general=Person, specific=extlibrary_Borrower)
gen_extlibrary_Person_Addressable = Generalization(general=Addressable, specific=extlibrary_Person)

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary_Book, CirculatingItem, extlibrary_Employee, extlibrary_Borrower, extlibrary_Item, extlibrary_Writer, extlibrary_Library, Addressable, extlibrary_Lendable, extlibrary_CirculatingItem, Item, Lendable, extlibrary_Periodical, extlibrary_AudioVisualItem, Person, extlibrary_Addressable, extlibrary_BookOnTape, AudioVisualItem, extlibrary_Person, extlibrary_VideoCassette, BookCategory},
    associations={writers2, employees3, borrowers5, stock7, books9, branches12, author0, borrowers22, parentBranch16, books19, manager35, reader25, author26, cast29, borrowed31},
    generalizations={gen_extlibrary_Book_CirculatingItem, gen_extlibrary_Library_Addressable, gen_extlibrary_CirculatingItem_Item, gen_extlibrary_CirculatingItem_Lendable, gen_extlibrary_Periodical_Item, gen_extlibrary_AudioVisualItem_CirculatingItem, gen_extlibrary_Writer_Person, gen_extlibrary_Employee_Person, gen_extlibrary_BookOnTape_AudioVisualItem, gen_extlibrary_VideoCassette_AudioVisualItem, gen_extlibrary_Borrower_Person, gen_extlibrary_Person_Addressable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
extlibrary__15CRUW60EeGkd4g88tZXfA = Class(name="extlibrary::::15CRUW60EeGkd4g88tZXfA")
extlibrary_Library = Class(name="extlibrary::Library")
_15OelG60EeGkd4g88tZXfA = Class(name="::15OelG60EeGkd4g88tZXfA")
extlibrary_Book = Class(name="extlibrary::Book")
_15LbQG60EeGkd4g88tZXfA = Class(name="::15LbQG60EeGkd4g88tZXfA")
extlibrary_Writer = Class(name="extlibrary::Writer")
_15N3gm60EeGkd4g88tZXfA = Class(name="::15N3gm60EeGkd4g88tZXfA")
extlibrary_Item = Class(name="extlibrary::Item", is_abstract=True)
extlibrary__15OekG60EeGkd4g88tZXfA = Class(name="extlibrary::::15OekG60EeGkd4g88tZXfA")
extlibrary__15NQcW60EeGkd4g88tZXfA = Class(name="extlibrary::::15NQcW60EeGkd4g88tZXfA")
extlibrary__15Hw4m60EeGkd4g88tZXfA = Class(name="extlibrary::::15Hw4m60EeGkd4g88tZXfA")
extlibrary__146VgG60EeGkd4g88tZXfA = Class(name="extlibrary::::146VgG60EeGkd4g88tZXfA")
extlibrary__148KsW60EeGkd4g88tZXfA = Class(name="extlibrary::::148KsW60EeGkd4g88tZXfA")
extlibrary_VideoCassette = Class(name="extlibrary::VideoCassette")
extlibrary_Borrower = Class(name="extlibrary::Borrower")
extlibrary__15IX8G60EeGkd4g88tZXfA = Class(name="extlibrary::::15IX8G60EeGkd4g88tZXfA")
extlibrary_Person = Class(name="extlibrary::Person")
extlibrary_Lendable = Class(name="extlibrary::Lendable", is_abstract=True)
extlibrary_CirculatingItem = Class(name="extlibrary::CirculatingItem", is_abstract=True)
extlibrary_Periodical = Class(name="extlibrary::Periodical", is_abstract=True)
extlibrary_AudioVisualItem = Class(name="extlibrary::AudioVisualItem", is_abstract=True)
extlibrary_BookOnTape = Class(name="extlibrary::BookOnTape")
extlibrary__15N3gm60EeGkd4g88tZXfA = Class(name="extlibrary::::15N3gm60EeGkd4g88tZXfA")
extlibrary_Employee = Class(name="extlibrary::Employee")
extlibrary_Addressable = Class(name="extlibrary::Addressable", is_abstract=True)

# extlibrary__15CRUW60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Library class attributes and methods
extlibrary_Library_name: Property = Property(name="name", type=StringType)
extlibrary_Library_people: Property = Property(name="people", type=StringType)
extlibrary_Library.attributes={extlibrary_Library_name, extlibrary_Library_people}

# _15OelG60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Book class attributes and methods
extlibrary_Book_title: Property = Property(name="title", type=StringType)
extlibrary_Book_pages: Property = Property(name="pages", type=IntegerType)
extlibrary_Book_category: Property = Property(name="category", type=StringType)
extlibrary_Book.attributes={extlibrary_Book_title, extlibrary_Book_category, extlibrary_Book_pages}

# _15LbQG60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Writer class attributes and methods
extlibrary_Writer_name: Property = Property(name="name", type=StringType)
extlibrary_Writer.attributes={extlibrary_Writer_name}

# _15N3gm60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Item class attributes and methods
extlibrary_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
extlibrary_Item.attributes={extlibrary_Item_publicationDate}

# extlibrary__15OekG60EeGkd4g88tZXfA class attributes and methods

# extlibrary__15NQcW60EeGkd4g88tZXfA class attributes and methods

# extlibrary__15Hw4m60EeGkd4g88tZXfA class attributes and methods

# extlibrary__146VgG60EeGkd4g88tZXfA class attributes and methods

# extlibrary__148KsW60EeGkd4g88tZXfA class attributes and methods

# extlibrary_VideoCassette class attributes and methods

# extlibrary_Borrower class attributes and methods

# extlibrary__15IX8G60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Person class attributes and methods
extlibrary_Person_firstName: Property = Property(name="firstName", type=StringType)
extlibrary_Person_lastName: Property = Property(name="lastName", type=StringType)
extlibrary_Person.attributes={extlibrary_Person_firstName, extlibrary_Person_lastName}

# extlibrary_Lendable class attributes and methods
extlibrary_Lendable_copies: Property = Property(name="copies", type=IntegerType)
extlibrary_Lendable.attributes={extlibrary_Lendable_copies}

# extlibrary_CirculatingItem class attributes and methods

# extlibrary_Periodical class attributes and methods
extlibrary_Periodical_title: Property = Property(name="title", type=StringType)
extlibrary_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
extlibrary_Periodical.attributes={extlibrary_Periodical_title, extlibrary_Periodical_issuesPerYear}

# extlibrary_AudioVisualItem class attributes and methods
extlibrary_AudioVisualItem_title: Property = Property(name="title", type=StringType)
extlibrary_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
extlibrary_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
extlibrary_AudioVisualItem.attributes={extlibrary_AudioVisualItem_damaged, extlibrary_AudioVisualItem_minutesLength, extlibrary_AudioVisualItem_title}

# extlibrary_BookOnTape class attributes and methods

# extlibrary__15N3gm60EeGkd4g88tZXfA class attributes and methods

# extlibrary_Employee class attributes and methods

# extlibrary_Addressable class attributes and methods
extlibrary_Addressable_address: Property = Property(name="address", type=StringType)
extlibrary_Addressable.attributes={extlibrary_Addressable_address}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="extlibrary__15CRUW60EeGkd4g88tZXfA", type=extlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Book", type=extlibrary__15CRUW60EeGkd4g88tZXfA, multiplicity=Multiplicity(1, 1))
    }
)
books16: BinaryAssociation = BinaryAssociation(
    name="books16",
    ends={
        Property(name="extlibrary__146VgG60EeGkd4g88tZXfA17", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Writer", type=extlibrary__146VgG60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="extlibrary__15CRUW60EeGkd4g88tZXfA2", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library", type=extlibrary__15CRUW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="extlibrary__15OekG60EeGkd4g88tZXfA", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library4", type=extlibrary__15OekG60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers5: BinaryAssociation = BinaryAssociation(
    name="borrowers5",
    ends={
        Property(name="extlibrary__15NQcW60EeGkd4g88tZXfA", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library6", type=extlibrary__15NQcW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stock7: BinaryAssociation = BinaryAssociation(
    name="stock7",
    ends={
        Property(name="extlibrary__15Hw4m60EeGkd4g88tZXfA", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library8", type=extlibrary__15Hw4m60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books9: BinaryAssociation = BinaryAssociation(
    name="books9",
    ends={
        Property(name="extlibrary__146VgG60EeGkd4g88tZXfA", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library10", type=extlibrary__146VgG60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999))
    }
)
branches11: BinaryAssociation = BinaryAssociation(
    name="branches11",
    ends={
        Property(name="extlibrary__148KsW60EeGkd4g88tZXfA", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library12", type=extlibrary__148KsW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentBranch13: BinaryAssociation = BinaryAssociation(
    name="parentBranch13",
    ends={
        Property(name="extlibrary__148KsW60EeGkd4g88tZXfA15", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library14", type=extlibrary__148KsW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 1))
    }
)
author21: BinaryAssociation = BinaryAssociation(
    name="author21",
    ends={
        Property(name="extlibrary__15CRUW60EeGkd4g88tZXfA23", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape22", type=extlibrary__15CRUW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 1))
    }
)
cast24: BinaryAssociation = BinaryAssociation(
    name="cast24",
    ends={
        Property(name="extlibrary__15N3gm60EeGkd4g88tZXfA25", type=extlibrary_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_VideoCassette", type=extlibrary__15N3gm60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed26: BinaryAssociation = BinaryAssociation(
    name="borrowed26",
    ends={
        Property(name="extlibrary__15IX8G60EeGkd4g88tZXfA", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Borrower", type=extlibrary__15IX8G60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999))
    }
)
borrowers18: BinaryAssociation = BinaryAssociation(
    name="borrowers18",
    ends={
        Property(name="extlibrary__15NQcW60EeGkd4g88tZXfA19", type=extlibrary_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Lendable", type=extlibrary__15NQcW60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 9999))
    }
)
reader20: BinaryAssociation = BinaryAssociation(
    name="reader20",
    ends={
        Property(name="extlibrary__15N3gm60EeGkd4g88tZXfA", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape", type=extlibrary__15N3gm60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 1))
    }
)
manager27: BinaryAssociation = BinaryAssociation(
    name="manager27",
    ends={
        Property(name="extlibrary__15OekG60EeGkd4g88tZXfA28", type=extlibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Employee", type=extlibrary__15OekG60EeGkd4g88tZXfA, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extlibrary_Library__15OelG60EeGkd4g88tZXfA = Generalization(general=_15OelG60EeGkd4g88tZXfA, specific=extlibrary_Library)
gen_extlibrary_Book__15LbQG60EeGkd4g88tZXfA = Generalization(general=_15LbQG60EeGkd4g88tZXfA, specific=extlibrary_Book)
gen_extlibrary_Writer__15N3gm60EeGkd4g88tZXfA = Generalization(general=_15N3gm60EeGkd4g88tZXfA, specific=extlibrary_Writer)
gen_extlibrary_VideoCassette_extlibrary_AudioVisualItem = Generalization(general=extlibrary_AudioVisualItem, specific=extlibrary_VideoCassette)
gen_extlibrary_Borrower__15N3gm60EeGkd4g88tZXfA = Generalization(general=_15N3gm60EeGkd4g88tZXfA, specific=extlibrary_Borrower)
gen_extlibrary_Person__15OelG60EeGkd4g88tZXfA = Generalization(general=_15OelG60EeGkd4g88tZXfA, specific=extlibrary_Person)
gen_extlibrary_CirculatingItem_extlibrary_Item = Generalization(general=extlibrary_Item, specific=extlibrary_CirculatingItem)
gen_extlibrary_CirculatingItem_extlibrary_Lendable = Generalization(general=extlibrary_Lendable, specific=extlibrary_CirculatingItem)
gen_extlibrary_Periodical_extlibrary_Item = Generalization(general=extlibrary_Item, specific=extlibrary_Periodical)
gen_extlibrary_AudioVisualItem__15LbQG60EeGkd4g88tZXfA = Generalization(general=_15LbQG60EeGkd4g88tZXfA, specific=extlibrary_AudioVisualItem)
gen_extlibrary_BookOnTape_extlibrary_AudioVisualItem = Generalization(general=extlibrary_AudioVisualItem, specific=extlibrary_BookOnTape)
gen_extlibrary_Employee__15N3gm60EeGkd4g88tZXfA = Generalization(general=_15N3gm60EeGkd4g88tZXfA, specific=extlibrary_Employee)

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary__15CRUW60EeGkd4g88tZXfA, extlibrary_Library, _15OelG60EeGkd4g88tZXfA, extlibrary_Book, _15LbQG60EeGkd4g88tZXfA, extlibrary_Writer, _15N3gm60EeGkd4g88tZXfA, extlibrary_Item, extlibrary__15OekG60EeGkd4g88tZXfA, extlibrary__15NQcW60EeGkd4g88tZXfA, extlibrary__15Hw4m60EeGkd4g88tZXfA, extlibrary__146VgG60EeGkd4g88tZXfA, extlibrary__148KsW60EeGkd4g88tZXfA, extlibrary_VideoCassette, extlibrary_Borrower, extlibrary__15IX8G60EeGkd4g88tZXfA, extlibrary_Person, extlibrary_Lendable, extlibrary_CirculatingItem, extlibrary_Periodical, extlibrary_AudioVisualItem, extlibrary_BookOnTape, extlibrary__15N3gm60EeGkd4g88tZXfA, extlibrary_Employee, extlibrary_Addressable, BookCategory},
    associations={author0, books16, writers1, employees3, borrowers5, stock7, books9, branches11, parentBranch13, author21, cast24, borrowed26, borrowers18, reader20, manager27},
    generalizations={gen_extlibrary_Library__15OelG60EeGkd4g88tZXfA, gen_extlibrary_Book__15LbQG60EeGkd4g88tZXfA, gen_extlibrary_Writer__15N3gm60EeGkd4g88tZXfA, gen_extlibrary_VideoCassette_extlibrary_AudioVisualItem, gen_extlibrary_Borrower__15N3gm60EeGkd4g88tZXfA, gen_extlibrary_Person__15OelG60EeGkd4g88tZXfA, gen_extlibrary_CirculatingItem_extlibrary_Item, gen_extlibrary_CirculatingItem_extlibrary_Lendable, gen_extlibrary_Periodical_extlibrary_Item, gen_extlibrary_AudioVisualItem__15LbQG60EeGkd4g88tZXfA, gen_extlibrary_BookOnTape_extlibrary_AudioVisualItem, gen_extlibrary_Employee__15N3gm60EeGkd4g88tZXfA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
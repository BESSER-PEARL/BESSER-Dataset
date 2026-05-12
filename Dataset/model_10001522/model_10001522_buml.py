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
User = Class(name="User")
Data = Class(name="Data")
CSV = Class(name="CSV")
XML = Class(name="XML")
File = Class(name="File")
book = Class(name="book")
librarian = Class(name="librarian")
library_member = Class(name="library_member")
fine = Class(name="fine")
transaction = Class(name="transaction")
library = Class(name="library")
credit_card = Class(name="credit_card")
cash = Class(name="cash")
status_of_book = Class(name="status_of_book")
member_profile = Class(name="member_profile")

# User class attributes and methods
User_user_id: Property = Property(name="user_id", type=User)
User.attributes={User_user_id}

# Data class attributes and methods
Data_key: Property = Property(name="key", type=StringType)
Data_value: Property = Property(name="value", type=StringType)
Data.attributes={Data_value, Data_key}

# CSV class attributes and methods
CSV_cloumn: Property = Property(name="cloumn", type=StringType)
CSV_row: Property = Property(name="row", type=StringType)
CSV.attributes={CSV_cloumn, CSV_row}

# XML class attributes and methods
XML_element: Property = Property(name="element", type=StringType)
XML_attribute: Property = Property(name="attribute", type=StringType)
XML.attributes={XML_attribute, XML_element}

# File class attributes and methods
File_file_type: Property = Property(name="file_type", type=File)
File.attributes={File_file_type}

# book class attributes and methods

# librarian class attributes and methods

# library_member class attributes and methods

# fine class attributes and methods

# transaction class attributes and methods

# library class attributes and methods

# credit_card class attributes and methods

# cash class attributes and methods

# status_of_book class attributes and methods

# member_profile class attributes and methods

# Relationships
User_data: BinaryAssociation = BinaryAssociation(
    name="User_data",
    ends={
        Property(name="User_data_00", type=Data, multiplicity=Multiplicity(0, 9999)),
        Property(name="modify1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
data_File: BinaryAssociation = BinaryAssociation(
    name="data_File",
    ends={
        Property(name="parse2", type=File, multiplicity=Multiplicity(1, 1)),
        Property(name="data_File_13", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
User_Parser: BinaryAssociation = BinaryAssociation(
    name="User_Parser",
    ends={
        Property(name="parser4", type=File, multiplicity=Multiplicity(0, 9999)),
        Property(name="upload5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
member_library_card: BinaryAssociation = BinaryAssociation(
    name="member_library_card",
    ends={
        Property(name="library_card6", type=library_member, multiplicity=Multiplicity(1, 1)),
        Property(name="member7", type=transaction, multiplicity=Multiplicity(1, 1))
    }
)
library_book: BinaryAssociation = BinaryAssociation(
    name="library_book",
    ends={
        Property(name="book8", type=book, multiplicity=Multiplicity(1, 9999)),
        Property(name="library9", type=library, multiplicity=Multiplicity(1, 1))
    }
)
library_librarian: BinaryAssociation = BinaryAssociation(
    name="library_librarian",
    ends={
        Property(name="librarian10", type=librarian, multiplicity=Multiplicity(1, 9999)),
        Property(name="library11", type=library, multiplicity=Multiplicity(1, 1))
    }
)
library_transaction: BinaryAssociation = BinaryAssociation(
    name="library_transaction",
    ends={
        Property(name="transaction12", type=transaction, multiplicity=Multiplicity(1, 9999)),
        Property(name="library13", type=library, multiplicity=Multiplicity(1, 1))
    }
)
transaction_fine: BinaryAssociation = BinaryAssociation(
    name="transaction_fine",
    ends={
        Property(name="fine14", type=fine, multiplicity=Multiplicity(0, 1)),
        Property(name="transaction15", type=transaction, multiplicity=Multiplicity(1, 1))
    }
)
librarian_transaction: BinaryAssociation = BinaryAssociation(
    name="librarian_transaction",
    ends={
        Property(name="transaction16", type=transaction, multiplicity=Multiplicity(1, 9999)),
        Property(name="librarian17", type=librarian, multiplicity=Multiplicity(1, 9999))
    }
)
fine_credit_card: BinaryAssociation = BinaryAssociation(
    name="fine_credit_card",
    ends={
        Property(name="credit_card18", type=credit_card, multiplicity=Multiplicity(0, 1)),
        Property(name="fine19", type=fine, multiplicity=Multiplicity(1, 1))
    }
)
fine_class: BinaryAssociation = BinaryAssociation(
    name="fine_class",
    ends={
        Property(name="class20", type=cash, multiplicity=Multiplicity(0, 1)),
        Property(name="fine21", type=fine, multiplicity=Multiplicity(1, 1))
    }
)
transaction_book: BinaryAssociation = BinaryAssociation(
    name="transaction_book",
    ends={
        Property(name="book22", type=book, multiplicity=Multiplicity(1, 1)),
        Property(name="transaction23", type=transaction, multiplicity=Multiplicity(1, 1))
    }
)
book_status_of_book: BinaryAssociation = BinaryAssociation(
    name="book_status_of_book",
    ends={
        Property(name="status_of_book24", type=status_of_book, multiplicity=Multiplicity(1, 1)),
        Property(name="book25", type=book, multiplicity=Multiplicity(1, 1))
    }
)
library_member_status_of_book: BinaryAssociation = BinaryAssociation(
    name="library_member_status_of_book",
    ends={
        Property(name="status_of_book26", type=status_of_book, multiplicity=Multiplicity(1, 9999)),
        Property(name="library_member27", type=library_member, multiplicity=Multiplicity(1, 9999))
    }
)
library_member_member_profile: BinaryAssociation = BinaryAssociation(
    name="library_member_member_profile",
    ends={
        Property(name="member_profile28", type=member_profile, multiplicity=Multiplicity(1, 1)),
        Property(name="library_member29", type=library_member, multiplicity=Multiplicity(1, 1))
    }
)
librarian_member_profile: BinaryAssociation = BinaryAssociation(
    name="librarian_member_profile",
    ends={
        Property(name="member_profile30", type=library_member, multiplicity=Multiplicity(1, 9999)),
        Property(name="librarian31", type=librarian, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DLKSUK1eEee6S77dw3LIvQ",
    types={User, Data, CSV, XML, File, book, librarian, library_member, fine, transaction, library, credit_card, cash, status_of_book, member_profile},
    associations={User_data, data_File, User_Parser, member_library_card, library_book, library_librarian, library_transaction, transaction_fine, librarian_transaction, fine_credit_card, fine_class, transaction_book, book_status_of_book, library_member_status_of_book, library_member_member_profile, librarian_member_profile},
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
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
librarian_Actor = Class(name="librarian_Actor")
search_for_book_UseCase = Class(name="search_for_book_UseCase")
make_reservation_UseCase = Class(name="make_reservation_UseCase")
issue_book_UseCase = Class(name="issue_book_UseCase")
remove_reservation_UseCase = Class(name="remove_reservation_UseCase")
publisher_Actor = Class(name="publisher_Actor")
buy_book_from_author_UseCase = Class(name="buy_book_from_author_UseCase")
publish_book_UseCase = Class(name="publish_book_UseCase")
display_details_UseCase = Class(name="display_details_UseCase")
system_Component = Class(name="system_Component")
DBA_Actor = Class(name="DBA_Actor")
maintenance_database_UseCase = Class(name="maintenance_database_UseCase")
add_book_UseCase = Class(name="add_book_UseCase")
update_details_UseCase = Class(name="update_details_UseCase")
check_account__UseCase = Class(name="check_account__UseCase")
buy_book_from_publisher_UseCase = Class(name="buy_book_from_publisher_UseCase")
remove_title_UseCase = Class(name="remove_title_UseCase")
user = Class(name="user")
ordinary_user = Class(name="ordinary_user")
student = Class(name="student")
librarian = Class(name="librarian")
date = Class(name="date")
loan_book = Class(name="loan_book")
DBA = Class(name="DBA")
book = Class(name="book")
publisher = Class(name="publisher")

# librarian_Actor class attributes and methods

# search_for_book_UseCase class attributes and methods

# make_reservation_UseCase class attributes and methods

# issue_book_UseCase class attributes and methods

# remove_reservation_UseCase class attributes and methods

# publisher_Actor class attributes and methods

# buy_book_from_author_UseCase class attributes and methods

# publish_book_UseCase class attributes and methods

# display_details_UseCase class attributes and methods

# system_Component class attributes and methods

# DBA_Actor class attributes and methods

# maintenance_database_UseCase class attributes and methods

# add_book_UseCase class attributes and methods

# update_details_UseCase class attributes and methods

# check_account__UseCase class attributes and methods

# buy_book_from_publisher_UseCase class attributes and methods

# remove_title_UseCase class attributes and methods

# user class attributes and methods
user_id: Property = Property(name="id", type=IntegerType)
user_first_name: Property = Property(name="first_name", type=StringType)
user_last_name: Property = Property(name="last_name", type=StringType)
user_phone_number: Property = Property(name="phone_number", type=IntegerType)
user_address: Property = Property(name="address", type=StringType)
user_card: Property = Property(name="card", type=IntegerType)
user_email: Property = Property(name="email", type=StringType)
user.attributes={user_first_name, user_email, user_last_name, user_phone_number, user_id, user_card, user_address}

# ordinary_user class attributes and methods

# student class attributes and methods
student_student_card: Property = Property(name="student_card", type=IntegerType)
student.attributes={student_student_card}

# librarian class attributes and methods
librarian_job: Property = Property(name="job", type=StringType)
librarian_id: Property = Property(name="id", type=IntegerType)
librarian_name: Property = Property(name="name", type=StringType)
librarian_birth_date: Property = Property(name="birth_date", type=DateType)
librarian_address: Property = Property(name="address", type=StringType)
librarian_email: Property = Property(name="email", type=StringType)
librarian_hire_date: Property = Property(name="hire_date", type=DateType)
librarian.attributes={librarian_id, librarian_hire_date, librarian_email, librarian_job, librarian_birth_date, librarian_address, librarian_name}

# date class attributes and methods

# loan_book class attributes and methods
loan_book_id: Property = Property(name="id", type=IntegerType)
loan_book_loan_date: Property = Property(name="loan_date", type=DateType)
loan_book_due_date: Property = Property(name="due_date", type=DateType)
loan_book_returned_date: Property = Property(name="returned_date", type=DateType)
loan_book_cost: Property = Property(name="cost", type=IntegerType)
loan_book.attributes={loan_book_id, loan_book_cost, loan_book_returned_date, loan_book_loan_date, loan_book_due_date}

# DBA class attributes and methods
DBA_ID: Property = Property(name="ID", type=IntegerType)
DBA_name: Property = Property(name="name", type=StringType)
DBA_email: Property = Property(name="email", type=StringType)
DBA.attributes={DBA_ID, DBA_email, DBA_name}

# book class attributes and methods
book_ISBN: Property = Property(name="ISBN", type=IntegerType)
book_title: Property = Property(name="title", type=StringType)
book_pages: Property = Property(name="pages", type=IntegerType)
book_author: Property = Property(name="author", type=StringType)
book_publisher: Property = Property(name="publisher", type=StringType)
book_type: Property = Property(name="type", type=StringType)
book.attributes={book_author, book_title, book_ISBN, book_type, book_pages, book_publisher}

# publisher class attributes and methods
publisher_id: Property = Property(name="id", type=IntegerType)
publisher_name: Property = Property(name="name", type=StringType)
publisher_address: Property = Property(name="address", type=StringType)
publisher_email: Property = Property(name="email", type=StringType)
publisher_website: Property = Property(name="website", type=StringType)
publisher.attributes={publisher_website, publisher_email, publisher_id, publisher_name, publisher_address}

# Relationships
librarian_search_for_book: BinaryAssociation = BinaryAssociation(
    name="librarian_search_for_book",
    ends={
        Property(name="search_for_book0", type=search_for_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian1", type=librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
make_reservation_librarian: BinaryAssociation = BinaryAssociation(
    name="make_reservation_librarian",
    ends={
        Property(name="librarian2", type=librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="make_reservation3", type=make_reservation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
issue_book_librarian: BinaryAssociation = BinaryAssociation(
    name="issue_book_librarian",
    ends={
        Property(name="librarian4", type=librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="issue_book5", type=issue_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
remove_reservation_librarian: BinaryAssociation = BinaryAssociation(
    name="remove_reservation_librarian",
    ends={
        Property(name="librarian6", type=librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="remove_reservation7", type=remove_reservation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
display_details_system: BinaryAssociation = BinaryAssociation(
    name="display_details_system",
    ends={
        Property(name="system8", type=system_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="display_details9", type=display_details_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
publisher_buy_book_from_author: BinaryAssociation = BinaryAssociation(
    name="publisher_buy_book_from_author",
    ends={
        Property(name="buy_book_from_author10", type=buy_book_from_author_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="publisher11", type=publisher_Actor, multiplicity=Multiplicity(0, 1))
    }
)
publisher_publish_book: BinaryAssociation = BinaryAssociation(
    name="publisher_publish_book",
    ends={
        Property(name="publish_book12", type=publish_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="publisher13", type=publisher_Actor, multiplicity=Multiplicity(0, 1))
    }
)
DBA_maintenance_database: BinaryAssociation = BinaryAssociation(
    name="DBA_maintenance_database",
    ends={
        Property(name="maintenance_database14", type=maintenance_database_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dBA15", type=DBA_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_loan_book: BinaryAssociation = BinaryAssociation(
    name="user_loan_book",
    ends={
        Property(name="loan_book216", type=loan_book, multiplicity=Multiplicity(0, 1)),
        Property(name="user17", type=user, multiplicity=Multiplicity(0, 1))
    }
)
user_librarian: BinaryAssociation = BinaryAssociation(
    name="user_librarian",
    ends={
        Property(name="librarian18", type=librarian, multiplicity=Multiplicity(1, 1)),
        Property(name="user19", type=user, multiplicity=Multiplicity(0, 1))
    }
)
librarian_DBA: BinaryAssociation = BinaryAssociation(
    name="librarian_DBA",
    ends={
        Property(name="dBA20", type=DBA, multiplicity=Multiplicity(1, 1)),
        Property(name="librarian21", type=librarian, multiplicity=Multiplicity(0, 1))
    }
)
publisher_DBA: BinaryAssociation = BinaryAssociation(
    name="publisher_DBA",
    ends={
        Property(name="dBA22", type=DBA, multiplicity=Multiplicity(0, 1)),
        Property(name="publisher23", type=publisher, multiplicity=Multiplicity(0, 1))
    }
)
book_publisher: BinaryAssociation = BinaryAssociation(
    name="book_publisher",
    ends={
        Property(name="publisher224", type=publisher, multiplicity=Multiplicity(0, 1)),
        Property(name="book25", type=book, multiplicity=Multiplicity(0, 1))
    }
)
loan_book_book: BinaryAssociation = BinaryAssociation(
    name="loan_book_book",
    ends={
        Property(name="book26", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="loan_book27", type=loan_book, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_AdSZ0HDmEemkSo3PkdMxbg",
    types={librarian_Actor, search_for_book_UseCase, make_reservation_UseCase, issue_book_UseCase, remove_reservation_UseCase, publisher_Actor, buy_book_from_author_UseCase, publish_book_UseCase, display_details_UseCase, system_Component, DBA_Actor, maintenance_database_UseCase, add_book_UseCase, update_details_UseCase, check_account__UseCase, buy_book_from_publisher_UseCase, remove_title_UseCase, user, ordinary_user, student, librarian, date, loan_book, DBA, book, publisher},
    associations={librarian_search_for_book, make_reservation_librarian, issue_book_librarian, remove_reservation_librarian, display_details_system, publisher_buy_book_from_author, publisher_publish_book, DBA_maintenance_database, user_loan_book, user_librarian, librarian_DBA, publisher_DBA, book_publisher, loan_book_book},
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
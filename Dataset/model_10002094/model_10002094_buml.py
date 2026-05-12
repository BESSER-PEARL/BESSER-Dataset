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
Library_Actor = Class(name="Library_Actor")
Send_book_return_due_reminder_UseCase = Class(name="Send_book_return_due_reminder_UseCase")
Manage_Interlibrary_loan_requests_UseCase = Class(name="Manage_Interlibrary_loan_requests_UseCase")
Renew_magazine_subscriptions_UseCase = Class(name="Renew_magazine_subscriptions_UseCase")
Retire_books_UseCase = Class(name="Retire_books_UseCase")
Check_out_book_UseCase = Class(name="Check_out_book_UseCase")
Put_book_on_reserve_UseCase = Class(name="Put_book_on_reserve_UseCase")
Pay_overdue_fine_UseCase = Class(name="Pay_overdue_fine_UseCase")
Fine_patron_for_overdue_book_UseCase = Class(name="Fine_patron_for_overdue_book_UseCase")
Library_patron_Actor = Class(name="Library_patron_Actor")
Return_book_UseCase = Class(name="Return_book_UseCase")
Check_in_book_UseCase = Class(name="Check_in_book_UseCase")
Assist_with_research_using_hard_copy_indexes_UseCase = Class(name="Assist_with_research_using_hard_copy_indexes_UseCase")
Assist_with_research_using_computer_based_tools_UseCase = Class(name="Assist_with_research_using_computer_based_tools_UseCase")
Library_staff_Actor = Class(name="Library_staff_Actor")
Reshelve_books_UseCase = Class(name="Reshelve_books_UseCase")
Bound_magazines_into_volumes_or_record_as_microfiche_UseCase = Class(name="Bound_magazines_into_volumes_or_record_as_microfiche_UseCase")
Order_new_library_resources_UseCase = Class(name="Order_new_library_resources_UseCase")
Library = Class(name="Library")
Double = Class(name="Double")
Item = Class(name="Item")
Book = Class(name="Book")
Magazine = Class(name="Magazine")
CD = Class(name="CD")
Software = Class(name="Software")
Video = Class(name="Video")
Library_Patron = Class(name="Library_Patron")
Faculty = Class(name="Faculty")
Class_ = Class(name="Class")
Library_staff = Class(name="Library_staff")

# Library_Actor class attributes and methods

# Send_book_return_due_reminder_UseCase class attributes and methods

# Manage_Interlibrary_loan_requests_UseCase class attributes and methods

# Renew_magazine_subscriptions_UseCase class attributes and methods

# Retire_books_UseCase class attributes and methods

# Check_out_book_UseCase class attributes and methods

# Put_book_on_reserve_UseCase class attributes and methods

# Pay_overdue_fine_UseCase class attributes and methods

# Fine_patron_for_overdue_book_UseCase class attributes and methods

# Library_patron_Actor class attributes and methods

# Return_book_UseCase class attributes and methods

# Check_in_book_UseCase class attributes and methods

# Assist_with_research_using_hard_copy_indexes_UseCase class attributes and methods

# Assist_with_research_using_computer_based_tools_UseCase class attributes and methods

# Library_staff_Actor class attributes and methods

# Reshelve_books_UseCase class attributes and methods

# Bound_magazines_into_volumes_or_record_as_microfiche_UseCase class attributes and methods

# Order_new_library_resources_UseCase class attributes and methods

# Library class attributes and methods
Library_book: Property = Property(name="book", type=StringType)
Library_Magazine: Property = Property(name="Magazine", type=StringType)
Library_finePerDar: Property = Property(name="finePerDar", type=Double)
Library_maxFine: Property = Property(name="maxFine", type=Double)
Library_software: Property = Property(name="software", type=StringType)
Library_videos: Property = Property(name="videos", type=StringType)
Library_computers: Property = Property(name="computers", type=StringType)
Library_CDs: Property = Property(name="CDs", type=StringType)
Library.attributes={Library_CDs, Library_Magazine, Library_finePerDar, Library_computers, Library_maxFine, Library_book, Library_videos, Library_software}

# Double class attributes and methods

# Item class attributes and methods
Item_maxCheckOut: Property = Property(name="maxCheckOut", type=IntegerType)
Item_age: Property = Property(name="age", type=IntegerType)
Item.attributes={Item_maxCheckOut, Item_age}

# Book class attributes and methods

# Magazine class attributes and methods

# CD class attributes and methods

# Software class attributes and methods

# Video class attributes and methods

# Library_Patron class attributes and methods
Library_Patron_books: Property = Property(name="books", type=StringType)
Library_Patron_maxBookCheckOut: Property = Property(name="maxBookCheckOut", type=IntegerType)
Library_Patron.attributes={Library_Patron_maxBookCheckOut, Library_Patron_books}

# Faculty class attributes and methods

# Class class attributes and methods

# Library_staff class attributes and methods

# Relationships
Send_book_return_due_reminder_Library: BinaryAssociation = BinaryAssociation(
    name="Send_book_return_due_reminder_Library",
    ends={
        Property(name="library0", type=Library_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="send_book_return_due_reminder1", type=Send_book_return_due_reminder_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manage_Interlibrary_loan_requests_Library: BinaryAssociation = BinaryAssociation(
    name="Manage_Interlibrary_loan_requests_Library",
    ends={
        Property(name="library2", type=Library_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Interlibrary_loan_requests3", type=Manage_Interlibrary_loan_requests_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Return_book_Check_in_book: BinaryAssociation = BinaryAssociation(
    name="Return_book_Check_in_book",
    ends={
        Property(name="check_in_book24", type=Check_in_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="return_book25", type=Return_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Check_in_book: BinaryAssociation = BinaryAssociation(
    name="Library_Check_in_book",
    ends={
        Property(name="check_in_book26", type=Check_in_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library27", type=Library_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_patron_Assist_with_research_using_hard_copy_indexes: BinaryAssociation = BinaryAssociation(
    name="Library_patron_Assist_with_research_using_hard_copy_indexes",
    ends={
        Property(name="assist_with_research_using_hard_copy_indexes28", type=Assist_with_research_using_hard_copy_indexes_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_patron29", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_patron_Assist_with_research_using_computer_based_tools: BinaryAssociation = BinaryAssociation(
    name="Library_patron_Assist_with_research_using_computer_based_tools",
    ends={
        Property(name="assist_with_research_using_computer_based_tools30", type=Assist_with_research_using_computer_based_tools_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_patron31", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Assist_with_research_using_hard_copy_indexes_Library_staff: BinaryAssociation = BinaryAssociation(
    name="Assist_with_research_using_hard_copy_indexes_Library_staff",
    ends={
        Property(name="library_staff32", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="assist_with_research_using_hard_copy_indexes33", type=Assist_with_research_using_hard_copy_indexes_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Assist_with_research_using_computer_based_tools_Library_staff: BinaryAssociation = BinaryAssociation(
    name="Assist_with_research_using_computer_based_tools_Library_staff",
    ends={
        Property(name="library_staff34", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="assist_with_research_using_computer_based_tools35", type=Assist_with_research_using_computer_based_tools_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_staff_Check_in_book: BinaryAssociation = BinaryAssociation(
    name="Library_staff_Check_in_book",
    ends={
        Property(name="check_in_book36", type=Check_in_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library_staff37", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Reshelve_books_Library_staff: BinaryAssociation = BinaryAssociation(
    name="Reshelve_books_Library_staff",
    ends={
        Property(name="library_staff38", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reshelve_books39", type=Reshelve_books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Bound_magazines_into_volumes_or_record_as_microfiche_Library_staff: BinaryAssociation = BinaryAssociation(
    name="Bound_magazines_into_volumes_or_record_as_microfiche_Library_staff",
    ends={
        Property(name="library_staff40", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="bound_magazines_into_volumes_or_record_as_microfiche41", type=Bound_magazines_into_volumes_or_record_as_microfiche_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_new_library_resources_Library_staff: BinaryAssociation = BinaryAssociation(
    name="Order_new_library_resources_Library_staff",
    ends={
        Property(name="library_staff42", type=Library_staff_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="order_new_library_resources43", type=Order_new_library_resources_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_new_library_resources_Library: BinaryAssociation = BinaryAssociation(
    name="Order_new_library_resources_Library",
    ends={
        Property(name="library44", type=Library_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="order_new_library_resources45", type=Order_new_library_resources_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Item: BinaryAssociation = BinaryAssociation(
    name="Library_Item",
    ends={
        Property(name="item46", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="library47", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
Library_Library_Patron: BinaryAssociation = BinaryAssociation(
    name="Library_Library_Patron",
    ends={
        Property(name="library_Patron48", type=Library_Patron, multiplicity=Multiplicity(0, 1)),
        Property(name="library49", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
Renew_magazine_subscriptions_Library: BinaryAssociation = BinaryAssociation(
    name="Renew_magazine_subscriptions_Library",
    ends={
        Property(name="library4", type=Library_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="renew_magazine_subscriptions5", type=Renew_magazine_subscriptions_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Retire_books_Library: BinaryAssociation = BinaryAssociation(
    name="Retire_books_Library",
    ends={
        Property(name="library6", type=Library_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="retire_books7", type=Retire_books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Fine_patron_for_overdue_book: BinaryAssociation = BinaryAssociation(
    name="Library_Fine_patron_for_overdue_book",
    ends={
        Property(name="fine_patron_for_overdue_book8", type=Fine_patron_for_overdue_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library9", type=Library_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Fine_patron_for_overdue_book_Pay_overdue_fine: BinaryAssociation = BinaryAssociation(
    name="Fine_patron_for_overdue_book_Pay_overdue_fine",
    ends={
        Property(name="pay_overdue_fine10", type=Pay_overdue_fine_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fine_patron_for_overdue_book11", type=Fine_patron_for_overdue_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Library_Put_book_on_reserve: BinaryAssociation = BinaryAssociation(
    name="Library_Put_book_on_reserve",
    ends={
        Property(name="put_book_on_reserve12", type=Put_book_on_reserve_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library13", type=Library_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Library_Check_out_book: BinaryAssociation = BinaryAssociation(
    name="Library_Check_out_book",
    ends={
        Property(name="check_out_book14", type=Check_out_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="library15", type=Library_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_out_book_Library_patron: BinaryAssociation = BinaryAssociation(
    name="Check_out_book_Library_patron",
    ends={
        Property(name="library_patron16", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_out_book17", type=Check_out_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Put_book_on_reserve_Library_patron: BinaryAssociation = BinaryAssociation(
    name="Put_book_on_reserve_Library_patron",
    ends={
        Property(name="library_patron18", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="put_book_on_reserve19", type=Put_book_on_reserve_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Pay_overdue_fine_Library_patron: BinaryAssociation = BinaryAssociation(
    name="Pay_overdue_fine_Library_patron",
    ends={
        Property(name="library_patron20", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pay_overdue_fine21", type=Pay_overdue_fine_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Return_book_Library_patron: BinaryAssociation = BinaryAssociation(
    name="Return_book_Library_patron",
    ends={
        Property(name="library_patron22", type=Library_patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="return_book23", type=Return_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nshpcAlTEeiTXI7G38ZLFQ",
    types={Library_Actor, Send_book_return_due_reminder_UseCase, Manage_Interlibrary_loan_requests_UseCase, Renew_magazine_subscriptions_UseCase, Retire_books_UseCase, Check_out_book_UseCase, Put_book_on_reserve_UseCase, Pay_overdue_fine_UseCase, Fine_patron_for_overdue_book_UseCase, Library_patron_Actor, Return_book_UseCase, Check_in_book_UseCase, Assist_with_research_using_hard_copy_indexes_UseCase, Assist_with_research_using_computer_based_tools_UseCase, Library_staff_Actor, Reshelve_books_UseCase, Bound_magazines_into_volumes_or_record_as_microfiche_UseCase, Order_new_library_resources_UseCase, Library, Double, Item, Book, Magazine, CD, Software, Video, Library_Patron, Faculty, Class_, Library_staff},
    associations={Send_book_return_due_reminder_Library, Manage_Interlibrary_loan_requests_Library, Return_book_Check_in_book, Library_Check_in_book, Library_patron_Assist_with_research_using_hard_copy_indexes, Library_patron_Assist_with_research_using_computer_based_tools, Assist_with_research_using_hard_copy_indexes_Library_staff, Assist_with_research_using_computer_based_tools_Library_staff, Library_staff_Check_in_book, Reshelve_books_Library_staff, Bound_magazines_into_volumes_or_record_as_microfiche_Library_staff, Order_new_library_resources_Library_staff, Order_new_library_resources_Library, Library_Item, Library_Library_Patron, Renew_magazine_subscriptions_Library, Retire_books_Library, Library_Fine_patron_for_overdue_book, Fine_patron_for_overdue_book_Pay_overdue_fine, Library_Put_book_on_reserve, Library_Check_out_book, Check_out_book_Library_patron, Put_book_on_reserve_Library_patron, Pay_overdue_fine_Library_patron, Return_book_Library_patron},
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
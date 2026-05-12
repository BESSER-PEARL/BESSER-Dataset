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
Library_Managment_System_Check_in___Return_UseCase = Class(name="Library_Managment_System_Check_in___Return_UseCase")
Library_Managment_System_Requested_UseCase = Class(name="Library_Managment_System_Requested_UseCase")
Library_Managment_System_Reference_UseCase = Class(name="Library_Managment_System_Reference_UseCase")
Library_Managment_System_Check_out_UseCase = Class(name="Library_Managment_System_Check_out_UseCase")
Library_Managment_System_Reserve_UseCase = Class(name="Library_Managment_System_Reserve_UseCase")
Library_Managment_System_Special_Status_UseCase = Class(name="Library_Managment_System_Special_Status_UseCase")
Library_Managment_System_Magazines_UseCase = Class(name="Library_Managment_System_Magazines_UseCase")
Library_Managment_System_Renew_Checkout_if_not_requested_UseCase = Class(name="Library_Managment_System_Renew_Checkout_if_not_requested_UseCase")
Library_Managment_System_Late_Notice_UseCase = Class(name="Library_Managment_System_Late_Notice_UseCase")
Library_Managment_System_Status_UseCase = Class(name="Library_Managment_System_Status_UseCase")
Library_Managment_System_Student_UseCase = Class(name="Library_Managment_System_Student_UseCase")
Library_Managment_System_Faculty_UseCase = Class(name="Library_Managment_System_Faculty_UseCase")
Library_Managment_System_Librarian_UseCase = Class(name="Library_Managment_System_Librarian_UseCase")
Library_Managment_System_4_week_check_out_UseCase = Class(name="Library_Managment_System_4_week_check_out_UseCase")
Library_Managment_System_Reserve_book__1_semester__UseCase = Class(name="Library_Managment_System_Reserve_book__1_semester__UseCase")
Library_Managment_System_Reserve_foreign_resources_UseCase = Class(name="Library_Managment_System_Reserve_foreign_resources_UseCase")
Library_Managment_System_3_month_check_out_UseCase = Class(name="Library_Managment_System_3_month_check_out_UseCase")
Library_Managment_System_1_year_check_out_UseCase = Class(name="Library_Managment_System_1_year_check_out_UseCase")
Library_Managment_System_Issue_fines_UseCase = Class(name="Library_Managment_System_Issue_fines_UseCase")
Library_Managment_System_Manage_Magazines_UseCase = Class(name="Library_Managment_System_Manage_Magazines_UseCase")
Library_Managment_System_Renew_subscriptions_UseCase = Class(name="Library_Managment_System_Renew_subscriptions_UseCase")
Library_Managment_System_Reshelving_books_UseCase = Class(name="Library_Managment_System_Reshelving_books_UseCase")
Library_Managment_System_Ordering_new_resources_UseCase = Class(name="Library_Managment_System_Ordering_new_resources_UseCase")
Library_Managment_System_Assist_patrons_in_research_UseCase = Class(name="Library_Managment_System_Assist_patrons_in_research_UseCase")
Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase = Class(name="Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase")
Library_Managment_System_Books_UseCase = Class(name="Library_Managment_System_Books_UseCase")
Library_Managment_System_Adding_UseCase = Class(name="Library_Managment_System_Adding_UseCase")
Library_Managment_System_Retiring_UseCase = Class(name="Library_Managment_System_Retiring_UseCase")
Library_Managment_System_Meet_requests_of_patrons_UseCase = Class(name="Library_Managment_System_Meet_requests_of_patrons_UseCase")
Library_Managment_System_Contents_out_of_date_UseCase = Class(name="Library_Managment_System_Contents_out_of_date_UseCase")
Library_Managment_System_Other_resources_UseCase = Class(name="Library_Managment_System_Other_resources_UseCase")
Library_Managment_System_CD_s_software_videos_UseCase = Class(name="Library_Managment_System_CD_s_software_videos_UseCase")
Library_Managment_System_1_week_check_out_UseCase = Class(name="Library_Managment_System_1_week_check_out_UseCase")
Librarian_Actor = Class(name="Librarian_Actor")
Student_Actor = Class(name="Student_Actor")
Library_Management_System_Patron = Class(name="Library_Management_System_Patron")
Library_Management_System_Student = Class(name="Library_Management_System_Student")
Library_Management_System_Faculty = Class(name="Library_Management_System_Faculty")
Library_Management_System_Librarian = Class(name="Library_Management_System_Librarian")
Faculty_Actor = Class(name="Faculty_Actor")

# Library_Managment_System_Check_in___Return_UseCase class attributes and methods

# Library_Managment_System_Requested_UseCase class attributes and methods

# Library_Managment_System_Reference_UseCase class attributes and methods

# Library_Managment_System_Check_out_UseCase class attributes and methods

# Library_Managment_System_Reserve_UseCase class attributes and methods

# Library_Managment_System_Special_Status_UseCase class attributes and methods

# Library_Managment_System_Magazines_UseCase class attributes and methods

# Library_Managment_System_Renew_Checkout_if_not_requested_UseCase class attributes and methods

# Library_Managment_System_Late_Notice_UseCase class attributes and methods

# Library_Managment_System_Status_UseCase class attributes and methods

# Library_Managment_System_Student_UseCase class attributes and methods

# Library_Managment_System_Faculty_UseCase class attributes and methods

# Library_Managment_System_Librarian_UseCase class attributes and methods

# Library_Managment_System_4_week_check_out_UseCase class attributes and methods

# Library_Managment_System_Reserve_book__1_semester__UseCase class attributes and methods

# Library_Managment_System_Reserve_foreign_resources_UseCase class attributes and methods

# Library_Managment_System_3_month_check_out_UseCase class attributes and methods

# Library_Managment_System_1_year_check_out_UseCase class attributes and methods

# Library_Managment_System_Issue_fines_UseCase class attributes and methods

# Library_Managment_System_Manage_Magazines_UseCase class attributes and methods

# Library_Managment_System_Renew_subscriptions_UseCase class attributes and methods

# Library_Managment_System_Reshelving_books_UseCase class attributes and methods

# Library_Managment_System_Ordering_new_resources_UseCase class attributes and methods

# Library_Managment_System_Assist_patrons_in_research_UseCase class attributes and methods

# Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase class attributes and methods

# Library_Managment_System_Books_UseCase class attributes and methods

# Library_Managment_System_Adding_UseCase class attributes and methods

# Library_Managment_System_Retiring_UseCase class attributes and methods

# Library_Managment_System_Meet_requests_of_patrons_UseCase class attributes and methods

# Library_Managment_System_Contents_out_of_date_UseCase class attributes and methods

# Library_Managment_System_Other_resources_UseCase class attributes and methods

# Library_Managment_System_CD_s_software_videos_UseCase class attributes and methods

# Library_Managment_System_1_week_check_out_UseCase class attributes and methods

# Librarian_Actor class attributes and methods

# Student_Actor class attributes and methods

# Library_Management_System_Patron class attributes and methods
Library_Management_System_Patron_Books: Property = Property(name="Books", type=StringType)
Library_Management_System_Patron_OtherResources: Property = Property(name="OtherResources", type=StringType)
Library_Management_System_Patron_Status: Property = Property(name="Status", type=Library_Management_System_Patron)
Library_Management_System_Patron_SpecialStatus: Property = Property(name="SpecialStatus", type=StringType)
Library_Management_System_Patron_Magazines: Property = Property(name="Magazines", type=StringType)
Library_Management_System_Patron.attributes={Library_Management_System_Patron_SpecialStatus, Library_Management_System_Patron_Books, Library_Management_System_Patron_Status, Library_Management_System_Patron_OtherResources, Library_Management_System_Patron_Magazines}

# Library_Management_System_Student class attributes and methods
Library_Management_System_Student_StudentId: Property = Property(name="StudentId", type=IntegerType)
Library_Management_System_Student_StudentName: Property = Property(name="StudentName", type=StringType)
Library_Management_System_Student.attributes={Library_Management_System_Student_StudentId, Library_Management_System_Student_StudentName}

# Library_Management_System_Faculty class attributes and methods
Library_Management_System_Faculty_FacultyId: Property = Property(name="FacultyId", type=IntegerType)
Library_Management_System_Faculty_FacultyName: Property = Property(name="FacultyName", type=StringType)
Library_Management_System_Faculty.attributes={Library_Management_System_Faculty_FacultyId, Library_Management_System_Faculty_FacultyName}

# Library_Management_System_Librarian class attributes and methods
Library_Management_System_Librarian_LibrarianName: Property = Property(name="LibrarianName", type=StringType)
Library_Management_System_Librarian.attributes={Library_Management_System_Librarian_LibrarianName}

# Faculty_Actor class attributes and methods

# Relationships
Librarian_1_year_check_out: BinaryAssociation = BinaryAssociation(
    name="Librarian_1_year_check_out",
    ends={
        Property(name="_1_year_check_out0", type=Library_Managment_System_1_year_check_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian1", type=Library_Managment_System_Librarian_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Check_in___Return: BinaryAssociation = BinaryAssociation(
    name="Librarian_Check_in___Return",
    ends={
        Property(name="check_in___Return2", type=Library_Managment_System_Check_in___Return_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian3", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Check_out: BinaryAssociation = BinaryAssociation(
    name="Librarian_Check_out",
    ends={
        Property(name="check_out4", type=Library_Managment_System_Check_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian5", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Librarian: BinaryAssociation = BinaryAssociation(
    name="Patron_Librarian",
    ends={
        Property(name="librarian40", type=Library_Management_System_Librarian, multiplicity=Multiplicity(1, 9999)),
        Property(name="patron41", type=Library_Management_System_Patron, multiplicity=Multiplicity(1, 9999))
    }
)
Faculty_Reserve: BinaryAssociation = BinaryAssociation(
    name="Faculty_Reserve",
    ends={
        Property(name="reserve42", type=Library_Managment_System_Reserve_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty43", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Check_in___Return: BinaryAssociation = BinaryAssociation(
    name="Faculty_Check_in___Return",
    ends={
        Property(name="check_in___Return44", type=Library_Managment_System_Check_in___Return_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty45", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Requested: BinaryAssociation = BinaryAssociation(
    name="Faculty_Requested",
    ends={
        Property(name="requested46", type=Library_Managment_System_Requested_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty47", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Check_out: BinaryAssociation = BinaryAssociation(
    name="Faculty_Check_out",
    ends={
        Property(name="check_out48", type=Library_Managment_System_Check_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty49", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Reference: BinaryAssociation = BinaryAssociation(
    name="Faculty_Reference",
    ends={
        Property(name="reference50", type=Library_Managment_System_Reference_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty51", type=Faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Requested: BinaryAssociation = BinaryAssociation(
    name="Librarian_Requested",
    ends={
        Property(name="requested6", type=Library_Managment_System_Requested_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian7", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Reserve: BinaryAssociation = BinaryAssociation(
    name="Librarian_Reserve",
    ends={
        Property(name="reserve8", type=Library_Managment_System_Reserve_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian9", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Reference: BinaryAssociation = BinaryAssociation(
    name="Librarian_Reference",
    ends={
        Property(name="reference10", type=Library_Managment_System_Reference_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian11", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Check_in___Return: BinaryAssociation = BinaryAssociation(
    name="Student_Check_in___Return",
    ends={
        Property(name="check_in___Return12", type=Library_Managment_System_Check_in___Return_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student13", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Check_out: BinaryAssociation = BinaryAssociation(
    name="Student_Check_out",
    ends={
        Property(name="check_out14", type=Library_Managment_System_Check_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student15", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Requested: BinaryAssociation = BinaryAssociation(
    name="Student_Requested",
    ends={
        Property(name="requested16", type=Library_Managment_System_Requested_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student17", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Reserve: BinaryAssociation = BinaryAssociation(
    name="Student_Reserve",
    ends={
        Property(name="reserve18", type=Library_Managment_System_Reserve_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student19", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Reference: BinaryAssociation = BinaryAssociation(
    name="Student_Reference",
    ends={
        Property(name="reference20", type=Library_Managment_System_Reference_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student21", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Issue_fines: BinaryAssociation = BinaryAssociation(
    name="Librarian_Issue_fines",
    ends={
        Property(name="issue_fines22", type=Library_Managment_System_Issue_fines_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian23", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Manage_Magazines: BinaryAssociation = BinaryAssociation(
    name="Librarian_Manage_Magazines",
    ends={
        Property(name="manage_Magazines24", type=Library_Managment_System_Manage_Magazines_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian25", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Reshelving_books: BinaryAssociation = BinaryAssociation(
    name="Librarian_Reshelving_books",
    ends={
        Property(name="reshelving_books26", type=Library_Managment_System_Reshelving_books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian27", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Ordering_new_resources: BinaryAssociation = BinaryAssociation(
    name="Librarian_Ordering_new_resources",
    ends={
        Property(name="ordering_new_resources28", type=Library_Managment_System_Ordering_new_resources_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian29", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Assist_patrons_in_research: BinaryAssociation = BinaryAssociation(
    name="Librarian_Assist_patrons_in_research",
    ends={
        Property(name="assist_patrons_in_research30", type=Library_Managment_System_Assist_patrons_in_research_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian31", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Connect_to_holding_of_other_libraries: BinaryAssociation = BinaryAssociation(
    name="Librarian_Connect_to_holding_of_other_libraries",
    ends={
        Property(name="connect_to_holding_of_other_libraries32", type=Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian33", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Librarian_Books: BinaryAssociation = BinaryAssociation(
    name="Librarian_Books",
    ends={
        Property(name="books34", type=Library_Managment_System_Books_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="librarian35", type=Librarian_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Student: BinaryAssociation = BinaryAssociation(
    name="Patron_Student",
    ends={
        Property(name="student36", type=Library_Management_System_Student, multiplicity=Multiplicity(1, 9999)),
        Property(name="patron37", type=Library_Management_System_Patron, multiplicity=Multiplicity(1, 9999))
    }
)
Patron_Faculty: BinaryAssociation = BinaryAssociation(
    name="Patron_Faculty",
    ends={
        Property(name="faculty38", type=Library_Management_System_Faculty, multiplicity=Multiplicity(1, 9999)),
        Property(name="patron39", type=Library_Management_System_Patron, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="cc609032_bac4_432b_ba8a_17fb8d177254",
    types={Library_Managment_System_Check_in___Return_UseCase, Library_Managment_System_Requested_UseCase, Library_Managment_System_Reference_UseCase, Library_Managment_System_Check_out_UseCase, Library_Managment_System_Reserve_UseCase, Library_Managment_System_Special_Status_UseCase, Library_Managment_System_Magazines_UseCase, Library_Managment_System_Renew_Checkout_if_not_requested_UseCase, Library_Managment_System_Late_Notice_UseCase, Library_Managment_System_Status_UseCase, Library_Managment_System_Student_UseCase, Library_Managment_System_Faculty_UseCase, Library_Managment_System_Librarian_UseCase, Library_Managment_System_4_week_check_out_UseCase, Library_Managment_System_Reserve_book__1_semester__UseCase, Library_Managment_System_Reserve_foreign_resources_UseCase, Library_Managment_System_3_month_check_out_UseCase, Library_Managment_System_1_year_check_out_UseCase, Library_Managment_System_Issue_fines_UseCase, Library_Managment_System_Manage_Magazines_UseCase, Library_Managment_System_Renew_subscriptions_UseCase, Library_Managment_System_Reshelving_books_UseCase, Library_Managment_System_Ordering_new_resources_UseCase, Library_Managment_System_Assist_patrons_in_research_UseCase, Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase, Library_Managment_System_Books_UseCase, Library_Managment_System_Adding_UseCase, Library_Managment_System_Retiring_UseCase, Library_Managment_System_Meet_requests_of_patrons_UseCase, Library_Managment_System_Contents_out_of_date_UseCase, Library_Managment_System_Other_resources_UseCase, Library_Managment_System_CD_s_software_videos_UseCase, Library_Managment_System_1_week_check_out_UseCase, Librarian_Actor, Student_Actor, Library_Management_System_Patron, Library_Management_System_Student, Library_Management_System_Faculty, Library_Management_System_Librarian, Faculty_Actor},
    associations={Librarian_1_year_check_out, Librarian_Check_in___Return, Librarian_Check_out, Patron_Librarian, Faculty_Reserve, Faculty_Check_in___Return, Faculty_Requested, Faculty_Check_out, Faculty_Reference, Librarian_Requested, Librarian_Reserve, Librarian_Reference, Student_Check_in___Return, Student_Check_out, Student_Requested, Student_Reserve, Student_Reference, Librarian_Issue_fines, Librarian_Manage_Magazines, Librarian_Reshelving_books, Librarian_Ordering_new_resources, Librarian_Assist_patrons_in_research, Librarian_Connect_to_holding_of_other_libraries, Librarian_Books, Patron_Student, Patron_Faculty},
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
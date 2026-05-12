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
Books = Class(name="Books")
Member = Class(name="Member")
Librarian = Class(name="Librarian")
Fine = Class(name="Fine")
Borrowed = Class(name="Borrowed")
Reserved = Class(name="Reserved")
Staff = Class(name="Staff")
admin = Class(name="admin")
lecturer = Class(name="lecturer")
Class_ = Class(name="Class")

# Books class attributes and methods
Books_book_id: Property = Property(name="book_id", type=IntegerType)
Books_title: Property = Property(name="title", type=StringType)
Books_author_name: Property = Property(name="author_name", type=StringType)
Books_ISBN_no: Property = Property(name="ISBN_no", type=StringType)
Books_publisher: Property = Property(name="publisher", type=StringType)
Books_book_qty: Property = Property(name="book_qty", type=IntegerType)
Books.attributes={Books_book_id, Books_publisher, Books_ISBN_no, Books_book_qty, Books_author_name, Books_title}

# Member class attributes and methods
Member_member_id: Property = Property(name="member_id", type=IntegerType)
Member_member_pwd: Property = Property(name="member_pwd", type=StringType)
Member_fname: Property = Property(name="fname", type=StringType)
Member_lname: Property = Property(name="lname", type=StringType)
Member_gender: Property = Property(name="gender", type=StringType)
Member_dob: Property = Property(name="dob", type=StringType)
Member_address: Property = Property(name="address", type=StringType)
Member_cont_no: Property = Property(name="cont_no", type=IntegerType)
Member.attributes={Member_address, Member_lname, Member_fname, Member_member_id, Member_dob, Member_cont_no, Member_gender, Member_member_pwd}

# Librarian class attributes and methods
Librarian_fname: Property = Property(name="fname", type=StringType)
Librarian_lname: Property = Property(name="lname", type=StringType)
Librarian_gender: Property = Property(name="gender", type=StringType)
Librarian_dob: Property = Property(name="dob", type=StringType)
Librarian_address: Property = Property(name="address", type=StringType)
Librarian_cont_no: Property = Property(name="cont_no", type=IntegerType)
Librarian_member_id: Property = Property(name="member_id", type=IntegerType)
Librarian_member_pwd: Property = Property(name="member_pwd", type=StringType)
Librarian.attributes={Librarian_member_pwd, Librarian_cont_no, Librarian_dob, Librarian_fname, Librarian_lname, Librarian_address, Librarian_member_id, Librarian_gender}

# Fine class attributes and methods
Fine_book_id: Property = Property(name="book_id", type=IntegerType)
Fine_member_id: Property = Property(name="member_id", type=IntegerType)
Fine_fine_amount: Property = Property(name="fine_amount", type=IntegerType)
Fine_borrowed_date: Property = Property(name="borrowed_date", type=StringType)
Fine_returned_date: Property = Property(name="returned_date", type=StringType)
Fine.attributes={Fine_book_id, Fine_fine_amount, Fine_borrowed_date, Fine_member_id, Fine_returned_date}

# Borrowed class attributes and methods
Borrowed_borrowed_date: Property = Property(name="borrowed_date", type=StringType)
Borrowed_returned_date: Property = Property(name="returned_date", type=StringType)
Borrowed.attributes={Borrowed_borrowed_date, Borrowed_returned_date}

# Reserved class attributes and methods
Reserved_reserved_date: Property = Property(name="reserved_date", type=StringType)
Reserved.attributes={Reserved_reserved_date}

# Staff class attributes and methods
Staff_Staff_ID: Property = Property(name="Staff_ID", type=IntegerType)
Staff_fname: Property = Property(name="fname", type=StringType)
Staff_lname: Property = Property(name="lname", type=StringType)
Staff_position: Property = Property(name="position", type=StringType)
Staff_address: Property = Property(name="address", type=StringType)
Staff_gender: Property = Property(name="gender", type=StringType)
Staff_email: Property = Property(name="email", type=StringType)
Staff_contact: Property = Property(name="contact", type=IntegerType)
Staff_username: Property = Property(name="username", type=StringType)
Staff_password: Property = Property(name="password", type=StringType)
Staff.attributes={Staff_fname, Staff_lname, Staff_contact, Staff_password, Staff_email, Staff_position, Staff_username, Staff_address, Staff_gender, Staff_Staff_ID}

# admin class attributes and methods
admin_Experience: Property = Property(name="Experience", type=StringType)
admin.attributes={admin_Experience}

# lecturer class attributes and methods
lecturer_module: Property = Property(name="module", type=StringType)
lecturer.attributes={lecturer_module}

# Class class attributes and methods

# Relationships
Books_Borrowed: BinaryAssociation = BinaryAssociation(
    name="Books_Borrowed",
    ends={
        Property(name="borrowed0", type=Borrowed, multiplicity=Multiplicity(0, 9999)),
        Property(name="books1", type=Books, multiplicity=Multiplicity(0, 9999))
    }
)
Borrowed_Member: BinaryAssociation = BinaryAssociation(
    name="Borrowed_Member",
    ends={
        Property(name="member2", type=Member, multiplicity=Multiplicity(0, 9999)),
        Property(name="borrowed3", type=Borrowed, multiplicity=Multiplicity(0, 9999))
    }
)
Books_Reserved: BinaryAssociation = BinaryAssociation(
    name="Books_Reserved",
    ends={
        Property(name="reserved4", type=Reserved, multiplicity=Multiplicity(0, 9999)),
        Property(name="books5", type=Books, multiplicity=Multiplicity(0, 9999))
    }
)
Reserved_Member: BinaryAssociation = BinaryAssociation(
    name="Reserved_Member",
    ends={
        Property(name="member6", type=Member, multiplicity=Multiplicity(0, 9999)),
        Property(name="reserved7", type=Reserved, multiplicity=Multiplicity(0, 9999))
    }
)
Librarian_Books: BinaryAssociation = BinaryAssociation(
    name="Librarian_Books",
    ends={
        Property(name="books8", type=Books, multiplicity=Multiplicity(0, 9999)),
        Property(name="librarian9", type=Librarian, multiplicity=Multiplicity(0, 9999))
    }
)
Librarian_Fine: BinaryAssociation = BinaryAssociation(
    name="Librarian_Fine",
    ends={
        Property(name="fine10", type=Fine, multiplicity=Multiplicity(0, 9999)),
        Property(name="librarian11", type=Librarian, multiplicity=Multiplicity(0, 9999))
    }
)
Fine_Member: BinaryAssociation = BinaryAssociation(
    name="Fine_Member",
    ends={
        Property(name="member12", type=Member, multiplicity=Multiplicity(1, 1)),
        Property(name="fine13", type=Fine, multiplicity=Multiplicity(0, 9999))
    }
)
Member_Librarian: BinaryAssociation = BinaryAssociation(
    name="Member_Librarian",
    ends={
        Property(name="librarian14", type=Librarian, multiplicity=Multiplicity(0, 9999)),
        Property(name="member15", type=Member, multiplicity=Multiplicity(0, 9999))
    }
)
Registar_Staff2: BinaryAssociation = BinaryAssociation(
    name="Registar_Staff2",
    ends={
        Property(name="staff16", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="registar17", type=admin, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Professor2: BinaryAssociation = BinaryAssociation(
    name="Staff_Professor2",
    ends={
        Property(name="professor18", type=lecturer, multiplicity=Multiplicity(0, 1)),
        Property(name="staff19", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_52339322_f246_45ff_8344_0fa2e942aec4",
    types={Books, Member, Librarian, Fine, Borrowed, Reserved, Staff, admin, lecturer, Class_},
    associations={Books_Borrowed, Borrowed_Member, Books_Reserved, Reserved_Member, Librarian_Books, Librarian_Fine, Fine_Member, Member_Librarian, Registar_Staff2, Staff_Professor2},
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
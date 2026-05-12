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
Retro_Projetor = Class(name="Retro_Projetor")
Members = Class(name="Members")
Quado_Branco = Class(name="Quado_Branco")
Ar_Condicionado = Class(name="Ar_Condicionado")
Borrowed = Class(name="Borrowed")
Reserved = Class(name="Reserved")
Staff = Class(name="Staff")
admin = Class(name="admin")
lecturer = Class(name="lecturer")
Class_ = Class(name="Class")

# Retro_Projetor class attributes and methods
Retro_Projetor_book_id: Property = Property(name="book_id", type=IntegerType)
Retro_Projetor_title: Property = Property(name="title", type=StringType)
Retro_Projetor_author_name: Property = Property(name="author_name", type=StringType)
Retro_Projetor_ISBN_no: Property = Property(name="ISBN_no", type=StringType)
Retro_Projetor_publisher: Property = Property(name="publisher", type=StringType)
Retro_Projetor_book_qty: Property = Property(name="book_qty", type=IntegerType)
Retro_Projetor.attributes={Retro_Projetor_publisher, Retro_Projetor_ISBN_no, Retro_Projetor_title, Retro_Projetor_book_id, Retro_Projetor_author_name, Retro_Projetor_book_qty}

# Members class attributes and methods
Members_member_id: Property = Property(name="member_id", type=IntegerType)
Members_member_pwd: Property = Property(name="member_pwd", type=StringType)
Members_fname: Property = Property(name="fname", type=StringType)
Members_lname: Property = Property(name="lname", type=StringType)
Members_gender: Property = Property(name="gender", type=StringType)
Members_dob: Property = Property(name="dob", type=StringType)
Members_address: Property = Property(name="address", type=StringType)
Members_cont_no: Property = Property(name="cont_no", type=IntegerType)
Members.attributes={Members_member_id, Members_gender, Members_member_pwd, Members_fname, Members_lname, Members_address, Members_cont_no, Members_dob}

# Quado_Branco class attributes and methods
Quado_Branco_member_id: Property = Property(name="member_id", type=IntegerType)
Quado_Branco_member_pwd: Property = Property(name="member_pwd", type=StringType)
Quado_Branco_fname: Property = Property(name="fname", type=StringType)
Quado_Branco_lname: Property = Property(name="lname", type=StringType)
Quado_Branco_gender: Property = Property(name="gender", type=StringType)
Quado_Branco_dob: Property = Property(name="dob", type=StringType)
Quado_Branco_address: Property = Property(name="address", type=StringType)
Quado_Branco_cont_no: Property = Property(name="cont_no", type=IntegerType)
Quado_Branco.attributes={Quado_Branco_dob, Quado_Branco_member_pwd, Quado_Branco_fname, Quado_Branco_cont_no, Quado_Branco_gender, Quado_Branco_lname, Quado_Branco_address, Quado_Branco_member_id}

# Ar_Condicionado class attributes and methods
Ar_Condicionado_book_id: Property = Property(name="book_id", type=IntegerType)
Ar_Condicionado_member_id: Property = Property(name="member_id", type=IntegerType)
Ar_Condicionado_fine_amount: Property = Property(name="fine_amount", type=IntegerType)
Ar_Condicionado_borrowed_date: Property = Property(name="borrowed_date", type=StringType)
Ar_Condicionado_returned_date: Property = Property(name="returned_date", type=StringType)
Ar_Condicionado.attributes={Ar_Condicionado_book_id, Ar_Condicionado_fine_amount, Ar_Condicionado_borrowed_date, Ar_Condicionado_returned_date, Ar_Condicionado_member_id}

# Borrowed class attributes and methods
Borrowed_borrowed_date: Property = Property(name="borrowed_date", type=StringType)
Borrowed_returned_date: Property = Property(name="returned_date", type=StringType)
Borrowed.attributes={Borrowed_returned_date, Borrowed_borrowed_date}

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
Staff.attributes={Staff_email, Staff_position, Staff_Staff_ID, Staff_fname, Staff_address, Staff_password, Staff_lname, Staff_gender, Staff_contact, Staff_username}

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
        Property(name="books1", type=Retro_Projetor, multiplicity=Multiplicity(0, 9999))
    }
)
Borrowed_Member: BinaryAssociation = BinaryAssociation(
    name="Borrowed_Member",
    ends={
        Property(name="member2", type=Members, multiplicity=Multiplicity(0, 9999)),
        Property(name="borrowed3", type=Borrowed, multiplicity=Multiplicity(0, 9999))
    }
)
Books_Reserved: BinaryAssociation = BinaryAssociation(
    name="Books_Reserved",
    ends={
        Property(name="reserved4", type=Reserved, multiplicity=Multiplicity(0, 9999)),
        Property(name="books5", type=Retro_Projetor, multiplicity=Multiplicity(0, 9999))
    }
)
Reserved_Member: BinaryAssociation = BinaryAssociation(
    name="Reserved_Member",
    ends={
        Property(name="member6", type=Members, multiplicity=Multiplicity(0, 9999)),
        Property(name="reserved7", type=Reserved, multiplicity=Multiplicity(0, 9999))
    }
)
Librarian_Books: BinaryAssociation = BinaryAssociation(
    name="Librarian_Books",
    ends={
        Property(name="books8", type=Retro_Projetor, multiplicity=Multiplicity(0, 9999)),
        Property(name="librarian9", type=Quado_Branco, multiplicity=Multiplicity(0, 9999))
    }
)
Librarian_Fine: BinaryAssociation = BinaryAssociation(
    name="Librarian_Fine",
    ends={
        Property(name="fine10", type=Ar_Condicionado, multiplicity=Multiplicity(0, 9999)),
        Property(name="librarian11", type=Quado_Branco, multiplicity=Multiplicity(0, 9999))
    }
)
Fine_Member: BinaryAssociation = BinaryAssociation(
    name="Fine_Member",
    ends={
        Property(name="member12", type=Members, multiplicity=Multiplicity(1, 1)),
        Property(name="fine13", type=Ar_Condicionado, multiplicity=Multiplicity(0, 9999))
    }
)
Member_Librarian: BinaryAssociation = BinaryAssociation(
    name="Member_Librarian",
    ends={
        Property(name="librarian14", type=Quado_Branco, multiplicity=Multiplicity(0, 9999)),
        Property(name="member15", type=Members, multiplicity=Multiplicity(0, 9999))
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
    name="_09e67711_ca1a_4860_80bb_1d4f1a7ca9a1",
    types={Retro_Projetor, Members, Quado_Branco, Ar_Condicionado, Borrowed, Reserved, Staff, admin, lecturer, Class_},
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
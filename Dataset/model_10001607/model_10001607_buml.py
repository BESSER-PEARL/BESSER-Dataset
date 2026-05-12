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
Admin = Class(name="Admin")
Bidder = Class(name="Bidder")
Biddee = Class(name="Biddee")
Bidding = Class(name="Bidding")
HasilBidding = Class(name="HasilBidding")

# User class attributes and methods
User_userName: Property = Property(name="userName", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User_nama: Property = Property(name="nama", type=StringType)
User.attributes={User_nama, User_loginStatus, User_userName, User_password}

# Admin class attributes and methods

# Bidder class attributes and methods

# Biddee class attributes and methods
Biddee_statusBiddee: Property = Property(name="statusBiddee", type=StringType)
Biddee.attributes={Biddee_statusBiddee}

# Bidding class attributes and methods
Bidding_biddee: Property = Property(name="biddee", type=StringType)
Bidding_bidder: Property = Property(name="bidder", type=StringType)
Bidding_statusBidding: Property = Property(name="statusBidding", type=StringType)
Bidding_jabatan: Property = Property(name="jabatan", type=StringType)
Bidding_notulensi: Property = Property(name="notulensi", type=StringType)
Bidding_nilai: Property = Property(name="nilai", type=IntegerType)
Bidding_catatanBidder: Property = Property(name="catatanBidder", type=StringType)
Bidding_berkas: Property = Property(name="berkas", type=StringType)
Bidding.attributes={Bidding_biddee, Bidding_catatanBidder, Bidding_nilai, Bidding_notulensi, Bidding_bidder, Bidding_berkas, Bidding_jabatan, Bidding_statusBidding}

# HasilBidding class attributes and methods

# Relationships
Admin_Biddee: BinaryAssociation = BinaryAssociation(
    name="Admin_Biddee",
    ends={
        Property(name="ubah_status7", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="biddee6", type=Biddee, multiplicity=Multiplicity(1, 9999))
    }
)
Bidder_Bidding: BinaryAssociation = BinaryAssociation(
    name="Bidder_Bidding",
    ends={
        Property(name="buat_catatan8", type=Bidding, multiplicity=Multiplicity(1, 9999)),
        Property(name="bidder29", type=Bidder, multiplicity=Multiplicity(1, 9999))
    }
)
Bidder_Bidding2: BinaryAssociation = BinaryAssociation(
    name="Bidder_Bidding2",
    ends={
        Property(name="edit_nilai10", type=Bidding, multiplicity=Multiplicity(1, 9999)),
        Property(name="Bidder_Bidding2_111", type=Bidder, multiplicity=Multiplicity(1, 9999))
    }
)
User_HasilBidding: BinaryAssociation = BinaryAssociation(
    name="User_HasilBidding",
    ends={
        Property(name="hasilBidding12", type=HasilBidding, multiplicity=Multiplicity(0, 9999)),
        Property(name="melihat13", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
HasilBidding_Bidding: BinaryAssociation = BinaryAssociation(
    name="HasilBidding_Bidding",
    ends={
        Property(name="bidding0", type=Bidding, multiplicity=Multiplicity(1, 9999)),
        Property(name="hasilBidding1", type=HasilBidding, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Bidding: BinaryAssociation = BinaryAssociation(
    name="Admin_Bidding",
    ends={
        Property(name="bidding2", type=Bidding, multiplicity=Multiplicity(1, 9999)),
        Property(name="CRUD_bidding3", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Bidding_Biddee: BinaryAssociation = BinaryAssociation(
    name="Bidding_Biddee",
    ends={
        Property(name="daftar4", type=Biddee, multiplicity=Multiplicity(0, 9999)),
        Property(name="bidding5", type=Bidding, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_J1VwkMnUEeeM1PgT03_3Vg",
    types={User, Admin, Bidder, Biddee, Bidding, HasilBidding},
    associations={Admin_Biddee, Bidder_Bidding, Bidder_Bidding2, User_HasilBidding, HasilBidding_Bidding, Admin_Bidding, Bidding_Biddee},
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
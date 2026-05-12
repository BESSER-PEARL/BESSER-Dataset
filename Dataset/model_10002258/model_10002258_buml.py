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
news = Class(name="news")
produk = Class(name="produk")
our_costumer___major = Class(name="our_costumer___major")
news_Interface = Class(name="news_Interface")
our_costumer_Interface = Class(name="our_costumer_Interface")
pengunjung_website = Class(name="pengunjung_website")
admin = Class(name="admin")
produk_Interface = Class(name="produk_Interface")
register_admin = Class(name="register_admin")
login_admin = Class(name="login_admin")
admin_Actor = Class(name="admin_Actor")
Pengunjung_Website_Actor = Class(name="Pengunjung_Website_Actor")
halaman_admin_produk_UseCase = Class(name="halaman_admin_produk_UseCase")
halaman_admin_register_UseCase = Class(name="halaman_admin_register_UseCase")
halaman_admin_produk_UseCase1 = Class(name="halaman_admin_produk_UseCase1")
halaman_admin_major_sales_record_UseCase = Class(name="halaman_admin_major_sales_record_UseCase")
halaman_admin_news_UseCase = Class(name="halaman_admin_news_UseCase")
halaman_admin_register_UseCase1 = Class(name="halaman_admin_register_UseCase1")
halaman_admin_register_UseCase2 = Class(name="halaman_admin_register_UseCase2")
halaman_admin_produk_UseCase2 = Class(name="halaman_admin_produk_UseCase2")
halaman_admin_news_UseCase1 = Class(name="halaman_admin_news_UseCase1")
halaman_admin_news_UseCase2 = Class(name="halaman_admin_news_UseCase2")
halaman_admin_major_sales_record_UseCase1 = Class(name="halaman_admin_major_sales_record_UseCase1")
halaman_admin_login_UseCase = Class(name="halaman_admin_login_UseCase")
Halaman_Publikasi__produk_UseCase = Class(name="Halaman_Publikasi__produk_UseCase")
Halaman_Publikasi__news_UseCase = Class(name="Halaman_Publikasi__news_UseCase")
Halaman_Publikasi__major_sales_record_UseCase = Class(name="Halaman_Publikasi__major_sales_record_UseCase")

# news class attributes and methods
news_id_news: Property = Property(name="id_news", type=IntegerType)
news_foto_news: Property = Property(name="foto_news", type=StringType)
news_judul_news: Property = Property(name="judul_news", type=StringType)
news_isi_news: Property = Property(name="isi_news", type=StringType)
news.attributes={news_isi_news, news_judul_news, news_id_news, news_foto_news}

# produk class attributes and methods
produk_id_produk: Property = Property(name="id_produk", type=IntegerType)
produk_website: Property = Property(name="website", type=StringType)
produk_foto_produk: Property = Property(name="foto_produk", type=StringType)
produk.attributes={produk_website, produk_id_produk, produk_foto_produk}

# our_costumer___major class attributes and methods
our_costumer___major_id_major: Property = Property(name="id_major", type=IntegerType)
our_costumer___major_logo_major: Property = Property(name="logo_major", type=StringType)
our_costumer___major.attributes={our_costumer___major_id_major, our_costumer___major_logo_major}

# news_Interface class attributes and methods

# our_costumer_Interface class attributes and methods

# pengunjung_website class attributes and methods

# admin class attributes and methods

# produk_Interface class attributes and methods

# register_admin class attributes and methods
register_admin_id_user: Property = Property(name="id_user", type=IntegerType)
register_admin_nama_lengkap: Property = Property(name="nama_lengkap", type=StringType)
register_admin_nik: Property = Property(name="nik", type=StringType)
register_admin_email: Property = Property(name="email", type=StringType)
register_admin_password: Property = Property(name="password", type=StringType)
register_admin.attributes={register_admin_id_user, register_admin_nik, register_admin_email, register_admin_password, register_admin_nama_lengkap}

# login_admin class attributes and methods
login_admin_email: Property = Property(name="email", type=StringType)
login_admin_password: Property = Property(name="password", type=StringType)
login_admin.attributes={login_admin_password, login_admin_email}

# admin_Actor class attributes and methods

# Pengunjung_Website_Actor class attributes and methods

# halaman_admin_produk_UseCase class attributes and methods

# halaman_admin_register_UseCase class attributes and methods

# halaman_admin_produk_UseCase1 class attributes and methods

# halaman_admin_major_sales_record_UseCase class attributes and methods

# halaman_admin_news_UseCase class attributes and methods

# halaman_admin_register_UseCase1 class attributes and methods

# halaman_admin_register_UseCase2 class attributes and methods

# halaman_admin_produk_UseCase2 class attributes and methods

# halaman_admin_news_UseCase1 class attributes and methods

# halaman_admin_news_UseCase2 class attributes and methods

# halaman_admin_major_sales_record_UseCase1 class attributes and methods

# halaman_admin_login_UseCase class attributes and methods

# Halaman_Publikasi__produk_UseCase class attributes and methods

# Halaman_Publikasi__news_UseCase class attributes and methods

# Halaman_Publikasi__major_sales_record_UseCase class attributes and methods

# Relationships
admin_our_costumer___major: BinaryAssociation = BinaryAssociation(
    name="admin_our_costumer___major",
    ends={
        Property(name="our_costumer___major0", type=our_costumer___major, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin1", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_produk: BinaryAssociation = BinaryAssociation(
    name="admin_produk",
    ends={
        Property(name="produk2", type=produk, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin3", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_news: BinaryAssociation = BinaryAssociation(
    name="admin_news",
    ends={
        Property(name="news4", type=news, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin5", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_our_costumer: BinaryAssociation = BinaryAssociation(
    name="admin_our_costumer",
    ends={
        Property(name="our_costumer6", type=our_costumer_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin7", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_news2: BinaryAssociation = BinaryAssociation(
    name="admin_news2",
    ends={
        Property(name="news8", type=news_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin9", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_Interface: BinaryAssociation = BinaryAssociation(
    name="admin_Interface",
    ends={
        Property(name="interface10", type=produk_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin11", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
pengunjung_website_our_costumer: BinaryAssociation = BinaryAssociation(
    name="pengunjung_website_our_costumer",
    ends={
        Property(name="our_costumer12", type=our_costumer_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="pengunjung_website13", type=pengunjung_website, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_website_news: BinaryAssociation = BinaryAssociation(
    name="pengunjung_website_news",
    ends={
        Property(name="news14", type=news_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="pengunjung_website15", type=pengunjung_website, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_website_produk: BinaryAssociation = BinaryAssociation(
    name="pengunjung_website_produk",
    ends={
        Property(name="produk16", type=produk_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="pengunjung_website17", type=pengunjung_website, multiplicity=Multiplicity(0, 1))
    }
)
admin_register_admin: BinaryAssociation = BinaryAssociation(
    name="admin_register_admin",
    ends={
        Property(name="register_admin18", type=register_admin, multiplicity=Multiplicity(1, 1)),
        Property(name="admin19", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_login_admin: BinaryAssociation = BinaryAssociation(
    name="admin_login_admin",
    ends={
        Property(name="login_admin20", type=login_admin, multiplicity=Multiplicity(1, 1)),
        Property(name="admin21", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_register: BinaryAssociation = BinaryAssociation(
    name="admin_register",
    ends={
        Property(name="register22", type=halaman_admin_register_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="admin23", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_produk2: BinaryAssociation = BinaryAssociation(
    name="admin_produk2",
    ends={
        Property(name="produk24", type=halaman_admin_produk_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin25", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_register2: BinaryAssociation = BinaryAssociation(
    name="admin_register2",
    ends={
        Property(name="register26", type=halaman_admin_register_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_register3: BinaryAssociation = BinaryAssociation(
    name="admin_register3",
    ends={
        Property(name="register28", type=halaman_admin_register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin29", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login30", type=halaman_admin_login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin31", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_major_sales_record: BinaryAssociation = BinaryAssociation(
    name="admin_major_sales_record",
    ends={
        Property(name="major_sales_record32", type=halaman_admin_major_sales_record_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin33", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_news4: BinaryAssociation = BinaryAssociation(
    name="admin_news4",
    ends={
        Property(name="news40", type=halaman_admin_news_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin41", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_news5: BinaryAssociation = BinaryAssociation(
    name="admin_news5",
    ends={
        Property(name="news42", type=halaman_admin_news_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin43", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_major_sales_record2: BinaryAssociation = BinaryAssociation(
    name="admin_major_sales_record2",
    ends={
        Property(name="major_sales_record44", type=halaman_admin_major_sales_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin45", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_produk5: BinaryAssociation = BinaryAssociation(
    name="admin_produk5",
    ends={
        Property(name="produk46", type=Halaman_Publikasi__produk_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin47", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_news6: BinaryAssociation = BinaryAssociation(
    name="admin_news6",
    ends={
        Property(name="news48", type=Halaman_Publikasi__news_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin49", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_major_sales_record3: BinaryAssociation = BinaryAssociation(
    name="admin_major_sales_record3",
    ends={
        Property(name="major_sales_record50", type=Halaman_Publikasi__major_sales_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin51", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Website_produk: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Website_produk",
    ends={
        Property(name="produk52", type=Halaman_Publikasi__produk_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung_Website53", type=Pengunjung_Website_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Website_news: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Website_news",
    ends={
        Property(name="news54", type=Halaman_Publikasi__news_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung_Website55", type=Pengunjung_Website_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Website_major_sales_record: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Website_major_sales_record",
    ends={
        Property(name="major_sales_record56", type=Halaman_Publikasi__major_sales_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung_Website57", type=Pengunjung_Website_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_produk3: BinaryAssociation = BinaryAssociation(
    name="admin_produk3",
    ends={
        Property(name="produk34", type=halaman_admin_produk_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="admin35", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_produk4: BinaryAssociation = BinaryAssociation(
    name="admin_produk4",
    ends={
        Property(name="produk36", type=halaman_admin_produk_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin37", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_news3: BinaryAssociation = BinaryAssociation(
    name="admin_news3",
    ends={
        Property(name="news38", type=halaman_admin_news_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="admin39", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_zxnC8Fr5EeqK2M3E1LfZ7Q",
    types={news, produk, our_costumer___major, news_Interface, our_costumer_Interface, pengunjung_website, admin, produk_Interface, register_admin, login_admin, admin_Actor, Pengunjung_Website_Actor, halaman_admin_produk_UseCase, halaman_admin_register_UseCase, halaman_admin_produk_UseCase1, halaman_admin_major_sales_record_UseCase, halaman_admin_news_UseCase, halaman_admin_register_UseCase1, halaman_admin_register_UseCase2, halaman_admin_produk_UseCase2, halaman_admin_news_UseCase1, halaman_admin_news_UseCase2, halaman_admin_major_sales_record_UseCase1, halaman_admin_login_UseCase, Halaman_Publikasi__produk_UseCase, Halaman_Publikasi__news_UseCase, Halaman_Publikasi__major_sales_record_UseCase},
    associations={admin_our_costumer___major, admin_produk, admin_news, admin_our_costumer, admin_news2, admin_Interface, pengunjung_website_our_costumer, pengunjung_website_news, pengunjung_website_produk, admin_register_admin, admin_login_admin, admin_register, admin_produk2, admin_register2, admin_register3, admin_login, admin_major_sales_record, admin_news4, admin_news5, admin_major_sales_record2, admin_produk5, admin_news6, admin_major_sales_record3, Pengunjung_Website_produk, Pengunjung_Website_news, Pengunjung_Website_major_sales_record, admin_produk3, admin_produk4, admin_news3},
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
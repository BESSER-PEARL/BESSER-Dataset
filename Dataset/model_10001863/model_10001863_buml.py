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
Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase = Class(name="Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase")
User__Pengunjung__Actor1 = Class(name="User__Pengunjung__Actor1")
Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase = Class(name="Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase")
Situs_Browsing_UseCase = Class(name="Situs_Browsing_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Kelola_data_website_UseCase = Class(name="Kelola_data_website_UseCase")
Menambah_membuat_data_website_UseCase = Class(name="Menambah_membuat_data_website_UseCase")
Menghapus_data_website_UseCase = Class(name="Menghapus_data_website_UseCase")
Mengedit_data_website_UseCase = Class(name="Mengedit_data_website_UseCase")
Browsing_Situs_UseCase = Class(name="Browsing_Situs_UseCase")
Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase = Class(name="Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase")
Nama_Tumbuh_Tumbuhan_Herbal_UseCase = Class(name="Nama_Tumbuh_Tumbuhan_Herbal_UseCase")
Nama_latinnya_UseCase = Class(name="Nama_latinnya_UseCase")
Jenis_tumbuhan_herbal_UseCase = Class(name="Jenis_tumbuhan_herbal_UseCase")
Asal_daerah_tumbuhan_herbal_UseCase = Class(name="Asal_daerah_tumbuhan_herbal_UseCase")
Kelas_Ordo_tumbuhan_herbal_UseCase = Class(name="Kelas_Ordo_tumbuhan_herbal_UseCase")
Khasiatnya_apa_UseCase = Class(name="Khasiatnya_apa_UseCase")
Dosisnya_UseCase = Class(name="Dosisnya_UseCase")
Cara_pengolahannya_UseCase = Class(name="Cara_pengolahannya_UseCase")
Gambar_tumbuhan_herbalnya_UseCase = Class(name="Gambar_tumbuhan_herbalnya_UseCase")
Obat__Produk_jadi__UseCase = Class(name="Obat__Produk_jadi__UseCase")
Fitur_Pencarian_berdsarkan_penyakit_UseCase = Class(name="Fitur_Pencarian_berdsarkan_penyakit_UseCase")
Forum_diskusi_UseCase = Class(name="Forum_diskusi_UseCase")
User__Pengunjung__Actor = Class(name="User__Pengunjung__Actor")
Login_Website = Class(name="Login_Website")
Browsing_Website = Class(name="Browsing_Website")
Pengelola_Website = Class(name="Pengelola_Website")
Menu_Halaman_Website = Class(name="Menu_Halaman_Website")
Nama_Tumbuh_Tumbuhan_Herbal = Class(name="Nama_Tumbuh_Tumbuhan_Herbal")
Admin_Website_Actor = Class(name="Admin_Website_Actor")
Website_Informasi_Tumbuhan_Herbal_UseCase = Class(name="Website_Informasi_Tumbuhan_Herbal_UseCase")
Halaman_Utama_Website_UseCase = Class(name="Halaman_Utama_Website_UseCase")
Fitur_Fitur_Pada_Website_UseCase = Class(name="Fitur_Fitur_Pada_Website_UseCase")
Fitur_Pencarian_Berdasarkan_Kategori_Penyakit_UseCase = Class(name="Fitur_Pencarian_Berdasarkan_Kategori_Penyakit_UseCase")
Fitur_Kolom_Diskusi_UseCase = Class(name="Fitur_Kolom_Diskusi_UseCase")
Fitur_Sosial_Media_Sharing_UseCase = Class(name="Fitur_Sosial_Media_Sharing_UseCase")
Fitur_Pencarian_Tumbuhan_Herbal_UseCase = Class(name="Fitur_Pencarian_Tumbuhan_Herbal_UseCase")
Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase = Class(name="Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase")
Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase = Class(name="Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase")
Nama_Tumbuhannya_UseCase = Class(name="Nama_Tumbuhannya_UseCase")
Nama_Latinnya_UseCase = Class(name="Nama_Latinnya_UseCase")
Jenis_Tumbuhan_Herbalnya_UseCase = Class(name="Jenis_Tumbuhan_Herbalnya_UseCase")
Asal_Tumbuhan_Herbalnya_UseCase = Class(name="Asal_Tumbuhan_Herbalnya_UseCase")
Khasiat_tumbuhan_Herbalnya_UseCase = Class(name="Khasiat_tumbuhan_Herbalnya_UseCase")
Cara_Pengolahannya_UseCase = Class(name="Cara_Pengolahannya_UseCase")
Kelas_Ordo_Tumbuhan_Herbal_UseCase = Class(name="Kelas_Ordo_Tumbuhan_Herbal_UseCase")
Gambar_Tumbuhan_Herbalnya_UseCase = Class(name="Gambar_Tumbuhan_Herbalnya_UseCase")
Obat__Produk_Jadinya__UseCase = Class(name="Obat__Produk_Jadinya__UseCase")
Dosisnya_UseCase1 = Class(name="Dosisnya_UseCase1")
Mengedit_Profil_Dan_Data_Website_UseCase = Class(name="Mengedit_Profil_Dan_Data_Website_UseCase")
Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase = Class(name="Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase")
Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase = Class(name="Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase")
Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase = Class(name="Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase")

# Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase class attributes and methods

# User__Pengunjung__Actor1 class attributes and methods

# Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase class attributes and methods

# Situs_Browsing_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Kelola_data_website_UseCase class attributes and methods

# Menambah_membuat_data_website_UseCase class attributes and methods

# Menghapus_data_website_UseCase class attributes and methods

# Mengedit_data_website_UseCase class attributes and methods

# Browsing_Situs_UseCase class attributes and methods

# Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase class attributes and methods

# Nama_Tumbuh_Tumbuhan_Herbal_UseCase class attributes and methods

# Nama_latinnya_UseCase class attributes and methods

# Jenis_tumbuhan_herbal_UseCase class attributes and methods

# Asal_daerah_tumbuhan_herbal_UseCase class attributes and methods

# Kelas_Ordo_tumbuhan_herbal_UseCase class attributes and methods

# Khasiatnya_apa_UseCase class attributes and methods

# Dosisnya_UseCase class attributes and methods

# Cara_pengolahannya_UseCase class attributes and methods

# Gambar_tumbuhan_herbalnya_UseCase class attributes and methods

# Obat__Produk_jadi__UseCase class attributes and methods

# Fitur_Pencarian_berdsarkan_penyakit_UseCase class attributes and methods

# Forum_diskusi_UseCase class attributes and methods

# User__Pengunjung__Actor class attributes and methods

# Login_Website class attributes and methods
Login_Website_attribute: Property = Property(name="attribute", type=Admin_Actor)
Login_Website.attributes={Login_Website_attribute}

# Browsing_Website class attributes and methods
Browsing_Website_attribute: Property = Property(name="attribute", type=User__Pengunjung__Actor)
Browsing_Website.attributes={Browsing_Website_attribute}

# Pengelola_Website class attributes and methods
Pengelola_Website_attribute: Property = Property(name="attribute", type=Kelola_data_website_UseCase)
Pengelola_Website_attribute2: Property = Property(name="attribute2", type=Menambah_membuat_data_website_UseCase)
Pengelola_Website_attribute3: Property = Property(name="attribute3", type=Menghapus_data_website_UseCase)
Pengelola_Website_attribute4: Property = Property(name="attribute4", type=Mengedit_data_website_UseCase)
Pengelola_Website.attributes={Pengelola_Website_attribute, Pengelola_Website_attribute4, Pengelola_Website_attribute3, Pengelola_Website_attribute2}

# Menu_Halaman_Website class attributes and methods
Menu_Halaman_Website_attribute: Property = Property(name="attribute", type=Forum_diskusi_UseCase)
Menu_Halaman_Website_attribute2: Property = Property(name="attribute2", type=Fitur_Pencarian_berdsarkan_penyakit_UseCase)
Menu_Halaman_Website.attributes={Menu_Halaman_Website_attribute2, Menu_Halaman_Website_attribute}

# Nama_Tumbuh_Tumbuhan_Herbal class attributes and methods
Nama_Tumbuh_Tumbuhan_Herbal_attribute: Property = Property(name="attribute", type=Nama_latinnya_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute2: Property = Property(name="attribute2", type=Jenis_tumbuhan_herbal_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute3: Property = Property(name="attribute3", type=Asal_daerah_tumbuhan_herbal_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute4: Property = Property(name="attribute4", type=Kelas_Ordo_tumbuhan_herbal_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute5: Property = Property(name="attribute5", type=Khasiatnya_apa_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute6: Property = Property(name="attribute6", type=Dosisnya_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute7: Property = Property(name="attribute7", type=Cara_pengolahannya_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute8: Property = Property(name="attribute8", type=Gambar_tumbuhan_herbalnya_UseCase)
Nama_Tumbuh_Tumbuhan_Herbal_attribute9: Property = Property(name="attribute9", type=Obat__Produk_jadi__UseCase)
Nama_Tumbuh_Tumbuhan_Herbal.attributes={Nama_Tumbuh_Tumbuhan_Herbal_attribute2, Nama_Tumbuh_Tumbuhan_Herbal_attribute5, Nama_Tumbuh_Tumbuhan_Herbal_attribute3, Nama_Tumbuh_Tumbuhan_Herbal_attribute7, Nama_Tumbuh_Tumbuhan_Herbal_attribute6, Nama_Tumbuh_Tumbuhan_Herbal_attribute9, Nama_Tumbuh_Tumbuhan_Herbal_attribute8, Nama_Tumbuh_Tumbuhan_Herbal_attribute, Nama_Tumbuh_Tumbuhan_Herbal_attribute4}

# Admin_Website_Actor class attributes and methods

# Website_Informasi_Tumbuhan_Herbal_UseCase class attributes and methods

# Halaman_Utama_Website_UseCase class attributes and methods

# Fitur_Fitur_Pada_Website_UseCase class attributes and methods

# Fitur_Pencarian_Berdasarkan_Kategori_Penyakit_UseCase class attributes and methods

# Fitur_Kolom_Diskusi_UseCase class attributes and methods

# Fitur_Sosial_Media_Sharing_UseCase class attributes and methods

# Fitur_Pencarian_Tumbuhan_Herbal_UseCase class attributes and methods

# Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase class attributes and methods

# Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase class attributes and methods

# Nama_Tumbuhannya_UseCase class attributes and methods

# Nama_Latinnya_UseCase class attributes and methods

# Jenis_Tumbuhan_Herbalnya_UseCase class attributes and methods

# Asal_Tumbuhan_Herbalnya_UseCase class attributes and methods

# Khasiat_tumbuhan_Herbalnya_UseCase class attributes and methods

# Cara_Pengolahannya_UseCase class attributes and methods

# Kelas_Ordo_Tumbuhan_Herbal_UseCase class attributes and methods

# Gambar_Tumbuhan_Herbalnya_UseCase class attributes and methods

# Obat__Produk_Jadinya__UseCase class attributes and methods

# Dosisnya_UseCase1 class attributes and methods

# Mengedit_Profil_Dan_Data_Website_UseCase class attributes and methods

# Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase class attributes and methods

# Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase class attributes and methods

# Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase class attributes and methods

# Relationships
Admin_Kelola_data_website: BinaryAssociation = BinaryAssociation(
    name="Admin_Kelola_data_website",
    ends={
        Property(name="admin0", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="kelola_data_website1", type=Kelola_data_website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Menambah_membuat_data_website: BinaryAssociation = BinaryAssociation(
    name="Admin_Menambah_membuat_data_website",
    ends={
        Property(name="admin2", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="menambah_membuat_data_website3", type=Menambah_membuat_data_website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Mengedit_data_website: BinaryAssociation = BinaryAssociation(
    name="Admin_Mengedit_data_website",
    ends={
        Property(name="admin4", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengedit_data_website5", type=Mengedit_data_website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Menghapus_data_website: BinaryAssociation = BinaryAssociation(
    name="Admin_Menghapus_data_website",
    ends={
        Property(name="admin6", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="menghapus_data_website7", type=Menghapus_data_website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User__Pengunjung__Browsing_Situs: BinaryAssociation = BinaryAssociation(
    name="User__Pengunjung__Browsing_Situs",
    ends={
        Property(name="user__Pengunjung_8", type=User__Pengunjung__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="browsing_Situs9", type=Browsing_Situs_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Forum_diskusi: BinaryAssociation = BinaryAssociation(
    name="Admin_Forum_diskusi",
    ends={
        Property(name="admin10", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="forum_diskusi11", type=Forum_diskusi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Website_Mengedit_Profil_Dan_Data_Website: BinaryAssociation = BinaryAssociation(
    name="Admin_Website_Mengedit_Profil_Dan_Data_Website",
    ends={
        Property(name="admin_Website12", type=Admin_Website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengedit_Profil_Dan_Data_Website13", type=Mengedit_Profil_Dan_Data_Website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Website_Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin: BinaryAssociation = BinaryAssociation(
    name="Admin_Website_Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin",
    ends={
        Property(name="admin_Website14", type=Admin_Website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin15", type=Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_Fitur_Fitur_Pada_Website: BinaryAssociation = BinaryAssociation(
    name="Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_Fitur_Fitur_Pada_Website",
    ends={
        Property(name="fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin16", type=Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Fitur_Pada_Website17", type=Fitur_Fitur_Pada_Website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Mengedit_Profil_Dan_Data_Website_Website_Informasi_Tumbuhan_Herbal: BinaryAssociation = BinaryAssociation(
    name="Mengedit_Profil_Dan_Data_Website_Website_Informasi_Tumbuhan_Herbal",
    ends={
        Property(name="mengedit_Profil_Dan_Data_Website18", type=Mengedit_Profil_Dan_Data_Website_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="website_Informasi_Tumbuhan_Herbal19", type=Website_Informasi_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Website_Informasi_Tumbuhan_Herbal_Halaman_Utama_Website: BinaryAssociation = BinaryAssociation(
    name="Website_Informasi_Tumbuhan_Herbal_Halaman_Utama_Website",
    ends={
        Property(name="website_Informasi_Tumbuhan_Herbal20", type=Website_Informasi_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="halaman_Utama_Website21", type=Halaman_Utama_Website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Halaman_Utama_Website_Fitur_Fitur_Pada_Website: BinaryAssociation = BinaryAssociation(
    name="Halaman_Utama_Website_Fitur_Fitur_Pada_Website",
    ends={
        Property(name="halaman_Utama_Website22", type=Halaman_Utama_Website_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Fitur_Pada_Website23", type=Fitur_Fitur_Pada_Website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Menambah_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal: BinaryAssociation = BinaryAssociation(
    name="Menambah_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal",
    ends={
        Property(name="menambah_Data_Tumbuh_Tumbuhan_Herbal24", type=Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal25", type=Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Mengedit_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal: BinaryAssociation = BinaryAssociation(
    name="Mengedit_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal",
    ends={
        Property(name="mengedit_Data_Tumbuh_Tumbuhan_Herbal26", type=Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal27", type=Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Menghapus_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal: BinaryAssociation = BinaryAssociation(
    name="Menghapus_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal",
    ends={
        Property(name="menghapus_Data_Tumbuh_Tumbuhan_Herbal28", type=Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal29", type=Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_Fitur_Fitur_Pada_Website: BinaryAssociation = BinaryAssociation(
    name="Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_Fitur_Fitur_Pada_Website",
    ends={
        Property(name="fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung30", type=Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="fitur_Fitur_Pada_Website31", type=Fitur_Fitur_Pada_Website_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User__Pengunjung__Situs_Browsing: BinaryAssociation = BinaryAssociation(
    name="User__Pengunjung__Situs_Browsing",
    ends={
        Property(name="user__Pengunjung_32", type=User__Pengunjung__Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="situs_Browsing33", type=Situs_Browsing_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_a67yIIKqEeqWAK1R3DAmBw",
    types={Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase, User__Pengunjung__Actor1, Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase, Situs_Browsing_UseCase, Admin_Actor, Kelola_data_website_UseCase, Menambah_membuat_data_website_UseCase, Menghapus_data_website_UseCase, Mengedit_data_website_UseCase, Browsing_Situs_UseCase, Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase, Nama_Tumbuh_Tumbuhan_Herbal_UseCase, Nama_latinnya_UseCase, Jenis_tumbuhan_herbal_UseCase, Asal_daerah_tumbuhan_herbal_UseCase, Kelas_Ordo_tumbuhan_herbal_UseCase, Khasiatnya_apa_UseCase, Dosisnya_UseCase, Cara_pengolahannya_UseCase, Gambar_tumbuhan_herbalnya_UseCase, Obat__Produk_jadi__UseCase, Fitur_Pencarian_berdsarkan_penyakit_UseCase, Forum_diskusi_UseCase, User__Pengunjung__Actor, Login_Website, Browsing_Website, Pengelola_Website, Menu_Halaman_Website, Nama_Tumbuh_Tumbuhan_Herbal, Admin_Website_Actor, Website_Informasi_Tumbuhan_Herbal_UseCase, Halaman_Utama_Website_UseCase, Fitur_Fitur_Pada_Website_UseCase, Fitur_Pencarian_Berdasarkan_Kategori_Penyakit_UseCase, Fitur_Kolom_Diskusi_UseCase, Fitur_Sosial_Media_Sharing_UseCase, Fitur_Pencarian_Tumbuhan_Herbal_UseCase, Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase, Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase, Nama_Tumbuhannya_UseCase, Nama_Latinnya_UseCase, Jenis_Tumbuhan_Herbalnya_UseCase, Asal_Tumbuhan_Herbalnya_UseCase, Khasiat_tumbuhan_Herbalnya_UseCase, Cara_Pengolahannya_UseCase, Kelas_Ordo_Tumbuhan_Herbal_UseCase, Gambar_Tumbuhan_Herbalnya_UseCase, Obat__Produk_Jadinya__UseCase, Dosisnya_UseCase1, Mengedit_Profil_Dan_Data_Website_UseCase, Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase, Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase, Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase},
    associations={Admin_Kelola_data_website, Admin_Menambah_membuat_data_website, Admin_Mengedit_data_website, Admin_Menghapus_data_website, User__Pengunjung__Browsing_Situs, Admin_Forum_diskusi, Admin_Website_Mengedit_Profil_Dan_Data_Website, Admin_Website_Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin, Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_Fitur_Fitur_Pada_Website, Mengedit_Profil_Dan_Data_Website_Website_Informasi_Tumbuhan_Herbal, Website_Informasi_Tumbuhan_Herbal_Halaman_Utama_Website, Halaman_Utama_Website_Fitur_Fitur_Pada_Website, Menambah_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal, Mengedit_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal, Menghapus_Data_Tumbuh_Tumbuhan_Herbal_Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal, Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_Fitur_Fitur_Pada_Website, User__Pengunjung__Situs_Browsing},
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
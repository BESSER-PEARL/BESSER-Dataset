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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Pengunjung_Actor = Class(name="Pengunjung_Actor")
Melihat_Katalog_Kamar_UseCase = Class(name="Melihat_Katalog_Kamar_UseCase")
Pemesan_Actor = Class(name="Pemesan_Actor")
Admin_Actor = Class(name="Admin_Actor")
Melakukan_reservasi_kamar_UseCase = Class(name="Melakukan_reservasi_kamar_UseCase")
Mengirim_e_bukti_Bayar_UseCase = Class(name="Mengirim_e_bukti_Bayar_UseCase")
Kirim_e_booking_email_UseCase = Class(name="Kirim_e_booking_email_UseCase")
Melakukan_pembayaran_UseCase = Class(name="Melakukan_pembayaran_UseCase")
Cancel_Pemesanan_UseCase = Class(name="Cancel_Pemesanan_UseCase")
Check_in_UseCase = Class(name="Check_in_UseCase")
Check_Out_UseCase = Class(name="Check_Out_UseCase")
Denda_UseCase = Class(name="Denda_UseCase")
Kamar_Deluxe_UseCase = Class(name="Kamar_Deluxe_UseCase")
Kamar_Keluarga_UseCase = Class(name="Kamar_Keluarga_UseCase")
Kamar_Standard_UseCase = Class(name="Kamar_Standard_UseCase")
Login_UseCase = Class(name="Login_UseCase")
Register_UseCase = Class(name="Register_UseCase")
Pemesan = Class(name="Pemesan")
Admin = Class(name="Admin")
hjb_Interface = Class(name="hjb_Interface")
Kamar = Class(name="Kamar")
ReservasiKamar = Class(name="ReservasiKamar")
Pembayaran = Class(name="Pembayaran")
Denda = Class(name="Denda")

# Pengunjung_Actor class attributes and methods

# Melihat_Katalog_Kamar_UseCase class attributes and methods

# Pemesan_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Melakukan_reservasi_kamar_UseCase class attributes and methods

# Mengirim_e_bukti_Bayar_UseCase class attributes and methods

# Kirim_e_booking_email_UseCase class attributes and methods

# Melakukan_pembayaran_UseCase class attributes and methods

# Cancel_Pemesanan_UseCase class attributes and methods

# Check_in_UseCase class attributes and methods

# Check_Out_UseCase class attributes and methods

# Denda_UseCase class attributes and methods

# Kamar_Deluxe_UseCase class attributes and methods

# Kamar_Keluarga_UseCase class attributes and methods

# Kamar_Standard_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# Register_UseCase class attributes and methods

# Pemesan class attributes and methods
Pemesan_NIK: Property = Property(name="NIK", type=IntegerType)
Pemesan_Nama: Property = Property(name="Nama", type=StringType)
Pemesan_Alamat: Property = Property(name="Alamat", type=StringType)
Pemesan_Emai: Property = Property(name="Emai", type=StringType)
Pemesan_username: Property = Property(name="username", type=StringType)
Pemesan_password: Property = Property(name="password", type=StringType)
Pemesan_phone_number: Property = Property(name="phone_number", type=StringType)
Pemesan.attributes={Pemesan_Emai, Pemesan_phone_number, Pemesan_password, Pemesan_username, Pemesan_Nama, Pemesan_NIK, Pemesan_Alamat}

# Admin class attributes and methods
Admin_ID_admin: Property = Property(name="ID_admin", type=IntegerType)
Admin_username: Property = Property(name="username", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin_insertData: Property = Property(name="insertData", type=StringType)
Admin_attribute: Property = Property(name="attribute", type=StringType)
Admin.attributes={Admin_attribute, Admin_ID_admin, Admin_password, Admin_insertData, Admin_username}

# hjb_Interface class attributes and methods

# Kamar class attributes and methods
Kamar__attr: Property = Property(name="_attr", type=StringType)
Kamar_no_kamar: Property = Property(name="no_kamar", type=IntegerType)
Kamar_tipe: Property = Property(name="tipe", type=StringType)
Kamar_status: Property = Property(name="status", type=StringType)
Kamar_jumlah_bed: Property = Property(name="jumlah_bed", type=IntegerType)
Kamar.attributes={Kamar_jumlah_bed, Kamar__attr, Kamar_no_kamar, Kamar_tipe, Kamar_status}

# ReservasiKamar class attributes and methods
ReservasiKamar_ID_Reservasi: Property = Property(name="ID_Reservasi", type=IntegerType)
ReservasiKamar_NIK: Property = Property(name="NIK", type=IntegerType)
ReservasiKamar_tgl_start_booking: Property = Property(name="tgl_start_booking", type=StringType)
ReservasiKamar_tgl_end_booking: Property = Property(name="tgl_end_booking", type=StringType)
ReservasiKamar_no_kamar: Property = Property(name="no_kamar", type=IntegerType)
ReservasiKamar_ID_admin: Property = Property(name="ID_admin", type=IntegerType)
ReservasiKamar_ID_pembayaran: Property = Property(name="ID_pembayaran", type=IntegerType)
ReservasiKamar.attributes={ReservasiKamar_ID_Reservasi, ReservasiKamar_NIK, ReservasiKamar_ID_pembayaran, ReservasiKamar_ID_admin, ReservasiKamar_tgl_end_booking, ReservasiKamar_tgl_start_booking, ReservasiKamar_no_kamar}

# Pembayaran class attributes and methods
Pembayaran_ID_Pembayaran: Property = Property(name="ID_Pembayaran", type=IntegerType)
Pembayaran_ID_Reservasi: Property = Property(name="ID_Reservasi", type=IntegerType)
Pembayaran_jumlah: Property = Property(name="jumlah", type=IntegerType)
Pembayaran_deadline_bayar: Property = Property(name="deadline_bayar", type=StringType)
Pembayaran_status: Property = Property(name="status", type=StringType)
Pembayaran.attributes={Pembayaran_deadline_bayar, Pembayaran_status, Pembayaran_ID_Reservasi, Pembayaran_jumlah, Pembayaran_ID_Pembayaran}

# Denda class attributes and methods
Denda_ID_Denda: Property = Property(name="ID_Denda", type=IntegerType)
Denda_jumlah: Property = Property(name="jumlah", type=IntegerType)
Denda_keterangan: Property = Property(name="keterangan", type=StringType)
Denda_ID_Reservasi: Property = Property(name="ID_Reservasi", type=IntegerType)
Denda.attributes={Denda_jumlah, Denda_ID_Reservasi, Denda_ID_Denda, Denda_keterangan}

# Relationships
Pengunjung_UseCase: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_UseCase",
    ends={
        Property(name="Melihat_Katalog_Kamar0", type=Melihat_Katalog_Kamar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung1", type=Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemesan_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Pemesan_UseCase2",
    ends={
        Property(name="useCase22", type=Melihat_Katalog_Kamar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemesan3", type=Pemesan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase3",
    ends={
        Property(name="useCase34", type=Mengirim_e_bukti_Bayar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Memasukkan_data_identitas: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Memasukkan_data_identitas",
    ends={
        Property(name="memasukkan_data_identitas6", type=Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung7", type=Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemesan_Melakukan_reservasi_kamar: BinaryAssociation = BinaryAssociation(
    name="Pemesan_Melakukan_reservasi_kamar",
    ends={
        Property(name="melakukan_reservasi_kamar8", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemesan9", type=Pemesan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Melakukan_reservasi_kamar_Melakukan_pembayaran: BinaryAssociation = BinaryAssociation(
    name="Melakukan_reservasi_kamar_Melakukan_pembayaran",
    ends={
        Property(name="melakukan_pembayaran10", type=Melakukan_pembayaran_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_reservasi_kamar11", type=Melakukan_reservasi_kamar_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Melakukan_reservasi_kamar_Mengirim_e_bukti_Bayar: BinaryAssociation = BinaryAssociation(
    name="Melakukan_reservasi_kamar_Mengirim_e_bukti_Bayar",
    ends={
        Property(name="mengirim_e_bukti_Bayar12", type=Mengirim_e_bukti_Bayar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_reservasi_kamar13", type=Melakukan_reservasi_kamar_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Kirim_e_booking_email: BinaryAssociation = BinaryAssociation(
    name="Admin_Kirim_e_booking_email",
    ends={
        Property(name="kirim_e_booking_email14", type=Kirim_e_booking_email_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Check_Out: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Check_Out",
    ends={
        Property(name="check_Out16", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung17", type=Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemesan_Check_in: BinaryAssociation = BinaryAssociation(
    name="Pemesan_Check_in",
    ends={
        Property(name="check_in18", type=Check_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemesan19", type=Pemesan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_Check_in: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_Check_in",
    ends={
        Property(name="check_in20", type=Check_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung21", type=Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemesan_Check_Out: BinaryAssociation = BinaryAssociation(
    name="Pemesan_Check_Out",
    ends={
        Property(name="check_Out22", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemesan23", type=Pemesan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemesan_ReservasiKamar: BinaryAssociation = BinaryAssociation(
    name="Pemesan_ReservasiKamar",
    ends={
        Property(name="reservasiKamar24", type=ReservasiKamar, multiplicity=Multiplicity(1, 9999)),
        Property(name="pemesan25", type=Pemesan, multiplicity=Multiplicity(1, 1))
    }
)
ReservasiKamar_Admin: BinaryAssociation = BinaryAssociation(
    name="ReservasiKamar_Admin",
    ends={
        Property(name="admin26", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="reservasiKamar27", type=ReservasiKamar, multiplicity=Multiplicity(1, 9999))
    }
)
Kamar_ReservasiKamar: BinaryAssociation = BinaryAssociation(
    name="Kamar_ReservasiKamar",
    ends={
        Property(name="reservasiKamar28", type=ReservasiKamar, multiplicity=Multiplicity(0, 1)),
        Property(name="kamar29", type=Kamar, multiplicity=Multiplicity(0, 1))
    }
)
Denda_ReservasiKamar: BinaryAssociation = BinaryAssociation(
    name="Denda_ReservasiKamar",
    ends={
        Property(name="reservasiKamar30", type=ReservasiKamar, multiplicity=Multiplicity(1, 1)),
        Property(name="denda31", type=Denda, multiplicity=Multiplicity(0, 9999))
    }
)
Pembayaran_ReservasiKamar: BinaryAssociation = BinaryAssociation(
    name="Pembayaran_ReservasiKamar",
    ends={
        Property(name="reservasiKamar32", type=ReservasiKamar, multiplicity=Multiplicity(1, 1)),
        Property(name="pembayaran33", type=Pembayaran, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZOfW4C_GEeqqcaoAsxFIeg",
    types={Pengunjung_Actor, Melihat_Katalog_Kamar_UseCase, Pemesan_Actor, Admin_Actor, Melakukan_reservasi_kamar_UseCase, Mengirim_e_bukti_Bayar_UseCase, Kirim_e_booking_email_UseCase, Melakukan_pembayaran_UseCase, Cancel_Pemesanan_UseCase, Check_in_UseCase, Check_Out_UseCase, Denda_UseCase, Kamar_Deluxe_UseCase, Kamar_Keluarga_UseCase, Kamar_Standard_UseCase, Login_UseCase, Register_UseCase, Pemesan, Admin, hjb_Interface, Kamar, ReservasiKamar, Pembayaran, Denda, Enumeration_},
    associations={Pengunjung_UseCase, Pemesan_UseCase2, Admin_UseCase3, Pengunjung_Memasukkan_data_identitas, Pemesan_Melakukan_reservasi_kamar, Melakukan_reservasi_kamar_Melakukan_pembayaran, Melakukan_reservasi_kamar_Mengirim_e_bukti_Bayar, Admin_Kirim_e_booking_email, Pengunjung_Check_Out, Pemesan_Check_in, Pengunjung_Check_in, Pemesan_Check_Out, Pemesan_ReservasiKamar, ReservasiKamar_Admin, Kamar_ReservasiKamar, Denda_ReservasiKamar, Pembayaran_ReservasiKamar},
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
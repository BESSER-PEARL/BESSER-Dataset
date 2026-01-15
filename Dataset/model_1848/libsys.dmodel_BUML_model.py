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
InstanceStatus: Enumeration = Enumeration(
    name="InstanceStatus",
    literals={
            EnumerationLiteral(name="Missing"),
			EnumerationLiteral(name="Overdue"),
			EnumerationLiteral(name="ReservedAndAvailable"),
			EnumerationLiteral(name="ReservedAndBorrowed"),
			EnumerationLiteral(name="AcquisitionProcess"),
			EnumerationLiteral(name="ReadingRoom"),
			EnumerationLiteral(name="Available"),
			EnumerationLiteral(name="Borrowed")
    }
)

MediumCode: Enumeration = Enumeration(
    name="MediumCode",
    literals={
            EnumerationLiteral(name="book"),
			EnumerationLiteral(name="magazine"),
			EnumerationLiteral(name="CD"),
			EnumerationLiteral(name="video")
    }
)

# Classes
libsys_Medium = Class(name="libsys::Medium")
libsys_ReservationEntry = Class(name="libsys::ReservationEntry")
libsys_BorrowedEntry = Class(name="libsys::BorrowedEntry")
libsys_Instance = Class(name="libsys::Instance")
libsys_User = Class(name="libsys::User")
libsys_UserAccount = Class(name="libsys::UserAccount")
libsys_Terminal = Class(name="libsys::Terminal")
libsys_SearchCriterion = Class(name="libsys::SearchCriterion")
libsys_StatusSignal = Class(name="libsys::StatusSignal")
libsys_ExtensionTime = Class(name="libsys::ExtensionTime")
libsys_Librarian = Class(name="libsys::Librarian")
libsys_UserAdministration = Class(name="libsys::UserAdministration")
libsys_MediaAdministration = Class(name="libsys::MediaAdministration")
libsys_UnpaidFee = Class(name="libsys::UnpaidFee")
libsys_IdentificationCard = Class(name="libsys::IdentificationCard")
libsys_BarCodeScanner = Class(name="libsys::BarCodeScanner")
libsys_Library = Class(name="libsys::Library")
libsys_CD = Class(name="libsys::CD")
libsys_Video = Class(name="libsys::Video")
libsys_Book = Class(name="libsys::Book")
Medium = Class(name="Medium")
libsys_Magazine = Class(name="libsys::Magazine")

# libsys_Medium class attributes and methods
libsys_Medium_partialShelfmark: Property = Property(name="partialShelfmark", type=StringType)
libsys_Medium_identificationCode: Property = Property(name="identificationCode", type=StringType)
libsys_Medium_title: Property = Property(name="title", type=StringType)
libsys_Medium_additionalTitle: Property = Property(name="additionalTitle", type=StringType)
libsys_Medium_publicationYear: Property = Property(name="publicationYear", type=DateType)
libsys_Medium_authors: Property = Property(name="authors", type=StringType)
libsys_Medium_keywords: Property = Property(name="keywords", type=StringType)
libsys_Medium.attributes={libsys_Medium_publicationYear, libsys_Medium_partialShelfmark, libsys_Medium_title, libsys_Medium_additionalTitle, libsys_Medium_identificationCode, libsys_Medium_keywords, libsys_Medium_authors}

# libsys_ReservationEntry class attributes and methods

# libsys_BorrowedEntry class attributes and methods
libsys_BorrowedEntry_returnDate: Property = Property(name="returnDate", type=DateType)
libsys_BorrowedEntry.attributes={libsys_BorrowedEntry_returnDate}

# libsys_Instance class attributes and methods
libsys_Instance_shelfmark: Property = Property(name="shelfmark", type=StringType)
libsys_Instance_status: Property = Property(name="status", type=StringType)
libsys_Instance_returnDate: Property = Property(name="returnDate", type=DateType)
libsys_Instance_location: Property = Property(name="location", type=StringType)
libsys_Instance_rentalPeriod: Property = Property(name="rentalPeriod", type=StringType)
libsys_Instance_comments: Property = Property(name="comments", type=StringType)
libsys_Instance_components: Property = Property(name="components", type=StringType)
libsys_Instance_m_extendRentalPeriod: Method = Method(name="extendRentalPeriod", parameters={})
libsys_Instance_m_borrowInstance: Method = Method(name="borrowInstance", parameters={})
libsys_Instance_m_returnInstance: Method = Method(name="returnInstance", parameters={})
libsys_Instance_m_reserveInstance: Method = Method(name="reserveInstance", parameters={})
libsys_Instance.attributes={libsys_Instance_shelfmark, libsys_Instance_returnDate, libsys_Instance_components, libsys_Instance_rentalPeriod, libsys_Instance_location, libsys_Instance_comments, libsys_Instance_status}
libsys_Instance.methods={libsys_Instance_m_extendRentalPeriod, libsys_Instance_m_reserveInstance, libsys_Instance_m_borrowInstance, libsys_Instance_m_returnInstance}

# libsys_User class attributes and methods
libsys_User_m_registerAtSystem: Method = Method(name="registerAtSystem", parameters={})
libsys_User_m_identifyToSystem: Method = Method(name="identifyToSystem", parameters={})
libsys_User.methods={libsys_User_m_identifyToSystem, libsys_User_m_registerAtSystem}

# libsys_UserAccount class attributes and methods
libsys_UserAccount_userClassification: Property = Property(name="userClassification", type=StringType)
libsys_UserAccount_userName: Property = Property(name="userName", type=StringType)
libsys_UserAccount_telephoneNumber: Property = Property(name="telephoneNumber", type=StringType)
libsys_UserAccount_emailAddress: Property = Property(name="emailAddress", type=StringType)
libsys_UserAccount_validUntilDate: Property = Property(name="validUntilDate", type=DateType)
libsys_UserAccount_postallAddress: Property = Property(name="postallAddress", type=StringType)
libsys_UserAccount_unpaidFeeAmount: Property = Property(name="unpaidFeeAmount", type=IntegerType)
libsys_UserAccount_lockIndication: Property = Property(name="lockIndication", type=BooleanType)
libsys_UserAccount_userData: Property = Property(name="userData", type=StringType)
libsys_UserAccount_userNumber: Property = Property(name="userNumber", type=IntegerType)
libsys_UserAccount.attributes={libsys_UserAccount_emailAddress, libsys_UserAccount_userNumber, libsys_UserAccount_telephoneNumber, libsys_UserAccount_userClassification, libsys_UserAccount_userName, libsys_UserAccount_lockIndication, libsys_UserAccount_userData, libsys_UserAccount_validUntilDate, libsys_UserAccount_postallAddress, libsys_UserAccount_unpaidFeeAmount}

# libsys_Terminal class attributes and methods

# libsys_SearchCriterion class attributes and methods

# libsys_StatusSignal class attributes and methods

# libsys_ExtensionTime class attributes and methods

# libsys_Librarian class attributes and methods

# libsys_UserAdministration class attributes and methods
libsys_UserAdministration_m_manageUserAccount: Method = Method(name="manageUserAccount", parameters={})
libsys_UserAdministration.methods={libsys_UserAdministration_m_manageUserAccount}

# libsys_MediaAdministration class attributes and methods
libsys_MediaAdministration_m_addNewMediaInstance: Method = Method(name="addNewMediaInstance", parameters={})
libsys_MediaAdministration_m_removeMediaInstance: Method = Method(name="removeMediaInstance", parameters={})
libsys_MediaAdministration_m_searchMedium: Method = Method(name="searchMedium", parameters={})
libsys_MediaAdministration_m_manageMedium: Method = Method(name="manageMedium", parameters={})
libsys_MediaAdministration.methods={libsys_MediaAdministration_m_addNewMediaInstance, libsys_MediaAdministration_m_manageMedium, libsys_MediaAdministration_m_removeMediaInstance, libsys_MediaAdministration_m_searchMedium}

# libsys_UnpaidFee class attributes and methods
libsys_UnpaidFee_amount: Property = Property(name="amount", type=IntegerType)
libsys_UnpaidFee_reason: Property = Property(name="reason", type=StringType)
libsys_UnpaidFee.attributes={libsys_UnpaidFee_reason, libsys_UnpaidFee_amount}

# libsys_IdentificationCard class attributes and methods
libsys_IdentificationCard_userNumber: Property = Property(name="userNumber", type=IntegerType)
libsys_IdentificationCard.attributes={libsys_IdentificationCard_userNumber}

# libsys_BarCodeScanner class attributes and methods
libsys_BarCodeScanner_m_readUserNumber: Method = Method(name="readUserNumber", parameters={})
libsys_BarCodeScanner.methods={libsys_BarCodeScanner_m_readUserNumber}

# libsys_Library class attributes and methods

# libsys_CD class attributes and methods
libsys_CD_genres: Property = Property(name="genres", type=StringType)
libsys_CD_tracks: Property = Property(name="tracks", type=StringType)
libsys_CD_artists: Property = Property(name="artists", type=StringType)
libsys_CD.attributes={libsys_CD_artists, libsys_CD_genres, libsys_CD_tracks}

# libsys_Video class attributes and methods
libsys_Video_genres: Property = Property(name="genres", type=StringType)
libsys_Video_actors: Property = Property(name="actors", type=StringType)
libsys_Video.attributes={libsys_Video_actors, libsys_Video_genres}

# libsys_Book class attributes and methods
libsys_Book_publisher: Property = Property(name="publisher", type=StringType)
libsys_Book_placeOfPublication: Property = Property(name="placeOfPublication", type=StringType)
libsys_Book_editor: Property = Property(name="editor", type=StringType)
libsys_Book_ISBN: Property = Property(name="ISBN", type=StringType)
libsys_Book.attributes={libsys_Book_publisher, libsys_Book_placeOfPublication, libsys_Book_editor, libsys_Book_ISBN}

# Medium class attributes and methods

# libsys_Magazine class attributes and methods
libsys_Magazine_publisher: Property = Property(name="publisher", type=StringType)
libsys_Magazine_articles: Property = Property(name="articles", type=StringType)
libsys_Magazine.attributes={libsys_Magazine_publisher, libsys_Magazine_articles}

# Relationships
reservationList1: BinaryAssociation = BinaryAssociation(
    name="reservationList1",
    ends={
        Property(name="libsys_ReservationEntry", type=libsys_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Instance2", type=libsys_ReservationEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowingList3: BinaryAssociation = BinaryAssociation(
    name="borrowingList3",
    ends={
        Property(name="libsys_BorrowedEntry", type=libsys_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Instance4", type=libsys_BorrowedEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances0: BinaryAssociation = BinaryAssociation(
    name="instances0",
    ends={
        Property(name="libsys_Instance", type=libsys_Medium, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Medium", type=libsys_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userAccount5: BinaryAssociation = BinaryAssociation(
    name="userAccount5",
    ends={
        Property(name="libsys_UserAccount", type=libsys_User, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_User", type=libsys_UserAccount, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mediaEntries14: BinaryAssociation = BinaryAssociation(
    name="mediaEntries14",
    ends={
        Property(name="libsys_MediaAdministration", type=libsys_Medium, multiplicity=Multiplicity(0, 9999)),
        Property(name="libsys_Medium15", type=libsys_MediaAdministration, multiplicity=Multiplicity(1, 1))
    }
)
borrowedInstances6: BinaryAssociation = BinaryAssociation(
    name="borrowedInstances6",
    ends={
        Property(name="libsys_Instance8", type=libsys_UserAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_UserAccount7", type=libsys_Instance, multiplicity=Multiplicity(0, 9999))
    }
)
reservationList9: BinaryAssociation = BinaryAssociation(
    name="reservationList9",
    ends={
        Property(name="libsys_Instance11", type=libsys_UserAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_UserAccount10", type=libsys_Instance, multiplicity=Multiplicity(0, 9999))
    }
)
userAccounts12: BinaryAssociation = BinaryAssociation(
    name="userAccounts12",
    ends={
        Property(name="libsys_UserAccount13", type=libsys_UserAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_UserAdministration", type=libsys_UserAccount, multiplicity=Multiplicity(0, 9999))
    }
)
librarians18: BinaryAssociation = BinaryAssociation(
    name="librarians18",
    ends={
        Property(name="libsys_Librarian", type=libsys_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Library19", type=libsys_Librarian, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users20: BinaryAssociation = BinaryAssociation(
    name="users20",
    ends={
        Property(name="libsys_User22", type=libsys_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Library21", type=libsys_User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
user23: BinaryAssociation = BinaryAssociation(
    name="user23",
    ends={
        Property(name="libsys_User25", type=libsys_BorrowedEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_BorrowedEntry24", type=libsys_User, multiplicity=Multiplicity(1, 1))
    }
)
media16: BinaryAssociation = BinaryAssociation(
    name="media16",
    ends={
        Property(name="libsys_Medium17", type=libsys_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_Library", type=libsys_Medium, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user26: BinaryAssociation = BinaryAssociation(
    name="user26",
    ends={
        Property(name="libsys_User28", type=libsys_ReservationEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="libsys_ReservationEntry27", type=libsys_User, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_libsys_Magazine_Medium = Generalization(general=Medium, specific=libsys_Magazine)
gen_libsys_CD_Medium = Generalization(general=Medium, specific=libsys_CD)
gen_libsys_Video_Medium = Generalization(general=Medium, specific=libsys_Video)
gen_libsys_Book_Medium = Generalization(general=Medium, specific=libsys_Book)

# Domain Model
domain_model = DomainModel(
    name="libsys",
    types={libsys_Medium, libsys_ReservationEntry, libsys_BorrowedEntry, libsys_Instance, libsys_User, libsys_UserAccount, libsys_Terminal, libsys_SearchCriterion, libsys_StatusSignal, libsys_ExtensionTime, libsys_Librarian, libsys_UserAdministration, libsys_MediaAdministration, libsys_UnpaidFee, libsys_IdentificationCard, libsys_BarCodeScanner, libsys_Library, libsys_CD, libsys_Video, libsys_Book, Medium, libsys_Magazine, InstanceStatus, MediumCode},
    associations={reservationList1, borrowingList3, instances0, userAccount5, mediaEntries14, borrowedInstances6, reservationList9, userAccounts12, librarians18, users20, user23, media16, user26},
    generalizations={gen_libsys_Magazine_Medium, gen_libsys_CD_Medium, gen_libsys_Video_Medium, gen_libsys_Book_Medium},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
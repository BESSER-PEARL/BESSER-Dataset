from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class InstanceStatus(Enum):
    Missing = "Missing"
    Overdue = "Overdue"
    ReservedAndAvailable = "ReservedAndAvailable"
    ReservedAndBorrowed = "ReservedAndBorrowed"
    AcquisitionProcess = "AcquisitionProcess"
    ReadingRoom = "ReadingRoom"
    Available = "Available"
    Borrowed = "Borrowed"
class MediumCode(Enum):
    book = "book"
    magazine = "magazine"
    CD = "CD"
    video = "video"


############################################
# Definition of Classes
############################################

class Medium:

    pass
class libsys_Magazine(Medium):

    def __init__(self, publisher: str, articles: str):
        self.publisher = publisher
        self.articles = articles
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def articles(self) -> str:
        return self.__articles

    @articles.setter
    def articles(self, articles: str):
        self.__articles = articles

class libsys_Book(Medium):

    def __init__(self, publisher: str, placeOfPublication: str, editor: str, ISBN: str):
        self.publisher = publisher
        self.placeOfPublication = placeOfPublication
        self.editor = editor
        self.ISBN = ISBN
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def placeOfPublication(self) -> str:
        return self.__placeOfPublication

    @placeOfPublication.setter
    def placeOfPublication(self, placeOfPublication: str):
        self.__placeOfPublication = placeOfPublication

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def ISBN(self) -> str:
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN: str):
        self.__ISBN = ISBN

class libsys_Video(Medium):

    def __init__(self, genres: str, actors: str):
        self.genres = genres
        self.actors = actors
        
    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def genres(self) -> str:
        return self.__genres

    @genres.setter
    def genres(self, genres: str):
        self.__genres = genres

class libsys_CD(Medium):

    def __init__(self, genres: str, tracks: str, artists: str):
        self.genres = genres
        self.tracks = tracks
        self.artists = artists
        
    @property
    def artists(self) -> str:
        return self.__artists

    @artists.setter
    def artists(self, artists: str):
        self.__artists = artists

    @property
    def genres(self) -> str:
        return self.__genres

    @genres.setter
    def genres(self, genres: str):
        self.__genres = genres

    @property
    def tracks(self) -> str:
        return self.__tracks

    @tracks.setter
    def tracks(self, tracks: str):
        self.__tracks = tracks

class libsys_Library:

    pass
class libsys_BarCodeScanner:

    def __init__(self):
        
    def readUserNumber(self):
        # TODO: Implement readUserNumber method
        pass

class libsys_IdentificationCard:

    def __init__(self, userNumber: int):
        self.userNumber = userNumber
        
    @property
    def userNumber(self) -> int:
        return self.__userNumber

    @userNumber.setter
    def userNumber(self, userNumber: int):
        self.__userNumber = userNumber

class libsys_UnpaidFee:

    def __init__(self, amount: int, reason: str):
        self.amount = amount
        self.reason = reason
        
    @property
    def reason(self) -> str:
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

class libsys_MediaAdministration:

    def __init__(self, libsys_MediaAdministration: set["libsys_Medium"] = None):
        self.libsys_MediaAdministration = libsys_MediaAdministration if libsys_MediaAdministration is not None else set()
        
    @property
    def libsys_MediaAdministration(self):
        return self.__libsys_MediaAdministration

    @libsys_MediaAdministration.setter
    def libsys_MediaAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_MediaAdministration__libsys_MediaAdministration", None)
        self.__libsys_MediaAdministration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_Medium15"):
                    opp_val = getattr(item, "libsys_Medium15", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_Medium15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_Medium15"):
                    opp_val = getattr(item, "libsys_Medium15", None)
                    
                    setattr(item, "libsys_Medium15", self)
                    

    def addNewMediaInstance(self):
        # TODO: Implement addNewMediaInstance method
        pass

    def manageMedium(self):
        # TODO: Implement manageMedium method
        pass

    def removeMediaInstance(self):
        # TODO: Implement removeMediaInstance method
        pass

    def searchMedium(self):
        # TODO: Implement searchMedium method
        pass

class libsys_UserAdministration:

    def __init__(self, libsys_UserAdministration: set["libsys_UserAccount"] = None):
        self.libsys_UserAdministration = libsys_UserAdministration if libsys_UserAdministration is not None else set()
        
    @property
    def libsys_UserAdministration(self):
        return self.__libsys_UserAdministration

    @libsys_UserAdministration.setter
    def libsys_UserAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_UserAdministration__libsys_UserAdministration", None)
        self.__libsys_UserAdministration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_UserAccount13"):
                    opp_val = getattr(item, "libsys_UserAccount13", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_UserAccount13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_UserAccount13"):
                    opp_val = getattr(item, "libsys_UserAccount13", None)
                    
                    setattr(item, "libsys_UserAccount13", self)
                    

    def manageUserAccount(self):
        # TODO: Implement manageUserAccount method
        pass

class libsys_Librarian:

    pass
class libsys_ExtensionTime:

    pass
class libsys_StatusSignal:

    pass
class libsys_SearchCriterion:

    pass
class libsys_Terminal:

    pass
class libsys_UserAccount:

    def __init__(self, userClassification: str, userName: str, telephoneNumber: str, emailAddress: str, validUntilDate: date, postallAddress: str, unpaidFeeAmount: int, lockIndication: bool, userData: str, userNumber: int, libsys_UserAccount: "libsys_User" = None, libsys_UserAccount7: set["libsys_Instance"] = None, libsys_UserAccount10: set["libsys_Instance"] = None, libsys_UserAccount13: "libsys_UserAdministration" = None):
        self.userClassification = userClassification
        self.userName = userName
        self.telephoneNumber = telephoneNumber
        self.emailAddress = emailAddress
        self.validUntilDate = validUntilDate
        self.postallAddress = postallAddress
        self.unpaidFeeAmount = unpaidFeeAmount
        self.lockIndication = lockIndication
        self.userData = userData
        self.userNumber = userNumber
        self.libsys_UserAccount = libsys_UserAccount
        self.libsys_UserAccount7 = libsys_UserAccount7 if libsys_UserAccount7 is not None else set()
        self.libsys_UserAccount10 = libsys_UserAccount10 if libsys_UserAccount10 is not None else set()
        self.libsys_UserAccount13 = libsys_UserAccount13
        
    @property
    def emailAddress(self) -> str:
        return self.__emailAddress

    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def userNumber(self) -> int:
        return self.__userNumber

    @userNumber.setter
    def userNumber(self, userNumber: int):
        self.__userNumber = userNumber

    @property
    def telephoneNumber(self) -> str:
        return self.__telephoneNumber

    @telephoneNumber.setter
    def telephoneNumber(self, telephoneNumber: str):
        self.__telephoneNumber = telephoneNumber

    @property
    def userClassification(self) -> str:
        return self.__userClassification

    @userClassification.setter
    def userClassification(self, userClassification: str):
        self.__userClassification = userClassification

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def lockIndication(self) -> bool:
        return self.__lockIndication

    @lockIndication.setter
    def lockIndication(self, lockIndication: bool):
        self.__lockIndication = lockIndication

    @property
    def userData(self) -> str:
        return self.__userData

    @userData.setter
    def userData(self, userData: str):
        self.__userData = userData

    @property
    def validUntilDate(self) -> date:
        return self.__validUntilDate

    @validUntilDate.setter
    def validUntilDate(self, validUntilDate: date):
        self.__validUntilDate = validUntilDate

    @property
    def postallAddress(self) -> str:
        return self.__postallAddress

    @postallAddress.setter
    def postallAddress(self, postallAddress: str):
        self.__postallAddress = postallAddress

    @property
    def unpaidFeeAmount(self) -> int:
        return self.__unpaidFeeAmount

    @unpaidFeeAmount.setter
    def unpaidFeeAmount(self, unpaidFeeAmount: int):
        self.__unpaidFeeAmount = unpaidFeeAmount

    @property
    def libsys_UserAccount13(self):
        return self.__libsys_UserAccount13

    @libsys_UserAccount13.setter
    def libsys_UserAccount13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_UserAccount__libsys_UserAccount13", None)
        self.__libsys_UserAccount13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_UserAdministration"):
                opp_val = getattr(old_value, "libsys_UserAdministration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_UserAdministration"):
                opp_val = getattr(value, "libsys_UserAdministration", None)
                if opp_val is None:
                    setattr(value, "libsys_UserAdministration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libsys_UserAccount7(self):
        return self.__libsys_UserAccount7

    @libsys_UserAccount7.setter
    def libsys_UserAccount7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_UserAccount__libsys_UserAccount7", None)
        self.__libsys_UserAccount7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_Instance8"):
                    opp_val = getattr(item, "libsys_Instance8", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_Instance8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_Instance8"):
                    opp_val = getattr(item, "libsys_Instance8", None)
                    
                    setattr(item, "libsys_Instance8", self)
                    

    @property
    def libsys_UserAccount(self):
        return self.__libsys_UserAccount

    @libsys_UserAccount.setter
    def libsys_UserAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_UserAccount__libsys_UserAccount", None)
        self.__libsys_UserAccount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_User"):
                opp_val = getattr(old_value, "libsys_User", None)
                if opp_val == self:
                    setattr(old_value, "libsys_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_User"):
                opp_val = getattr(value, "libsys_User", None)
                setattr(value, "libsys_User", self)

    @property
    def libsys_UserAccount10(self):
        return self.__libsys_UserAccount10

    @libsys_UserAccount10.setter
    def libsys_UserAccount10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_UserAccount__libsys_UserAccount10", None)
        self.__libsys_UserAccount10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_Instance11"):
                    opp_val = getattr(item, "libsys_Instance11", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_Instance11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_Instance11"):
                    opp_val = getattr(item, "libsys_Instance11", None)
                    
                    setattr(item, "libsys_Instance11", self)
                    

class libsys_User:

    def __init__(self, libsys_User: "libsys_UserAccount" = None, libsys_User22: "libsys_Library" = None, libsys_User25: "libsys_BorrowedEntry" = None, libsys_User28: "libsys_ReservationEntry" = None):
        self.libsys_User = libsys_User
        self.libsys_User22 = libsys_User22
        self.libsys_User25 = libsys_User25
        self.libsys_User28 = libsys_User28
        
    @property
    def libsys_User28(self):
        return self.__libsys_User28

    @libsys_User28.setter
    def libsys_User28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_User__libsys_User28", None)
        self.__libsys_User28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_ReservationEntry27"):
                opp_val = getattr(old_value, "libsys_ReservationEntry27", None)
                if opp_val == self:
                    setattr(old_value, "libsys_ReservationEntry27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_ReservationEntry27"):
                opp_val = getattr(value, "libsys_ReservationEntry27", None)
                setattr(value, "libsys_ReservationEntry27", self)

    @property
    def libsys_User25(self):
        return self.__libsys_User25

    @libsys_User25.setter
    def libsys_User25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_User__libsys_User25", None)
        self.__libsys_User25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_BorrowedEntry24"):
                opp_val = getattr(old_value, "libsys_BorrowedEntry24", None)
                if opp_val == self:
                    setattr(old_value, "libsys_BorrowedEntry24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_BorrowedEntry24"):
                opp_val = getattr(value, "libsys_BorrowedEntry24", None)
                setattr(value, "libsys_BorrowedEntry24", self)

    @property
    def libsys_User22(self):
        return self.__libsys_User22

    @libsys_User22.setter
    def libsys_User22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_User__libsys_User22", None)
        self.__libsys_User22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_Library21"):
                opp_val = getattr(old_value, "libsys_Library21", None)
                if opp_val == self:
                    setattr(old_value, "libsys_Library21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_Library21"):
                opp_val = getattr(value, "libsys_Library21", None)
                setattr(value, "libsys_Library21", self)

    @property
    def libsys_User(self):
        return self.__libsys_User

    @libsys_User.setter
    def libsys_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_User__libsys_User", None)
        self.__libsys_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_UserAccount"):
                opp_val = getattr(old_value, "libsys_UserAccount", None)
                if opp_val == self:
                    setattr(old_value, "libsys_UserAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_UserAccount"):
                opp_val = getattr(value, "libsys_UserAccount", None)
                setattr(value, "libsys_UserAccount", self)

    def identifyToSystem(self):
        # TODO: Implement identifyToSystem method
        pass

    def registerAtSystem(self):
        # TODO: Implement registerAtSystem method
        pass

class libsys_Instance:

    def __init__(self, shelfmark: str, status: str, returnDate: date, location: str, rentalPeriod: str, comments: str, components: str, libsys_Instance2: set["libsys_ReservationEntry"] = None, libsys_Instance4: set["libsys_BorrowedEntry"] = None, libsys_Instance: "libsys_Medium" = None, libsys_Instance8: "libsys_UserAccount" = None, libsys_Instance11: "libsys_UserAccount" = None):
        self.shelfmark = shelfmark
        self.status = status
        self.returnDate = returnDate
        self.location = location
        self.rentalPeriod = rentalPeriod
        self.comments = comments
        self.components = components
        self.libsys_Instance2 = libsys_Instance2 if libsys_Instance2 is not None else set()
        self.libsys_Instance4 = libsys_Instance4 if libsys_Instance4 is not None else set()
        self.libsys_Instance = libsys_Instance
        self.libsys_Instance8 = libsys_Instance8
        self.libsys_Instance11 = libsys_Instance11
        
    @property
    def shelfmark(self) -> str:
        return self.__shelfmark

    @shelfmark.setter
    def shelfmark(self, shelfmark: str):
        self.__shelfmark = shelfmark

    @property
    def returnDate(self) -> date:
        return self.__returnDate

    @returnDate.setter
    def returnDate(self, returnDate: date):
        self.__returnDate = returnDate

    @property
    def components(self) -> str:
        return self.__components

    @components.setter
    def components(self, components: str):
        self.__components = components

    @property
    def rentalPeriod(self) -> str:
        return self.__rentalPeriod

    @rentalPeriod.setter
    def rentalPeriod(self, rentalPeriod: str):
        self.__rentalPeriod = rentalPeriod

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def libsys_Instance(self):
        return self.__libsys_Instance

    @libsys_Instance.setter
    def libsys_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Instance__libsys_Instance", None)
        self.__libsys_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_Medium"):
                opp_val = getattr(old_value, "libsys_Medium", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_Medium"):
                opp_val = getattr(value, "libsys_Medium", None)
                if opp_val is None:
                    setattr(value, "libsys_Medium", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libsys_Instance2(self):
        return self.__libsys_Instance2

    @libsys_Instance2.setter
    def libsys_Instance2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Instance__libsys_Instance2", None)
        self.__libsys_Instance2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_ReservationEntry"):
                    opp_val = getattr(item, "libsys_ReservationEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_ReservationEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_ReservationEntry"):
                    opp_val = getattr(item, "libsys_ReservationEntry", None)
                    
                    setattr(item, "libsys_ReservationEntry", self)
                    

    @property
    def libsys_Instance8(self):
        return self.__libsys_Instance8

    @libsys_Instance8.setter
    def libsys_Instance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Instance__libsys_Instance8", None)
        self.__libsys_Instance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_UserAccount7"):
                opp_val = getattr(old_value, "libsys_UserAccount7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_UserAccount7"):
                opp_val = getattr(value, "libsys_UserAccount7", None)
                if opp_val is None:
                    setattr(value, "libsys_UserAccount7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libsys_Instance4(self):
        return self.__libsys_Instance4

    @libsys_Instance4.setter
    def libsys_Instance4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Instance__libsys_Instance4", None)
        self.__libsys_Instance4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_BorrowedEntry"):
                    opp_val = getattr(item, "libsys_BorrowedEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_BorrowedEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_BorrowedEntry"):
                    opp_val = getattr(item, "libsys_BorrowedEntry", None)
                    
                    setattr(item, "libsys_BorrowedEntry", self)
                    

    @property
    def libsys_Instance11(self):
        return self.__libsys_Instance11

    @libsys_Instance11.setter
    def libsys_Instance11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Instance__libsys_Instance11", None)
        self.__libsys_Instance11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_UserAccount10"):
                opp_val = getattr(old_value, "libsys_UserAccount10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_UserAccount10"):
                opp_val = getattr(value, "libsys_UserAccount10", None)
                if opp_val is None:
                    setattr(value, "libsys_UserAccount10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def extendRentalPeriod(self):
        # TODO: Implement extendRentalPeriod method
        pass

    def reserveInstance(self):
        # TODO: Implement reserveInstance method
        pass

    def borrowInstance(self):
        # TODO: Implement borrowInstance method
        pass

    def returnInstance(self):
        # TODO: Implement returnInstance method
        pass

class libsys_BorrowedEntry:

    def __init__(self, returnDate: date, libsys_BorrowedEntry: "libsys_Instance" = None, libsys_BorrowedEntry24: "libsys_User" = None):
        self.returnDate = returnDate
        self.libsys_BorrowedEntry = libsys_BorrowedEntry
        self.libsys_BorrowedEntry24 = libsys_BorrowedEntry24
        
    @property
    def returnDate(self) -> date:
        return self.__returnDate

    @returnDate.setter
    def returnDate(self, returnDate: date):
        self.__returnDate = returnDate

    @property
    def libsys_BorrowedEntry24(self):
        return self.__libsys_BorrowedEntry24

    @libsys_BorrowedEntry24.setter
    def libsys_BorrowedEntry24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_BorrowedEntry__libsys_BorrowedEntry24", None)
        self.__libsys_BorrowedEntry24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_User25"):
                opp_val = getattr(old_value, "libsys_User25", None)
                if opp_val == self:
                    setattr(old_value, "libsys_User25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_User25"):
                opp_val = getattr(value, "libsys_User25", None)
                setattr(value, "libsys_User25", self)

    @property
    def libsys_BorrowedEntry(self):
        return self.__libsys_BorrowedEntry

    @libsys_BorrowedEntry.setter
    def libsys_BorrowedEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_BorrowedEntry__libsys_BorrowedEntry", None)
        self.__libsys_BorrowedEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_Instance4"):
                opp_val = getattr(old_value, "libsys_Instance4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_Instance4"):
                opp_val = getattr(value, "libsys_Instance4", None)
                if opp_val is None:
                    setattr(value, "libsys_Instance4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libsys_ReservationEntry:

    pass
class libsys_Medium:

    def __init__(self, partialShelfmark: str, identificationCode: str, title: str, additionalTitle: str, publicationYear: date, authors: str, keywords: str, libsys_Medium: set["libsys_Instance"] = None, libsys_Medium15: "libsys_MediaAdministration" = None, libsys_Medium17: "libsys_Library" = None):
        self.partialShelfmark = partialShelfmark
        self.identificationCode = identificationCode
        self.title = title
        self.additionalTitle = additionalTitle
        self.publicationYear = publicationYear
        self.authors = authors
        self.keywords = keywords
        self.libsys_Medium = libsys_Medium if libsys_Medium is not None else set()
        self.libsys_Medium15 = libsys_Medium15
        self.libsys_Medium17 = libsys_Medium17
        
    @property
    def publicationYear(self) -> date:
        return self.__publicationYear

    @publicationYear.setter
    def publicationYear(self, publicationYear: date):
        self.__publicationYear = publicationYear

    @property
    def partialShelfmark(self) -> str:
        return self.__partialShelfmark

    @partialShelfmark.setter
    def partialShelfmark(self, partialShelfmark: str):
        self.__partialShelfmark = partialShelfmark

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def additionalTitle(self) -> str:
        return self.__additionalTitle

    @additionalTitle.setter
    def additionalTitle(self, additionalTitle: str):
        self.__additionalTitle = additionalTitle

    @property
    def identificationCode(self) -> str:
        return self.__identificationCode

    @identificationCode.setter
    def identificationCode(self, identificationCode: str):
        self.__identificationCode = identificationCode

    @property
    def keywords(self) -> str:
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords

    @property
    def authors(self) -> str:
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

    @property
    def libsys_Medium17(self):
        return self.__libsys_Medium17

    @libsys_Medium17.setter
    def libsys_Medium17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Medium__libsys_Medium17", None)
        self.__libsys_Medium17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_Library"):
                opp_val = getattr(old_value, "libsys_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_Library"):
                opp_val = getattr(value, "libsys_Library", None)
                if opp_val is None:
                    setattr(value, "libsys_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libsys_Medium(self):
        return self.__libsys_Medium

    @libsys_Medium.setter
    def libsys_Medium(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Medium__libsys_Medium", None)
        self.__libsys_Medium = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libsys_Instance"):
                    opp_val = getattr(item, "libsys_Instance", None)
                    
                    if opp_val == self:
                        setattr(item, "libsys_Instance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libsys_Instance"):
                    opp_val = getattr(item, "libsys_Instance", None)
                    
                    setattr(item, "libsys_Instance", self)
                    

    @property
    def libsys_Medium15(self):
        return self.__libsys_Medium15

    @libsys_Medium15.setter
    def libsys_Medium15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libsys_Medium__libsys_Medium15", None)
        self.__libsys_Medium15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libsys_MediaAdministration"):
                opp_val = getattr(old_value, "libsys_MediaAdministration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libsys_MediaAdministration"):
                opp_val = getattr(value, "libsys_MediaAdministration", None)
                if opp_val is None:
                    setattr(value, "libsys_MediaAdministration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

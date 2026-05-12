from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class book_chapters:

    pass


class book:

    def __init__(self, Title: str, AuthoredBy: author, Year: int, Publisher: publisher, Region: str, Price: float, RefTo: publishments, publishments3: "publishments" = None):
        self.Title = Title
        self.AuthoredBy = AuthoredBy
        self.Year = Year
        self.Publisher = Publisher
        self.Region = Region
        self.Price = Price
        self.RefTo = RefTo
        self.publishments3 = publishments3
        
        pass
    @property
    def AuthoredBy(self):
        return self.__AuthoredBy
    @AuthoredBy.setter
    def AuthoredBy(self, AuthoredBy: author):
        self.__AuthoredBy = AuthoredBy

    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def Publisher(self):
        return self.__Publisher
    @Publisher.setter
    def Publisher(self, Publisher: publisher):
        self.__Publisher = Publisher

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: float):
        self.__Price = Price

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Region(self):
        return self.__Region
    @Region.setter
    def Region(self, Region: str):
        self.__Region = Region

    @property
    def RefTo(self):
        return self.__RefTo
    @RefTo.setter
    def RefTo(self, RefTo: publishments):
        self.__RefTo = RefTo

    @property
    def publishments3(self):
        return self.__publishments3
    @publishments3.setter
    def publishments3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book__publishments3", None)
        self.__publishments3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book2"):
                opp_val = getattr(old_value, "book2", None)
                if opp_val == self:
                    setattr(old_value, "book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book2"):
                opp_val = getattr(value, "book2", None)
                setattr(value, "book2", self)



class journal_article:

    def __init__(self, Title: str, Year: int, Publisher: publisher, JournalName: str, AuthoredBy: author, Volume: int, Pages: int):
        self.Title = Title
        self.Year = Year
        self.Publisher = Publisher
        self.JournalName = JournalName
        self.AuthoredBy = AuthoredBy
        self.Volume = Volume
        self.Pages = Pages
        
        pass
    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Publisher(self):
        return self.__Publisher
    @Publisher.setter
    def Publisher(self, Publisher: publisher):
        self.__Publisher = Publisher

    @property
    def Pages(self):
        return self.__Pages
    @Pages.setter
    def Pages(self, Pages: int):
        self.__Pages = Pages

    @property
    def AuthoredBy(self):
        return self.__AuthoredBy
    @AuthoredBy.setter
    def AuthoredBy(self, AuthoredBy: author):
        self.__AuthoredBy = AuthoredBy

    @property
    def JournalName(self):
        return self.__JournalName
    @JournalName.setter
    def JournalName(self, JournalName: str):
        self.__JournalName = JournalName

    @property
    def Volume(self):
        return self.__Volume
    @Volume.setter
    def Volume(self, Volume: int):
        self.__Volume = Volume



class conference_paper:

    def __init__(self, Title: str, AuthoredBy: author, Year: int, Publisher: publisher, ConferenceName: str, Location: str, publishments0: "publishments" = None):
        self.Title = Title
        self.AuthoredBy = AuthoredBy
        self.Year = Year
        self.Publisher = Publisher
        self.ConferenceName = ConferenceName
        self.Location = Location
        self.publishments0 = publishments0
        
        pass
    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def ConferenceName(self):
        return self.__ConferenceName
    @ConferenceName.setter
    def ConferenceName(self, ConferenceName: str):
        self.__ConferenceName = ConferenceName

    @property
    def AuthoredBy(self):
        return self.__AuthoredBy
    @AuthoredBy.setter
    def AuthoredBy(self, AuthoredBy: author):
        self.__AuthoredBy = AuthoredBy

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Publisher(self):
        return self.__Publisher
    @Publisher.setter
    def Publisher(self, Publisher: publisher):
        self.__Publisher = Publisher

    @property
    def publishments0(self):
        return self.__publishments0
    @publishments0.setter
    def publishments0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_paper__publishments0", None)
        self.__publishments0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_paper1"):
                opp_val = getattr(old_value, "conference_paper1", None)
                if opp_val == self:
                    setattr(old_value, "conference_paper1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_paper1"):
                opp_val = getattr(value, "conference_paper1", None)
                setattr(value, "conference_paper1", self)



class publisher:

    def __init__(self, OrgName: str, EstablishedYear: int, OrgContact: str, OrgAddress: str):
        self.OrgName = OrgName
        self.EstablishedYear = EstablishedYear
        self.OrgContact = OrgContact
        self.OrgAddress = OrgAddress
        
        pass
    @property
    def OrgContact(self):
        return self.__OrgContact
    @OrgContact.setter
    def OrgContact(self, OrgContact: str):
        self.__OrgContact = OrgContact

    @property
    def EstablishedYear(self):
        return self.__EstablishedYear
    @EstablishedYear.setter
    def EstablishedYear(self, EstablishedYear: int):
        self.__EstablishedYear = EstablishedYear

    @property
    def OrgName(self):
        return self.__OrgName
    @OrgName.setter
    def OrgName(self, OrgName: str):
        self.__OrgName = OrgName

    @property
    def OrgAddress(self):
        return self.__OrgAddress
    @OrgAddress.setter
    def OrgAddress(self, OrgAddress: str):
        self.__OrgAddress = OrgAddress



class publishments:

    def __init__(self, Title: str, Publisher: publisher, AuthoredBy: author, Year: int, conference_paper1: "conference_paper" = None, book2: "book" = None):
        self.Title = Title
        self.Publisher = Publisher
        self.AuthoredBy = AuthoredBy
        self.Year = Year
        self.conference_paper1 = conference_paper1
        self.book2 = book2
        
        pass
    @property
    def Year(self):
        return self.__Year
    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def AuthoredBy(self):
        return self.__AuthoredBy
    @AuthoredBy.setter
    def AuthoredBy(self, AuthoredBy: author):
        self.__AuthoredBy = AuthoredBy

    @property
    def Publisher(self):
        return self.__Publisher
    @Publisher.setter
    def Publisher(self, Publisher: publisher):
        self.__Publisher = Publisher

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def book2(self):
        return self.__book2
    @book2.setter
    def book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publishments__book2", None)
        self.__book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publishments3"):
                opp_val = getattr(old_value, "publishments3", None)
                if opp_val == self:
                    setattr(old_value, "publishments3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publishments3"):
                opp_val = getattr(value, "publishments3", None)
                setattr(value, "publishments3", self)

    @property
    def conference_paper1(self):
        return self.__conference_paper1
    @conference_paper1.setter
    def conference_paper1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publishments__conference_paper1", None)
        self.__conference_paper1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publishments0"):
                opp_val = getattr(old_value, "publishments0", None)
                if opp_val == self:
                    setattr(old_value, "publishments0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publishments0"):
                opp_val = getattr(value, "publishments0", None)
                setattr(value, "publishments0", self)



class author:

    def __init__(self, GivenName: str, FamilyName: str, Mail: str, Phone: str, Address: str):
        self.GivenName = GivenName
        self.FamilyName = FamilyName
        self.Mail = Mail
        self.Phone = Phone
        self.Address = Address
        
        pass
    @property
    def GivenName(self):
        return self.__GivenName
    @GivenName.setter
    def GivenName(self, GivenName: str):
        self.__GivenName = GivenName

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def FamilyName(self):
        return self.__FamilyName
    @FamilyName.setter
    def FamilyName(self, FamilyName: str):
        self.__FamilyName = FamilyName

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address



class orgnazition:

    def __init__(self, name: str, establishedDate: str, icon: str, orgID: str, president: person):
        self.name = name
        self.establishedDate = establishedDate
        self.icon = icon
        self.orgID = orgID
        self.president = president
        
        pass
    @property
    def establishedDate(self):
        return self.__establishedDate
    @establishedDate.setter
    def establishedDate(self, establishedDate: str):
        self.__establishedDate = establishedDate

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def icon(self):
        return self.__icon
    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def president(self):
        return self.__president
    @president.setter
    def president(self, president: person):
        self.__president = president

    @property
    def orgID(self):
        return self.__orgID
    @orgID.setter
    def orgID(self, orgID: str):
        self.__orgID = orgID



class person:

    def __init__(self, name: str, birthday: str, portrait: str, gender: bool, personID: str, belongsTo: orgnazition):
        self.name = name
        self.birthday = birthday
        self.portrait = portrait
        self.gender = gender
        self.personID = personID
        self.belongsTo = belongsTo
        
        pass
    @property
    def belongsTo(self):
        return self.__belongsTo
    @belongsTo.setter
    def belongsTo(self, belongsTo: orgnazition):
        self.__belongsTo = belongsTo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: bool):
        self.__gender = gender

    @property
    def birthday(self):
        return self.__birthday
    @birthday.setter
    def birthday(self, birthday: str):
        self.__birthday = birthday

    @property
    def portrait(self):
        return self.__portrait
    @portrait.setter
    def portrait(self, portrait: str):
        self.__portrait = portrait

    @property
    def personID(self):
        return self.__personID
    @personID.setter
    def personID(self, personID: str):
        self.__personID = personID



class song:

    def __init__(self, title: str, duration: str, belongsTo: album, year: int, cover: str, artistLyrics: person, price: str, genre: str, artistCompose: person, artistVocal: person, rightsReserve: orgnazition, trackID: int, songID: str, artistPerform: person):
        self.title = title
        self.duration = duration
        self.belongsTo = belongsTo
        self.year = year
        self.cover = cover
        self.artistLyrics = artistLyrics
        self.price = price
        self.genre = genre
        self.artistCompose = artistCompose
        self.artistVocal = artistVocal
        self.rightsReserve = rightsReserve
        self.trackID = trackID
        self.songID = songID
        self.artistPerform = artistPerform
        
        pass
    @property
    def artistLyrics(self):
        return self.__artistLyrics
    @artistLyrics.setter
    def artistLyrics(self, artistLyrics: person):
        self.__artistLyrics = artistLyrics

    @property
    def belongsTo(self):
        return self.__belongsTo
    @belongsTo.setter
    def belongsTo(self, belongsTo: album):
        self.__belongsTo = belongsTo

    @property
    def songID(self):
        return self.__songID
    @songID.setter
    def songID(self, songID: str):
        self.__songID = songID

    @property
    def cover(self):
        return self.__cover
    @cover.setter
    def cover(self, cover: str):
        self.__cover = cover

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def artistPerform(self):
        return self.__artistPerform
    @artistPerform.setter
    def artistPerform(self, artistPerform: person):
        self.__artistPerform = artistPerform

    @property
    def artistVocal(self):
        return self.__artistVocal
    @artistVocal.setter
    def artistVocal(self, artistVocal: person):
        self.__artistVocal = artistVocal

    @property
    def rightsReserve(self):
        return self.__rightsReserve
    @rightsReserve.setter
    def rightsReserve(self, rightsReserve: orgnazition):
        self.__rightsReserve = rightsReserve

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def trackID(self):
        return self.__trackID
    @trackID.setter
    def trackID(self, trackID: int):
        self.__trackID = trackID

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def artistCompose(self):
        return self.__artistCompose
    @artistCompose.setter
    def artistCompose(self, artistCompose: person):
        self.__artistCompose = artistCompose



class album:

    def __init__(self, title: str, publishDate: str, cover: str, albumID: str, duration: str, publisher: orgnazition, price: str, genre: str, artists: person, rightsReserve: orgnazition):
        self.title = title
        self.publishDate = publishDate
        self.cover = cover
        self.albumID = albumID
        self.duration = duration
        self.publisher = publisher
        self.price = price
        self.genre = genre
        self.artists = artists
        self.rightsReserve = rightsReserve
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def artists(self):
        return self.__artists
    @artists.setter
    def artists(self, artists: person):
        self.__artists = artists

    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher: orgnazition):
        self.__publisher = publisher

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def cover(self):
        return self.__cover
    @cover.setter
    def cover(self, cover: str):
        self.__cover = cover

    @property
    def publishDate(self):
        return self.__publishDate
    @publishDate.setter
    def publishDate(self, publishDate: str):
        self.__publishDate = publishDate

    @property
    def albumID(self):
        return self.__albumID
    @albumID.setter
    def albumID(self, albumID: str):
        self.__albumID = albumID

    @property
    def rightsReserve(self):
        return self.__rightsReserve
    @rightsReserve.setter
    def rightsReserve(self, rightsReserve: orgnazition):
        self.__rightsReserve = rightsReserve

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title



class document:

    pass

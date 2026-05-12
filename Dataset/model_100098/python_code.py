from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Cocus_Activity:

    pass
class Cocus_Description:

    pass
class URL:

    pass
class Cocus_Event_URL(URL):

    pass
class Cocus_Event_Setup:

    pass
class Help_Request:

    pass
class Cocus_Assistance(Help_Request):

    pass
class Cocus_Feature_Request(Help_Request):

    pass
class Cocus_Misc(Help_Request):

    pass
class Review_Form:

    pass
class Cocus_Review_Form_Setup(Review_Form):

    pass
class Cocus_Preview(Review_Form):

    pass
class Email:

    pass
class Cocus_Approval_Email(Email):

    pass
class Cocus_Rejection_Email(Email):

    pass
class Cocus_Group_Email(Email):

    pass
class Cocus_Notification_Email(Email):

    pass
class Cocus_URL:

    pass
class Account:

    pass
class Activity:

    pass
class Cocus_Registration(Activity):

    pass
class Cocus_Request(Activity):

    pass
class Cocus_Event_Approval(Activity):

    pass
class Cocus_Event_Creation(Activity):

    pass
class Cocus_Inforamtion:

    pass
class Cocus_Account:

    pass
class Event_Setup:

    pass
class Cocus_Email_Template(Event_Setup):

    pass
class Cocus_Research_Topic(Event_Setup):

    pass
class Cocus_Event_Tracks(Event_Setup):

    pass
class Cocus_Review_Form(Event_Setup):

    pass
class Cocus_Paper_Typologies(Event_Setup):

    pass
class Cocus_Submission_Template(Event_Setup):

    pass
class Approval_Email:

    pass
class Inforamtion:

    pass
class Request:

    pass
class Cocus_Help_Request(Request):

    pass
class Role:

    pass
class Cocus_Admin_Role(Role):

    pass
class Cocus_Head_Role(Role):

    pass
class Cocus_Reviewer_Role(Role):

    pass
class Cocus_Committe_Role(Role):

    pass
class Cocus_Author_Role(Role):

    pass
class Event_Tracks:

    pass
class Meta_Reviewer:

    pass
class SubjectArea:

    pass
class Cocus_SubjectArea:

    pass
class Author:

    pass
class Cocus_Corresponding_Author(Author):

    pass
class Cocus_Co_author(Author):

    pass
class Cocus_AuthorNotReviewer(Author):

    pass
class ProgramCommittee:

    pass
class Co_author:

    pass
class Document:

    pass
class Cocus_Paper(Document):

    def __init__(self, paperID: str, title: str, Cocus_Paper63: "Meta_Reviewer" = None, hasBeenAssigned: "Reviewer" = None, Cocus_Paper51: "SubjectArea" = None, readPaper: "Reviewer" = None, Cocus_Paper55: "Author" = None, Cocus_Paper57: "Administrator" = None, Cocus_Paper60: "Administrator" = None, co_writePaper: "Co_author" = None, Cocus_Paper: "Bid" = None, Cocus_Paper47: "Decision" = None, Document146: "Cocus_Person" = None, Document: "Cocus_User" = None, Document115: "Cocus_User" = None, Document126: "Cocus_Person" = None):
        self.paperID = paperID
        self.title = title
        self.Cocus_Paper63 = Cocus_Paper63
        self.hasBeenAssigned = hasBeenAssigned
        self.Cocus_Paper51 = Cocus_Paper51
        self.readPaper = readPaper
        self.Cocus_Paper55 = Cocus_Paper55
        self.Cocus_Paper57 = Cocus_Paper57
        self.Cocus_Paper60 = Cocus_Paper60
        self.co_writePaper = co_writePaper
        self.Cocus_Paper = Cocus_Paper
        self.Cocus_Paper47 = Cocus_Paper47
        
        pass
    @property
    def paperID(self):
        return self.__paperID

    @paperID.setter
    def paperID(self, paperID: str):
        self.__paperID = paperID


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def Cocus_Paper60(self):
        return self.__Cocus_Paper60

    @Cocus_Paper60.setter
    def Cocus_Paper60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper60", None)
        self.__Cocus_Paper60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator61"):
                opp_val = getattr(old_value, "Administrator61", None)
                if opp_val == self:
                    setattr(old_value, "Administrator61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator61"):
                opp_val = getattr(value, "Administrator61", None)
                setattr(value, "Administrator61", self)

    @property
    def Cocus_Paper57(self):
        return self.__Cocus_Paper57

    @Cocus_Paper57.setter
    def Cocus_Paper57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper57", None)
        self.__Cocus_Paper57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator58"):
                opp_val = getattr(old_value, "Administrator58", None)
                if opp_val == self:
                    setattr(old_value, "Administrator58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator58"):
                opp_val = getattr(value, "Administrator58", None)
                setattr(value, "Administrator58", self)

    @property
    def Cocus_Paper51(self):
        return self.__Cocus_Paper51

    @Cocus_Paper51.setter
    def Cocus_Paper51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper51", None)
        self.__Cocus_Paper51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubjectArea"):
                opp_val = getattr(old_value, "SubjectArea", None)
                if opp_val == self:
                    setattr(old_value, "SubjectArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubjectArea"):
                opp_val = getattr(value, "SubjectArea", None)
                setattr(value, "SubjectArea", self)

    @property
    def Cocus_Paper47(self):
        return self.__Cocus_Paper47

    @Cocus_Paper47.setter
    def Cocus_Paper47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper47", None)
        self.__Cocus_Paper47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Decision"):
                opp_val = getattr(old_value, "Decision", None)
                if opp_val == self:
                    setattr(old_value, "Decision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Decision"):
                opp_val = getattr(value, "Decision", None)
                setattr(value, "Decision", self)

    @property
    def Cocus_Paper(self):
        return self.__Cocus_Paper

    @Cocus_Paper.setter
    def Cocus_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper", None)
        self.__Cocus_Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bid45"):
                opp_val = getattr(old_value, "Bid45", None)
                if opp_val == self:
                    setattr(old_value, "Bid45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bid45"):
                opp_val = getattr(value, "Bid45", None)
                setattr(value, "Bid45", self)

    @property
    def hasBeenAssigned(self):
        return self.__hasBeenAssigned

    @hasBeenAssigned.setter
    def hasBeenAssigned(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__hasBeenAssigned", None)
        self.__hasBeenAssigned = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reviewer49"):
                opp_val = getattr(old_value, "Reviewer49", None)
                if opp_val == self:
                    setattr(old_value, "Reviewer49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reviewer49"):
                opp_val = getattr(value, "Reviewer49", None)
                setattr(value, "Reviewer49", self)

    @property
    def Cocus_Paper55(self):
        return self.__Cocus_Paper55

    @Cocus_Paper55.setter
    def Cocus_Paper55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper55", None)
        self.__Cocus_Paper55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Author"):
                opp_val = getattr(old_value, "Author", None)
                if opp_val == self:
                    setattr(old_value, "Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Author"):
                opp_val = getattr(value, "Author", None)
                setattr(value, "Author", self)

    @property
    def readPaper(self):
        return self.__readPaper

    @readPaper.setter
    def readPaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__readPaper", None)
        self.__readPaper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reviewer53"):
                opp_val = getattr(old_value, "Reviewer53", None)
                if opp_val == self:
                    setattr(old_value, "Reviewer53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reviewer53"):
                opp_val = getattr(value, "Reviewer53", None)
                setattr(value, "Reviewer53", self)

    @property
    def Cocus_Paper63(self):
        return self.__Cocus_Paper63

    @Cocus_Paper63.setter
    def Cocus_Paper63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__Cocus_Paper63", None)
        self.__Cocus_Paper63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Meta_Reviewer"):
                opp_val = getattr(old_value, "Meta_Reviewer", None)
                if opp_val == self:
                    setattr(old_value, "Meta_Reviewer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Meta_Reviewer"):
                opp_val = getattr(value, "Meta_Reviewer", None)
                setattr(value, "Meta_Reviewer", self)

    @property
    def co_writePaper(self):
        return self.__co_writePaper

    @co_writePaper.setter
    def co_writePaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Paper__co_writePaper", None)
        self.__co_writePaper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Co_author"):
                opp_val = getattr(old_value, "Co_author", None)
                if opp_val == self:
                    setattr(old_value, "Co_author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Co_author"):
                opp_val = getattr(value, "Co_author", None)
                setattr(value, "Co_author", self)

class Cocus_Email(Document):

    pass
class Cocus_Submission(Document):

    pass
class Cocus_Template(Document):

    pass
class Cocus_Review(Document):

    pass
class Decision:

    pass
class Cocus_Rejection(Decision):

    pass
class Cocus_Acceptance(Decision):

    pass
class Event:

    pass
class Cocus_Symposium(Event):

    pass
class Cocus_Workshop(Event):

    pass
class Thing:

    pass
class Cocus_Document(Thing):

    pass
class Cocus_Event(Thing):

    pass
class Cocus_Person(Thing):

    def __init__(self, email: str, Cocus_Person: set["Thing"] = None, Cocus_Person121: set["Thing"] = None, Cocus_Person124: "Inforamtion" = None, sent_by: "Activity" = None, Cocus_Person142: "Person" = None, Cocus_Person145: "Document" = None, used_by: "Document" = None, registred_by: "Account" = None, Cocus_Person129: set["Thing"] = None, Cocus_Person132: "Event" = None, Cocus_Person135: set["Thing"] = None, Cocus_Person138: "Person" = None, Thing130: "Cocus_Person" = None, Thing119: "Cocus_Person" = None, Thing136: "Cocus_Person" = None, Thing: "Cocus_User" = None, Thing159: "Cocus_Activity" = None, Thing122: "Cocus_Person" = None):
        self.email = email
        self.Cocus_Person = Cocus_Person if Cocus_Person is not None else set()
        self.Cocus_Person121 = Cocus_Person121 if Cocus_Person121 is not None else set()
        self.Cocus_Person124 = Cocus_Person124
        self.sent_by = sent_by
        self.Cocus_Person142 = Cocus_Person142
        self.Cocus_Person145 = Cocus_Person145
        self.used_by = used_by
        self.registred_by = registred_by
        self.Cocus_Person129 = Cocus_Person129 if Cocus_Person129 is not None else set()
        self.Cocus_Person132 = Cocus_Person132
        self.Cocus_Person135 = Cocus_Person135 if Cocus_Person135 is not None else set()
        self.Cocus_Person138 = Cocus_Person138
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def Cocus_Person129(self):
        return self.__Cocus_Person129

    @Cocus_Person129.setter
    def Cocus_Person129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person129", None)
        self.__Cocus_Person129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Thing130"):
                    opp_val = getattr(item, "Thing130", None)
                    
                    if opp_val == self:
                        setattr(item, "Thing130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Thing130"):
                    opp_val = getattr(item, "Thing130", None)
                    
                    setattr(item, "Thing130", self)
                    

    @property
    def Cocus_Person135(self):
        return self.__Cocus_Person135

    @Cocus_Person135.setter
    def Cocus_Person135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person135", None)
        self.__Cocus_Person135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Thing136"):
                    opp_val = getattr(item, "Thing136", None)
                    
                    if opp_val == self:
                        setattr(item, "Thing136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Thing136"):
                    opp_val = getattr(item, "Thing136", None)
                    
                    setattr(item, "Thing136", self)
                    

    @property
    def Cocus_Person121(self):
        return self.__Cocus_Person121

    @Cocus_Person121.setter
    def Cocus_Person121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person121", None)
        self.__Cocus_Person121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Thing122"):
                    opp_val = getattr(item, "Thing122", None)
                    
                    if opp_val == self:
                        setattr(item, "Thing122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Thing122"):
                    opp_val = getattr(item, "Thing122", None)
                    
                    setattr(item, "Thing122", self)
                    

    @property
    def Cocus_Person145(self):
        return self.__Cocus_Person145

    @Cocus_Person145.setter
    def Cocus_Person145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person145", None)
        self.__Cocus_Person145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Document146"):
                opp_val = getattr(old_value, "Document146", None)
                if opp_val == self:
                    setattr(old_value, "Document146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Document146"):
                opp_val = getattr(value, "Document146", None)
                setattr(value, "Document146", self)

    @property
    def sent_by(self):
        return self.__sent_by

    @sent_by.setter
    def sent_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__sent_by", None)
        self.__sent_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def Cocus_Person132(self):
        return self.__Cocus_Person132

    @Cocus_Person132.setter
    def Cocus_Person132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person132", None)
        self.__Cocus_Person132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event133"):
                opp_val = getattr(old_value, "Event133", None)
                if opp_val == self:
                    setattr(old_value, "Event133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event133"):
                opp_val = getattr(value, "Event133", None)
                setattr(value, "Event133", self)

    @property
    def Cocus_Person(self):
        return self.__Cocus_Person

    @Cocus_Person.setter
    def Cocus_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person", None)
        self.__Cocus_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Thing119"):
                    opp_val = getattr(item, "Thing119", None)
                    
                    if opp_val == self:
                        setattr(item, "Thing119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Thing119"):
                    opp_val = getattr(item, "Thing119", None)
                    
                    setattr(item, "Thing119", self)
                    

    @property
    def Cocus_Person142(self):
        return self.__Cocus_Person142

    @Cocus_Person142.setter
    def Cocus_Person142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person142", None)
        self.__Cocus_Person142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person143"):
                opp_val = getattr(old_value, "Person143", None)
                if opp_val == self:
                    setattr(old_value, "Person143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person143"):
                opp_val = getattr(value, "Person143", None)
                setattr(value, "Person143", self)

    @property
    def Cocus_Person124(self):
        return self.__Cocus_Person124

    @Cocus_Person124.setter
    def Cocus_Person124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person124", None)
        self.__Cocus_Person124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Inforamtion"):
                opp_val = getattr(old_value, "Inforamtion", None)
                if opp_val == self:
                    setattr(old_value, "Inforamtion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Inforamtion"):
                opp_val = getattr(value, "Inforamtion", None)
                setattr(value, "Inforamtion", self)

    @property
    def Cocus_Person138(self):
        return self.__Cocus_Person138

    @Cocus_Person138.setter
    def Cocus_Person138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__Cocus_Person138", None)
        self.__Cocus_Person138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person139"):
                opp_val = getattr(old_value, "Person139", None)
                if opp_val == self:
                    setattr(old_value, "Person139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person139"):
                opp_val = getattr(value, "Person139", None)
                setattr(value, "Person139", self)

    @property
    def registred_by(self):
        return self.__registred_by

    @registred_by.setter
    def registred_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__registred_by", None)
        self.__registred_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Account"):
                opp_val = getattr(old_value, "Account", None)
                if opp_val == self:
                    setattr(old_value, "Account", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Account"):
                opp_val = getattr(value, "Account", None)
                setattr(value, "Account", self)

    @property
    def used_by(self):
        return self.__used_by

    @used_by.setter
    def used_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Person__used_by", None)
        self.__used_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Document126"):
                opp_val = getattr(old_value, "Document126", None)
                if opp_val == self:
                    setattr(old_value, "Document126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Document126"):
                opp_val = getattr(value, "Document126", None)
                setattr(value, "Document126", self)

class Cocus_Role(Thing):

    pass
class Cocus_Detail(Thing):

    pass
class Cocus_Conference(Thing, Event):

    def __init__(self, date: str, reviewsPerPaper: str, logoURL: str, acceptsHardcopySubmissions: str, siteURL: str, Cocus_Conference25: "Administrator" = None, Cocus_Conference28: "Administrator" = None, Cocus_Conference31: "Administrator" = None, memberOfConference: "ConferenceMember" = None, Cocus_Conference: "Administrator" = None, Cocus_Conference16: "Administrator" = None, Cocus_Conference19: "Administrator" = None, Cocus_Conference22: "Administrator" = None, Thing130: "Cocus_Person" = None, Thing119: "Cocus_Person" = None, Thing136: "Cocus_Person" = None, Thing: "Cocus_User" = None, Thing159: "Cocus_Activity" = None, Thing122: "Cocus_Person" = None, Event155: "Cocus_Event_URL" = None, Event153: "Cocus_Event_Setup" = None, Event157: "Cocus_Approval_Email" = None, Event133: "Cocus_Person" = None, Event: "Cocus_Administrator" = None):
        self.date = date
        self.reviewsPerPaper = reviewsPerPaper
        self.logoURL = logoURL
        self.acceptsHardcopySubmissions = acceptsHardcopySubmissions
        self.siteURL = siteURL
        self.Cocus_Conference25 = Cocus_Conference25
        self.Cocus_Conference28 = Cocus_Conference28
        self.Cocus_Conference31 = Cocus_Conference31
        self.memberOfConference = memberOfConference
        self.Cocus_Conference = Cocus_Conference
        self.Cocus_Conference16 = Cocus_Conference16
        self.Cocus_Conference19 = Cocus_Conference19
        self.Cocus_Conference22 = Cocus_Conference22
        
        pass
    @property
    def logoURL(self):
        return self.__logoURL

    @logoURL.setter
    def logoURL(self, logoURL: str):
        self.__logoURL = logoURL


    @property
    def siteURL(self):
        return self.__siteURL

    @siteURL.setter
    def siteURL(self, siteURL: str):
        self.__siteURL = siteURL


    @property
    def reviewsPerPaper(self):
        return self.__reviewsPerPaper

    @reviewsPerPaper.setter
    def reviewsPerPaper(self, reviewsPerPaper: str):
        self.__reviewsPerPaper = reviewsPerPaper


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


    @property
    def acceptsHardcopySubmissions(self):
        return self.__acceptsHardcopySubmissions

    @acceptsHardcopySubmissions.setter
    def acceptsHardcopySubmissions(self, acceptsHardcopySubmissions: str):
        self.__acceptsHardcopySubmissions = acceptsHardcopySubmissions


    @property
    def Cocus_Conference16(self):
        return self.__Cocus_Conference16

    @Cocus_Conference16.setter
    def Cocus_Conference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference16", None)
        self.__Cocus_Conference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator17"):
                opp_val = getattr(old_value, "Administrator17", None)
                if opp_val == self:
                    setattr(old_value, "Administrator17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator17"):
                opp_val = getattr(value, "Administrator17", None)
                setattr(value, "Administrator17", self)

    @property
    def Cocus_Conference22(self):
        return self.__Cocus_Conference22

    @Cocus_Conference22.setter
    def Cocus_Conference22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference22", None)
        self.__Cocus_Conference22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator23"):
                opp_val = getattr(old_value, "Administrator23", None)
                if opp_val == self:
                    setattr(old_value, "Administrator23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator23"):
                opp_val = getattr(value, "Administrator23", None)
                setattr(value, "Administrator23", self)

    @property
    def Cocus_Conference(self):
        return self.__Cocus_Conference

    @Cocus_Conference.setter
    def Cocus_Conference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference", None)
        self.__Cocus_Conference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator14"):
                opp_val = getattr(old_value, "Administrator14", None)
                if opp_val == self:
                    setattr(old_value, "Administrator14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator14"):
                opp_val = getattr(value, "Administrator14", None)
                setattr(value, "Administrator14", self)

    @property
    def Cocus_Conference19(self):
        return self.__Cocus_Conference19

    @Cocus_Conference19.setter
    def Cocus_Conference19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference19", None)
        self.__Cocus_Conference19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator20"):
                opp_val = getattr(old_value, "Administrator20", None)
                if opp_val == self:
                    setattr(old_value, "Administrator20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator20"):
                opp_val = getattr(value, "Administrator20", None)
                setattr(value, "Administrator20", self)

    @property
    def Cocus_Conference25(self):
        return self.__Cocus_Conference25

    @Cocus_Conference25.setter
    def Cocus_Conference25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference25", None)
        self.__Cocus_Conference25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator26"):
                opp_val = getattr(old_value, "Administrator26", None)
                if opp_val == self:
                    setattr(old_value, "Administrator26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator26"):
                opp_val = getattr(value, "Administrator26", None)
                setattr(value, "Administrator26", self)

    @property
    def memberOfConference(self):
        return self.__memberOfConference

    @memberOfConference.setter
    def memberOfConference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__memberOfConference", None)
        self.__memberOfConference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConferenceMember"):
                opp_val = getattr(old_value, "ConferenceMember", None)
                if opp_val == self:
                    setattr(old_value, "ConferenceMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConferenceMember"):
                opp_val = getattr(value, "ConferenceMember", None)
                setattr(value, "ConferenceMember", self)

    @property
    def Cocus_Conference31(self):
        return self.__Cocus_Conference31

    @Cocus_Conference31.setter
    def Cocus_Conference31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference31", None)
        self.__Cocus_Conference31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator32"):
                opp_val = getattr(old_value, "Administrator32", None)
                if opp_val == self:
                    setattr(old_value, "Administrator32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator32"):
                opp_val = getattr(value, "Administrator32", None)
                setattr(value, "Administrator32", self)

    @property
    def Cocus_Conference28(self):
        return self.__Cocus_Conference28

    @Cocus_Conference28.setter
    def Cocus_Conference28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_Conference__Cocus_Conference28", None)
        self.__Cocus_Conference28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator29"):
                opp_val = getattr(old_value, "Administrator29", None)
                if opp_val == self:
                    setattr(old_value, "Administrator29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator29"):
                opp_val = getattr(value, "Administrator29", None)
                setattr(value, "Administrator29", self)

class Conference:

    pass
class Person:

    pass
class Cocus_User(Person):

    pass
class Cocus_ExternalReviewer(Person):

    pass
class Cocus_ConferenceMember(Person):

    pass
class Chairman:

    pass
class Administrator:

    pass
class User:

    pass
class Cocus_Administrator(User, Person):

    pass
class Cocus_Committee(User):

    pass
class ConferenceMember:

    pass
class Cocus_Chairman(ConferenceMember, Person):

    pass
class Cocus_AssociatedChair(ConferenceMember, Chairman):

    pass
class Cocus_ConferenceChair(ConferenceMember, Chairman):

    pass
class Cocus_Author(ConferenceMember, User):

    pass
class Cocus_ProgramCommitteeMember(ConferenceMember, Person):

    def __init__(self, maxPapers: str, hasProgramCommitteeMember: "ProgramCommittee" = None, Cocus_ProgramCommitteeMember: "Administrator" = None, ConferenceMember: "Cocus_Conference" = None, Person: "Cocus_Account" = None, Person161: "Cocus_Activity" = None, Person149: "Cocus_Document" = None, Person143: "Cocus_Person" = None, Person139: "Cocus_Person" = None):
        self.maxPapers = maxPapers
        self.hasProgramCommitteeMember = hasProgramCommitteeMember
        self.Cocus_ProgramCommitteeMember = Cocus_ProgramCommitteeMember
        
        pass
    @property
    def maxPapers(self):
        return self.__maxPapers

    @maxPapers.setter
    def maxPapers(self, maxPapers: str):
        self.__maxPapers = maxPapers


    @property
    def hasProgramCommitteeMember(self):
        return self.__hasProgramCommitteeMember

    @hasProgramCommitteeMember.setter
    def hasProgramCommitteeMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_ProgramCommitteeMember__hasProgramCommitteeMember", None)
        self.__hasProgramCommitteeMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProgramCommittee"):
                opp_val = getattr(old_value, "ProgramCommittee", None)
                if opp_val == self:
                    setattr(old_value, "ProgramCommittee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProgramCommittee"):
                opp_val = getattr(value, "ProgramCommittee", None)
                setattr(value, "ProgramCommittee", self)

    @property
    def Cocus_ProgramCommitteeMember(self):
        return self.__Cocus_ProgramCommitteeMember

    @Cocus_ProgramCommitteeMember.setter
    def Cocus_ProgramCommitteeMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cocus_ProgramCommitteeMember__Cocus_ProgramCommitteeMember", None)
        self.__Cocus_ProgramCommitteeMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator36"):
                opp_val = getattr(old_value, "Administrator36", None)
                if opp_val == self:
                    setattr(old_value, "Administrator36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator36"):
                opp_val = getattr(value, "Administrator36", None)
                setattr(value, "Administrator36", self)

class Cocus_Reviewer(ConferenceMember, User):

    pass
class Reviewer:

    pass
class Cocus_Meta_Reviewer(Reviewer):

    pass
class Cocus_Thing:

    pass
class Cocus_Bid:

    pass
class ProgramCommitteeMember:

    pass
class Cocus_ProgramCommitteeChair(ProgramCommitteeMember, Chairman):

    pass
class Cocus_ProgramCommittee:

    pass
class Cocus_Preference:

    pass
class Cocus_Decision:

    pass
class ExternalReviewer:

    pass
class Review:

    pass
class Cocus_Meta_Review(Review):

    pass
class Paper:

    pass
class Cocus_PaperAbstract(Paper):

    pass
class Cocus_Invited_Paper(Paper):

    pass
class Cocus_Full_Paper(Paper):

    pass
class Cocus_PaperFullVersion(Paper):

    pass
class Cocus_Abstract(Paper):

    pass
class Cocus_Short_Paper(Paper):

    pass
class Bid:

    pass
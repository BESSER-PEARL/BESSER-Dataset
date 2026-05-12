from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SubjectArea:

    pass
class Meta_Reviewer:

    pass
class ProgramCommittee:

    pass
class Conference:

    pass
class Person:

    pass
class cmt_User(Person):

    pass
class cmt_ConferenceMember(Person):

    pass
class Co_author:

    pass
class Decision:

    pass
class cmt_Rejection(Decision):

    pass
class cmt_Acceptance(Decision):

    pass
class cmt_ExternalReviewer(Person):

    pass
class cmt_SubjectArea:

    pass
class Author:

    pass
class cmt_Co_author(Author):

    pass
class cmt_AuthorNotReviewer(Author):

    pass
class cmt_Bid:

    pass
class ProgramCommitteeMember:

    pass
class cmt_ProgramCommittee:

    pass
class cmt_Preference:

    pass
class cmt_Document:

    pass
class Chairman:

    pass
class cmt_ProgramCommitteeChair(ProgramCommitteeMember, Chairman):

    pass
class Thing:

    pass
class cmt_Conference(Thing):

    def __init__(self, date: str, reviewsPerPaper: str, logoURL: str, acceptsHardcopySubmissions: str, siteURL: str, memberOfConference: "ConferenceMember" = None, finalizePaperAssignment: "Administrator" = None, enterReviewCriteria: "Administrator" = None, runPaperAssignmentTools: "Administrator" = None, enableVirtualMeeting: "Administrator" = None, printHardcopyMailingManifests: "Administrator" = None, enterConferenceDetails: "Administrator" = None, startReviewerBidding: "Administrator" = None):
        self.date = date
        self.reviewsPerPaper = reviewsPerPaper
        self.logoURL = logoURL
        self.acceptsHardcopySubmissions = acceptsHardcopySubmissions
        self.siteURL = siteURL
        self.memberOfConference = memberOfConference
        self.finalizePaperAssignment = finalizePaperAssignment
        self.enterReviewCriteria = enterReviewCriteria
        self.runPaperAssignmentTools = runPaperAssignmentTools
        self.enableVirtualMeeting = enableVirtualMeeting
        self.printHardcopyMailingManifests = printHardcopyMailingManifests
        self.enterConferenceDetails = enterConferenceDetails
        self.startReviewerBidding = startReviewerBidding
        
        pass
    @property
    def acceptsHardcopySubmissions(self):
        return self.__acceptsHardcopySubmissions

    @acceptsHardcopySubmissions.setter
    def acceptsHardcopySubmissions(self, acceptsHardcopySubmissions: str):
        self.__acceptsHardcopySubmissions = acceptsHardcopySubmissions


    @property
    def logoURL(self):
        return self.__logoURL

    @logoURL.setter
    def logoURL(self, logoURL: str):
        self.__logoURL = logoURL


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


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
    def memberOfConference(self):
        return self.__memberOfConference

    @memberOfConference.setter
    def memberOfConference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__memberOfConference", None)
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
    def enableVirtualMeeting(self):
        return self.__enableVirtualMeeting

    @enableVirtualMeeting.setter
    def enableVirtualMeeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__enableVirtualMeeting", None)
        self.__enableVirtualMeeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator18"):
                opp_val = getattr(old_value, "Administrator18", None)
                if opp_val == self:
                    setattr(old_value, "Administrator18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator18"):
                opp_val = getattr(value, "Administrator18", None)
                setattr(value, "Administrator18", self)

    @property
    def runPaperAssignmentTools(self):
        return self.__runPaperAssignmentTools

    @runPaperAssignmentTools.setter
    def runPaperAssignmentTools(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__runPaperAssignmentTools", None)
        self.__runPaperAssignmentTools = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator16"):
                opp_val = getattr(old_value, "Administrator16", None)
                if opp_val == self:
                    setattr(old_value, "Administrator16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator16"):
                opp_val = getattr(value, "Administrator16", None)
                setattr(value, "Administrator16", self)

    @property
    def finalizePaperAssignment(self):
        return self.__finalizePaperAssignment

    @finalizePaperAssignment.setter
    def finalizePaperAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__finalizePaperAssignment", None)
        self.__finalizePaperAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator12"):
                opp_val = getattr(old_value, "Administrator12", None)
                if opp_val == self:
                    setattr(old_value, "Administrator12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator12"):
                opp_val = getattr(value, "Administrator12", None)
                setattr(value, "Administrator12", self)

    @property
    def startReviewerBidding(self):
        return self.__startReviewerBidding

    @startReviewerBidding.setter
    def startReviewerBidding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__startReviewerBidding", None)
        self.__startReviewerBidding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator24"):
                opp_val = getattr(old_value, "Administrator24", None)
                if opp_val == self:
                    setattr(old_value, "Administrator24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator24"):
                opp_val = getattr(value, "Administrator24", None)
                setattr(value, "Administrator24", self)

    @property
    def enterReviewCriteria(self):
        return self.__enterReviewCriteria

    @enterReviewCriteria.setter
    def enterReviewCriteria(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__enterReviewCriteria", None)
        self.__enterReviewCriteria = value
        
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
    def enterConferenceDetails(self):
        return self.__enterConferenceDetails

    @enterConferenceDetails.setter
    def enterConferenceDetails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__enterConferenceDetails", None)
        self.__enterConferenceDetails = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator22"):
                opp_val = getattr(old_value, "Administrator22", None)
                if opp_val == self:
                    setattr(old_value, "Administrator22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator22"):
                opp_val = getattr(value, "Administrator22", None)
                setattr(value, "Administrator22", self)

    @property
    def printHardcopyMailingManifests(self):
        return self.__printHardcopyMailingManifests

    @printHardcopyMailingManifests.setter
    def printHardcopyMailingManifests(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Conference__printHardcopyMailingManifests", None)
        self.__printHardcopyMailingManifests = value
        
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

class Document:

    pass
class cmt_Review(Document):

    pass
class cmt_Paper(Document):

    def __init__(self, paperID: str, title: str, co_writePaper: "Co_author" = None, cmt_Paper: "Bid" = None, cmt_Paper39: "Decision" = None, hasBeenAssigned: "Reviewer" = None, acceptPaper: "Administrator" = None, rejectPaper: "Administrator" = None, cmt_Paper52: "Meta_Reviewer" = None, cmt_Paper43: "SubjectArea" = None, readPaper: "Reviewer" = None, writePaper: "Author" = None, Document: "cmt_Person" = None):
        self.paperID = paperID
        self.title = title
        self.co_writePaper = co_writePaper
        self.cmt_Paper = cmt_Paper
        self.cmt_Paper39 = cmt_Paper39
        self.hasBeenAssigned = hasBeenAssigned
        self.acceptPaper = acceptPaper
        self.rejectPaper = rejectPaper
        self.cmt_Paper52 = cmt_Paper52
        self.cmt_Paper43 = cmt_Paper43
        self.readPaper = readPaper
        self.writePaper = writePaper
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def paperID(self):
        return self.__paperID

    @paperID.setter
    def paperID(self, paperID: str):
        self.__paperID = paperID


    @property
    def acceptPaper(self):
        return self.__acceptPaper

    @acceptPaper.setter
    def acceptPaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__acceptPaper", None)
        self.__acceptPaper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator48"):
                opp_val = getattr(old_value, "Administrator48", None)
                if opp_val == self:
                    setattr(old_value, "Administrator48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator48"):
                opp_val = getattr(value, "Administrator48", None)
                setattr(value, "Administrator48", self)

    @property
    def cmt_Paper43(self):
        return self.__cmt_Paper43

    @cmt_Paper43.setter
    def cmt_Paper43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__cmt_Paper43", None)
        self.__cmt_Paper43 = value
        
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
    def readPaper(self):
        return self.__readPaper

    @readPaper.setter
    def readPaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__readPaper", None)
        self.__readPaper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reviewer45"):
                opp_val = getattr(old_value, "Reviewer45", None)
                if opp_val == self:
                    setattr(old_value, "Reviewer45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reviewer45"):
                opp_val = getattr(value, "Reviewer45", None)
                setattr(value, "Reviewer45", self)

    @property
    def cmt_Paper(self):
        return self.__cmt_Paper

    @cmt_Paper.setter
    def cmt_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__cmt_Paper", None)
        self.__cmt_Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bid37"):
                opp_val = getattr(old_value, "Bid37", None)
                if opp_val == self:
                    setattr(old_value, "Bid37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bid37"):
                opp_val = getattr(value, "Bid37", None)
                setattr(value, "Bid37", self)

    @property
    def hasBeenAssigned(self):
        return self.__hasBeenAssigned

    @hasBeenAssigned.setter
    def hasBeenAssigned(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__hasBeenAssigned", None)
        self.__hasBeenAssigned = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reviewer41"):
                opp_val = getattr(old_value, "Reviewer41", None)
                if opp_val == self:
                    setattr(old_value, "Reviewer41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reviewer41"):
                opp_val = getattr(value, "Reviewer41", None)
                setattr(value, "Reviewer41", self)

    @property
    def cmt_Paper52(self):
        return self.__cmt_Paper52

    @cmt_Paper52.setter
    def cmt_Paper52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__cmt_Paper52", None)
        self.__cmt_Paper52 = value
        
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
    def cmt_Paper39(self):
        return self.__cmt_Paper39

    @cmt_Paper39.setter
    def cmt_Paper39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__cmt_Paper39", None)
        self.__cmt_Paper39 = value
        
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
    def writePaper(self):
        return self.__writePaper

    @writePaper.setter
    def writePaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__writePaper", None)
        self.__writePaper = value
        
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
    def co_writePaper(self):
        return self.__co_writePaper

    @co_writePaper.setter
    def co_writePaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__co_writePaper", None)
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

    @property
    def rejectPaper(self):
        return self.__rejectPaper

    @rejectPaper.setter
    def rejectPaper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Paper__rejectPaper", None)
        self.__rejectPaper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator50"):
                opp_val = getattr(old_value, "Administrator50", None)
                if opp_val == self:
                    setattr(old_value, "Administrator50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator50"):
                opp_val = getattr(value, "Administrator50", None)
                setattr(value, "Administrator50", self)

class cmt_Person:

    def __init__(self, email: str, cmt_Person: "Document" = None):
        self.email = email
        self.cmt_Person = cmt_Person
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def cmt_Person(self):
        return self.__cmt_Person

    @cmt_Person.setter
    def cmt_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_Person__cmt_Person", None)
        self.__cmt_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Document"):
                opp_val = getattr(old_value, "Document", None)
                if opp_val == self:
                    setattr(old_value, "Document", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Document"):
                opp_val = getattr(value, "Document", None)
                setattr(value, "Document", self)

class cmt_Decision:

    pass
class ExternalReviewer:

    pass
class Review:

    pass
class cmt_Meta_Review(Review):

    pass
class Paper:

    pass
class cmt_PaperFullVersion(Paper):

    pass
class cmt_PaperAbstract(Paper):

    pass
class Bid:

    pass
class Administrator:

    pass
class User:

    pass
class cmt_Administrator(User):

    pass
class ConferenceMember:

    pass
class cmt_AssociatedChair(ConferenceMember, Chairman):

    pass
class cmt_ProgramCommitteeMember(ConferenceMember, Person):

    def __init__(self, maxPapers: str, hasProgramCommitteeMember: "ProgramCommittee" = None, addProgramCommitteeMember: "Administrator" = None, ConferenceMember: "cmt_Conference" = None):
        self.maxPapers = maxPapers
        self.hasProgramCommitteeMember = hasProgramCommitteeMember
        self.addProgramCommitteeMember = addProgramCommitteeMember
        
        pass
    @property
    def maxPapers(self):
        return self.__maxPapers

    @maxPapers.setter
    def maxPapers(self, maxPapers: str):
        self.__maxPapers = maxPapers


    @property
    def addProgramCommitteeMember(self):
        return self.__addProgramCommitteeMember

    @addProgramCommitteeMember.setter
    def addProgramCommitteeMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_ProgramCommitteeMember__addProgramCommitteeMember", None)
        self.__addProgramCommitteeMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator28"):
                opp_val = getattr(old_value, "Administrator28", None)
                if opp_val == self:
                    setattr(old_value, "Administrator28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator28"):
                opp_val = getattr(value, "Administrator28", None)
                setattr(value, "Administrator28", self)

    @property
    def hasProgramCommitteeMember(self):
        return self.__hasProgramCommitteeMember

    @hasProgramCommitteeMember.setter
    def hasProgramCommitteeMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmt_ProgramCommitteeMember__hasProgramCommitteeMember", None)
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

class cmt_Chairman(ConferenceMember, Person):

    pass
class cmt_ConferenceChair(ConferenceMember, Chairman):

    pass
class cmt_Author(ConferenceMember, User):

    pass
class cmt_Reviewer(ConferenceMember, User):

    pass
class Reviewer:

    pass
class cmt_Meta_Reviewer(Reviewer):

    pass
class cmt_Thing:

    pass
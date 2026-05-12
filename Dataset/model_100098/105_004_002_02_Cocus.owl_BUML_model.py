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
Bid = Class(name="Bid")
Paper = Class(name="Paper")
Review = Class(name="Review")
ExternalReviewer = Class(name="ExternalReviewer")
Cocus_Decision = Class(name="Cocus_Decision")
Cocus_Preference = Class(name="Cocus_Preference")
Cocus_ProgramCommittee = Class(name="Cocus_ProgramCommittee")
ProgramCommitteeMember = Class(name="ProgramCommitteeMember")
Cocus_Bid = Class(name="Cocus_Bid")
Cocus_Thing = Class(name="Cocus_Thing")
Cocus_Meta_Reviewer = Class(name="Cocus_Meta_Reviewer")
Reviewer = Class(name="Reviewer")
Cocus_Reviewer = Class(name="Cocus_Reviewer")
ConferenceMember = Class(name="ConferenceMember")
User = Class(name="User")
Administrator = Class(name="Administrator")
Cocus_ConferenceChair = Class(name="Cocus_ConferenceChair")
Chairman = Class(name="Chairman")
Cocus_ConferenceMember = Class(name="Cocus_ConferenceMember")
Person = Class(name="Person")
Conference = Class(name="Conference")
Cocus_Conference = Class(name="Cocus_Conference")
Thing = Class(name="Thing")
Event = Class(name="Event")
Cocus_Chairman = Class(name="Cocus_Chairman")
Cocus_ProgramCommitteeChair = Class(name="Cocus_ProgramCommitteeChair")
Cocus_Acceptance = Class(name="Cocus_Acceptance")
Decision = Class(name="Decision")
Cocus_Rejection = Class(name="Cocus_Rejection")
Cocus_Review = Class(name="Cocus_Review")
Document = Class(name="Document")
Cocus_Paper = Class(name="Cocus_Paper")
Co_author = Class(name="Co_author")
Cocus_AssociatedChair = Class(name="Cocus_AssociatedChair")
Cocus_ProgramCommitteeMember = Class(name="Cocus_ProgramCommitteeMember")
ProgramCommittee = Class(name="ProgramCommittee")
Cocus_AuthorNotReviewer = Class(name="Cocus_AuthorNotReviewer")
Author = Class(name="Author")
Cocus_SubjectArea = Class(name="Cocus_SubjectArea")
Cocus_ExternalReviewer = Class(name="Cocus_ExternalReviewer")
Cocus_Author = Class(name="Cocus_Author")
Cocus_Co_author = Class(name="Cocus_Co_author")
Cocus_PaperAbstract = Class(name="Cocus_PaperAbstract")
Cocus_PaperFullVersion = Class(name="Cocus_PaperFullVersion")
Cocus_Administrator = Class(name="Cocus_Administrator")
SubjectArea = Class(name="SubjectArea")
Meta_Reviewer = Class(name="Meta_Reviewer")
Cocus_Meta_Review = Class(name="Cocus_Meta-Review")
Cocus_Workshop = Class(name="Cocus_Workshop")
Cocus_Event = Class(name="Cocus_Event")
Event_Tracks = Class(name="Event_Tracks")
Role = Class(name="Role")
Cocus_Role = Class(name="Cocus_Role")
Cocus_Help_Request = Class(name="Cocus_Help_Request")
Request = Class(name="Request")
Cocus_Person = Class(name="Cocus_Person")
Inforamtion = Class(name="Inforamtion")
Approval_Email = Class(name="Approval_Email")
Event_Setup = Class(name="Event_Setup")
Cocus_Account = Class(name="Cocus_Account")
Cocus_Inforamtion = Class(name="Cocus_Inforamtion")
Cocus_User = Class(name="Cocus_User")
Activity = Class(name="Activity")
Cocus_Symposium = Class(name="Cocus_Symposium")
Cocus_Abstract = Class(name="Cocus_Abstract")
Cocus_Document = Class(name="Cocus_Document")
Account = Class(name="Account")
Cocus_URL = Class(name="Cocus_URL")
Cocus_Notification_Email = Class(name="Cocus_Notification_Email")
Email = Class(name="Email")
Cocus_Email = Class(name="Cocus_Email")
Cocus_Short_Paper = Class(name="Cocus_Short_Paper")
Cocus_Author_Role = Class(name="Cocus_Author_Role")
Cocus_Preview = Class(name="Cocus_Preview")
Review_Form = Class(name="Review_Form")
Cocus_Review_Form = Class(name="Cocus_Review_Form")
Cocus_Committe_Role = Class(name="Cocus_Committe_Role")
Cocus_Group_Email = Class(name="Cocus_Group_Email")
Cocus_Submission_Template = Class(name="Cocus_Submission_Template")
Cocus_Review_Form_Setup = Class(name="Cocus_Review_Form_Setup")
Cocus_Misc = Class(name="Cocus_Misc")
Help_Request = Class(name="Help_Request")
Cocus_Event_Creation = Class(name="Cocus_Event_Creation")
Cocus_Approval_Email = Class(name="Cocus_Approval_Email")
Cocus_Invited_Paper = Class(name="Cocus_Invited_Paper")
Cocus_Admin_Role = Class(name="Cocus_Admin_Role")
Cocus_Paper_Typologies = Class(name="Cocus_Paper_Typologies")
Cocus_Event_Setup = Class(name="Cocus_Event_Setup")
Cocus_Event_URL = Class(name="Cocus_Event_URL")
URL = Class(name="URL")
Cocus_Head_Role = Class(name="Cocus_Head_Role")
Cocus_Detail = Class(name="Cocus_Detail")
Cocus_Corresponding_Author = Class(name="Cocus_Corresponding_Author")
Cocus_Reviewer_Role = Class(name="Cocus_Reviewer_Role")
Cocus_Event_Approval = Class(name="Cocus_Event_Approval")
Cocus_Registration = Class(name="Cocus_Registration")
Cocus_Full_Paper = Class(name="Cocus_Full_Paper")
Cocus_Research_Topic = Class(name="Cocus_Research_Topic")
Cocus_Description = Class(name="Cocus_Description")
Cocus_Assistance = Class(name="Cocus_Assistance")
Cocus_Email_Template = Class(name="Cocus_Email_Template")
Cocus_Rejection_Email = Class(name="Cocus_Rejection_Email")
Cocus_Submission = Class(name="Cocus_Submission")
Cocus_Template = Class(name="Cocus_Template")
Cocus_Feature_Request = Class(name="Cocus_Feature_Request")
Cocus_Committee = Class(name="Cocus_Committee")
Cocus_Event_Tracks = Class(name="Cocus_Event_Tracks")
Cocus_Request = Class(name="Cocus_Request")
Cocus_Activity = Class(name="Cocus_Activity")

# Bid class attributes and methods

# Paper class attributes and methods

# Review class attributes and methods

# ExternalReviewer class attributes and methods

# Cocus_Decision class attributes and methods

# Cocus_Preference class attributes and methods

# Cocus_ProgramCommittee class attributes and methods

# ProgramCommitteeMember class attributes and methods

# Cocus_Bid class attributes and methods

# Cocus_Thing class attributes and methods

# Cocus_Meta_Reviewer class attributes and methods

# Reviewer class attributes and methods

# Cocus_Reviewer class attributes and methods

# ConferenceMember class attributes and methods

# User class attributes and methods

# Administrator class attributes and methods

# Cocus_ConferenceChair class attributes and methods

# Chairman class attributes and methods

# Cocus_ConferenceMember class attributes and methods

# Person class attributes and methods

# Conference class attributes and methods

# Cocus_Conference class attributes and methods
Cocus_Conference_date: Property = Property(name="date", type=StringType)
Cocus_Conference_reviewsPerPaper: Property = Property(name="reviewsPerPaper", type=StringType)
Cocus_Conference_logoURL: Property = Property(name="logoURL", type=StringType)
Cocus_Conference_acceptsHardcopySubmissions: Property = Property(name="acceptsHardcopySubmissions", type=StringType)
Cocus_Conference_siteURL: Property = Property(name="siteURL", type=StringType)
Cocus_Conference.attributes={Cocus_Conference_siteURL, Cocus_Conference_logoURL, Cocus_Conference_reviewsPerPaper, Cocus_Conference_date, Cocus_Conference_acceptsHardcopySubmissions}

# Thing class attributes and methods

# Event class attributes and methods

# Cocus_Chairman class attributes and methods

# Cocus_ProgramCommitteeChair class attributes and methods

# Cocus_Acceptance class attributes and methods

# Decision class attributes and methods

# Cocus_Rejection class attributes and methods

# Cocus_Review class attributes and methods

# Document class attributes and methods

# Cocus_Paper class attributes and methods
Cocus_Paper_paperID: Property = Property(name="paperID", type=StringType)
Cocus_Paper_title: Property = Property(name="title", type=StringType)
Cocus_Paper.attributes={Cocus_Paper_paperID, Cocus_Paper_title}

# Co_author class attributes and methods

# Cocus_AssociatedChair class attributes and methods

# Cocus_ProgramCommitteeMember class attributes and methods
Cocus_ProgramCommitteeMember_maxPapers: Property = Property(name="maxPapers", type=StringType)
Cocus_ProgramCommitteeMember.attributes={Cocus_ProgramCommitteeMember_maxPapers}

# ProgramCommittee class attributes and methods

# Cocus_AuthorNotReviewer class attributes and methods

# Author class attributes and methods

# Cocus_SubjectArea class attributes and methods

# Cocus_ExternalReviewer class attributes and methods

# Cocus_Author class attributes and methods

# Cocus_Co_author class attributes and methods

# Cocus_PaperAbstract class attributes and methods

# Cocus_PaperFullVersion class attributes and methods

# Cocus_Administrator class attributes and methods

# SubjectArea class attributes and methods

# Meta_Reviewer class attributes and methods

# Cocus_Meta_Review class attributes and methods

# Cocus_Workshop class attributes and methods

# Cocus_Event class attributes and methods

# Event_Tracks class attributes and methods

# Role class attributes and methods

# Cocus_Role class attributes and methods

# Cocus_Help_Request class attributes and methods

# Request class attributes and methods

# Cocus_Person class attributes and methods
Cocus_Person_email: Property = Property(name="email", type=StringType)
Cocus_Person.attributes={Cocus_Person_email}

# Inforamtion class attributes and methods

# Approval_Email class attributes and methods

# Event_Setup class attributes and methods

# Cocus_Account class attributes and methods

# Cocus_Inforamtion class attributes and methods

# Cocus_User class attributes and methods

# Activity class attributes and methods

# Cocus_Symposium class attributes and methods

# Cocus_Abstract class attributes and methods

# Cocus_Document class attributes and methods

# Account class attributes and methods

# Cocus_URL class attributes and methods

# Cocus_Notification_Email class attributes and methods

# Email class attributes and methods

# Cocus_Email class attributes and methods

# Cocus_Short_Paper class attributes and methods

# Cocus_Author_Role class attributes and methods

# Cocus_Preview class attributes and methods

# Review_Form class attributes and methods

# Cocus_Review_Form class attributes and methods

# Cocus_Committe_Role class attributes and methods

# Cocus_Group_Email class attributes and methods

# Cocus_Submission_Template class attributes and methods

# Cocus_Review_Form_Setup class attributes and methods

# Cocus_Misc class attributes and methods

# Help_Request class attributes and methods

# Cocus_Event_Creation class attributes and methods

# Cocus_Approval_Email class attributes and methods

# Cocus_Invited_Paper class attributes and methods

# Cocus_Admin_Role class attributes and methods

# Cocus_Paper_Typologies class attributes and methods

# Cocus_Event_Setup class attributes and methods

# Cocus_Event_URL class attributes and methods

# URL class attributes and methods

# Cocus_Head_Role class attributes and methods

# Cocus_Detail class attributes and methods

# Cocus_Corresponding_Author class attributes and methods

# Cocus_Reviewer_Role class attributes and methods

# Cocus_Event_Approval class attributes and methods

# Cocus_Registration class attributes and methods

# Cocus_Full_Paper class attributes and methods

# Cocus_Research_Topic class attributes and methods

# Cocus_Description class attributes and methods

# Cocus_Assistance class attributes and methods

# Cocus_Email_Template class attributes and methods

# Cocus_Rejection_Email class attributes and methods

# Cocus_Submission class attributes and methods

# Cocus_Template class attributes and methods

# Cocus_Feature_Request class attributes and methods

# Cocus_Committee class attributes and methods

# Cocus_Event_Tracks class attributes and methods

# Cocus_Request class attributes and methods

# Cocus_Activity class attributes and methods

# Relationships
adjustBid1: BinaryAssociation = BinaryAssociation(
    name="adjustBid1",
    ends={
        Property(name="Bid", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="adjustedBy", type=Bid, multiplicity=Multiplicity(0, 1))
    }
)
readPaper2: BinaryAssociation = BinaryAssociation(
    name="readPaper2",
    ends={
        Property(name="Paper", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Reviewer3", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
hasBeenAssigned4: BinaryAssociation = BinaryAssociation(
    name="hasBeenAssigned4",
    ends={
        Property(name="Paper6", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Reviewer5", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
writeReview7: BinaryAssociation = BinaryAssociation(
    name="writeReview7",
    ends={
        Property(name="Review", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Reviewer8", type=Review, multiplicity=Multiplicity(0, 1))
    }
)
assignExternalReviewer9: BinaryAssociation = BinaryAssociation(
    name="assignExternalReviewer9",
    ends={
        Property(name="ExternalReviewer", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedByReviewer", type=ExternalReviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasProgramCommitteeMember10: BinaryAssociation = BinaryAssociation(
    name="hasProgramCommitteeMember10",
    ends={
        Property(name="ProgramCommitteeMember", type=Cocus_ProgramCommittee, multiplicity=Multiplicity(1, 1)),
        Property(name="memberOfProgramCommittee", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
assignedByAdministrator0: BinaryAssociation = BinaryAssociation(
    name="assignedByAdministrator0",
    ends={
        Property(name="Administrator", type=Cocus_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Reviewer", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
hardcopyMailingManifestsPrintedBy24: BinaryAssociation = BinaryAssociation(
    name="hardcopyMailingManifestsPrintedBy24",
    ends={
        Property(name="Administrator26", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference25", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
detailsEnteredBy27: BinaryAssociation = BinaryAssociation(
    name="detailsEnteredBy27",
    ends={
        Property(name="Administrator29", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference28", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
reviewerBiddingStartedBy30: BinaryAssociation = BinaryAssociation(
    name="reviewerBiddingStartedBy30",
    ends={
        Property(name="Administrator32", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference31", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
memberOfConference33: BinaryAssociation = BinaryAssociation(
    name="memberOfConference33",
    ends={
        Property(name="Conference", type=Cocus_ConferenceMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_ConferenceMember", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
adjustedBy11: BinaryAssociation = BinaryAssociation(
    name="adjustedBy11",
    ends={
        Property(name="Reviewer", type=Cocus_Bid, multiplicity=Multiplicity(1, 1)),
        Property(name="adjustBid", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasConferenceMember12: BinaryAssociation = BinaryAssociation(
    name="hasConferenceMember12",
    ends={
        Property(name="ConferenceMember", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="memberOfConference", type=ConferenceMember, multiplicity=Multiplicity(0, 1))
    }
)
paperAssignmentFinalizedBy13: BinaryAssociation = BinaryAssociation(
    name="paperAssignmentFinalizedBy13",
    ends={
        Property(name="Administrator14", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
reviewCriteriaEnteredBy15: BinaryAssociation = BinaryAssociation(
    name="reviewCriteriaEnteredBy15",
    ends={
        Property(name="Administrator17", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference16", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
paperAssignmentToolsRunBy18: BinaryAssociation = BinaryAssociation(
    name="paperAssignmentToolsRunBy18",
    ends={
        Property(name="Administrator20", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference19", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
virtualMeetingEnabledBy21: BinaryAssociation = BinaryAssociation(
    name="virtualMeetingEnabledBy21",
    ends={
        Property(name="Administrator23", type=Cocus_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Conference22", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
endReview39: BinaryAssociation = BinaryAssociation(
    name="endReview39",
    ends={
        Property(name="Review40", type=Cocus_ProgramCommitteeChair, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_ProgramCommitteeChair", type=Review, multiplicity=Multiplicity(0, 1))
    }
)
writtenBy41: BinaryAssociation = BinaryAssociation(
    name="writtenBy41",
    ends={
        Property(name="Reviewer42", type=Cocus_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="writeReview", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasCo_author43: BinaryAssociation = BinaryAssociation(
    name="hasCo_author43",
    ends={
        Property(name="Co_author", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="co-writePaper", type=Co_author, multiplicity=Multiplicity(0, 1))
    }
)
hasBid44: BinaryAssociation = BinaryAssociation(
    name="hasBid44",
    ends={
        Property(name="Bid45", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper", type=Bid, multiplicity=Multiplicity(0, 1))
    }
)
hasDecision46: BinaryAssociation = BinaryAssociation(
    name="hasDecision46",
    ends={
        Property(name="Decision", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper47", type=Decision, multiplicity=Multiplicity(0, 1))
    }
)
memberOfProgramCommittee34: BinaryAssociation = BinaryAssociation(
    name="memberOfProgramCommittee34",
    ends={
        Property(name="ProgramCommittee", type=Cocus_ProgramCommitteeMember, multiplicity=Multiplicity(1, 1)),
        Property(name="hasProgramCommitteeMember", type=ProgramCommittee, multiplicity=Multiplicity(0, 1))
    }
)
addedBy35: BinaryAssociation = BinaryAssociation(
    name="addedBy35",
    ends={
        Property(name="Administrator36", type=Cocus_ProgramCommitteeMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_ProgramCommitteeMember", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
assignedByReviewer37: BinaryAssociation = BinaryAssociation(
    name="assignedByReviewer37",
    ends={
        Property(name="Reviewer38", type=Cocus_ExternalReviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignExternalReviewer", type=Reviewer, multiplicity=Multiplicity(1, 1))
    }
)
readByMeta_Reviewer62: BinaryAssociation = BinaryAssociation(
    name="readByMeta_Reviewer62",
    ends={
        Property(name="Meta_Reviewer", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper63", type=Meta_Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
submitPaper64: BinaryAssociation = BinaryAssociation(
    name="submitPaper64",
    ends={
        Property(name="Paper65", type=Cocus_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Author", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
writePaper66: BinaryAssociation = BinaryAssociation(
    name="writePaper66",
    ends={
        Property(name="Paper68", type=Cocus_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Author67", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
co_writePaper69: BinaryAssociation = BinaryAssociation(
    name="co_writePaper69",
    ends={
        Property(name="Paper70", type=Cocus_Co_author, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Co_author", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
approve71: BinaryAssociation = BinaryAssociation(
    name="approve71",
    ends={
        Property(name="Event", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="approved_by", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
assignedTo48: BinaryAssociation = BinaryAssociation(
    name="assignedTo48",
    ends={
        Property(name="Reviewer49", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="hasBeenAssigned", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasSubjectArea50: BinaryAssociation = BinaryAssociation(
    name="hasSubjectArea50",
    ends={
        Property(name="SubjectArea", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper51", type=SubjectArea, multiplicity=Multiplicity(0, 1))
    }
)
readByReviewer52: BinaryAssociation = BinaryAssociation(
    name="readByReviewer52",
    ends={
        Property(name="Reviewer53", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="readPaper", type=Reviewer, multiplicity=Multiplicity(1, 1))
    }
)
hasAuthor54: BinaryAssociation = BinaryAssociation(
    name="hasAuthor54",
    ends={
        Property(name="Author", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper55", type=Author, multiplicity=Multiplicity(0, 1))
    }
)
acceptedBy56: BinaryAssociation = BinaryAssociation(
    name="acceptedBy56",
    ends={
        Property(name="Administrator58", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper57", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
rejectedBy59: BinaryAssociation = BinaryAssociation(
    name="rejectedBy59",
    ends={
        Property(name="Administrator61", type=Cocus_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Paper60", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
printHardcopyMailingManifests92: BinaryAssociation = BinaryAssociation(
    name="printHardcopyMailingManifests92",
    ends={
        Property(name="Conference94", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator93", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
setMaxPapers95: BinaryAssociation = BinaryAssociation(
    name="setMaxPapers95",
    ends={
        Property(name="ProgramCommitteeMember97", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator96", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
enterReviewCriteria98: BinaryAssociation = BinaryAssociation(
    name="enterReviewCriteria98",
    ends={
        Property(name="Conference100", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator99", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
acceptPaper101: BinaryAssociation = BinaryAssociation(
    name="acceptPaper101",
    ends={
        Property(name="Paper103", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator102", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
addProgramCommitteeMember104: BinaryAssociation = BinaryAssociation(
    name="addProgramCommitteeMember104",
    ends={
        Property(name="ProgramCommitteeMember105", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="addedBy", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
assign72: BinaryAssociation = BinaryAssociation(
    name="assign72",
    ends={
        Property(name="Role", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="assigned_by", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
finalizePaperAssignment73: BinaryAssociation = BinaryAssociation(
    name="finalizePaperAssignment73",
    ends={
        Property(name="Conference74", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
runPaperAssignmentTools75: BinaryAssociation = BinaryAssociation(
    name="runPaperAssignmentTools75",
    ends={
        Property(name="Conference77", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator76", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
enableVirtualMeeting78: BinaryAssociation = BinaryAssociation(
    name="enableVirtualMeeting78",
    ends={
        Property(name="Conference80", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator79", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
startReviewerBidding81: BinaryAssociation = BinaryAssociation(
    name="startReviewerBidding81",
    ends={
        Property(name="Conference83", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator82", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
assignReviewer84: BinaryAssociation = BinaryAssociation(
    name="assignReviewer84",
    ends={
        Property(name="Reviewer85", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedByAdministrator", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
rejectPaper86: BinaryAssociation = BinaryAssociation(
    name="rejectPaper86",
    ends={
        Property(name="Paper88", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator87", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
enterConferenceDetails89: BinaryAssociation = BinaryAssociation(
    name="enterConferenceDetails89",
    ends={
        Property(name="Conference91", type=Cocus_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Administrator90", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
create113: BinaryAssociation = BinaryAssociation(
    name="create113",
    ends={
        Property(name="Thing", type=Cocus_User, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_User", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
submit114: BinaryAssociation = BinaryAssociation(
    name="submit114",
    ends={
        Property(name="Document115", type=Cocus_User, multiplicity=Multiplicity(1, 1)),
        Property(name="submited__by", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
assigned_by116: BinaryAssociation = BinaryAssociation(
    name="assigned_by116",
    ends={
        Property(name="Administrator117", type=Cocus_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="assign", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
inverse_of_add118: BinaryAssociation = BinaryAssociation(
    name="inverse_of_add118",
    ends={
        Property(name="Thing119", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
execute120: BinaryAssociation = BinaryAssociation(
    name="execute120",
    ends={
        Property(name="Thing122", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person121", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
get123: BinaryAssociation = BinaryAssociation(
    name="get123",
    ends={
        Property(name="Inforamtion", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person124", type=Inforamtion, multiplicity=Multiplicity(0, 1))
    }
)
conists_of106: BinaryAssociation = BinaryAssociation(
    name="conists_of106",
    ends={
        Property(name="Event_Tracks", type=Cocus_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Event", type=Event_Tracks, multiplicity=Multiplicity(0, 1))
    }
)
confirmed_by107: BinaryAssociation = BinaryAssociation(
    name="confirmed_by107",
    ends={
        Property(name="Approval_Email", type=Cocus_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="confirm", type=Approval_Email, multiplicity=Multiplicity(0, 1))
    }
)
defined_by108: BinaryAssociation = BinaryAssociation(
    name="defined_by108",
    ends={
        Property(name="Event_Setup", type=Cocus_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="define", type=Event_Setup, multiplicity=Multiplicity(0, 1))
    }
)
approved_by109: BinaryAssociation = BinaryAssociation(
    name="approved_by109",
    ends={
        Property(name="Administrator110", type=Cocus_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="approve", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
registred_by111: BinaryAssociation = BinaryAssociation(
    name="registred_by111",
    ends={
        Property(name="Person", type=Cocus_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="register", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
recieve112: BinaryAssociation = BinaryAssociation(
    name="recieve112",
    ends={
        Property(name="Document", type=Cocus_User, multiplicity=Multiplicity(1, 1)),
        Property(name="recieved_by", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
send140: BinaryAssociation = BinaryAssociation(
    name="send140",
    ends={
        Property(name="Activity", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="sent_by", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)
added_by141: BinaryAssociation = BinaryAssociation(
    name="added_by141",
    ends={
        Property(name="Person143", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person142", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
hasConflictOfInterest144: BinaryAssociation = BinaryAssociation(
    name="hasConflictOfInterest144",
    ends={
        Property(name="Document146", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person145", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
recieved_by147: BinaryAssociation = BinaryAssociation(
    name="recieved_by147",
    ends={
        Property(name="User", type=Cocus_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="recieve", type=User, multiplicity=Multiplicity(0, 1))
    }
)
used_by148: BinaryAssociation = BinaryAssociation(
    name="used_by148",
    ends={
        Property(name="Person149", type=Cocus_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="use", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
use125: BinaryAssociation = BinaryAssociation(
    name="use125",
    ends={
        Property(name="Document126", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="used_by", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
register127: BinaryAssociation = BinaryAssociation(
    name="register127",
    ends={
        Property(name="Account", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="registred_by", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
modify128: BinaryAssociation = BinaryAssociation(
    name="modify128",
    ends={
        Property(name="Thing130", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person129", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
take_part_in131: BinaryAssociation = BinaryAssociation(
    name="take_part_in131",
    ends={
        Property(name="Event133", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person132", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
remove134: BinaryAssociation = BinaryAssociation(
    name="remove134",
    ends={
        Property(name="Thing136", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person135", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
add137: BinaryAssociation = BinaryAssociation(
    name="add137",
    ends={
        Property(name="Person139", type=Cocus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Person138", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
concerned154: BinaryAssociation = BinaryAssociation(
    name="concerned154",
    ends={
        Property(name="Event155", type=Cocus_Event_URL, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Event_URL", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
submited__by150: BinaryAssociation = BinaryAssociation(
    name="submited__by150",
    ends={
        Property(name="User151", type=Cocus_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="submit", type=User, multiplicity=Multiplicity(0, 1))
    }
)
define152: BinaryAssociation = BinaryAssociation(
    name="define152",
    ends={
        Property(name="Event153", type=Cocus_Event_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="defined_by", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
sent_by160: BinaryAssociation = BinaryAssociation(
    name="sent_by160",
    ends={
        Property(name="Person161", type=Cocus_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="send", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
confirm156: BinaryAssociation = BinaryAssociation(
    name="confirm156",
    ends={
        Property(name="Event157", type=Cocus_Approval_Email, multiplicity=Multiplicity(1, 1)),
        Property(name="confirmed_by", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
has_result158: BinaryAssociation = BinaryAssociation(
    name="has_result158",
    ends={
        Property(name="Thing159", type=Cocus_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Cocus_Activity", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Cocus_Meta_Reviewer_Reviewer = Generalization(general=Reviewer, specific=Cocus_Meta_Reviewer)
gen_Cocus_Reviewer_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_Reviewer)
gen_Cocus_Reviewer_User = Generalization(general=User, specific=Cocus_Reviewer)
gen_Cocus_ConferenceChair_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_ConferenceChair)
gen_Cocus_ConferenceChair_Chairman = Generalization(general=Chairman, specific=Cocus_ConferenceChair)
gen_Cocus_ConferenceMember_Person = Generalization(general=Person, specific=Cocus_ConferenceMember)
gen_Cocus_Conference_Thing = Generalization(general=Thing, specific=Cocus_Conference)
gen_Cocus_Conference_Event = Generalization(general=Event, specific=Cocus_Conference)
gen_Cocus_Chairman_Person = Generalization(general=Person, specific=Cocus_Chairman)
gen_Cocus_Chairman_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_Chairman)
gen_Cocus_ProgramCommitteeChair_ProgramCommitteeMember = Generalization(general=ProgramCommitteeMember, specific=Cocus_ProgramCommitteeChair)
gen_Cocus_ProgramCommitteeChair_Chairman = Generalization(general=Chairman, specific=Cocus_ProgramCommitteeChair)
gen_Cocus_Acceptance_Decision = Generalization(general=Decision, specific=Cocus_Acceptance)
gen_Cocus_Rejection_Decision = Generalization(general=Decision, specific=Cocus_Rejection)
gen_Cocus_Review_Document = Generalization(general=Document, specific=Cocus_Review)
gen_Cocus_Paper_Document = Generalization(general=Document, specific=Cocus_Paper)
gen_Cocus_AssociatedChair_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_AssociatedChair)
gen_Cocus_AssociatedChair_Chairman = Generalization(general=Chairman, specific=Cocus_AssociatedChair)
gen_Cocus_ProgramCommitteeMember_Person = Generalization(general=Person, specific=Cocus_ProgramCommitteeMember)
gen_Cocus_ProgramCommitteeMember_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_ProgramCommitteeMember)
gen_Cocus_AuthorNotReviewer_Author = Generalization(general=Author, specific=Cocus_AuthorNotReviewer)
gen_Cocus_ExternalReviewer_Person = Generalization(general=Person, specific=Cocus_ExternalReviewer)
gen_Cocus_Author_ConferenceMember = Generalization(general=ConferenceMember, specific=Cocus_Author)
gen_Cocus_Author_User = Generalization(general=User, specific=Cocus_Author)
gen_Cocus_Co_author_Author = Generalization(general=Author, specific=Cocus_Co_author)
gen_Cocus_PaperAbstract_Paper = Generalization(general=Paper, specific=Cocus_PaperAbstract)
gen_Cocus_PaperFullVersion_Paper = Generalization(general=Paper, specific=Cocus_PaperFullVersion)
gen_Cocus_Administrator_User = Generalization(general=User, specific=Cocus_Administrator)
gen_Cocus_Administrator_Person = Generalization(general=Person, specific=Cocus_Administrator)
gen_Cocus_Meta_Review_Review = Generalization(general=Review, specific=Cocus_Meta_Review)
gen_Cocus_Workshop_Event = Generalization(general=Event, specific=Cocus_Workshop)
gen_Cocus_Event_Thing = Generalization(general=Thing, specific=Cocus_Event)
gen_Cocus_Role_Thing = Generalization(general=Thing, specific=Cocus_Role)
gen_Cocus_Help_Request_Request = Generalization(general=Request, specific=Cocus_Help_Request)
gen_Cocus_Person_Thing = Generalization(general=Thing, specific=Cocus_Person)
gen_Cocus_User_Person = Generalization(general=Person, specific=Cocus_User)
gen_Cocus_Symposium_Event = Generalization(general=Event, specific=Cocus_Symposium)
gen_Cocus_Abstract_Paper = Generalization(general=Paper, specific=Cocus_Abstract)
gen_Cocus_Document_Thing = Generalization(general=Thing, specific=Cocus_Document)
gen_Cocus_Notification_Email_Email = Generalization(general=Email, specific=Cocus_Notification_Email)
gen_Cocus_Email_Document = Generalization(general=Document, specific=Cocus_Email)
gen_Cocus_Short_Paper_Paper = Generalization(general=Paper, specific=Cocus_Short_Paper)
gen_Cocus_Author_Role_Role = Generalization(general=Role, specific=Cocus_Author_Role)
gen_Cocus_Preview_Review_Form = Generalization(general=Review_Form, specific=Cocus_Preview)
gen_Cocus_Review_Form_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Review_Form)
gen_Cocus_Committe_Role_Role = Generalization(general=Role, specific=Cocus_Committe_Role)
gen_Cocus_Group_Email_Email = Generalization(general=Email, specific=Cocus_Group_Email)
gen_Cocus_Submission_Template_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Submission_Template)
gen_Cocus_Review_Form_Setup_Review_Form = Generalization(general=Review_Form, specific=Cocus_Review_Form_Setup)
gen_Cocus_Misc_Help_Request = Generalization(general=Help_Request, specific=Cocus_Misc)
gen_Cocus_Event_Creation_Activity = Generalization(general=Activity, specific=Cocus_Event_Creation)
gen_Cocus_Approval_Email_Email = Generalization(general=Email, specific=Cocus_Approval_Email)
gen_Cocus_Invited_Paper_Paper = Generalization(general=Paper, specific=Cocus_Invited_Paper)
gen_Cocus_Admin_Role_Role = Generalization(general=Role, specific=Cocus_Admin_Role)
gen_Cocus_Paper_Typologies_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Paper_Typologies)
gen_Cocus_Event_URL_URL = Generalization(general=URL, specific=Cocus_Event_URL)
gen_Cocus_Head_Role_Role = Generalization(general=Role, specific=Cocus_Head_Role)
gen_Cocus_Detail_Thing = Generalization(general=Thing, specific=Cocus_Detail)
gen_Cocus_Corresponding_Author_Author = Generalization(general=Author, specific=Cocus_Corresponding_Author)
gen_Cocus_Reviewer_Role_Role = Generalization(general=Role, specific=Cocus_Reviewer_Role)
gen_Cocus_Event_Approval_Activity = Generalization(general=Activity, specific=Cocus_Event_Approval)
gen_Cocus_Registration_Activity = Generalization(general=Activity, specific=Cocus_Registration)
gen_Cocus_Full_Paper_Paper = Generalization(general=Paper, specific=Cocus_Full_Paper)
gen_Cocus_Research_Topic_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Research_Topic)
gen_Cocus_Assistance_Help_Request = Generalization(general=Help_Request, specific=Cocus_Assistance)
gen_Cocus_Email_Template_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Email_Template)
gen_Cocus_Rejection_Email_Email = Generalization(general=Email, specific=Cocus_Rejection_Email)
gen_Cocus_Submission_Document = Generalization(general=Document, specific=Cocus_Submission)
gen_Cocus_Template_Document = Generalization(general=Document, specific=Cocus_Template)
gen_Cocus_Feature_Request_Help_Request = Generalization(general=Help_Request, specific=Cocus_Feature_Request)
gen_Cocus_Committee_User = Generalization(general=User, specific=Cocus_Committee)
gen_Cocus_Event_Tracks_Event_Setup = Generalization(general=Event_Setup, specific=Cocus_Event_Tracks)
gen_Cocus_Request_Activity = Generalization(general=Activity, specific=Cocus_Request)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Bid, Paper, Review, ExternalReviewer, Cocus_Decision, Cocus_Preference, Cocus_ProgramCommittee, ProgramCommitteeMember, Cocus_Bid, Cocus_Thing, Cocus_Meta_Reviewer, Reviewer, Cocus_Reviewer, ConferenceMember, User, Administrator, Cocus_ConferenceChair, Chairman, Cocus_ConferenceMember, Person, Conference, Cocus_Conference, Thing, Event, Cocus_Chairman, Cocus_ProgramCommitteeChair, Cocus_Acceptance, Decision, Cocus_Rejection, Cocus_Review, Document, Cocus_Paper, Co_author, Cocus_AssociatedChair, Cocus_ProgramCommitteeMember, ProgramCommittee, Cocus_AuthorNotReviewer, Author, Cocus_SubjectArea, Cocus_ExternalReviewer, Cocus_Author, Cocus_Co_author, Cocus_PaperAbstract, Cocus_PaperFullVersion, Cocus_Administrator, SubjectArea, Meta_Reviewer, Cocus_Meta_Review, Cocus_Workshop, Cocus_Event, Event_Tracks, Role, Cocus_Role, Cocus_Help_Request, Request, Cocus_Person, Inforamtion, Approval_Email, Event_Setup, Cocus_Account, Cocus_Inforamtion, Cocus_User, Activity, Cocus_Symposium, Cocus_Abstract, Cocus_Document, Account, Cocus_URL, Cocus_Notification_Email, Email, Cocus_Email, Cocus_Short_Paper, Cocus_Author_Role, Cocus_Preview, Review_Form, Cocus_Review_Form, Cocus_Committe_Role, Cocus_Group_Email, Cocus_Submission_Template, Cocus_Review_Form_Setup, Cocus_Misc, Help_Request, Cocus_Event_Creation, Cocus_Approval_Email, Cocus_Invited_Paper, Cocus_Admin_Role, Cocus_Paper_Typologies, Cocus_Event_Setup, Cocus_Event_URL, URL, Cocus_Head_Role, Cocus_Detail, Cocus_Corresponding_Author, Cocus_Reviewer_Role, Cocus_Event_Approval, Cocus_Registration, Cocus_Full_Paper, Cocus_Research_Topic, Cocus_Description, Cocus_Assistance, Cocus_Email_Template, Cocus_Rejection_Email, Cocus_Submission, Cocus_Template, Cocus_Feature_Request, Cocus_Committee, Cocus_Event_Tracks, Cocus_Request, Cocus_Activity},
    associations={adjustBid1, readPaper2, hasBeenAssigned4, writeReview7, assignExternalReviewer9, hasProgramCommitteeMember10, assignedByAdministrator0, hardcopyMailingManifestsPrintedBy24, detailsEnteredBy27, reviewerBiddingStartedBy30, memberOfConference33, adjustedBy11, hasConferenceMember12, paperAssignmentFinalizedBy13, reviewCriteriaEnteredBy15, paperAssignmentToolsRunBy18, virtualMeetingEnabledBy21, endReview39, writtenBy41, hasCo_author43, hasBid44, hasDecision46, memberOfProgramCommittee34, addedBy35, assignedByReviewer37, readByMeta_Reviewer62, submitPaper64, writePaper66, co_writePaper69, approve71, assignedTo48, hasSubjectArea50, readByReviewer52, hasAuthor54, acceptedBy56, rejectedBy59, printHardcopyMailingManifests92, setMaxPapers95, enterReviewCriteria98, acceptPaper101, addProgramCommitteeMember104, assign72, finalizePaperAssignment73, runPaperAssignmentTools75, enableVirtualMeeting78, startReviewerBidding81, assignReviewer84, rejectPaper86, enterConferenceDetails89, create113, submit114, assigned_by116, inverse_of_add118, execute120, get123, conists_of106, confirmed_by107, defined_by108, approved_by109, registred_by111, recieve112, send140, added_by141, hasConflictOfInterest144, recieved_by147, used_by148, use125, register127, modify128, take_part_in131, remove134, add137, concerned154, submited__by150, define152, sent_by160, confirm156, has_result158},
    generalizations={gen_Cocus_Meta_Reviewer_Reviewer, gen_Cocus_Reviewer_ConferenceMember, gen_Cocus_Reviewer_User, gen_Cocus_ConferenceChair_ConferenceMember, gen_Cocus_ConferenceChair_Chairman, gen_Cocus_ConferenceMember_Person, gen_Cocus_Conference_Thing, gen_Cocus_Conference_Event, gen_Cocus_Chairman_Person, gen_Cocus_Chairman_ConferenceMember, gen_Cocus_ProgramCommitteeChair_ProgramCommitteeMember, gen_Cocus_ProgramCommitteeChair_Chairman, gen_Cocus_Acceptance_Decision, gen_Cocus_Rejection_Decision, gen_Cocus_Review_Document, gen_Cocus_Paper_Document, gen_Cocus_AssociatedChair_ConferenceMember, gen_Cocus_AssociatedChair_Chairman, gen_Cocus_ProgramCommitteeMember_Person, gen_Cocus_ProgramCommitteeMember_ConferenceMember, gen_Cocus_AuthorNotReviewer_Author, gen_Cocus_ExternalReviewer_Person, gen_Cocus_Author_ConferenceMember, gen_Cocus_Author_User, gen_Cocus_Co_author_Author, gen_Cocus_PaperAbstract_Paper, gen_Cocus_PaperFullVersion_Paper, gen_Cocus_Administrator_User, gen_Cocus_Administrator_Person, gen_Cocus_Meta_Review_Review, gen_Cocus_Workshop_Event, gen_Cocus_Event_Thing, gen_Cocus_Role_Thing, gen_Cocus_Help_Request_Request, gen_Cocus_Person_Thing, gen_Cocus_User_Person, gen_Cocus_Symposium_Event, gen_Cocus_Abstract_Paper, gen_Cocus_Document_Thing, gen_Cocus_Notification_Email_Email, gen_Cocus_Email_Document, gen_Cocus_Short_Paper_Paper, gen_Cocus_Author_Role_Role, gen_Cocus_Preview_Review_Form, gen_Cocus_Review_Form_Event_Setup, gen_Cocus_Committe_Role_Role, gen_Cocus_Group_Email_Email, gen_Cocus_Submission_Template_Event_Setup, gen_Cocus_Review_Form_Setup_Review_Form, gen_Cocus_Misc_Help_Request, gen_Cocus_Event_Creation_Activity, gen_Cocus_Approval_Email_Email, gen_Cocus_Invited_Paper_Paper, gen_Cocus_Admin_Role_Role, gen_Cocus_Paper_Typologies_Event_Setup, gen_Cocus_Event_URL_URL, gen_Cocus_Head_Role_Role, gen_Cocus_Detail_Thing, gen_Cocus_Corresponding_Author_Author, gen_Cocus_Reviewer_Role_Role, gen_Cocus_Event_Approval_Activity, gen_Cocus_Registration_Activity, gen_Cocus_Full_Paper_Paper, gen_Cocus_Research_Topic_Event_Setup, gen_Cocus_Assistance_Help_Request, gen_Cocus_Email_Template_Event_Setup, gen_Cocus_Rejection_Email_Email, gen_Cocus_Submission_Document, gen_Cocus_Template_Document, gen_Cocus_Feature_Request_Help_Request, gen_Cocus_Committee_User, gen_Cocus_Event_Tracks_Event_Setup, gen_Cocus_Request_Activity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
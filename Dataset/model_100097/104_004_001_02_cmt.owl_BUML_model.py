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
cmt_Thing = Class(name="cmt_Thing")
cmt_Meta_Reviewer = Class(name="cmt_Meta-Reviewer")
Reviewer = Class(name="Reviewer")
cmt_Reviewer = Class(name="cmt_Reviewer")
ConferenceMember = Class(name="ConferenceMember")
User = Class(name="User")
Administrator = Class(name="Administrator")
Bid = Class(name="Bid")
Paper = Class(name="Paper")
Review = Class(name="Review")
ExternalReviewer = Class(name="ExternalReviewer")
cmt_Decision = Class(name="cmt_Decision")
cmt_Person = Class(name="cmt_Person")
Document = Class(name="Document")
cmt_Conference = Class(name="cmt_Conference")
Thing = Class(name="Thing")
cmt_ConferenceChair = Class(name="cmt_ConferenceChair")
Chairman = Class(name="Chairman")
cmt_Document = Class(name="cmt_Document")
cmt_Preference = Class(name="cmt_Preference")
cmt_ProgramCommittee = Class(name="cmt_ProgramCommittee")
ProgramCommitteeMember = Class(name="ProgramCommitteeMember")
cmt_Bid = Class(name="cmt_Bid")
cmt_AuthorNotReviewer = Class(name="cmt_AuthorNotReviewer")
Author = Class(name="Author")
cmt_SubjectArea = Class(name="cmt_SubjectArea")
cmt_ExternalReviewer = Class(name="cmt_ExternalReviewer")
cmt_Chairman = Class(name="cmt_Chairman")
cmt_ProgramCommitteeChair = Class(name="cmt_ProgramCommitteeChair")
cmt_Acceptance = Class(name="cmt_Acceptance")
Decision = Class(name="Decision")
cmt_Rejection = Class(name="cmt_Rejection")
cmt_Review = Class(name="cmt_Review")
cmt_Paper = Class(name="cmt_Paper")
Co_author = Class(name="Co_author")
cmt_ConferenceMember = Class(name="cmt_ConferenceMember")
Person = Class(name="Person")
Conference = Class(name="Conference")
cmt_AssociatedChair = Class(name="cmt_AssociatedChair")
cmt_ProgramCommitteeMember = Class(name="cmt_ProgramCommitteeMember")
ProgramCommittee = Class(name="ProgramCommittee")
Meta_Reviewer = Class(name="Meta_Reviewer")
cmt_Author = Class(name="cmt_Author")
cmt_User = Class(name="cmt_User")
cmt_Co_author = Class(name="cmt_Co_author")
cmt_PaperAbstract = Class(name="cmt_PaperAbstract")
cmt_PaperFullVersion = Class(name="cmt_PaperFullVersion")
cmt_Administrator = Class(name="cmt_Administrator")
SubjectArea = Class(name="SubjectArea")
cmt_Meta_Review= Class(name="cmt_Meta-Review")

# cmt_Thing class attributes and methods

# cmt_Meta_Reviewer class attributes and methods

# Reviewer class attributes and methods

# cmt_Reviewer class attributes and methods

# ConferenceMember class attributes and methods

# User class attributes and methods

# Administrator class attributes and methods

# Bid class attributes and methods

# Paper class attributes and methods

# Review class attributes and methods

# ExternalReviewer class attributes and methods

# cmt_Decision class attributes and methods

# cmt_Person class attributes and methods
cmt_Person_email: Property = Property(name="email", type=StringType)
cmt_Person.attributes={cmt_Person_email}

# Document class attributes and methods

# cmt_Conference class attributes and methods
cmt_Conference_date: Property = Property(name="date", type=StringType)
cmt_Conference_reviewsPerPaper: Property = Property(name="reviewsPerPaper", type=StringType)
cmt_Conference_logoURL: Property = Property(name="logoURL", type=StringType)
cmt_Conference_acceptsHardcopySubmissions: Property = Property(name="acceptsHardcopySubmissions", type=StringType)
cmt_Conference_siteURL: Property = Property(name="siteURL", type=StringType)
cmt_Conference.attributes={cmt_Conference_date, cmt_Conference_logoURL, cmt_Conference_reviewsPerPaper, cmt_Conference_siteURL, cmt_Conference_acceptsHardcopySubmissions}

# Thing class attributes and methods

# cmt_ConferenceChair class attributes and methods

# Chairman class attributes and methods

# cmt_Document class attributes and methods

# cmt_Preference class attributes and methods

# cmt_ProgramCommittee class attributes and methods

# ProgramCommitteeMember class attributes and methods

# cmt_Bid class attributes and methods

# cmt_AuthorNotReviewer class attributes and methods

# Author class attributes and methods

# cmt_SubjectArea class attributes and methods

# cmt_ExternalReviewer class attributes and methods

# cmt_Chairman class attributes and methods

# cmt_ProgramCommitteeChair class attributes and methods

# cmt_Acceptance class attributes and methods

# Decision class attributes and methods

# cmt_Rejection class attributes and methods

# cmt_Review class attributes and methods

# cmt_Paper class attributes and methods
cmt_Paper_paperID: Property = Property(name="paperID", type=StringType)
cmt_Paper_title: Property = Property(name="title", type=StringType)
cmt_Paper.attributes={cmt_Paper_title, cmt_Paper_paperID}

# Co_author class attributes and methods

# cmt_ConferenceMember class attributes and methods

# Person class attributes and methods

# Conference class attributes and methods

# cmt_AssociatedChair class attributes and methods

# cmt_ProgramCommitteeMember class attributes and methods
cmt_ProgramCommitteeMember_maxPapers: Property = Property(name="maxPapers", type=StringType)
cmt_ProgramCommitteeMember.attributes={cmt_ProgramCommitteeMember_maxPapers}

# ProgramCommittee class attributes and methods

# Meta_Reviewer class attributes and methods

# cmt_Author class attributes and methods

# cmt_User class attributes and methods

# cmt_Co_author class attributes and methods

# cmt_PaperAbstract class attributes and methods

# cmt_PaperFullVersion class attributes and methods

# cmt_Administrator class attributes and methods

# SubjectArea class attributes and methods

# cmt_Meta_Reviewclass attributes and methods

# Relationships
assignedByAdministrator0: BinaryAssociation = BinaryAssociation(
    name="assignedByAdministrator0",
    ends={
        Property(name="Administrator", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignReviewer", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
adjustBid1: BinaryAssociation = BinaryAssociation(
    name="adjustBid1",
    ends={
        Property(name="Bid", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="adjustedBy", type=Bid, multiplicity=Multiplicity(0, 1))
    }
)
readPaper2: BinaryAssociation = BinaryAssociation(
    name="readPaper2",
    ends={
        Property(name="Paper", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="readByReviewer", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
hasBeenAssigned3: BinaryAssociation = BinaryAssociation(
    name="hasBeenAssigned3",
    ends={
        Property(name="Paper4", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedTo", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
writeReview5: BinaryAssociation = BinaryAssociation(
    name="writeReview5",
    ends={
        Property(name="Review", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="writtenBy", type=Review, multiplicity=Multiplicity(0, 1))
    }
)
assignExternalReviewer6: BinaryAssociation = BinaryAssociation(
    name="assignExternalReviewer6",
    ends={
        Property(name="ExternalReviewer", type=cmt_Reviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedByReviewer", type=ExternalReviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasConflictOfInterest7: BinaryAssociation = BinaryAssociation(
    name="hasConflictOfInterest7",
    ends={
        Property(name="Document", type=cmt_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Person", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
hasConferenceMember10: BinaryAssociation = BinaryAssociation(
    name="hasConferenceMember10",
    ends={
        Property(name="ConferenceMember", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="memberOfConference", type=ConferenceMember, multiplicity=Multiplicity(0, 1))
    }
)
paperAssignmentFinalizedBy11: BinaryAssociation = BinaryAssociation(
    name="paperAssignmentFinalizedBy11",
    ends={
        Property(name="Administrator12", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="finalizePaperAssignment", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
reviewCriteriaEnteredBy13: BinaryAssociation = BinaryAssociation(
    name="reviewCriteriaEnteredBy13",
    ends={
        Property(name="Administrator14", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="enterReviewCriteria", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
paperAssignmentToolsRunBy15: BinaryAssociation = BinaryAssociation(
    name="paperAssignmentToolsRunBy15",
    ends={
        Property(name="Administrator16", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="runPaperAssignmentTools", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
virtualMeetingEnabledBy17: BinaryAssociation = BinaryAssociation(
    name="virtualMeetingEnabledBy17",
    ends={
        Property(name="Administrator18", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="enableVirtualMeeting", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
hardcopyMailingManifestsPrintedBy19: BinaryAssociation = BinaryAssociation(
    name="hardcopyMailingManifestsPrintedBy19",
    ends={
        Property(name="Administrator20", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="printHardcopyMailingManifests", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
detailsEnteredBy21: BinaryAssociation = BinaryAssociation(
    name="detailsEnteredBy21",
    ends={
        Property(name="Administrator22", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="enterConferenceDetails", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
reviewerBiddingStartedBy23: BinaryAssociation = BinaryAssociation(
    name="reviewerBiddingStartedBy23",
    ends={
        Property(name="Administrator24", type=cmt_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="startReviewerBidding", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
addedBy27: BinaryAssociation = BinaryAssociation(
    name="addedBy27",
    ends={
        Property(name="Administrator28", type=cmt_ProgramCommitteeMember, multiplicity=Multiplicity(1, 1)),
        Property(name="addProgramCommitteeMember", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
hasProgramCommitteeMember8: BinaryAssociation = BinaryAssociation(
    name="hasProgramCommitteeMember8",
    ends={
        Property(name="ProgramCommitteeMember", type=cmt_ProgramCommittee, multiplicity=Multiplicity(1, 1)),
        Property(name="memberOfProgramCommittee", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
adjustedBy9: BinaryAssociation = BinaryAssociation(
    name="adjustedBy9",
    ends={
        Property(name="Reviewer", type=cmt_Bid, multiplicity=Multiplicity(1, 1)),
        Property(name="adjustBid", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
assignedByReviewer29: BinaryAssociation = BinaryAssociation(
    name="assignedByReviewer29",
    ends={
        Property(name="Reviewer30", type=cmt_ExternalReviewer, multiplicity=Multiplicity(1, 1)),
        Property(name="assignExternalReviewer", type=Reviewer, multiplicity=Multiplicity(1, 1))
    }
)
endReview31: BinaryAssociation = BinaryAssociation(
    name="endReview31",
    ends={
        Property(name="Review32", type=cmt_ProgramCommitteeChair, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_ProgramCommitteeChair", type=Review, multiplicity=Multiplicity(0, 1))
    }
)
writtenBy33: BinaryAssociation = BinaryAssociation(
    name="writtenBy33",
    ends={
        Property(name="Reviewer34", type=cmt_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="writeReview", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
hasCo_author35: BinaryAssociation = BinaryAssociation(
    name="hasCo_author35",
    ends={
        Property(name="Co_author", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="co-writePaper", type=Co_author, multiplicity=Multiplicity(0, 1))
    }
)
hasBid36: BinaryAssociation = BinaryAssociation(
    name="hasBid36",
    ends={
        Property(name="Bid37", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Paper", type=Bid, multiplicity=Multiplicity(0, 1))
    }
)
hasDecision38: BinaryAssociation = BinaryAssociation(
    name="hasDecision38",
    ends={
        Property(name="Decision", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Paper39", type=Decision, multiplicity=Multiplicity(0, 1))
    }
)
assignedTo40: BinaryAssociation = BinaryAssociation(
    name="assignedTo40",
    ends={
        Property(name="Reviewer41", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="hasBeenAssigned", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
memberOfConference25: BinaryAssociation = BinaryAssociation(
    name="memberOfConference25",
    ends={
        Property(name="Conference", type=cmt_ConferenceMember, multiplicity=Multiplicity(1, 1)),
        Property(name="hasConferenceMember", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
memberOfProgramCommittee26: BinaryAssociation = BinaryAssociation(
    name="memberOfProgramCommittee26",
    ends={
        Property(name="ProgramCommittee", type=cmt_ProgramCommitteeMember, multiplicity=Multiplicity(1, 1)),
        Property(name="hasProgramCommitteeMember", type=ProgramCommittee, multiplicity=Multiplicity(0, 1))
    }
)
acceptedBy47: BinaryAssociation = BinaryAssociation(
    name="acceptedBy47",
    ends={
        Property(name="Administrator48", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="acceptPaper", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
rejectedBy49: BinaryAssociation = BinaryAssociation(
    name="rejectedBy49",
    ends={
        Property(name="Administrator50", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="rejectPaper", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
readByMeta_Reviewer51: BinaryAssociation = BinaryAssociation(
    name="readByMeta_Reviewer51",
    ends={
        Property(name="Meta_Reviewer", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Paper52", type=Meta_Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
submitPaper53: BinaryAssociation = BinaryAssociation(
    name="submitPaper53",
    ends={
        Property(name="Paper54", type=cmt_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Author", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
writePaper55: BinaryAssociation = BinaryAssociation(
    name="writePaper55",
    ends={
        Property(name="Paper56", type=cmt_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="hasAuthor", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
co_writePaper57: BinaryAssociation = BinaryAssociation(
    name="co_writePaper57",
    ends={
        Property(name="Paper58", type=cmt_Co_author, multiplicity=Multiplicity(1, 1)),
        Property(name="hasCo_author", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
finalizePaperAssignment59: BinaryAssociation = BinaryAssociation(
    name="finalizePaperAssignment59",
    ends={
        Property(name="Conference60", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="paperAssignmentFinalizedBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
runPaperAssignmentTools61: BinaryAssociation = BinaryAssociation(
    name="runPaperAssignmentTools61",
    ends={
        Property(name="Conference62", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="paperAssignmentToolsRunBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
enableVirtualMeeting63: BinaryAssociation = BinaryAssociation(
    name="enableVirtualMeeting63",
    ends={
        Property(name="Conference64", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualMeetingEnabledBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
hasSubjectArea42: BinaryAssociation = BinaryAssociation(
    name="hasSubjectArea42",
    ends={
        Property(name="SubjectArea", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Paper43", type=SubjectArea, multiplicity=Multiplicity(0, 1))
    }
)
startReviewerBidding65: BinaryAssociation = BinaryAssociation(
    name="startReviewerBidding65",
    ends={
        Property(name="Conference66", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewerBiddingStartedBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
readByReviewer44: BinaryAssociation = BinaryAssociation(
    name="readByReviewer44",
    ends={
        Property(name="Reviewer45", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="readPaper", type=Reviewer, multiplicity=Multiplicity(1, 1))
    }
)
hasAuthor46: BinaryAssociation = BinaryAssociation(
    name="hasAuthor46",
    ends={
        Property(name="Author", type=cmt_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="writePaper", type=Author, multiplicity=Multiplicity(0, 1))
    }
)
setMaxPapers75: BinaryAssociation = BinaryAssociation(
    name="setMaxPapers75",
    ends={
        Property(name="ProgramCommitteeMember76", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="cmt_Administrator", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
enterReviewCriteria77: BinaryAssociation = BinaryAssociation(
    name="enterReviewCriteria77",
    ends={
        Property(name="Conference78", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewCriteriaEnteredBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
acceptPaper79: BinaryAssociation = BinaryAssociation(
    name="acceptPaper79",
    ends={
        Property(name="Paper80", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="acceptedBy", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
addProgramCommitteeMember81: BinaryAssociation = BinaryAssociation(
    name="addProgramCommitteeMember81",
    ends={
        Property(name="ProgramCommitteeMember82", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="addedBy", type=ProgramCommitteeMember, multiplicity=Multiplicity(0, 1))
    }
)
assignReviewer67: BinaryAssociation = BinaryAssociation(
    name="assignReviewer67",
    ends={
        Property(name="Reviewer68", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedByAdministrator", type=Reviewer, multiplicity=Multiplicity(0, 1))
    }
)
rejectPaper69: BinaryAssociation = BinaryAssociation(
    name="rejectPaper69",
    ends={
        Property(name="Paper70", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="rejectedBy", type=Paper, multiplicity=Multiplicity(0, 1))
    }
)
enterConferenceDetails71: BinaryAssociation = BinaryAssociation(
    name="enterConferenceDetails71",
    ends={
        Property(name="Conference72", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="detailsEnteredBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)
printHardcopyMailingManifests73: BinaryAssociation = BinaryAssociation(
    name="printHardcopyMailingManifests73",
    ends={
        Property(name="Conference74", type=cmt_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="hardcopyMailingManifestsPrintedBy", type=Conference, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cmt_Meta_Reviewer_Reviewer = Generalization(general=Reviewer, specific=cmt_Meta_Reviewer)
gen_cmt_Reviewer_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_Reviewer)
gen_cmt_Reviewer_User = Generalization(general=User, specific=cmt_Reviewer)
gen_cmt_Conference_Thing = Generalization(general=Thing, specific=cmt_Conference)
gen_cmt_ConferenceChair_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_ConferenceChair)
gen_cmt_ConferenceChair_Chairman = Generalization(general=Chairman, specific=cmt_ConferenceChair)
gen_cmt_AuthorNotReviewer_Author = Generalization(general=Author, specific=cmt_AuthorNotReviewer)
gen_cmt_ExternalReviewer_Person = Generalization(general=Person, specific=cmt_ExternalReviewer)
gen_cmt_Chairman_Person = Generalization(general=Person, specific=cmt_Chairman)
gen_cmt_Chairman_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_Chairman)
gen_cmt_ProgramCommitteeChair_ProgramCommitteeMember = Generalization(general=ProgramCommitteeMember, specific=cmt_ProgramCommitteeChair)
gen_cmt_ProgramCommitteeChair_Chairman = Generalization(general=Chairman, specific=cmt_ProgramCommitteeChair)
gen_cmt_Acceptance_Decision = Generalization(general=Decision, specific=cmt_Acceptance)
gen_cmt_Rejection_Decision = Generalization(general=Decision, specific=cmt_Rejection)
gen_cmt_Review_Document = Generalization(general=Document, specific=cmt_Review)
gen_cmt_Paper_Document = Generalization(general=Document, specific=cmt_Paper)
gen_cmt_ConferenceMember_Person = Generalization(general=Person, specific=cmt_ConferenceMember)
gen_cmt_AssociatedChair_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_AssociatedChair)
gen_cmt_AssociatedChair_Chairman = Generalization(general=Chairman, specific=cmt_AssociatedChair)
gen_cmt_ProgramCommitteeMember_Person = Generalization(general=Person, specific=cmt_ProgramCommitteeMember)
gen_cmt_ProgramCommitteeMember_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_ProgramCommitteeMember)
gen_cmt_Author_ConferenceMember = Generalization(general=ConferenceMember, specific=cmt_Author)
gen_cmt_Author_User = Generalization(general=User, specific=cmt_Author)
gen_cmt_User_Person = Generalization(general=Person, specific=cmt_User)
gen_cmt_Co_author_Author = Generalization(general=Author, specific=cmt_Co_author)
gen_cmt_PaperAbstract_Paper = Generalization(general=Paper, specific=cmt_PaperAbstract)
gen_cmt_PaperFullVersion_Paper = Generalization(general=Paper, specific=cmt_PaperFullVersion)
gen_cmt_Administrator_User = Generalization(general=User, specific=cmt_Administrator)
gen_cmt_Meta_Review_Review = Generalization(general=Review, specific=cmt_Meta_Review)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={cmt_Thing, cmt_Meta_Reviewer, Reviewer, cmt_Reviewer, ConferenceMember, User, Administrator, Bid, Paper, Review, ExternalReviewer, cmt_Decision, cmt_Person, Document, cmt_Conference, Thing, cmt_ConferenceChair, Chairman, cmt_Document, cmt_Preference, cmt_ProgramCommittee, ProgramCommitteeMember, cmt_Bid, cmt_AuthorNotReviewer, Author, cmt_SubjectArea, cmt_ExternalReviewer, cmt_Chairman, cmt_ProgramCommitteeChair, cmt_Acceptance, Decision, cmt_Rejection, cmt_Review, cmt_Paper, Co_author, cmt_ConferenceMember, Person, Conference, cmt_AssociatedChair, cmt_ProgramCommitteeMember, ProgramCommittee, Meta_Reviewer, cmt_Author, cmt_User, cmt_Co_author, cmt_PaperAbstract, cmt_PaperFullVersion, cmt_Administrator, SubjectArea, cmt_Meta_Review},
    associations={assignedByAdministrator0, adjustBid1, readPaper2, hasBeenAssigned3, writeReview5, assignExternalReviewer6, hasConflictOfInterest7, hasConferenceMember10, paperAssignmentFinalizedBy11, reviewCriteriaEnteredBy13, paperAssignmentToolsRunBy15, virtualMeetingEnabledBy17, hardcopyMailingManifestsPrintedBy19, detailsEnteredBy21, reviewerBiddingStartedBy23, addedBy27, hasProgramCommitteeMember8, adjustedBy9, assignedByReviewer29, endReview31, writtenBy33, hasCo_author35, hasBid36, hasDecision38, assignedTo40, memberOfConference25, memberOfProgramCommittee26, acceptedBy47, rejectedBy49, readByMeta_Reviewer51, submitPaper53, writePaper55, co_writePaper57, finalizePaperAssignment59, runPaperAssignmentTools61, enableVirtualMeeting63, hasSubjectArea42, startReviewerBidding65, readByReviewer44, hasAuthor46, setMaxPapers75, enterReviewCriteria77, acceptPaper79, addProgramCommitteeMember81, assignReviewer67, rejectPaper69, enterConferenceDetails71, printHardcopyMailingManifests73},
    generalizations={gen_cmt_Meta_Reviewer_Reviewer, gen_cmt_Reviewer_ConferenceMember, gen_cmt_Reviewer_User, gen_cmt_Conference_Thing, gen_cmt_ConferenceChair_ConferenceMember, gen_cmt_ConferenceChair_Chairman, gen_cmt_AuthorNotReviewer_Author, gen_cmt_ExternalReviewer_Person, gen_cmt_Chairman_Person, gen_cmt_Chairman_ConferenceMember, gen_cmt_ProgramCommitteeChair_ProgramCommitteeMember, gen_cmt_ProgramCommitteeChair_Chairman, gen_cmt_Acceptance_Decision, gen_cmt_Rejection_Decision, gen_cmt_Review_Document, gen_cmt_Paper_Document, gen_cmt_ConferenceMember_Person, gen_cmt_AssociatedChair_ConferenceMember, gen_cmt_AssociatedChair_Chairman, gen_cmt_ProgramCommitteeMember_Person, gen_cmt_ProgramCommitteeMember_ConferenceMember, gen_cmt_Author_ConferenceMember, gen_cmt_Author_User, gen_cmt_User_Person, gen_cmt_Co_author_Author, gen_cmt_PaperAbstract_Paper, gen_cmt_PaperFullVersion_Paper, gen_cmt_Administrator_User, gen_cmt_Meta_Review_Review},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
UserSkillLevel: Enumeration = Enumeration(
    name="UserSkillLevel",
    literals={
            EnumerationLiteral(name="NOVICE"),
			EnumerationLiteral(name="COMPETENT"),
			EnumerationLiteral(name="PROFICIENT"),
			EnumerationLiteral(name="EXPERT"),
			EnumerationLiteral(name="AUTHORITY")
    }
)

TechSkillLevel: Enumeration = Enumeration(
    name="TechSkillLevel",
    literals={
            EnumerationLiteral(name="BEGINNER"),
			EnumerationLiteral(name="INTERMEDIATE"),
			EnumerationLiteral(name="ADVANCED"),
			EnumerationLiteral(name="EXPERT"),
			EnumerationLiteral(name="MASTERCLASS")
    }
)

SkillRequestStatus: Enumeration = Enumeration(
    name="SkillRequestStatus",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="MATCHED"),
			EnumerationLiteral(name="COMPLETED"),
			EnumerationLiteral(name="CANCELLED")
    }
)

SkillMatchStatus: Enumeration = Enumeration(
    name="SkillMatchStatus",
    literals={
            EnumerationLiteral(name="PENDING"),
			EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="COMPLETED"),
			EnumerationLiteral(name="REJECTED")
    }
)

SessionType: Enumeration = Enumeration(
    name="SessionType",
    literals={
            EnumerationLiteral(name="ONLINE"),
			EnumerationLiteral(name="OFFLINE"),
			EnumerationLiteral(name="HYBRID")
    }
)

# Classes
User = Class(name="User")
UserSkill = Class(name="UserSkill")
Skill = Class(name="Skill")
SkillRequest = Class(name="SkillRequest")
SkillMatch = Class(name="SkillMatch")
Review = Class(name="Review")
Session = Class(name="Session")

# User class attributes and methods
User_userId: Property = Property(name="userId", type=IntegerType)
User_userName: Property = Property(name="userName", type=StringType)
User_emailId: Property = Property(name="emailId", type=StringType)
User.attributes={User_emailId, User_userId, User_userName}

# UserSkill class attributes and methods
UserSkill_skillId: Property = Property(name="skillId", type=IntegerType)
UserSkill_skillLevel: Property = Property(name="skillLevel", type=UserSkillLevel)
UserSkill_yearsOfExperience: Property = Property(name="yearsOfExperience", type=IntegerType)
UserSkill_certification: Property = Property(name="certification", type=BooleanType)
UserSkill.attributes={UserSkill_certification, UserSkill_skillId, UserSkill_skillLevel, UserSkill_yearsOfExperience}

# Skill class attributes and methods
Skill_skillId: Property = Property(name="skillId", type=IntegerType)
Skill_skillName: Property = Property(name="skillName", type=StringType)
Skill_category: Property = Property(name="category", type=StringType)
Skill_description: Property = Property(name="description", type=StringType)
Skill_skillLevel: Property = Property(name="skillLevel", type=TechSkillLevel)
Skill_estimatedDuration: Property = Property(name="estimatedDuration", type=IntegerType)
Skill.attributes={Skill_category, Skill_description, Skill_estimatedDuration, Skill_skillId, Skill_skillLevel, Skill_skillName}

# SkillRequest class attributes and methods
SkillRequest_requestId: Property = Property(name="requestId", type=IntegerType)
SkillRequest_createdDate: Property = Property(name="createdDate", type=DateType)
SkillRequest_status: Property = Property(name="status", type=SkillRequestStatus)
SkillRequest_deadlineDate: Property = Property(name="deadlineDate", type=DateType)
SkillRequest.attributes={SkillRequest_createdDate, SkillRequest_deadlineDate, SkillRequest_requestId, SkillRequest_status}

# SkillMatch class attributes and methods
SkillMatch_matchId: Property = Property(name="matchId", type=IntegerType)
SkillMatch_createdDate: Property = Property(name="createdDate", type=DateType)
SkillMatch_startDate: Property = Property(name="startDate", type=DateType)
SkillMatch_status: Property = Property(name="status", type=SkillMatchStatus)
SkillMatch.attributes={SkillMatch_createdDate, SkillMatch_matchId, SkillMatch_startDate, SkillMatch_status}

# Review class attributes and methods
Review_reviewId: Property = Property(name="reviewId", type=IntegerType)
Review_rating: Property = Property(name="rating", type=IntegerType)
Review_comments: Property = Property(name="comments", type=StringType)
Review.attributes={Review_comments, Review_rating, Review_reviewId}

# Session class attributes and methods
Session_sessionId: Property = Property(name="sessionId", type=IntegerType)
Session_sessionDate: Property = Property(name="sessionDate", type=DateType)
Session_duration: Property = Property(name="duration", type=IntegerType)
Session_sessionType: Property = Property(name="sessionType", type=SessionType)
Session.attributes={Session_duration, Session_sessionDate, Session_sessionId, Session_sessionType}

# Relationships
review: BinaryAssociation = BinaryAssociation(
    name="review",
    ends={
        Property(name="review", type=Review, multiplicity=Multiplicity(0, 1)),
        Property(name="session_1", type=Session, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
leads_to: BinaryAssociation = BinaryAssociation(
    name="leads_to",
    ends={
        Property(name="skillrequest_1", type=SkillRequest, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="skillmatch_2", type=SkillMatch, multiplicity=Multiplicity(0, 1))
    }
)

teaches: BinaryAssociation = BinaryAssociation(
    name="teaches",
    ends={
        Property(name="user", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="userskill", type=UserSkill, multiplicity=Multiplicity(1, 9999))
    }
)
wants: BinaryAssociation = BinaryAssociation(
    name="wants",
    ends={
        Property(name="skillrequest_2", type=SkillRequest, multiplicity=Multiplicity(0, 9999)),
        Property(name="skill_1", type=Skill, multiplicity=Multiplicity(1, 1))
    }
)
refers_to: BinaryAssociation = BinaryAssociation(
    name="refers_to",
    ends={
        Property(name="userskill_1", type=UserSkill, multiplicity=Multiplicity(0, 9999), is_navigable=False),
        Property(name="skill", type=Skill, multiplicity=Multiplicity(1, 1))
    }
)
creates: BinaryAssociation = BinaryAssociation(
    name="creates",
    ends={
        Property(name="user_1", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="skillrequest", type=SkillRequest, multiplicity=Multiplicity(0, 9999))
    }
)

has: BinaryAssociation = BinaryAssociation(
    name="has",
    ends={
        Property(name="skillmatch_1", type=SkillMatch, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="session", type=Session, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={User, UserSkill, Skill, SkillRequest, SkillMatch, Review, Session, UserSkillLevel, TechSkillLevel, SkillRequestStatus, SkillMatchStatus, SessionType},
    associations={review, leads_to, teaches, wants, refers_to, creates,  has},
    generalizations={},
    metadata=None
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="New project")
project = Project(
    name="skillset_match",
    models=[domain_model],
    owner="User",
    metadata=metadata
)

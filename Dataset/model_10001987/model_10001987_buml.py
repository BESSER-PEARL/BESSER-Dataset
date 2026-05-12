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
Candidate = Class(name="Candidate")
Voter = Class(name="Voter")
BallotInformation = Class(name="BallotInformation")
Post = Class(name="Post")
Election = Class(name="Election")
Admin = Class(name="Admin")

# Candidate class attributes and methods
Candidate_candidate_ID: Property = Property(name="candidate_ID", type=IntegerType)
Candidate_Candidate_PostID: Property = Property(name="Candidate_PostID", type=IntegerType)
Candidate_Candidate_Name: Property = Property(name="Candidate_Name", type=StringType)
Candidate_CandidatePartyName: Property = Property(name="CandidatePartyName", type=StringType)
Candidate.attributes={Candidate_candidate_ID, Candidate_Candidate_Name, Candidate_Candidate_PostID, Candidate_CandidatePartyName}

# Voter class attributes and methods
Voter_student_faculty_ID: Property = Property(name="student_faculty_ID", type=IntegerType)
Voter_Name: Property = Property(name="Name", type=StringType)
Voter_Address: Property = Property(name="Address", type=StringType)
Voter_Age: Property = Property(name="Age", type=IntegerType)
Voter_Eligibilty: Property = Property(name="Eligibilty", type=BooleanType)
Voter.attributes={Voter_Age, Voter_Address, Voter_student_faculty_ID, Voter_Name, Voter_Eligibilty}

# BallotInformation class attributes and methods
BallotInformation_BallotID: Property = Property(name="BallotID", type=IntegerType)
BallotInformation_BallotElectionID: Property = Property(name="BallotElectionID", type=IntegerType)
BallotInformation_BallotVotersID: Property = Property(name="BallotVotersID", type=IntegerType)
BallotInformation_BallotPropID: Property = Property(name="BallotPropID", type=IntegerType)
BallotInformation_BallotPropBallotID: Property = Property(name="BallotPropBallotID", type=IntegerType)
BallotInformation_BallotPropResults: Property = Property(name="BallotPropResults", type=IntegerType)
BallotInformation.attributes={BallotInformation_BallotPropID, BallotInformation_BallotElectionID, BallotInformation_BallotID, BallotInformation_BallotVotersID, BallotInformation_BallotPropResults, BallotInformation_BallotPropBallotID}

# Post class attributes and methods
Post_PostId: Property = Property(name="PostId", type=IntegerType)
Post_PostElectionId: Property = Property(name="PostElectionId", type=IntegerType)
Post_PostDesc: Property = Property(name="PostDesc", type=StringType)
Post.attributes={Post_PostElectionId, Post_PostId, Post_PostDesc}

# Election class attributes and methods
Election_ElectionID: Property = Property(name="ElectionID", type=IntegerType)
Election_ElectionDate: Property = Property(name="ElectionDate", type=StringType)
Election_ElectionCriteria: Property = Property(name="ElectionCriteria", type=StringType)
Election_ElectionName: Property = Property(name="ElectionName", type=StringType)
Election.attributes={Election_ElectionDate, Election_ElectionCriteria, Election_ElectionName, Election_ElectionID}

# Admin class attributes and methods
Admin_AdminID: Property = Property(name="AdminID", type=IntegerType)
Admin_AminName: Property = Property(name="AminName", type=StringType)
Admin_UserLogin: Property = Property(name="UserLogin", type=IntegerType)
Admin.attributes={Admin_UserLogin, Admin_AdminID, Admin_AminName}

# Relationships
Candidate__BallotInformation: BinaryAssociation = BinaryAssociation(
    name="Candidate__BallotInformation",
    ends={
        Property(name="ballotInformation0", type=BallotInformation, multiplicity=Multiplicity(0, 1)),
        Property(name="candidate1", type=Candidate, multiplicity=Multiplicity(0, 1))
    }
)
Election_BallotInformation: BinaryAssociation = BinaryAssociation(
    name="Election_BallotInformation",
    ends={
        Property(name="ballotInformation2", type=BallotInformation, multiplicity=Multiplicity(0, 1)),
        Property(name="election3", type=Election, multiplicity=Multiplicity(0, 1))
    }
)
Voter_Election: BinaryAssociation = BinaryAssociation(
    name="Voter_Election",
    ends={
        Property(name="election4", type=Election, multiplicity=Multiplicity(0, 1)),
        Property(name="voter5", type=Voter, multiplicity=Multiplicity(0, 1))
    }
)
Voter_Post: BinaryAssociation = BinaryAssociation(
    name="Voter_Post",
    ends={
        Property(name="post6", type=Post, multiplicity=Multiplicity(0, 1)),
        Property(name="voter7", type=Voter, multiplicity=Multiplicity(0, 1))
    }
)
Post_BallotInformation: BinaryAssociation = BinaryAssociation(
    name="Post_BallotInformation",
    ends={
        Property(name="ballotInformation8", type=BallotInformation, multiplicity=Multiplicity(0, 1)),
        Property(name="post9", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Candidate__Election: BinaryAssociation = BinaryAssociation(
    name="Candidate__Election",
    ends={
        Property(name="election10", type=Election, multiplicity=Multiplicity(0, 1)),
        Property(name="candidate11", type=Candidate, multiplicity=Multiplicity(0, 1))
    }
)
Voter_Admin: BinaryAssociation = BinaryAssociation(
    name="Voter_Admin",
    ends={
        Property(name="admin12", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="voter13", type=Voter, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Candidate: BinaryAssociation = BinaryAssociation(
    name="Admin_Candidate",
    ends={
        Property(name="candidate14", type=Candidate, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Election: BinaryAssociation = BinaryAssociation(
    name="Admin_Election",
    ends={
        Property(name="election16", type=Election, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_BallotInformation: BinaryAssociation = BinaryAssociation(
    name="Admin_BallotInformation",
    ends={
        Property(name="ballotInformation18", type=BallotInformation, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hyLswNE_EeeLcIicqHdTUQ",
    types={Candidate, Voter, BallotInformation, Post, Election, Admin},
    associations={Candidate__BallotInformation, Election_BallotInformation, Voter_Election, Voter_Post, Post_BallotInformation, Candidate__Election, Voter_Admin, Admin_Candidate, Admin_Election, Admin_BallotInformation},
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
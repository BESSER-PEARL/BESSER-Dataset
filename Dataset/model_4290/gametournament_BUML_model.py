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
GameType: Enumeration = Enumeration(
    name="GameType",
    literals={
            EnumerationLiteral(name="ACTION"),
			EnumerationLiteral(name="RPG"),
			EnumerationLiteral(name="FPS"),
			EnumerationLiteral(name="STRATEGIC"),
			EnumerationLiteral(name="COMBAT")
    }
)

# Classes
gametournament_Tournament = Class(name="gametournament::Tournament")
gametournament_Pool = Class(name="gametournament::Pool")
gametournament_Game = Class(name="gametournament::Game")
gametournament_Gamer = Class(name="gametournament::Gamer")
gametournament_FinalPhase = Class(name="gametournament::FinalPhase")
gametournament_QualificationPhase = Class(name="gametournament::QualificationPhase")

# gametournament_Tournament class attributes and methods
gametournament_Tournament_name: Property = Property(name="name", type=StringType)
gametournament_Tournament_location: Property = Property(name="location", type=StringType)
gametournament_Tournament_startDate: Property = Property(name="startDate", type=DateType)
gametournament_Tournament_endDate: Property = Property(name="endDate", type=DateType)
gametournament_Tournament_prize: Property = Property(name="prize", type=IntegerType)
gametournament_Tournament.attributes={gametournament_Tournament_endDate, gametournament_Tournament_prize, gametournament_Tournament_location, gametournament_Tournament_startDate, gametournament_Tournament_name}

# gametournament_Pool class attributes and methods
gametournament_Pool_m_generateClassment: Method = Method(name="generateClassment", parameters={})
gametournament_Pool.methods={gametournament_Pool_m_generateClassment}

# gametournament_Game class attributes and methods
gametournament_Game_name: Property = Property(name="name", type=StringType)
gametournament_Game_type: Property = Property(name="type", type=StringType)
gametournament_Game.attributes={gametournament_Game_name, gametournament_Game_type}

# gametournament_Gamer class attributes and methods
gametournament_Gamer_firstName: Property = Property(name="firstName", type=StringType)
gametournament_Gamer_lastName: Property = Property(name="lastName", type=StringType)
gametournament_Gamer_pseudo: Property = Property(name="pseudo", type=StringType)
gametournament_Gamer_victories: Property = Property(name="victories", type=IntegerType)
gametournament_Gamer_matches: Property = Property(name="matches", type=IntegerType)
gametournament_Gamer.attributes={gametournament_Gamer_firstName, gametournament_Gamer_pseudo, gametournament_Gamer_matches, gametournament_Gamer_lastName, gametournament_Gamer_victories}

# gametournament_FinalPhase class attributes and methods

# gametournament_QualificationPhase class attributes and methods
gametournament_QualificationPhase_m_createPools: Method = Method(name="createPools", parameters={}, type=StringType)
gametournament_QualificationPhase.methods={gametournament_QualificationPhase_m_createPools}

# Relationships
pools7: BinaryAssociation = BinaryAssociation(
    name="pools7",
    ends={
        Property(name="gametournament_Pool", type=gametournament_QualificationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_QualificationPhase8", type=gametournament_Pool, multiplicity=Multiplicity(1, 16), is_composite=True)
    }
)
finalists9: BinaryAssociation = BinaryAssociation(
    name="finalists9",
    ends={
        Property(name="gametournament_Gamer11", type=gametournament_FinalPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_FinalPhase10", type=gametournament_Gamer, multiplicity=Multiplicity(1, 16), is_composite=True)
    }
)
qualificationphase12: BinaryAssociation = BinaryAssociation(
    name="qualificationphase12",
    ends={
        Property(name="gametournament_QualificationPhase14", type=gametournament_FinalPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_FinalPhase13", type=gametournament_QualificationPhase, multiplicity=Multiplicity(1, 1))
    }
)
participants15: BinaryAssociation = BinaryAssociation(
    name="participants15",
    ends={
        Property(name="gametournament_Gamer17", type=gametournament_Pool, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Pool16", type=gametournament_Gamer, multiplicity=Multiplicity(4, 4), is_composite=True)
    }
)
classment18: BinaryAssociation = BinaryAssociation(
    name="classment18",
    ends={
        Property(name="gametournament_Gamer20", type=gametournament_Pool, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Pool19", type=gametournament_Gamer, multiplicity=Multiplicity(4, 4))
    }
)
game0: BinaryAssociation = BinaryAssociation(
    name="game0",
    ends={
        Property(name="gametournament_Game", type=gametournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Tournament", type=gametournament_Game, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gamers1: BinaryAssociation = BinaryAssociation(
    name="gamers1",
    ends={
        Property(name="gametournament_Gamer", type=gametournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Tournament2", type=gametournament_Gamer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalPhase3: BinaryAssociation = BinaryAssociation(
    name="finalPhase3",
    ends={
        Property(name="gametournament_FinalPhase", type=gametournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Tournament4", type=gametournament_FinalPhase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualificationPhase5: BinaryAssociation = BinaryAssociation(
    name="qualificationPhase5",
    ends={
        Property(name="gametournament_QualificationPhase", type=gametournament_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="gametournament_Tournament6", type=gametournament_QualificationPhase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="gametournament",
    types={gametournament_Tournament, gametournament_Pool, gametournament_Game, gametournament_Gamer, gametournament_FinalPhase, gametournament_QualificationPhase, GameType},
    associations={pools7, finalists9, qualificationphase12, participants15, classment18, game0, gamers1, finalPhase3, qualificationPhase5},
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
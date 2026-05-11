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
TournamentType: Enumeration = Enumeration(
    name="TournamentType",
    literals={
            EnumerationLiteral(name="Pro"),
			EnumerationLiteral(name="Amateur")
    }
)

# Classes
bowling_Player = Class(name="bowling_Player")
bowling_League = Class(name="bowling_League")
bowling_Game = Class(name="bowling_Game")
bowling_Matchup = Class(name="bowling_Matchup")
bowling_Tournament = Class(name="bowling_Tournament")

# bowling_Player class attributes and methods
bowling_Player_name: Property = Property(name="name", type=StringType)
bowling_Player_street: Property = Property(name="street", type=StringType)
bowling_Player_telephon: Property = Property(name="telephon", type=StringType)
bowling_Player_notes: Property = Property(name="notes", type=StringType)
bowling_Player_isAvailable: Property = Property(name="isAvailable", type=BooleanType)
bowling_Player_streetNumber: Property = Property(name="streetNumber", type=IntegerType)
bowling_Player_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
bowling_Player_height: Property = Property(name="height", type=FloatType)
bowling_Player_isProfessional: Property = Property(name="isProfessional", type=BooleanType)
bowling_Player_eMail: Property = Property(name="eMail", type=StringType)
bowling_Player_m_hasName: Method = Method(name="hasName", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Player_m_hasStreet: Method = Method(name="hasStreet", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Player_m_hasCorrectStreetNumber: Method = Method(name="hasCorrectStreetNumber", parameters={Parameter(name='bowling_context', type=StringType), Parameter(name='bowling_diagnosticianChain', type=StringType)}, type=BooleanType)
bowling_Player_m_hasTelephon: Method = Method(name="hasTelephon", parameters={Parameter(name='bowling_context', type=StringType), Parameter(name='bowling_diagnosticianChain', type=StringType)}, type=BooleanType)
bowling_Player_m_hasDateOfBirth: Method = Method(name="hasDateOfBirth", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Player_m_hasNotes: Method = Method(name="hasNotes", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Player_m_hasGame: Method = Method(name="hasGame", parameters={Parameter(name='bowling_context', type=StringType), Parameter(name='bowling_diagnosticianChain', type=StringType)}, type=BooleanType)
bowling_Player_m_hasHeight: Method = Method(name="hasHeight", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Player_m_hasIsAvailable: Method = Method(name="hasIsAvailable", parameters={Parameter(name='bowling_context', type=StringType), Parameter(name='bowling_diagnosticianChain', type=StringType)}, type=BooleanType)
bowling_Player.attributes={bowling_Player_telephon, bowling_Player_streetNumber, bowling_Player_height, bowling_Player_dateOfBirth, bowling_Player_isProfessional, bowling_Player_notes, bowling_Player_street, bowling_Player_eMail, bowling_Player_isAvailable, bowling_Player_name}
bowling_Player.methods={bowling_Player_m_hasDateOfBirth, bowling_Player_m_hasTelephon, bowling_Player_m_hasName, bowling_Player_m_hasStreet, bowling_Player_m_hasCorrectStreetNumber, bowling_Player_m_hasHeight, bowling_Player_m_hasNotes, bowling_Player_m_hasGame, bowling_Player_m_hasIsAvailable}

# bowling_League class attributes and methods
bowling_League_name: Property = Property(name="name", type=StringType)
bowling_League.attributes={bowling_League_name}

# bowling_Game class attributes and methods
bowling_Game_frames: Property = Property(name="frames", type=IntegerType)
bowling_Game.attributes={bowling_Game_frames}

# bowling_Matchup class attributes and methods
bowling_Matchup_date: Property = Property(name="date", type=DateType)
bowling_Matchup.attributes={bowling_Matchup_date}

# bowling_Tournament class attributes and methods
bowling_Tournament_title: Property = Property(name="title", type=StringType)
bowling_Tournament_type: Property = Property(name="type", type=StringType)
bowling_Tournament_m_hasTounamentPro: Method = Method(name="hasTounamentPro", parameters={Parameter(name='bowling_diagnosticianChain', type=StringType), Parameter(name='bowling_context', type=StringType)}, type=BooleanType)
bowling_Tournament_m_hasLeague: Method = Method(name="hasLeague", parameters={Parameter(name='bowling_context', type=StringType), Parameter(name='bowling_diagnosticianChain', type=StringType)}, type=BooleanType)
bowling_Tournament.attributes={bowling_Tournament_title, bowling_Tournament_type}
bowling_Tournament.methods={bowling_Tournament_m_hasTounamentPro, bowling_Tournament_m_hasLeague}

# Relationships
players1: BinaryAssociation = BinaryAssociation(
    name="players1",
    ends={
        Property(name="bowling_Player", type=bowling_League, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_League", type=bowling_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
games0: BinaryAssociation = BinaryAssociation(
    name="games0",
    ends={
        Property(name="Game", type=bowling_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="player", type=bowling_Game, multiplicity=Multiplicity(0, 9999))
    }
)
matchups2: BinaryAssociation = BinaryAssociation(
    name="matchups2",
    ends={
        Property(name="bowling_Matchup", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament", type=bowling_Matchup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchup8: BinaryAssociation = BinaryAssociation(
    name="matchup8",
    ends={
        Property(name="Matchup", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=bowling_Matchup, multiplicity=Multiplicity(1, 1))
    }
)
player9: BinaryAssociation = BinaryAssociation(
    name="player9",
    ends={
        Property(name="Player", type=bowling_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games10", type=bowling_Player, multiplicity=Multiplicity(0, 1))
    }
)
league3: BinaryAssociation = BinaryAssociation(
    name="league3",
    ends={
        Property(name="bowling_League5", type=bowling_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="bowling_Tournament4", type=bowling_League, multiplicity=Multiplicity(0, 1))
    }
)
games6: BinaryAssociation = BinaryAssociation(
    name="games6",
    ends={
        Property(name="Game7", type=bowling_Matchup, multiplicity=Multiplicity(1, 1)),
        Property(name="matchup", type=bowling_Game, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bowling",
    types={bowling_Player, bowling_League, bowling_Game, bowling_Matchup, bowling_Tournament, TournamentType},
    associations={players1, games0, matchups2, matchup8, player9, league3, games6},
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
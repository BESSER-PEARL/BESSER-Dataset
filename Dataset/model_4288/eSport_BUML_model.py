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
CapacityType: Enumeration = Enumeration(
    name="CapacityType",
    literals={
            EnumerationLiteral(name="positioning"),
			EnumerationLiteral(name="stressManagement"),
			EnumerationLiteral(name="playmakingMechanics"),
			EnumerationLiteral(name="escapeMechanics"),
			EnumerationLiteral(name="patience"),
			EnumerationLiteral(name="farm"),
			EnumerationLiteral(name="steal"),
			EnumerationLiteral(name="splitPush"),
			EnumerationLiteral(name="teamPlay"),
			EnumerationLiteral(name="aggressivity"),
			EnumerationLiteral(name="leadership"),
			EnumerationLiteral(name="draft"),
			EnumerationLiteral(name="pathing"),
			EnumerationLiteral(name="awareness"),
			EnumerationLiteral(name="experience"),
			EnumerationLiteral(name="objectivePlay"),
			EnumerationLiteral(name="metaGame")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="attackDamageCarry"),
			EnumerationLiteral(name="support"),
			EnumerationLiteral(name="midLane"),
			EnumerationLiteral(name="topLane"),
			EnumerationLiteral(name="jungle")
    }
)

TournamentType: Enumeration = Enumeration(
    name="TournamentType",
    literals={
            EnumerationLiteral(name="worlds"),
			EnumerationLiteral(name="regionals"),
			EnumerationLiteral(name="allStars"),
			EnumerationLiteral(name="promotion"),
			EnumerationLiteral(name="midSeasonInvitational"),
			EnumerationLiteral(name="riftRivals"),
			EnumerationLiteral(name="playOff")
    }
)

GroupStageType: Enumeration = Enumeration(
    name="GroupStageType",
    literals={
            EnumerationLiteral(name="league"),
			EnumerationLiteral(name="worldsPlayIn"),
			EnumerationLiteral(name="worldsGroup"),
			EnumerationLiteral(name="riftRivalsGroup"),
			EnumerationLiteral(name="msiPlayIn"),
			EnumerationLiteral(name="msiGroup"),
			EnumerationLiteral(name="allStarsGroup")
    }
)

MatchType: Enumeration = Enumeration(
    name="MatchType",
    literals={
            EnumerationLiteral(name="quarterFinal"),
			EnumerationLiteral(name="singleRoundElimination"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="final"),
			EnumerationLiteral(name="semiFinal")
    }
)

Season: Enumeration = Enumeration(
    name="Season",
    literals={
            EnumerationLiteral(name="spring"),
			EnumerationLiteral(name="summer")
    }
)

# Classes
eSport_Player = Class(name="eSport::Player")
Person = Class(name="Person")
eSport_Team = Class(name="eSport::Team")
eSport_Capacity = Class(name="eSport::Capacity")
eSport_Person = Class(name="eSport::Person", is_abstract=True)
eSport_Coach = Class(name="eSport::Coach")
eSport_Tournament = Class(name="eSport::Tournament")
eSport_Country = Class(name="eSport::Country")
eSport_Zone = Class(name="eSport::Zone")
eSport_FinalStage = Class(name="eSport::FinalStage")
eSport_GroupStage = Class(name="eSport::GroupStage")
eSport_Qualification = Class(name="eSport::Qualification")
eSport_League = Class(name="eSport::League")
eSport_Match = Class(name="eSport::Match")
eSport_Group = Class(name="eSport::Group")
eSport_Root = Class(name="eSport::Root")

# eSport_Player class attributes and methods
eSport_Player_position: Property = Property(name="position", type=StringType)
eSport_Player.attributes={eSport_Player_position}

# Person class attributes and methods

# eSport_Team class attributes and methods
eSport_Team_championshipPoints: Property = Property(name="championshipPoints", type=IntegerType)
eSport_Team_name: Property = Property(name="name", type=StringType)
eSport_Team.attributes={eSport_Team_name, eSport_Team_championshipPoints}

# eSport_Capacity class attributes and methods
eSport_Capacity_type: Property = Property(name="type", type=StringType)
eSport_Capacity_value: Property = Property(name="value", type=IntegerType)
eSport_Capacity.attributes={eSport_Capacity_value, eSport_Capacity_type}

# eSport_Person class attributes and methods
eSport_Person_name: Property = Property(name="name", type=StringType)
eSport_Person_age: Property = Property(name="age", type=IntegerType)
eSport_Person_description: Property = Property(name="description", type=StringType)
eSport_Person.attributes={eSport_Person_description, eSport_Person_age, eSport_Person_name}

# eSport_Coach class attributes and methods

# eSport_Tournament class attributes and methods
eSport_Tournament_name: Property = Property(name="name", type=StringType)
eSport_Tournament_size: Property = Property(name="size", type=IntegerType)
eSport_Tournament_type: Property = Property(name="type", type=StringType)
eSport_Tournament_year: Property = Property(name="year", type=IntegerType)
eSport_Tournament.attributes={eSport_Tournament_name, eSport_Tournament_type, eSport_Tournament_year, eSport_Tournament_size}

# eSport_Country class attributes and methods
eSport_Country_name: Property = Property(name="name", type=StringType)
eSport_Country.attributes={eSport_Country_name}

# eSport_Zone class attributes and methods
eSport_Zone_name: Property = Property(name="name", type=StringType)
eSport_Zone.attributes={eSport_Zone_name}

# eSport_FinalStage class attributes and methods
eSport_FinalStage_maxNbGames: Property = Property(name="maxNbGames", type=IntegerType)
eSport_FinalStage.attributes={eSport_FinalStage_maxNbGames}

# eSport_GroupStage class attributes and methods
eSport_GroupStage_type: Property = Property(name="type", type=StringType)
eSport_GroupStage_maxNbGames: Property = Property(name="maxNbGames", type=IntegerType)
eSport_GroupStage_meetingsInSameGroup: Property = Property(name="meetingsInSameGroup", type=IntegerType)
eSport_GroupStage_meetingsWithOtherGroups: Property = Property(name="meetingsWithOtherGroups", type=IntegerType)
eSport_GroupStage.attributes={eSport_GroupStage_meetingsWithOtherGroups, eSport_GroupStage_maxNbGames, eSport_GroupStage_meetingsInSameGroup, eSport_GroupStage_type}

# eSport_Qualification class attributes and methods
eSport_Qualification_name: Property = Property(name="name", type=StringType)
eSport_Qualification.attributes={eSport_Qualification_name}

# eSport_League class attributes and methods
eSport_League_year: Property = Property(name="year", type=IntegerType)
eSport_League_season: Property = Property(name="season", type=StringType)
eSport_League_name: Property = Property(name="name", type=StringType)
eSport_League_size: Property = Property(name="size", type=IntegerType)
eSport_League.attributes={eSport_League_year, eSport_League_size, eSport_League_season, eSport_League_name}

# eSport_Match class attributes and methods
eSport_Match_loserWins: Property = Property(name="loserWins", type=IntegerType)
eSport_Match_type: Property = Property(name="type", type=StringType)
eSport_Match.attributes={eSport_Match_loserWins, eSport_Match_type}

# eSport_Group class attributes and methods

# eSport_Root class attributes and methods

# Relationships
team0: BinaryAssociation = BinaryAssociation(
    name="team0",
    ends={
        Property(name="Team", type=eSport_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="players", type=eSport_Team, multiplicity=Multiplicity(0, 1))
    }
)
zone12: BinaryAssociation = BinaryAssociation(
    name="zone12",
    ends={
        Property(name="Zone13", type=eSport_League, multiplicity=Multiplicity(1, 1)),
        Property(name="leagues", type=eSport_Zone, multiplicity=Multiplicity(0, 1))
    }
)
groupstage14: BinaryAssociation = BinaryAssociation(
    name="groupstage14",
    ends={
        Property(name="GroupStage15", type=eSport_League, multiplicity=Multiplicity(1, 1)),
        Property(name="league", type=eSport_GroupStage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiesFor16: BinaryAssociation = BinaryAssociation(
    name="qualifiesFor16",
    ends={
        Property(name="Qualification17", type=eSport_League, multiplicity=Multiplicity(1, 1)),
        Property(name="leagueFrom", type=eSport_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
country18: BinaryAssociation = BinaryAssociation(
    name="country18",
    ends={
        Property(name="Country19", type=eSport_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=eSport_Country, multiplicity=Multiplicity(0, 1))
    }
)
capacities20: BinaryAssociation = BinaryAssociation(
    name="capacities20",
    ends={
        Property(name="eSport_Capacity", type=eSport_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Person", type=eSport_Capacity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
team1: BinaryAssociation = BinaryAssociation(
    name="team1",
    ends={
        Property(name="Team2", type=eSport_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coach", type=eSport_Team, multiplicity=Multiplicity(0, 1))
    }
)
countries3: BinaryAssociation = BinaryAssociation(
    name="countries3",
    ends={
        Property(name="Country", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournaments", type=eSport_Country, multiplicity=Multiplicity(0, 9999))
    }
)
allowedZones4: BinaryAssociation = BinaryAssociation(
    name="allowedZones4",
    ends={
        Property(name="Zone", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournaments5", type=eSport_Zone, multiplicity=Multiplicity(0, 9999))
    }
)
finalstages6: BinaryAssociation = BinaryAssociation(
    name="finalstages6",
    ends={
        Property(name="FinalStage", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament", type=eSport_FinalStage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupstages7: BinaryAssociation = BinaryAssociation(
    name="groupstages7",
    ends={
        Property(name="GroupStage", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament8", type=eSport_GroupStage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiesFor9: BinaryAssociation = BinaryAssociation(
    name="qualifiesFor9",
    ends={
        Property(name="Qualification", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournamentFrom", type=eSport_Qualification, multiplicity=Multiplicity(0, 1))
    }
)
qualifiesFrom10: BinaryAssociation = BinaryAssociation(
    name="qualifiesFrom10",
    ends={
        Property(name="Qualification11", type=eSport_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournamentTo", type=eSport_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
matchsWon42: BinaryAssociation = BinaryAssociation(
    name="matchsWon42",
    ends={
        Property(name="Match", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="teamWinner", type=eSport_Match, multiplicity=Multiplicity(0, 9999))
    }
)
matchsLost43: BinaryAssociation = BinaryAssociation(
    name="matchsLost43",
    ends={
        Property(name="Match44", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="teamLoser", type=eSport_Match, multiplicity=Multiplicity(0, 9999))
    }
)
finalstages45: BinaryAssociation = BinaryAssociation(
    name="finalstages45",
    ends={
        Property(name="FinalStage47", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="teams46", type=eSport_FinalStage, multiplicity=Multiplicity(0, 9999))
    }
)
tournaments21: BinaryAssociation = BinaryAssociation(
    name="tournaments21",
    ends={
        Property(name="Tournament", type=eSport_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="countries", type=eSport_Tournament, multiplicity=Multiplicity(0, 9999))
    }
)
zone22: BinaryAssociation = BinaryAssociation(
    name="zone22",
    ends={
        Property(name="Zone24", type=eSport_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="countries23", type=eSport_Zone, multiplicity=Multiplicity(0, 1))
    }
)
persons25: BinaryAssociation = BinaryAssociation(
    name="persons25",
    ends={
        Property(name="Person", type=eSport_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="country", type=eSport_Person, multiplicity=Multiplicity(0, 9999))
    }
)
tournaments26: BinaryAssociation = BinaryAssociation(
    name="tournaments26",
    ends={
        Property(name="Tournament27", type=eSport_Zone, multiplicity=Multiplicity(1, 1)),
        Property(name="allowedZones", type=eSport_Tournament, multiplicity=Multiplicity(0, 9999))
    }
)
leagues28: BinaryAssociation = BinaryAssociation(
    name="leagues28",
    ends={
        Property(name="League", type=eSport_Zone, multiplicity=Multiplicity(1, 1)),
        Property(name="zone", type=eSport_League, multiplicity=Multiplicity(0, 9999))
    }
)
countries29: BinaryAssociation = BinaryAssociation(
    name="countries29",
    ends={
        Property(name="Country31", type=eSport_Zone, multiplicity=Multiplicity(1, 1)),
        Property(name="zone30", type=eSport_Country, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teams32: BinaryAssociation = BinaryAssociation(
    name="teams32",
    ends={
        Property(name="Team34", type=eSport_Zone, multiplicity=Multiplicity(1, 1)),
        Property(name="zone33", type=eSport_Team, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
players35: BinaryAssociation = BinaryAssociation(
    name="players35",
    ends={
        Property(name="Player", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="team", type=eSport_Player, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coach36: BinaryAssociation = BinaryAssociation(
    name="coach36",
    ends={
        Property(name="Coach", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="team37", type=eSport_Coach, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
zone38: BinaryAssociation = BinaryAssociation(
    name="zone38",
    ends={
        Property(name="Zone39", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="teams", type=eSport_Zone, multiplicity=Multiplicity(0, 1))
    }
)
groups40: BinaryAssociation = BinaryAssociation(
    name="groups40",
    ends={
        Property(name="Group", type=eSport_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="teams41", type=eSport_Group, multiplicity=Multiplicity(0, 9999))
    }
)
groupstage57: BinaryAssociation = BinaryAssociation(
    name="groupstage57",
    ends={
        Property(name="GroupStage58", type=eSport_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=eSport_GroupStage, multiplicity=Multiplicity(0, 1))
    }
)
matchs59: BinaryAssociation = BinaryAssociation(
    name="matchs59",
    ends={
        Property(name="Match60", type=eSport_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=eSport_Match, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teams61: BinaryAssociation = BinaryAssociation(
    name="teams61",
    ends={
        Property(name="Team63", type=eSport_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups62", type=eSport_Team, multiplicity=Multiplicity(0, 9999))
    }
)
groups64: BinaryAssociation = BinaryAssociation(
    name="groups64",
    ends={
        Property(name="Group65", type=eSport_GroupStage, multiplicity=Multiplicity(1, 1)),
        Property(name="groupstage", type=eSport_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournament66: BinaryAssociation = BinaryAssociation(
    name="tournament66",
    ends={
        Property(name="Tournament67", type=eSport_GroupStage, multiplicity=Multiplicity(1, 1)),
        Property(name="groupstages", type=eSport_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
league68: BinaryAssociation = BinaryAssociation(
    name="league68",
    ends={
        Property(name="League70", type=eSport_GroupStage, multiplicity=Multiplicity(1, 1)),
        Property(name="groupstage69", type=eSport_League, multiplicity=Multiplicity(0, 1))
    }
)
group48: BinaryAssociation = BinaryAssociation(
    name="group48",
    ends={
        Property(name="Group49", type=eSport_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="matchs", type=eSport_Group, multiplicity=Multiplicity(0, 1))
    }
)
finalstage50: BinaryAssociation = BinaryAssociation(
    name="finalstage50",
    ends={
        Property(name="FinalStage52", type=eSport_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="matchs51", type=eSport_FinalStage, multiplicity=Multiplicity(0, 1))
    }
)
teamWinner53: BinaryAssociation = BinaryAssociation(
    name="teamWinner53",
    ends={
        Property(name="Team54", type=eSport_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="matchsWon", type=eSport_Team, multiplicity=Multiplicity(0, 1))
    }
)
teamLoser55: BinaryAssociation = BinaryAssociation(
    name="teamLoser55",
    ends={
        Property(name="Team56", type=eSport_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="matchsLost", type=eSport_Team, multiplicity=Multiplicity(0, 1))
    }
)
zones85: BinaryAssociation = BinaryAssociation(
    name="zones85",
    ends={
        Property(name="eSport_Zone", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root", type=eSport_Zone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournaments86: BinaryAssociation = BinaryAssociation(
    name="tournaments86",
    ends={
        Property(name="eSport_Tournament", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root87", type=eSport_Tournament, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leagues88: BinaryAssociation = BinaryAssociation(
    name="leagues88",
    ends={
        Property(name="eSport_League", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root89", type=eSport_League, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teams90: BinaryAssociation = BinaryAssociation(
    name="teams90",
    ends={
        Property(name="eSport_Team", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root91", type=eSport_Team, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons92: BinaryAssociation = BinaryAssociation(
    name="persons92",
    ends={
        Property(name="eSport_Person94", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root93", type=eSport_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifications95: BinaryAssociation = BinaryAssociation(
    name="qualifications95",
    ends={
        Property(name="eSport_Qualification", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root96", type=eSport_Qualification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchs71: BinaryAssociation = BinaryAssociation(
    name="matchs71",
    ends={
        Property(name="Match72", type=eSport_FinalStage, multiplicity=Multiplicity(1, 1)),
        Property(name="finalstage", type=eSport_Match, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournament73: BinaryAssociation = BinaryAssociation(
    name="tournament73",
    ends={
        Property(name="Tournament74", type=eSport_FinalStage, multiplicity=Multiplicity(1, 1)),
        Property(name="finalstages", type=eSport_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
teams75: BinaryAssociation = BinaryAssociation(
    name="teams75",
    ends={
        Property(name="Team77", type=eSport_FinalStage, multiplicity=Multiplicity(1, 1)),
        Property(name="finalstages76", type=eSport_Team, multiplicity=Multiplicity(0, 9999))
    }
)
tournamentFrom78: BinaryAssociation = BinaryAssociation(
    name="tournamentFrom78",
    ends={
        Property(name="Tournament79", type=eSport_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiesFor", type=eSport_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
tournamentTo80: BinaryAssociation = BinaryAssociation(
    name="tournamentTo80",
    ends={
        Property(name="Tournament81", type=eSport_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiesFrom", type=eSport_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
leagueFrom82: BinaryAssociation = BinaryAssociation(
    name="leagueFrom82",
    ends={
        Property(name="League84", type=eSport_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiesFor83", type=eSport_League, multiplicity=Multiplicity(0, 1))
    }
)
countries97: BinaryAssociation = BinaryAssociation(
    name="countries97",
    ends={
        Property(name="eSport_Country", type=eSport_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="eSport_Root98", type=eSport_Country, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_eSport_Player_Person = Generalization(general=Person, specific=eSport_Player)
gen_eSport_Coach_Person = Generalization(general=Person, specific=eSport_Coach)

# Domain Model
domain_model = DomainModel(
    name="eSport",
    types={eSport_Player, Person, eSport_Team, eSport_Capacity, eSport_Person, eSport_Coach, eSport_Tournament, eSport_Country, eSport_Zone, eSport_FinalStage, eSport_GroupStage, eSport_Qualification, eSport_League, eSport_Match, eSport_Group, eSport_Root, CapacityType, Position, TournamentType, GroupStageType, MatchType, Season},
    associations={team0, zone12, groupstage14, qualifiesFor16, country18, capacities20, team1, countries3, allowedZones4, finalstages6, groupstages7, qualifiesFor9, qualifiesFrom10, matchsWon42, matchsLost43, finalstages45, tournaments21, zone22, persons25, tournaments26, leagues28, countries29, teams32, players35, coach36, zone38, groups40, groupstage57, matchs59, teams61, groups64, tournament66, league68, group48, finalstage50, teamWinner53, teamLoser55, zones85, tournaments86, leagues88, teams90, persons92, qualifications95, matchs71, tournament73, teams75, tournamentFrom78, tournamentTo80, leagueFrom82, countries97},
    generalizations={gen_eSport_Player_Person, gen_eSport_Coach_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
InvitationEventType: Enumeration = Enumeration(
    name="InvitationEventType",
    literals={
            EnumerationLiteral(name="GENERATED"),
			EnumerationLiteral(name="CHANGED")
    }
)

InvitationReply: Enumeration = Enumeration(
    name="InvitationReply",
    literals={
            EnumerationLiteral(name="NO_REPLY"),
			EnumerationLiteral(name="ACCEPTED"),
			EnumerationLiteral(name="REJECTED")
    }
)

# Classes
pokerleague_DataVersion = Class(name="pokerleague::DataVersion")
pokerleague_Settings = Class(name="pokerleague::Settings")
pokerleague_IdentifiableEntity = Class(name="pokerleague::IdentifiableEntity", is_abstract=True)
pokerleague_DescribedEntity = Class(name="pokerleague::DescribedEntity", is_abstract=True)
IdentifiableEntity = Class(name="IdentifiableEntity")
pokerleague_Player = Class(name="pokerleague::Player")
pokerleague_Serializable = Class(name="pokerleague::Serializable", is_abstract=True)
pokerleague_DataStructureVersion = Class(name="pokerleague::DataStructureVersion")
Serializable = Class(name="Serializable")
pokerleague_PrizeMoneyFormula = Class(name="pokerleague::PrizeMoneyFormula")
pokerleague_Competition = Class(name="pokerleague::Competition")
pokerleague_Tournament = Class(name="pokerleague::Tournament")
pokerleague_PrizeMoneyRuleSet = Class(name="pokerleague::PrizeMoneyRuleSet")
DescribedEntity = Class(name="DescribedEntity")
pokerleague_PrizeMoneyRule = Class(name="pokerleague::PrizeMoneyRule")
pokerleague_Invitation = Class(name="pokerleague::Invitation")
pokerleague_Game = Class(name="pokerleague::Game")
pokerleague_InvitationEvent = Class(name="pokerleague::InvitationEvent")
pokerleague_PlayerInGame = Class(name="pokerleague::PlayerInGame")

# pokerleague_DataVersion class attributes and methods
pokerleague_DataVersion_id: Property = Property(name="id", type=IntegerType)
pokerleague_DataVersion_currentVersion: Property = Property(name="currentVersion", type=StringType)
pokerleague_DataVersion.attributes={pokerleague_DataVersion_id, pokerleague_DataVersion_currentVersion}

# pokerleague_Settings class attributes and methods
pokerleague_Settings_id: Property = Property(name="id", type=IntegerType)
pokerleague_Settings_adminPassword: Property = Property(name="adminPassword", type=StringType)
pokerleague_Settings_defaultTimeZone: Property = Property(name="defaultTimeZone", type=StringType)
pokerleague_Settings_smtpHost: Property = Property(name="smtpHost", type=StringType)
pokerleague_Settings_smtpPort: Property = Property(name="smtpPort", type=StringType)
pokerleague_Settings_smtpUser: Property = Property(name="smtpUser", type=StringType)
pokerleague_Settings_smtpPassword: Property = Property(name="smtpPassword", type=StringType)
pokerleague_Settings_smtpFrom: Property = Property(name="smtpFrom", type=StringType)
pokerleague_Settings_urlBase: Property = Property(name="urlBase", type=StringType)
pokerleague_Settings.attributes={pokerleague_Settings_adminPassword, pokerleague_Settings_smtpUser, pokerleague_Settings_defaultTimeZone, pokerleague_Settings_smtpPassword, pokerleague_Settings_id, pokerleague_Settings_urlBase, pokerleague_Settings_smtpPort, pokerleague_Settings_smtpFrom, pokerleague_Settings_smtpHost}

# pokerleague_IdentifiableEntity class attributes and methods
pokerleague_IdentifiableEntity_id: Property = Property(name="id", type=IntegerType)
pokerleague_IdentifiableEntity_proxy: Property = Property(name="proxy", type=BooleanType)
pokerleague_IdentifiableEntity_obsolete: Property = Property(name="obsolete", type=BooleanType)
pokerleague_IdentifiableEntity.attributes={pokerleague_IdentifiableEntity_obsolete, pokerleague_IdentifiableEntity_id, pokerleague_IdentifiableEntity_proxy}

# pokerleague_DescribedEntity class attributes and methods
pokerleague_DescribedEntity_name: Property = Property(name="name", type=StringType)
pokerleague_DescribedEntity_description: Property = Property(name="description", type=StringType)
pokerleague_DescribedEntity.attributes={pokerleague_DescribedEntity_name, pokerleague_DescribedEntity_description}

# IdentifiableEntity class attributes and methods

# pokerleague_Player class attributes and methods
pokerleague_Player_active: Property = Property(name="active", type=BooleanType)
pokerleague_Player_nick: Property = Property(name="nick", type=StringType)
pokerleague_Player_firstName: Property = Property(name="firstName", type=StringType)
pokerleague_Player_lastName: Property = Property(name="lastName", type=StringType)
pokerleague_Player_emailAddress: Property = Property(name="emailAddress", type=StringType)
pokerleague_Player.attributes={pokerleague_Player_active, pokerleague_Player_nick, pokerleague_Player_emailAddress, pokerleague_Player_lastName, pokerleague_Player_firstName}

# pokerleague_Serializable class attributes and methods

# pokerleague_DataStructureVersion class attributes and methods
pokerleague_DataStructureVersion_id: Property = Property(name="id", type=IntegerType)
pokerleague_DataStructureVersion_currentVersion: Property = Property(name="currentVersion", type=StringType)
pokerleague_DataStructureVersion.attributes={pokerleague_DataStructureVersion_currentVersion, pokerleague_DataStructureVersion_id}

# Serializable class attributes and methods

# pokerleague_PrizeMoneyFormula class attributes and methods
pokerleague_PrizeMoneyFormula_rank: Property = Property(name="rank", type=IntegerType)
pokerleague_PrizeMoneyFormula_relativePrizeMoney: Property = Property(name="relativePrizeMoney", type=IntegerType)
pokerleague_PrizeMoneyFormula.attributes={pokerleague_PrizeMoneyFormula_relativePrizeMoney, pokerleague_PrizeMoneyFormula_rank}

# pokerleague_Competition class attributes and methods
pokerleague_Competition_startDate: Property = Property(name="startDate", type=DateType)
pokerleague_Competition_endDate: Property = Property(name="endDate", type=DateType)
pokerleague_Competition_minimalAttendance: Property = Property(name="minimalAttendance", type=IntegerType)
pokerleague_Competition_defaultBuyIn: Property = Property(name="defaultBuyIn", type=IntegerType)
pokerleague_Competition_defaultMinPlayers: Property = Property(name="defaultMinPlayers", type=IntegerType)
pokerleague_Competition_defaultMaxPlayers: Property = Property(name="defaultMaxPlayers", type=IntegerType)
pokerleague_Competition_defaultTournamentAnnouncementLead: Property = Property(name="defaultTournamentAnnouncementLead", type=IntegerType)
pokerleague_Competition_defaultTournamentInvitationClosure: Property = Property(name="defaultTournamentInvitationClosure", type=IntegerType)
pokerleague_Competition_defaultTournamentInvitationContact: Property = Property(name="defaultTournamentInvitationContact", type=StringType)
pokerleague_Competition.attributes={pokerleague_Competition_defaultBuyIn, pokerleague_Competition_defaultTournamentInvitationClosure, pokerleague_Competition_endDate, pokerleague_Competition_minimalAttendance, pokerleague_Competition_defaultMaxPlayers, pokerleague_Competition_startDate, pokerleague_Competition_defaultMinPlayers, pokerleague_Competition_defaultTournamentAnnouncementLead, pokerleague_Competition_defaultTournamentInvitationContact}

# pokerleague_Tournament class attributes and methods
pokerleague_Tournament_tournamentStart: Property = Property(name="tournamentStart", type=StringType)
pokerleague_Tournament_tournamentEnd: Property = Property(name="tournamentEnd", type=StringType)
pokerleague_Tournament_minPlayers: Property = Property(name="minPlayers", type=IntegerType)
pokerleague_Tournament_maxPlayers: Property = Property(name="maxPlayers", type=IntegerType)
pokerleague_Tournament_defaultBuyIn: Property = Property(name="defaultBuyIn", type=IntegerType)
pokerleague_Tournament_tournamentAnnouncementLead: Property = Property(name="tournamentAnnouncementLead", type=IntegerType)
pokerleague_Tournament_tournamentInvitationClosure: Property = Property(name="tournamentInvitationClosure", type=IntegerType)
pokerleague_Tournament_tournamentInvitationContact: Property = Property(name="tournamentInvitationContact", type=StringType)
pokerleague_Tournament.attributes={pokerleague_Tournament_tournamentInvitationClosure, pokerleague_Tournament_defaultBuyIn, pokerleague_Tournament_tournamentEnd, pokerleague_Tournament_tournamentInvitationContact, pokerleague_Tournament_minPlayers, pokerleague_Tournament_tournamentAnnouncementLead, pokerleague_Tournament_tournamentStart, pokerleague_Tournament_maxPlayers}

# pokerleague_PrizeMoneyRuleSet class attributes and methods

# DescribedEntity class attributes and methods

# pokerleague_PrizeMoneyRule class attributes and methods
pokerleague_PrizeMoneyRule_numberOfPlayers: Property = Property(name="numberOfPlayers", type=IntegerType)
pokerleague_PrizeMoneyRule.attributes={pokerleague_PrizeMoneyRule_numberOfPlayers}

# pokerleague_Invitation class attributes and methods
pokerleague_Invitation_reply: Property = Property(name="reply", type=StringType)
pokerleague_Invitation_ordinal: Property = Property(name="ordinal", type=IntegerType)
pokerleague_Invitation_uuid: Property = Property(name="uuid", type=StringType)
pokerleague_Invitation.attributes={pokerleague_Invitation_uuid, pokerleague_Invitation_reply, pokerleague_Invitation_ordinal}

# pokerleague_Game class attributes and methods
pokerleague_Game_buyIn: Property = Property(name="buyIn", type=IntegerType)
pokerleague_Game_ordinal: Property = Property(name="ordinal", type=IntegerType)
pokerleague_Game.attributes={pokerleague_Game_buyIn, pokerleague_Game_ordinal}

# pokerleague_InvitationEvent class attributes and methods
pokerleague_InvitationEvent_eventTime: Property = Property(name="eventTime", type=StringType)
pokerleague_InvitationEvent_eventType: Property = Property(name="eventType", type=StringType)
pokerleague_InvitationEvent_sent: Property = Property(name="sent", type=BooleanType)
pokerleague_InvitationEvent.attributes={pokerleague_InvitationEvent_sent, pokerleague_InvitationEvent_eventType, pokerleague_InvitationEvent_eventTime}

# pokerleague_PlayerInGame class attributes and methods
pokerleague_PlayerInGame_rank: Property = Property(name="rank", type=IntegerType)
pokerleague_PlayerInGame.attributes={pokerleague_PlayerInGame_rank}

# Relationships
prizeMoneyRuleSet1: BinaryAssociation = BinaryAssociation(
    name="prizeMoneyRuleSet1",
    ends={
        Property(name="PrizeMoneyRuleSet", type=pokerleague_PrizeMoneyRule, multiplicity=Multiplicity(1, 1)),
        Property(name="prizeMoneyRules", type=pokerleague_PrizeMoneyRuleSet, multiplicity=Multiplicity(0, 1))
    }
)
prizeMoneyFormulas2: BinaryAssociation = BinaryAssociation(
    name="prizeMoneyFormulas2",
    ends={
        Property(name="PrizeMoneyFormula", type=pokerleague_PrizeMoneyRule, multiplicity=Multiplicity(1, 1)),
        Property(name="prizeMoneyRule", type=pokerleague_PrizeMoneyFormula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prizeMoneyRule3: BinaryAssociation = BinaryAssociation(
    name="prizeMoneyRule3",
    ends={
        Property(name="PrizeMoneyRule4", type=pokerleague_PrizeMoneyFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="prizeMoneyFormulas", type=pokerleague_PrizeMoneyRule, multiplicity=Multiplicity(0, 1))
    }
)
defaultPrizeMoneyRuleSet5: BinaryAssociation = BinaryAssociation(
    name="defaultPrizeMoneyRuleSet5",
    ends={
        Property(name="pokerleague_PrizeMoneyRuleSet", type=pokerleague_Competition, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_Competition", type=pokerleague_PrizeMoneyRuleSet, multiplicity=Multiplicity(0, 1))
    }
)
tournaments6: BinaryAssociation = BinaryAssociation(
    name="tournaments6",
    ends={
        Property(name="Tournament", type=pokerleague_Competition, multiplicity=Multiplicity(1, 1)),
        Property(name="competition", type=pokerleague_Tournament, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
players7: BinaryAssociation = BinaryAssociation(
    name="players7",
    ends={
        Property(name="pokerleague_Player", type=pokerleague_Competition, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_Competition8", type=pokerleague_Player, multiplicity=Multiplicity(0, 9999))
    }
)
prizeMoneyRules0: BinaryAssociation = BinaryAssociation(
    name="prizeMoneyRules0",
    ends={
        Property(name="PrizeMoneyRule", type=pokerleague_PrizeMoneyRuleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="prizeMoneyRuleSet", type=pokerleague_PrizeMoneyRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invitations11: BinaryAssociation = BinaryAssociation(
    name="invitations11",
    ends={
        Property(name="Invitation", type=pokerleague_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament", type=pokerleague_Invitation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
competition12: BinaryAssociation = BinaryAssociation(
    name="competition12",
    ends={
        Property(name="Competition", type=pokerleague_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournaments", type=pokerleague_Competition, multiplicity=Multiplicity(0, 1))
    }
)
games13: BinaryAssociation = BinaryAssociation(
    name="games13",
    ends={
        Property(name="Game", type=pokerleague_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="tournament14", type=pokerleague_Game, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tournament15: BinaryAssociation = BinaryAssociation(
    name="tournament15",
    ends={
        Property(name="Tournament16", type=pokerleague_Invitation, multiplicity=Multiplicity(1, 1)),
        Property(name="invitations", type=pokerleague_Tournament, multiplicity=Multiplicity(0, 1))
    }
)
player17: BinaryAssociation = BinaryAssociation(
    name="player17",
    ends={
        Property(name="pokerleague_Player18", type=pokerleague_Invitation, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_Invitation", type=pokerleague_Player, multiplicity=Multiplicity(0, 1))
    }
)
events19: BinaryAssociation = BinaryAssociation(
    name="events19",
    ends={
        Property(name="InvitationEvent", type=pokerleague_Invitation, multiplicity=Multiplicity(1, 1)),
        Property(name="invitation", type=pokerleague_InvitationEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invitation20: BinaryAssociation = BinaryAssociation(
    name="invitation20",
    ends={
        Property(name="Invitation21", type=pokerleague_InvitationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=pokerleague_Invitation, multiplicity=Multiplicity(0, 1))
    }
)
defaultPrizeMoneyRuleSet9: BinaryAssociation = BinaryAssociation(
    name="defaultPrizeMoneyRuleSet9",
    ends={
        Property(name="pokerleague_PrizeMoneyRuleSet10", type=pokerleague_Tournament, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_Tournament", type=pokerleague_PrizeMoneyRuleSet, multiplicity=Multiplicity(0, 1))
    }
)
prizeMoneyRuleSet24: BinaryAssociation = BinaryAssociation(
    name="prizeMoneyRuleSet24",
    ends={
        Property(name="pokerleague_PrizeMoneyRuleSet25", type=pokerleague_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_Game", type=pokerleague_PrizeMoneyRuleSet, multiplicity=Multiplicity(0, 1))
    }
)
playersInGame26: BinaryAssociation = BinaryAssociation(
    name="playersInGame26",
    ends={
        Property(name="PlayerInGame", type=pokerleague_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game", type=pokerleague_PlayerInGame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
player27: BinaryAssociation = BinaryAssociation(
    name="player27",
    ends={
        Property(name="pokerleague_Player28", type=pokerleague_PlayerInGame, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerleague_PlayerInGame", type=pokerleague_Player, multiplicity=Multiplicity(0, 1))
    }
)
game29: BinaryAssociation = BinaryAssociation(
    name="game29",
    ends={
        Property(name="Game30", type=pokerleague_PlayerInGame, multiplicity=Multiplicity(1, 1)),
        Property(name="playersInGame", type=pokerleague_Game, multiplicity=Multiplicity(0, 1))
    }
)
tournament22: BinaryAssociation = BinaryAssociation(
    name="tournament22",
    ends={
        Property(name="Tournament23", type=pokerleague_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="games", type=pokerleague_Tournament, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pokerleague_DataVersion_Serializable = Generalization(general=Serializable, specific=pokerleague_DataVersion)
gen_pokerleague_Settings_Serializable = Generalization(general=Serializable, specific=pokerleague_Settings)
gen_pokerleague_IdentifiableEntity_Serializable = Generalization(general=Serializable, specific=pokerleague_IdentifiableEntity)
gen_pokerleague_DescribedEntity_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_DescribedEntity)
gen_pokerleague_Player_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_Player)
gen_pokerleague_DataStructureVersion_Serializable = Generalization(general=Serializable, specific=pokerleague_DataStructureVersion)
gen_pokerleague_PrizeMoneyRule_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_PrizeMoneyRule)
gen_pokerleague_PrizeMoneyFormula_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_PrizeMoneyFormula)
gen_pokerleague_Competition_DescribedEntity = Generalization(general=DescribedEntity, specific=pokerleague_Competition)
gen_pokerleague_Tournament_DescribedEntity = Generalization(general=DescribedEntity, specific=pokerleague_Tournament)
gen_pokerleague_PrizeMoneyRuleSet_DescribedEntity = Generalization(general=DescribedEntity, specific=pokerleague_PrizeMoneyRuleSet)
gen_pokerleague_Invitation_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_Invitation)
gen_pokerleague_InvitationEvent_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_InvitationEvent)
gen_pokerleague_PlayerInGame_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_PlayerInGame)
gen_pokerleague_Game_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=pokerleague_Game)

# Domain Model
domain_model = DomainModel(
    name="pokerleague",
    types={pokerleague_DataVersion, pokerleague_Settings, pokerleague_IdentifiableEntity, pokerleague_DescribedEntity, IdentifiableEntity, pokerleague_Player, pokerleague_Serializable, pokerleague_DataStructureVersion, Serializable, pokerleague_PrizeMoneyFormula, pokerleague_Competition, pokerleague_Tournament, pokerleague_PrizeMoneyRuleSet, DescribedEntity, pokerleague_PrizeMoneyRule, pokerleague_Invitation, pokerleague_Game, pokerleague_InvitationEvent, pokerleague_PlayerInGame, InvitationEventType, InvitationReply},
    associations={prizeMoneyRuleSet1, prizeMoneyFormulas2, prizeMoneyRule3, defaultPrizeMoneyRuleSet5, tournaments6, players7, prizeMoneyRules0, invitations11, competition12, games13, tournament15, player17, events19, invitation20, defaultPrizeMoneyRuleSet9, prizeMoneyRuleSet24, playersInGame26, player27, game29, tournament22},
    generalizations={gen_pokerleague_DataVersion_Serializable, gen_pokerleague_Settings_Serializable, gen_pokerleague_IdentifiableEntity_Serializable, gen_pokerleague_DescribedEntity_IdentifiableEntity, gen_pokerleague_Player_IdentifiableEntity, gen_pokerleague_DataStructureVersion_Serializable, gen_pokerleague_PrizeMoneyRule_IdentifiableEntity, gen_pokerleague_PrizeMoneyFormula_IdentifiableEntity, gen_pokerleague_Competition_DescribedEntity, gen_pokerleague_Tournament_DescribedEntity, gen_pokerleague_PrizeMoneyRuleSet_DescribedEntity, gen_pokerleague_Invitation_IdentifiableEntity, gen_pokerleague_InvitationEvent_IdentifiableEntity, gen_pokerleague_PlayerInGame_IdentifiableEntity, gen_pokerleague_Game_IdentifiableEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
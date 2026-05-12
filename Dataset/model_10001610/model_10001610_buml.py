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
Int: Enumeration = Enumeration(
    name="Int",
    literals={
            
    }
)

# Classes
game_Deck = Class(name="game_Deck", is_abstract=True)
game_Card = Class(name="game_Card")
game_Ace = Class(name="game_Ace")
game_Pack = Class(name="game_Pack")
game_GameController = Class(name="game_GameController")
account_UserAccount = Class(name="account_UserAccount")
account_UserAccountController = Class(name="account_UserAccountController")
account_UserAccountRepository_Interface = Class(name="account_UserAccountRepository_Interface")
account_UserAccountPublicInfo = Class(name="account_UserAccountPublicInfo")
account_UserAccountPasswordChange = Class(name="account_UserAccountPasswordChange")
profile_UserProfileRepository_Interface = Class(name="profile_UserProfileRepository_Interface")
profile_UserProfileController = Class(name="profile_UserProfileController")
profile_UserProfile = Class(name="profile_UserProfile")
Integer_Interface = Class(name="Integer_Interface")
CrudRepository_Interface = Class(name="CrudRepository_Interface")
UserAccount = Class(name="UserAccount")
UserProfileRequestCreate = Class(name="UserProfileRequestCreate")

# game_Deck class attributes and methods
game_Deck_cards: Property = Property(name="cards", type=StringType)
game_Deck.attributes={game_Deck_cards}

# game_Card class attributes and methods
game_Card_name: Property = Property(name="name", type=StringType)
game_Card_suit: Property = Property(name="suit", type=StringType)
game_Card.attributes={game_Card_suit, game_Card_name}

# game_Ace class attributes and methods

# game_Pack class attributes and methods

# game_GameController class attributes and methods

# account_UserAccount class attributes and methods
account_UserAccount_id: Property = Property(name="id", type=StringType)
account_UserAccount_email: Property = Property(name="email", type=StringType)
account_UserAccount_password: Property = Property(name="password", type=StringType)
account_UserAccount_createdAt: Property = Property(name="createdAt", type=StringType)
account_UserAccount_gamesPlayed: Property = Property(name="gamesPlayed", type=StringType)
account_UserAccount_gamesWon: Property = Property(name="gamesWon", type=StringType)
account_UserAccount_alias: Property = Property(name="alias", type=StringType)
account_UserAccount.attributes={account_UserAccount_gamesPlayed, account_UserAccount_id, account_UserAccount_alias, account_UserAccount_password, account_UserAccount_gamesWon, account_UserAccount_createdAt, account_UserAccount_email}

# account_UserAccountController class attributes and methods
account_UserAccountController_URL: Property = Property(name="URL", type=StringType)
account_UserAccountController_userAccountRepository: Property = Property(name="userAccountRepository", type=account_UserAccountRepository_Interface)
account_UserAccountController.attributes={account_UserAccountController_userAccountRepository, account_UserAccountController_URL}

# account_UserAccountRepository_Interface class attributes and methods

# account_UserAccountPublicInfo class attributes and methods
account_UserAccountPublicInfo_id: Property = Property(name="id", type=StringType)
account_UserAccountPublicInfo_alias: Property = Property(name="alias", type=StringType)
account_UserAccountPublicInfo_gamesPlayed: Property = Property(name="gamesPlayed", type=StringType)
account_UserAccountPublicInfo_gamesWon: Property = Property(name="gamesWon", type=StringType)
account_UserAccountPublicInfo.attributes={account_UserAccountPublicInfo_gamesPlayed, account_UserAccountPublicInfo_gamesWon, account_UserAccountPublicInfo_id, account_UserAccountPublicInfo_alias}

# account_UserAccountPasswordChange class attributes and methods
account_UserAccountPasswordChange_email: Property = Property(name="email", type=StringType)
account_UserAccountPasswordChange_oldPassword: Property = Property(name="oldPassword", type=StringType)
account_UserAccountPasswordChange_newPassword: Property = Property(name="newPassword", type=StringType)
account_UserAccountPasswordChange.attributes={account_UserAccountPasswordChange_oldPassword, account_UserAccountPasswordChange_email, account_UserAccountPasswordChange_newPassword}

# profile_UserProfileRepository_Interface class attributes and methods

# profile_UserProfileController class attributes and methods
profile_UserProfileController_URL: Property = Property(name="URL", type=StringType)
profile_UserProfileController_userAccountRepository: Property = Property(name="userAccountRepository", type=account_UserAccountRepository_Interface)
profile_UserProfileController_attribute: Property = Property(name="attribute", type=StringType)
profile_UserProfileController_userProfileRepository: Property = Property(name="userProfileRepository", type=profile_UserProfileRepository_Interface)
profile_UserProfileController.attributes={profile_UserProfileController_attribute, profile_UserProfileController_userProfileRepository, profile_UserProfileController_userAccountRepository, profile_UserProfileController_URL}

# profile_UserProfile class attributes and methods
profile_UserProfile_id: Property = Property(name="id", type=StringType)
profile_UserProfile_name: Property = Property(name="name", type=StringType)
profile_UserProfile_uid: Property = Property(name="uid", type=StringType)
profile_UserProfile_credits: Property = Property(name="credits", type=StringType)
profile_UserProfile_attribute: Property = Property(name="attribute", type=StringType)
profile_UserProfile.attributes={profile_UserProfile_name, profile_UserProfile_attribute, profile_UserProfile_uid, profile_UserProfile_credits, profile_UserProfile_id}

# Integer_Interface class attributes and methods

# CrudRepository_Interface class attributes and methods

# UserAccount class attributes and methods

# UserProfileRequestCreate class attributes and methods

# Relationships
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="deck0", type=game_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=game_Card, multiplicity=Multiplicity(52, 52))
    }
)
UserAccountRepository_UserAccountController: BinaryAssociation = BinaryAssociation(
    name="UserAccountRepository_UserAccountController",
    ends={
        Property(name="userAccountController2", type=account_UserAccountController, multiplicity=Multiplicity(0, 1)),
        Property(name="userAccountRepository23", type=account_UserAccountRepository_Interface, multiplicity=Multiplicity(0, 1))
    }
)
UserAccountPublicInfo_UserAccountController: BinaryAssociation = BinaryAssociation(
    name="UserAccountPublicInfo_UserAccountController",
    ends={
        Property(name="userAccountController4", type=account_UserAccountController, multiplicity=Multiplicity(0, 1)),
        Property(name="userAccountPublicInfo5", type=account_UserAccountPublicInfo, multiplicity=Multiplicity(0, 1))
    }
)
UserAccount_UserAccountController: BinaryAssociation = BinaryAssociation(
    name="UserAccount_UserAccountController",
    ends={
        Property(name="userAccountController6", type=account_UserAccountController, multiplicity=Multiplicity(0, 1)),
        Property(name="userAccount7", type=account_UserAccount, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JJhpINiMEemWXYASHrbj8g",
    types={game_Deck, game_Card, game_Ace, game_Pack, game_GameController, account_UserAccount, account_UserAccountController, account_UserAccountRepository_Interface, account_UserAccountPublicInfo, account_UserAccountPasswordChange, profile_UserProfileRepository_Interface, profile_UserProfileController, profile_UserProfile, Integer_Interface, CrudRepository_Interface, UserAccount, UserProfileRequestCreate, Int},
    associations={Card_Deck, UserAccountRepository_UserAccountController, UserAccountPublicInfo_UserAccountController, UserAccount_UserAccountController},
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
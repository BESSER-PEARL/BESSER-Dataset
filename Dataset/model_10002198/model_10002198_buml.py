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
Carte = Class(name="Carte")
Croupier = Class(name="Croupier")
Main = Class(name="Main")
Joueur = Class(name="Joueur")
Blackjack = Class(name="Blackjack")

# Carte class attributes and methods
Carte_ordre: Property = Property(name="ordre", type=StringType)
Carte_suit: Property = Property(name="suit", type=IntegerType)
Carte.attributes={Carte_ordre, Carte_suit}

# Croupier class attributes and methods
Croupier_main: Property = Property(name="main", type=StringType)
Croupier.attributes={Croupier_main}

# Main class attributes and methods
Main_cartes: Property = Property(name="cartes", type=StringType)
Main_value: Property = Property(name="value", type=IntegerType)
Main_bet: Property = Property(name="bet", type=StringType)
Main.attributes={Main_value, Main_cartes, Main_bet}

# Joueur class attributes and methods
Joueur_main: Property = Property(name="main", type=StringType)
Joueur_nom: Property = Property(name="nom", type=StringType)
Joueur_playerbank: Property = Property(name="playerbank", type=IntegerType)
Joueur.attributes={Joueur_nom, Joueur_main, Joueur_playerbank}

# Blackjack class attributes and methods
Blackjack_joueurs: Property = Property(name="joueurs", type=StringType)
Blackjack_croupier: Property = Property(name="croupier", type=Croupier)
Blackjack.attributes={Blackjack_joueurs, Blackjack_croupier}

# Relationships
Card_Hand: BinaryAssociation = BinaryAssociation(
    name="Card_Hand",
    ends={
        Property(name="hand0", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="card1", type=Carte, multiplicity=Multiplicity(1, 9999))
    }
)
Blackjack_Dealer: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Dealer",
    ends={
        Property(name="dealer2", type=Croupier, multiplicity=Multiplicity(1, 1)),
        Property(name="blackjack3", type=Blackjack, multiplicity=Multiplicity(1, 1))
    }
)
Dealer_Hand: BinaryAssociation = BinaryAssociation(
    name="Dealer_Hand",
    ends={
        Property(name="hand4", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer5", type=Croupier, multiplicity=Multiplicity(1, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand6", type=Main, multiplicity=Multiplicity(1, 9999)),
        Property(name="player7", type=Joueur, multiplicity=Multiplicity(1, 1))
    }
)
Blackjack_Player: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Player",
    ends={
        Property(name="player8", type=Joueur, multiplicity=Multiplicity(1, 9999)),
        Property(name="blackjack9", type=Blackjack, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vkJhQARWEeipbtix_oa2Dg",
    types={Carte, Croupier, Main, Joueur, Blackjack},
    associations={Card_Hand, Blackjack_Dealer, Dealer_Hand, Player_Hand, Blackjack_Player},
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
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
game_PackObjets = Class(name="game_PackObjets")
game_Interaction = Class(name="game_Interaction")
GameElement = Class(name="GameElement")
game_Chemin = Class(name="game_Chemin")
game_Game = Class(name="game_Game")
game_Explorateur = Class(name="game_Explorateur")
game_Lieu = Class(name="game_Lieu")
game_GameElement = Class(name="game_GameElement")
game_EntiteLieu = Class(name="game_EntiteLieu")
game_Personne = Class(name="game_Personne")
game_Condition = Class(name="game_Condition")
game_ConnaissanceLieu = Class(name="game_ConnaissanceLieu")
EntiteLieu = Class(name="EntiteLieu")
game_Connaissance = Class(name="game_Connaissance")
game_Description = Class(name="game_Description")
game_Litteral = Class(name="game_Litteral")
game_Texte = Class(name="game_Texte")
game_Objet = Class(name="game_Objet")
game_Recompense = Class(name="game_Recompense")
game_Conjonction = Class(name="game_Conjonction")
game_Action = Class(name="game_Action")
game_Choix = Class(name="game_Choix")

# game_PackObjets class attributes and methods
game_PackObjets_quantite: Property = Property(name="quantite", type=IntegerType)
game_PackObjets.attributes={game_PackObjets_quantite}

# game_Interaction class attributes and methods

# GameElement class attributes and methods

# game_Chemin class attributes and methods

# game_Game class attributes and methods
game_Game_name: Property = Property(name="name", type=StringType)
game_Game.attributes={game_Game_name}

# game_Explorateur class attributes and methods
game_Explorateur_name: Property = Property(name="name", type=StringType)
game_Explorateur_tailleInventaire: Property = Property(name="tailleInventaire", type=IntegerType)
game_Explorateur.attributes={game_Explorateur_name, game_Explorateur_tailleInventaire}

# game_Lieu class attributes and methods

# game_GameElement class attributes and methods
game_GameElement_name: Property = Property(name="name", type=StringType)
game_GameElement.attributes={game_GameElement_name}

# game_EntiteLieu class attributes and methods

# game_Personne class attributes and methods
game_Personne_name: Property = Property(name="name", type=StringType)
game_Personne.attributes={game_Personne_name}

# game_Condition class attributes and methods

# game_ConnaissanceLieu class attributes and methods

# EntiteLieu class attributes and methods

# game_Connaissance class attributes and methods

# game_Description class attributes and methods

# game_Litteral class attributes and methods
game_Litteral_operateur: Property = Property(name="operateur", type=StringType)
game_Litteral_quantite: Property = Property(name="quantite", type=IntegerType)
game_Litteral.attributes={game_Litteral_operateur, game_Litteral_quantite}

# game_Texte class attributes and methods
game_Texte_contenu: Property = Property(name="contenu", type=StringType)
game_Texte.attributes={game_Texte_contenu}

# game_Objet class attributes and methods
game_Objet_taille: Property = Property(name="taille", type=IntegerType)
game_Objet.attributes={game_Objet_taille}

# game_Recompense class attributes and methods

# game_Conjonction class attributes and methods

# game_Action class attributes and methods

# game_Choix class attributes and methods
game_Choix_name: Property = Property(name="name", type=StringType)
game_Choix.attributes={game_Choix_name}

# Relationships
connaissances14: BinaryAssociation = BinaryAssociation(
    name="connaissances14",
    ends={
        Property(name="game_Connaissance16", type=game_Explorateur, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Explorateur15", type=game_Connaissance, multiplicity=Multiplicity(0, 9999))
    }
)
inventaire17: BinaryAssociation = BinaryAssociation(
    name="inventaire17",
    ends={
        Property(name="game_PackObjets", type=game_Explorateur, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Explorateur18", type=game_PackObjets, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interaction19: BinaryAssociation = BinaryAssociation(
    name="interaction19",
    ends={
        Property(name="game_Interaction", type=game_Personne, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Personne20", type=game_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
explorateur0: BinaryAssociation = BinaryAssociation(
    name="explorateur0",
    ends={
        Property(name="game_Explorateur", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game", type=game_Explorateur, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lieuDepart1: BinaryAssociation = BinaryAssociation(
    name="lieuDepart1",
    ends={
        Property(name="game_Lieu", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game2", type=game_Lieu, multiplicity=Multiplicity(0, 1))
    }
)
lieuxArrivee3: BinaryAssociation = BinaryAssociation(
    name="lieuxArrivee3",
    ends={
        Property(name="game_Lieu5", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game4", type=game_Lieu, multiplicity=Multiplicity(0, 9999))
    }
)
gameElements6: BinaryAssociation = BinaryAssociation(
    name="gameElements6",
    ends={
        Property(name="game_GameElement", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game7", type=game_GameElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entite8: BinaryAssociation = BinaryAssociation(
    name="entite8",
    ends={
        Property(name="game_Personne", type=game_EntiteLieu, multiplicity=Multiplicity(1, 1)),
        Property(name="game_EntiteLieu", type=game_Personne, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionVisibilite9: BinaryAssociation = BinaryAssociation(
    name="conditionVisibilite9",
    ends={
        Property(name="game_Condition", type=game_EntiteLieu, multiplicity=Multiplicity(1, 1)),
        Property(name="game_EntiteLieu10", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connaissance11: BinaryAssociation = BinaryAssociation(
    name="connaissance11",
    ends={
        Property(name="game_Connaissance", type=game_ConnaissanceLieu, multiplicity=Multiplicity(1, 1)),
        Property(name="game_ConnaissanceLieu", type=game_Connaissance, multiplicity=Multiplicity(0, 1))
    }
)
description12: BinaryAssociation = BinaryAssociation(
    name="description12",
    ends={
        Property(name="game_Description", type=game_GameElement, multiplicity=Multiplicity(1, 1)),
        Property(name="game_GameElement13", type=game_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
litteraux47: BinaryAssociation = BinaryAssociation(
    name="litteraux47",
    ends={
        Property(name="game_Litteral", type=game_Conjonction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Conjonction48", type=game_Litteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objet49: BinaryAssociation = BinaryAssociation(
    name="objet49",
    ends={
        Property(name="game_Objet51", type=game_Litteral, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Litteral50", type=game_Objet, multiplicity=Multiplicity(0, 1))
    }
)
connaissance52: BinaryAssociation = BinaryAssociation(
    name="connaissance52",
    ends={
        Property(name="game_Connaissance54", type=game_Litteral, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Litteral53", type=game_Connaissance, multiplicity=Multiplicity(0, 1))
    }
)
textes55: BinaryAssociation = BinaryAssociation(
    name="textes55",
    ends={
        Property(name="game_Texte", type=game_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Description56", type=game_Texte, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cheminsPossibles21: BinaryAssociation = BinaryAssociation(
    name="cheminsPossibles21",
    ends={
        Property(name="game_Chemin", type=game_Lieu, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Lieu22", type=game_Chemin, multiplicity=Multiplicity(0, 9999))
    }
)
entiteLieu23: BinaryAssociation = BinaryAssociation(
    name="entiteLieu23",
    ends={
        Property(name="game_EntiteLieu25", type=game_Lieu, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Lieu24", type=game_EntiteLieu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objet26: BinaryAssociation = BinaryAssociation(
    name="objet26",
    ends={
        Property(name="game_Objet", type=game_PackObjets, multiplicity=Multiplicity(1, 1)),
        Property(name="game_PackObjets27", type=game_Objet, multiplicity=Multiplicity(0, 1))
    }
)
conditionVisibilite28: BinaryAssociation = BinaryAssociation(
    name="conditionVisibilite28",
    ends={
        Property(name="game_Condition30", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin29", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lieu131: BinaryAssociation = BinaryAssociation(
    name="lieu131",
    ends={
        Property(name="game_Lieu33", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin32", type=game_Lieu, multiplicity=Multiplicity(0, 1))
    }
)
lieu234: BinaryAssociation = BinaryAssociation(
    name="lieu234",
    ends={
        Property(name="game_Lieu36", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin35", type=game_Lieu, multiplicity=Multiplicity(0, 1))
    }
)
ouvert37: BinaryAssociation = BinaryAssociation(
    name="ouvert37",
    ends={
        Property(name="game_Condition39", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin38", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recompenses40: BinaryAssociation = BinaryAssociation(
    name="recompenses40",
    ends={
        Property(name="game_Recompense", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin41", type=game_Recompense, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consommations42: BinaryAssociation = BinaryAssociation(
    name="consommations42",
    ends={
        Property(name="game_PackObjets44", type=game_Chemin, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Chemin43", type=game_PackObjets, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conjonctions45: BinaryAssociation = BinaryAssociation(
    name="conjonctions45",
    ends={
        Property(name="game_Conjonction", type=game_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Condition46", type=game_Conjonction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeConditionsDebut88: BinaryAssociation = BinaryAssociation(
    name="listeConditionsDebut88",
    ends={
        Property(name="game_Condition90", type=game_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Interaction89", type=game_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seulChoixDebut91: BinaryAssociation = BinaryAssociation(
    name="seulChoixDebut91",
    ends={
        Property(name="game_Choix93", type=game_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Interaction92", type=game_Choix, multiplicity=Multiplicity(0, 1))
    }
)
listeChoix94: BinaryAssociation = BinaryAssociation(
    name="listeChoix94",
    ends={
        Property(name="game_Choix96", type=game_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Interaction95", type=game_Choix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description97: BinaryAssociation = BinaryAssociation(
    name="description97",
    ends={
        Property(name="game_Description99", type=game_Choix, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Choix98", type=game_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
choixFin100: BinaryAssociation = BinaryAssociation(
    name="choixFin100",
    ends={
        Property(name="game_Condition102", type=game_Choix, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Choix101", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition57: BinaryAssociation = BinaryAssociation(
    name="condition57",
    ends={
        Property(name="game_Condition59", type=game_Texte, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Texte58", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connaissanceObtenue60: BinaryAssociation = BinaryAssociation(
    name="connaissanceObtenue60",
    ends={
        Property(name="game_Connaissance62", type=game_Recompense, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Recompense61", type=game_Connaissance, multiplicity=Multiplicity(0, 1))
    }
)
objetsObtenus63: BinaryAssociation = BinaryAssociation(
    name="objetsObtenus63",
    ends={
        Property(name="game_PackObjets65", type=game_Recompense, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Recompense64", type=game_PackObjets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionObtention66: BinaryAssociation = BinaryAssociation(
    name="conditionObtention66",
    ends={
        Property(name="game_Condition68", type=game_Recompense, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Recompense67", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description69: BinaryAssociation = BinaryAssociation(
    name="description69",
    ends={
        Property(name="game_Description70", type=game_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Action", type=game_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition71: BinaryAssociation = BinaryAssociation(
    name="condition71",
    ends={
        Property(name="game_Condition73", type=game_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Action72", type=game_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recompenses74: BinaryAssociation = BinaryAssociation(
    name="recompenses74",
    ends={
        Property(name="game_Recompense76", type=game_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Action75", type=game_Recompense, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consommations77: BinaryAssociation = BinaryAssociation(
    name="consommations77",
    ends={
        Property(name="game_PackObjets79", type=game_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Action78", type=game_PackObjets, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choixSuivant80: BinaryAssociation = BinaryAssociation(
    name="choixSuivant80",
    ends={
        Property(name="game_Choix", type=game_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Action81", type=game_Choix, multiplicity=Multiplicity(0, 1))
    }
)
recompenses82: BinaryAssociation = BinaryAssociation(
    name="recompenses82",
    ends={
        Property(name="game_Recompense84", type=game_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Interaction83", type=game_Recompense, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeChoixDebut85: BinaryAssociation = BinaryAssociation(
    name="listeChoixDebut85",
    ends={
        Property(name="game_Choix87", type=game_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Interaction86", type=game_Choix, multiplicity=Multiplicity(0, 9999))
    }
)
listeActions103: BinaryAssociation = BinaryAssociation(
    name="listeActions103",
    ends={
        Property(name="game_Action105", type=game_Choix, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Choix104", type=game_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_game_Lieu_GameElement = Generalization(general=GameElement, specific=game_Lieu)
gen_game_ConnaissanceLieu_EntiteLieu = Generalization(general=EntiteLieu, specific=game_ConnaissanceLieu)
gen_game_Objet_GameElement = Generalization(general=GameElement, specific=game_Objet)
gen_game_PackObjets_EntiteLieu = Generalization(general=EntiteLieu, specific=game_PackObjets)
gen_game_Chemin_GameElement = Generalization(general=GameElement, specific=game_Chemin)
gen_game_Connaissance_GameElement = Generalization(general=GameElement, specific=game_Connaissance)


# OCL Constraints
nomNonNul: Constraint = Constraint(
    name="nomNonNul",
    context=game_Game,
    expression="context Game inv: self.name <> null",
    language="OCL"
)
inventaireNonSurcharge: Constraint = Constraint(
    name="inventaireNonSurcharge",
    context=game_Explorateur,
    expression="context Explorateur inv: let tailleTotale =(self.inventaire -> iterate(p: PackObjets; sum: Integer = 0 | sum + (p.objet.taille)*p.quantite))in tailleTotale <= self.tailleInventaire",
    language="OCL"
)
nomNonNul1: Constraint = Constraint(
    name="nomNonNul1",
    context=game_Explorateur,
    expression="context Explorateur inv: self.name <> null",
    language="OCL"
)
nomNonNul2: Constraint = Constraint(
    name="nomNonNul2",
    context=game_Lieu,
    expression="context Lieu inv: self.name <> null",
    language="OCL"
)
nomNonNul3: Constraint = Constraint(
    name="nomNonNul3",
    context=game_Objet,
    expression="context Objet inv: self.name <> null",
    language="OCL"
)
nomNonNul4: Constraint = Constraint(
    name="nomNonNul4",
    context=game_ConnaissanceLieu,
    expression="context Connaissance inv: self.name <> null",
    language="OCL"
)
nomNonNul5: Constraint = Constraint(
    name="nomNonNul5",
    context=game_Choix,
    expression="context Choix inv: self.name <> null",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="game",
    types={game_PackObjets, game_Interaction, GameElement, game_Chemin, game_Game, game_Explorateur, game_Lieu, game_GameElement, game_EntiteLieu, game_Personne, game_Condition, game_ConnaissanceLieu, EntiteLieu, game_Connaissance, game_Description, game_Litteral, game_Texte, game_Objet, game_Recompense, game_Conjonction, game_Action, game_Choix},
    associations={connaissances14, inventaire17, interaction19, explorateur0, lieuDepart1, lieuxArrivee3, gameElements6, entite8, conditionVisibilite9, connaissance11, description12, litteraux47, objet49, connaissance52, textes55, cheminsPossibles21, entiteLieu23, objet26, conditionVisibilite28, lieu131, lieu234, ouvert37, recompenses40, consommations42, conjonctions45, listeConditionsDebut88, seulChoixDebut91, listeChoix94, description97, choixFin100, condition57, connaissanceObtenue60, objetsObtenus63, conditionObtention66, description69, condition71, recompenses74, consommations77, choixSuivant80, recompenses82, listeChoixDebut85, listeActions103},
    constraints={nomNonNul, inventaireNonSurcharge, nomNonNul1, nomNonNul2, nomNonNul3, nomNonNul4, nomNonNul5},
    generalizations={gen_game_Lieu_GameElement, gen_game_ConnaissanceLieu_EntiteLieu, gen_game_Objet_GameElement, gen_game_PackObjets_EntiteLieu, gen_game_Chemin_GameElement, gen_game_Connaissance_GameElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
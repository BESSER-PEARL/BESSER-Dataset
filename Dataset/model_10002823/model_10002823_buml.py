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
ModelTraint = Class(name="ModelTraint")
Observable = Class(name="Observable", is_abstract=True)
Wagon = Class(name="Wagon")
Joueur = Class(name="Joueur")
Cellule = Class(name="Cellule")
Obsever_Interface = Class(name="Obsever_Interface")
Vue = Class(name="Vue")
Controleur = Class(name="Controleur")
Position = Class(name="Position")
Interieur = Class(name="Interieur")
Toit = Class(name="Toit")

# ModelTraint class attributes and methods
ModelTraint_listeWagon__: Property = Property(name="listeWagon__", type=Wagon)
ModelTraint_cellule____: Property = Property(name="cellule____", type=Cellule)
ModelTraint_joueurs__: Property = Property(name="joueurs__", type=Joueur)
ModelTraint_indiceWagonCourant: Property = Property(name="indiceWagonCourant", type=IntegerType)
ModelTraint_indiceJoueurCourant: Property = Property(name="indiceJoueurCourant", type=IntegerType)
ModelTraint_nombreWagon: Property = Property(name="nombreWagon", type=IntegerType)
ModelTraint_nombreJoueur: Property = Property(name="nombreJoueur", type=IntegerType)
ModelTraint.attributes={ModelTraint_nombreWagon, ModelTraint_listeWagon__, ModelTraint_indiceJoueurCourant, ModelTraint_joueurs__, ModelTraint_nombreJoueur, ModelTraint_cellule____, ModelTraint_indiceWagonCourant}

# Observable class attributes and methods
Observable_listObservers__: Property = Property(name="listObservers__", type=StringType)
Observable.attributes={Observable_listObservers__}

# Wagon class attributes and methods
Wagon_modele: Property = Property(name="modele", type=ModelTraint)
Wagon_numeroWagon: Property = Property(name="numeroWagon", type=IntegerType)
Wagon_ListedesButin__: Property = Property(name="ListedesButin__", type=StringType)
Wagon_listeDesBandit: Property = Property(name="listeDesBandit", type=Joueur)
Wagon.attributes={Wagon_listeDesBandit, Wagon_modele, Wagon_numeroWagon, Wagon_ListedesButin__}

# Joueur class attributes and methods
Joueur_model: Property = Property(name="model", type=ModelTraint)
Joueur_nomJoueur: Property = Property(name="nomJoueur", type=StringType)
Joueur_x_y: Property = Property(name="x_y", type=IntegerType)
Joueur_a_b: Property = Property(name="a_b", type=IntegerType)
Joueur_positionBandit: Property = Property(name="positionBandit", type=Position)
Joueur_attribute: Property = Property(name="attribute", type=StringType)
Joueur.attributes={Joueur_a_b, Joueur_model, Joueur_attribute, Joueur_positionBandit, Joueur_x_y, Joueur_nomJoueur}

# Cellule class attributes and methods
Cellule_model: Property = Property(name="model", type=ModelTraint)
Cellule.attributes={Cellule_model}

# Obsever_Interface class attributes and methods

# Vue class attributes and methods
Vue_modeltrain: Property = Property(name="modeltrain", type=ModelTraint)
Vue.attributes={Vue_modeltrain}

# Controleur class attributes and methods
Controleur_modeletrain: Property = Property(name="modeletrain", type=ModelTraint)
Controleur_vue: Property = Property(name="vue", type=Vue)
Controleur.attributes={Controleur_modeletrain, Controleur_vue}

# Position class attributes and methods
Position_numeroWagon: Property = Property(name="numeroWagon", type=IntegerType)
Position.attributes={Position_numeroWagon}

# Interieur class attributes and methods
Interieur_InnumeroWagon: Property = Property(name="InnumeroWagon", type=IntegerType)
Interieur.attributes={Interieur_InnumeroWagon}

# Toit class attributes and methods
Toit_IntNumereoWagon: Property = Property(name="IntNumereoWagon", type=IntegerType)
Toit.attributes={Toit_IntNumereoWagon}

# Relationships
Cellule_ModelTrant: BinaryAssociation = BinaryAssociation(
    name="Cellule_ModelTrant",
    ends={
        Property(name="modelTraint0", type=ModelTraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cellule1", type=Cellule, multiplicity=Multiplicity(1, 1))
    }
)
ModelTrant_Joueur: BinaryAssociation = BinaryAssociation(
    name="ModelTrant_Joueur",
    ends={
        Property(name="joueurs2", type=Joueur, multiplicity=Multiplicity(0, 9999)),
        Property(name="modelTrant3", type=ModelTraint, multiplicity=Multiplicity(1, 1))
    }
)
ModelTrant_Wagon: BinaryAssociation = BinaryAssociation(
    name="ModelTrant_Wagon",
    ends={
        Property(name="wagons4", type=Wagon, multiplicity=Multiplicity(0, 9999)),
        Property(name="modelTrant5", type=ModelTraint, multiplicity=Multiplicity(0, 9999))
    }
)
Controleur_Vue: BinaryAssociation = BinaryAssociation(
    name="Controleur_Vue",
    ends={
        Property(name="vue6", type=Vue, multiplicity=Multiplicity(1, 1)),
        Property(name="controleur7", type=Controleur, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="def49224_4445_4930_8671_9bd1c5dc68af",
    types={ModelTraint, Observable, Wagon, Joueur, Cellule, Obsever_Interface, Vue, Controleur, Position, Interieur, Toit},
    associations={Cellule_ModelTrant, ModelTrant_Joueur, ModelTrant_Wagon, Controleur_Vue},
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
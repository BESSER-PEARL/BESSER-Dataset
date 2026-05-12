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
compte = Class(name="compte")
reservation = Class(name="reservation")
paiement = Class(name="paiement")
trajet = Class(name="trajet")
administrateur = Class(name="administrateur")
inscription = Class(name="inscription")
passager = Class(name="passager")
conducteur = Class(name="conducteur")
voiture = Class(name="voiture")

# compte class attributes and methods
compte_informations_conducteur: Property = Property(name="informations_conducteur", type=StringType)
compte_informations_passager: Property = Property(name="informations_passager", type=StringType)
compte.attributes={compte_informations_conducteur, compte_informations_passager}

# reservation class attributes and methods
reservation_nombre_de_passager: Property = Property(name="nombre_de_passager", type=IntegerType)
reservation.attributes={reservation_nombre_de_passager}

# paiement class attributes and methods
paiement_m_thode_de_paiement: Property = Property(name="m_thode_de_paiement", type=StringType)
paiement.attributes={paiement_m_thode_de_paiement}

# trajet class attributes and methods
trajet_prix_du_trajet: Property = Property(name="prix_du_trajet", type=FloatType)
trajet_l_heure_de_d_part: Property = Property(name="l_heure_de_d_part", type=FloatType)
trajet_la_date: Property = Property(name="la_date", type=StringType)
trajet_lieu_de_d_part: Property = Property(name="lieu_de_d_part", type=StringType)
trajet.attributes={trajet_prix_du_trajet, trajet_la_date, trajet_l_heure_de_d_part, trajet_lieu_de_d_part}

# administrateur class attributes and methods

# inscription class attributes and methods
inscription_informations_passager: Property = Property(name="informations_passager", type=StringType)
inscription_informations_conducteur: Property = Property(name="informations_conducteur", type=StringType)
inscription.attributes={inscription_informations_conducteur, inscription_informations_passager}

# passager class attributes and methods
passager_informations_passager: Property = Property(name="informations_passager", type=StringType)
passager.attributes={passager_informations_passager}

# conducteur class attributes and methods
conducteur_informations_conducteur: Property = Property(name="informations_conducteur", type=StringType)
conducteur.attributes={conducteur_informations_conducteur}

# voiture class attributes and methods
voiture_type_de_voiture: Property = Property(name="type_de_voiture", type=StringType)
voiture_nombre_de_si_ges: Property = Property(name="nombre_de_si_ges", type=IntegerType)
voiture.attributes={voiture_type_de_voiture, voiture_nombre_de_si_ges}

# Relationships
inscription_passager: BinaryAssociation = BinaryAssociation(
    name="inscription_passager",
    ends={
        Property(name="inscription0", type=inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="passager1", type=passager, multiplicity=Multiplicity(1, 1))
    }
)
compte_passager: BinaryAssociation = BinaryAssociation(
    name="compte_passager",
    ends={
        Property(name="compte2", type=compte, multiplicity=Multiplicity(1, 1)),
        Property(name="passager3", type=passager, multiplicity=Multiplicity(1, 1))
    }
)
passager_paiement: BinaryAssociation = BinaryAssociation(
    name="passager_paiement",
    ends={
        Property(name="passager4", type=passager, multiplicity=Multiplicity(0, 1)),
        Property(name="paiement5", type=paiement, multiplicity=Multiplicity(0, 1))
    }
)
administrateur_reservation: BinaryAssociation = BinaryAssociation(
    name="administrateur_reservation",
    ends={
        Property(name="administrateur6", type=administrateur, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation7", type=reservation, multiplicity=Multiplicity(0, 1))
    }
)
administrateur_paiement: BinaryAssociation = BinaryAssociation(
    name="administrateur_paiement",
    ends={
        Property(name="administrateur8", type=administrateur, multiplicity=Multiplicity(1, 1)),
        Property(name="paiement9", type=paiement, multiplicity=Multiplicity(1, 9999))
    }
)
administrateur_passager: BinaryAssociation = BinaryAssociation(
    name="administrateur_passager",
    ends={
        Property(name="administrateur10", type=administrateur, multiplicity=Multiplicity(0, 1)),
        Property(name="passager11", type=passager, multiplicity=Multiplicity(0, 1))
    }
)
administrateur_inscription: BinaryAssociation = BinaryAssociation(
    name="administrateur_inscription",
    ends={
        Property(name="administrateur12", type=administrateur, multiplicity=Multiplicity(0, 1)),
        Property(name="inscription13", type=inscription, multiplicity=Multiplicity(0, 1))
    }
)
trajet_passager: BinaryAssociation = BinaryAssociation(
    name="trajet_passager",
    ends={
        Property(name="trajet14", type=trajet, multiplicity=Multiplicity(1, 1)),
        Property(name="passager15", type=passager, multiplicity=Multiplicity(1, 9999))
    }
)
inscription_conducteur: BinaryAssociation = BinaryAssociation(
    name="inscription_conducteur",
    ends={
        Property(name="inscription16", type=inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="conducteur17", type=conducteur, multiplicity=Multiplicity(1, 1))
    }
)
administrateur_trajet: BinaryAssociation = BinaryAssociation(
    name="administrateur_trajet",
    ends={
        Property(name="administrateur18", type=administrateur, multiplicity=Multiplicity(0, 1)),
        Property(name="trajet19", type=trajet, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_TZCTQIWlEeqgBLhX7Ryhyw",
    types={compte, reservation, paiement, trajet, administrateur, inscription, passager, conducteur, voiture},
    associations={inscription_passager, compte_passager, passager_paiement, administrateur_reservation, administrateur_paiement, administrateur_passager, administrateur_inscription, trajet_passager, inscription_conducteur, administrateur_trajet},
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
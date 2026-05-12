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
G_rant_Actor = Class(name="G_rant_Actor")
Comptable_Actor = Class(name="Comptable_Actor")
Livreur_Actor = Class(name="Livreur_Actor")
Logistique_Actor = Class(name="Logistique_Actor")
__Syst_me___Banques_Actor = Class(name="__Syst_me___Banques_Actor")
__Syst_me___GPS_Actor = Class(name="__Syst_me___GPS_Actor")
System_Component = Class(name="System_Component")
T = Class(name="T")
T1 = Class(name="T1")
Caissier_Actor = Class(name="Caissier_Actor")
Client_Actor = Class(name="Client_Actor")
Pizza_olo_Actor = Class(name="Pizza_olo_Actor")
G_rant_Actor1 = Class(name="G_rant_Actor1")
Comptable_Actor1 = Class(name="Comptable_Actor1")
Caissier_Actor1 = Class(name="Caissier_Actor1")
Livreur_Actor1 = Class(name="Livreur_Actor1")
Logistique_Actor1 = Class(name="Logistique_Actor1")
__Syst_me___Banques_Actor1 = Class(name="__Syst_me___Banques_Actor1")
__Syst_me___GPS_API_Actor = Class(name="__Syst_me___GPS_API_Actor")
System_Component1 = Class(name="System_Component1")
T2 = Class(name="T2")
T11 = Class(name="T11")
Achats_Gestion_des_achats_Component = Class(name="Achats_Gestion_des_achats_Component")
Administratif_Gestion_administrative_Component = Class(name="Administratif_Gestion_administrative_Component")
Client_Actor1 = Class(name="Client_Actor1")
Pizza_olo_Actor1 = Class(name="Pizza_olo_Actor1")
G_rant_Actor2 = Class(name="G_rant_Actor2")
Comptable_Actor2 = Class(name="Comptable_Actor2")
Caissier_Actor2 = Class(name="Caissier_Actor2")
Livreur_Actor2 = Class(name="Livreur_Actor2")
Logistique_Actor2 = Class(name="Logistique_Actor2")
__Syst_me___Banques_Actor2 = Class(name="__Syst_me___Banques_Actor2")
__Syst_me___GPS_API_Actor1 = Class(name="__Syst_me___GPS_API_Actor1")
System_Component2 = Class(name="System_Component2")
Pr_parer_une_livraison_UseCase = Class(name="Pr_parer_une_livraison_UseCase")
Logistique_Actor3 = Class(name="Logistique_Actor3")
Caissier_Actor3 = Class(name="Caissier_Actor3")
Livreur_Actor3 = Class(name="Livreur_Actor3")
Pizza_olo_Actor2 = Class(name="Pizza_olo_Actor2")
Client_Actor2 = Class(name="Client_Actor2")
__Syst_me___Banques_Actor3 = Class(name="__Syst_me___Banques_Actor3")
__Syst_me___GPS_API_Actor2 = Class(name="__Syst_me___GPS_API_Actor2")
System_Component3 = Class(name="System_Component3")
Pr_parer_une_livraison_UseCase1 = Class(name="Pr_parer_une_livraison_UseCase1")
G_rant_Actor3 = Class(name="G_rant_Actor3")
Comptable_Actor3 = Class(name="Comptable_Actor3")
System_Component4 = Class(name="System_Component4")
Pr_parer_une_livraison_UseCase2 = Class(name="Pr_parer_une_livraison_UseCase2")
R_glement_UseCase = Class(name="R_glement_UseCase")
R_glement_UseCase1 = Class(name="R_glement_UseCase1")
Livreur_Actor4 = Class(name="Livreur_Actor4")
Logistique_Actor4 = Class(name="Logistique_Actor4")
Client_Actor3 = Class(name="Client_Actor3")
Caissier_Actor4 = Class(name="Caissier_Actor4")
__Syst_me___GPS_API_Actor3 = Class(name="__Syst_me___GPS_API_Actor3")
__Syst_me___Banques_Actor4 = Class(name="__Syst_me___Banques_Actor4")
Pizza_olo_Actor3 = Class(name="Pizza_olo_Actor3")
G_rant_Actor4 = Class(name="G_rant_Actor4")
System_Component5 = Class(name="System_Component5")
Pr_parer_une_livraison_UseCase3 = Class(name="Pr_parer_une_livraison_UseCase3")
Pr_parer_une_commande_external = Class(name="Pr_parer_une_commande_external")
_3_external = Class(name="_3_external")
Chiffre_d_affaires_external = Class(name="Chiffre_d_affaires_external")
_2_external = Class(name="_2_external")
Analyse_commande_external = Class(name="Analyse_commande_external")
Modification_Lecture_du_catalogue_des_pizzas_external = Class(name="Modification_Lecture_du_catalogue_des_pizzas_external")
Co_t_de_fonctionnement_external = Class(name="Co_t_de_fonctionnement_external")
Effectuer_un_achat_external = Class(name="Effectuer_un_achat_external")
Point_de_retrait_external = Class(name="Point_de_retrait_external")
Encaisser_une_commande_external = Class(name="Encaisser_une_commande_external")
Consulter_le_catalogue_des_pizzas_external = Class(name="Consulter_le_catalogue_des_pizzas_external")
G_rer_le_stock_external = Class(name="G_rer_le_stock_external")
R_glement_en_ligne_external = Class(name="R_glement_en_ligne_external")
Information_livraison_external = Class(name="Information_livraison_external")

# G_rant_Actor class attributes and methods

# Comptable_Actor class attributes and methods

# Livreur_Actor class attributes and methods

# Logistique_Actor class attributes and methods

# __Syst_me___Banques_Actor class attributes and methods

# __Syst_me___GPS_Actor class attributes and methods

# System_Component class attributes and methods

# T class attributes and methods

# T1 class attributes and methods

# Caissier_Actor class attributes and methods

# Client_Actor class attributes and methods

# Pizza_olo_Actor class attributes and methods

# G_rant_Actor1 class attributes and methods

# Comptable_Actor1 class attributes and methods

# Caissier_Actor1 class attributes and methods

# Livreur_Actor1 class attributes and methods

# Logistique_Actor1 class attributes and methods

# __Syst_me___Banques_Actor1 class attributes and methods

# __Syst_me___GPS_API_Actor class attributes and methods

# System_Component1 class attributes and methods

# T2 class attributes and methods

# T11 class attributes and methods

# Achats_Gestion_des_achats_Component class attributes and methods

# Administratif_Gestion_administrative_Component class attributes and methods

# Client_Actor1 class attributes and methods

# Pizza_olo_Actor1 class attributes and methods

# G_rant_Actor2 class attributes and methods

# Comptable_Actor2 class attributes and methods

# Caissier_Actor2 class attributes and methods

# Livreur_Actor2 class attributes and methods

# Logistique_Actor2 class attributes and methods

# __Syst_me___Banques_Actor2 class attributes and methods

# __Syst_me___GPS_API_Actor1 class attributes and methods

# System_Component2 class attributes and methods

# Pr_parer_une_livraison_UseCase class attributes and methods

# Logistique_Actor3 class attributes and methods

# Caissier_Actor3 class attributes and methods

# Livreur_Actor3 class attributes and methods

# Pizza_olo_Actor2 class attributes and methods

# Client_Actor2 class attributes and methods

# __Syst_me___Banques_Actor3 class attributes and methods

# __Syst_me___GPS_API_Actor2 class attributes and methods

# System_Component3 class attributes and methods

# Pr_parer_une_livraison_UseCase1 class attributes and methods

# G_rant_Actor3 class attributes and methods

# Comptable_Actor3 class attributes and methods

# System_Component4 class attributes and methods

# Pr_parer_une_livraison_UseCase2 class attributes and methods

# R_glement_UseCase class attributes and methods

# R_glement_UseCase1 class attributes and methods

# Livreur_Actor4 class attributes and methods

# Logistique_Actor4 class attributes and methods

# Client_Actor3 class attributes and methods

# Caissier_Actor4 class attributes and methods

# __Syst_me___GPS_API_Actor3 class attributes and methods

# __Syst_me___Banques_Actor4 class attributes and methods

# Pizza_olo_Actor3 class attributes and methods

# G_rant_Actor4 class attributes and methods

# System_Component5 class attributes and methods

# Pr_parer_une_livraison_UseCase3 class attributes and methods

# Pr_parer_une_commande_external class attributes and methods

# _3_external class attributes and methods

# Chiffre_d_affaires_external class attributes and methods

# _2_external class attributes and methods

# Analyse_commande_external class attributes and methods

# Modification_Lecture_du_catalogue_des_pizzas_external class attributes and methods

# Co_t_de_fonctionnement_external class attributes and methods

# Effectuer_un_achat_external class attributes and methods

# Point_de_retrait_external class attributes and methods

# Encaisser_une_commande_external class attributes and methods

# Consulter_le_catalogue_des_pizzas_external class attributes and methods

# G_rer_le_stock_external class attributes and methods

# R_glement_en_ligne_external class attributes and methods

# Information_livraison_external class attributes and methods

# Relationships
GPS_System: BinaryAssociation = BinaryAssociation(
    name="GPS_System",
    ends={
        Property(name="gPS11", type=__Syst_me___GPS_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="system10", type=System_Component, multiplicity=Multiplicity(0, 1))
    }
)
Caissier_System: BinaryAssociation = BinaryAssociation(
    name="Caissier_System",
    ends={
        Property(name="system12", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="caissier13", type=Caissier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_System: BinaryAssociation = BinaryAssociation(
    name="Client_System",
    ends={
        Property(name="system14", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="client15", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pizza_olo_System: BinaryAssociation = BinaryAssociation(
    name="Pizza_olo_System",
    ends={
        Property(name="system16", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="pizza_olo17", type=Pizza_olo_Actor, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_System2: BinaryAssociation = BinaryAssociation(
    name="G_rant_System2",
    ends={
        Property(name="system18", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant19", type=G_rant_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Comptable_System2: BinaryAssociation = BinaryAssociation(
    name="Comptable_System2",
    ends={
        Property(name="system20", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="comptable21", type=Comptable_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Livreur_System2: BinaryAssociation = BinaryAssociation(
    name="Livreur_System2",
    ends={
        Property(name="system22", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="livreur23", type=Livreur_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Caissier_System2: BinaryAssociation = BinaryAssociation(
    name="Caissier_System2",
    ends={
        Property(name="system24", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="caissier25", type=Caissier_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Logistique_System2: BinaryAssociation = BinaryAssociation(
    name="Logistique_System2",
    ends={
        Property(name="system26", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="logistique27", type=Logistique_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
System___Syst_me___Banques: BinaryAssociation = BinaryAssociation(
    name="System___Syst_me___Banques",
    ends={
        Property(name="__Syst_me___Banques28", type=__Syst_me___Banques_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="system29", type=System_Component, multiplicity=Multiplicity(0, 1))
    }
)
__Syst_me___GPS_API_System: BinaryAssociation = BinaryAssociation(
    name="__Syst_me___GPS_API_System",
    ends={
        Property(name="system30", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="__Syst_me___GPS_API31", type=__Syst_me___GPS_API_Actor, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_System22: BinaryAssociation = BinaryAssociation(
    name="G_rant_System22",
    ends={
        Property(name="system32", type=Administratif_Gestion_administrative_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant33", type=G_rant_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Caissier_System22: BinaryAssociation = BinaryAssociation(
    name="Caissier_System22",
    ends={
        Property(name="system34", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="caissier35", type=Caissier_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Pizza_olo_System2: BinaryAssociation = BinaryAssociation(
    name="Pizza_olo_System2",
    ends={
        Property(name="system36", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="pizza_olo37", type=Pizza_olo_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_System: BinaryAssociation = BinaryAssociation(
    name="G_rant_System",
    ends={
        Property(name="system0", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant1", type=G_rant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Comptable_System: BinaryAssociation = BinaryAssociation(
    name="Comptable_System",
    ends={
        Property(name="system2", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="comptable3", type=Comptable_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Livreur_System: BinaryAssociation = BinaryAssociation(
    name="Livreur_System",
    ends={
        Property(name="system4", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="livreur5", type=Livreur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Logistique_System: BinaryAssociation = BinaryAssociation(
    name="Logistique_System",
    ends={
        Property(name="system6", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="logistique7", type=Logistique_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Banques_System: BinaryAssociation = BinaryAssociation(
    name="Banques_System",
    ends={
        Property(name="system8", type=System_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="banques9", type=__Syst_me___Banques_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pizza_olo_Pr_parer_une_commande: BinaryAssociation = BinaryAssociation(
    name="Pizza_olo_Pr_parer_une_commande",
    ends={
        Property(name="pr_parer_une_commande72", type=Pr_parer_une_commande_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pizza_olo73", type=Pizza_olo_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Pizza_olo_Consulter_le_catalogue_des_pizzas: BinaryAssociation = BinaryAssociation(
    name="Pizza_olo_Consulter_le_catalogue_des_pizzas",
    ends={
        Property(name="consulter_le_catalogue_des_pizzas74", type=Consulter_le_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pizza_olo75", type=Pizza_olo_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Caissier_Encaisser_une_commande: BinaryAssociation = BinaryAssociation(
    name="Caissier_Encaisser_une_commande",
    ends={
        Property(name="encaisser_une_commande76", type=Encaisser_une_commande_external, multiplicity=Multiplicity(0, 1)),
        Property(name="caissier77", type=Caissier_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Effectuer_un_achat___Syst_me___Banques1: BinaryAssociation = BinaryAssociation(
    name="Effectuer_un_achat___Syst_me___Banques1",
    ends={
        Property(name="__Syst_me___Banques78", type=_3_external, multiplicity=Multiplicity(0, 1)),
        Property(name="effectuer_un_achat79", type=Chiffre_d_affaires_external, multiplicity=Multiplicity(0, 1))
    }
)
Point_de_retrait___Syst_me___GPS_API1: BinaryAssociation = BinaryAssociation(
    name="Point_de_retrait___Syst_me___GPS_API1",
    ends={
        Property(name="__Syst_me___GPS_API80", type=_2_external, multiplicity=Multiplicity(0, 1)),
        Property(name="point_de_retrait81", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1))
    }
)
Encaisser_une_commande___Syst_me___Banques1: BinaryAssociation = BinaryAssociation(
    name="Encaisser_une_commande___Syst_me___Banques1",
    ends={
        Property(name="__Syst_me___Banques82", type=_3_external, multiplicity=Multiplicity(0, 1)),
        Property(name="encaisser_une_commande83", type=Encaisser_une_commande_external, multiplicity=Multiplicity(0, 1))
    }
)
Commandes_G_rant: BinaryAssociation = BinaryAssociation(
    name="Commandes_G_rant",
    ends={
        Property(name="g_rant84", type=G_rant_Actor3, multiplicity=Multiplicity(0, 1)),
        Property(name="commandes85", type=Analyse_commande_external, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Modification_Lecture_du_catalogue_des_pizzas: BinaryAssociation = BinaryAssociation(
    name="G_rant_Modification_Lecture_du_catalogue_des_pizzas",
    ends={
        Property(name="modification_Lecture_du_catalogue_des_pizzas86", type=Modification_Lecture_du_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant87", type=G_rant_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Chiffres_d_affaire: BinaryAssociation = BinaryAssociation(
    name="G_rant_Chiffres_d_affaire",
    ends={
        Property(name="chiffres_d_affaire88", type=Chiffre_d_affaires_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant89", type=G_rant_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Comptable_Chiffres_d_affaire: BinaryAssociation = BinaryAssociation(
    name="Comptable_Chiffres_d_affaire",
    ends={
        Property(name="chiffres_d_affaire90", type=Chiffre_d_affaires_external, multiplicity=Multiplicity(0, 1)),
        Property(name="comptable91", type=Comptable_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Logistique_System22: BinaryAssociation = BinaryAssociation(
    name="Logistique_System22",
    ends={
        Property(name="system38", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="logistique39", type=Logistique_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Comptable_System22: BinaryAssociation = BinaryAssociation(
    name="Comptable_System22",
    ends={
        Property(name="system40", type=Administratif_Gestion_administrative_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="comptable41", type=Comptable_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
System___Syst_me___Banques2: BinaryAssociation = BinaryAssociation(
    name="System___Syst_me___Banques2",
    ends={
        Property(name="__Syst_me___Banques42", type=__Syst_me___Banques_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="system43", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1))
    }
)
Client_System2: BinaryAssociation = BinaryAssociation(
    name="Client_System2",
    ends={
        Property(name="system44", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="client45", type=Client_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
__Syst_me___GPS_API_System2: BinaryAssociation = BinaryAssociation(
    name="__Syst_me___GPS_API_System2",
    ends={
        Property(name="system46", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="__Syst_me___GPS_API47", type=__Syst_me___GPS_API_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Livreur_System22: BinaryAssociation = BinaryAssociation(
    name="Livreur_System22",
    ends={
        Property(name="system48", type=Achats_Gestion_des_achats_Component, multiplicity=Multiplicity(0, 1)),
        Property(name="livreur49", type=Livreur_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Effectuer_un_achat___Syst_me___Banques: BinaryAssociation = BinaryAssociation(
    name="Effectuer_un_achat___Syst_me___Banques",
    ends={
        Property(name="__Syst_me___Banques50", type=__Syst_me___Banques_Actor3, multiplicity=Multiplicity(0, 1)),
        Property(name="effectuer_un_achat51", type=Effectuer_un_achat_external, multiplicity=Multiplicity(0, 1))
    }
)
Point_de_retrait___Syst_me___GPS_API: BinaryAssociation = BinaryAssociation(
    name="Point_de_retrait___Syst_me___GPS_API",
    ends={
        Property(name="__Syst_me___GPS_API52", type=__Syst_me___GPS_API_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="point_de_retrait53", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1))
    }
)
Encaisser_une_commande___Syst_me___Banques: BinaryAssociation = BinaryAssociation(
    name="Encaisser_une_commande___Syst_me___Banques",
    ends={
        Property(name="__Syst_me___Banques54", type=__Syst_me___Banques_Actor3, multiplicity=Multiplicity(0, 1)),
        Property(name="encaisser_une_commande55", type=Encaisser_une_commande_external, multiplicity=Multiplicity(0, 1))
    }
)
Effectuer_un_achat___Syst_me___GPS_API: BinaryAssociation = BinaryAssociation(
    name="Effectuer_un_achat___Syst_me___GPS_API",
    ends={
        Property(name="__Syst_me___GPS_API56", type=__Syst_me___GPS_API_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="effectuer_un_achat57", type=Effectuer_un_achat_external, multiplicity=Multiplicity(0, 1))
    }
)
Pr_parer_une_livraison___Syst_me___Banques: BinaryAssociation = BinaryAssociation(
    name="Pr_parer_une_livraison___Syst_me___Banques",
    ends={
        Property(name="__Syst_me___Banques58", type=__Syst_me___Banques_Actor3, multiplicity=Multiplicity(0, 1)),
        Property(name="pr_parer_une_livraison59", type=Pr_parer_une_livraison_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Client_Consulter_le_catalogue_de_pizza: BinaryAssociation = BinaryAssociation(
    name="Client_Consulter_le_catalogue_de_pizza",
    ends={
        Property(name="consulter_le_catalogue_de_pizza60", type=Consulter_le_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client61", type=Client_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
__Syst_me___Banques_Consulter_le_catalogue_de_pizza: BinaryAssociation = BinaryAssociation(
    name="__Syst_me___Banques_Consulter_le_catalogue_de_pizza",
    ends={
        Property(name="consulter_le_catalogue_de_pizza62", type=Consulter_le_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="__Syst_me___Banques63", type=__Syst_me___Banques_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Livreur_Pr_parer_une_livraison: BinaryAssociation = BinaryAssociation(
    name="Livreur_Pr_parer_une_livraison",
    ends={
        Property(name="pr_parer_une_livraison64", type=Pr_parer_une_livraison_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="livreur65", type=Livreur_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Logistique_G_rer_le_stock: BinaryAssociation = BinaryAssociation(
    name="Logistique_G_rer_le_stock",
    ends={
        Property(name="g_rer_le_stock66", type=G_rer_le_stock_external, multiplicity=Multiplicity(0, 1)),
        Property(name="logistique67", type=Logistique_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Client_Effectuer_un_achat: BinaryAssociation = BinaryAssociation(
    name="Client_Effectuer_un_achat",
    ends={
        Property(name="effectuer_un_achat68", type=Effectuer_un_achat_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client69", type=Client_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Client_Point_de_retrait: BinaryAssociation = BinaryAssociation(
    name="Client_Point_de_retrait",
    ends={
        Property(name="point_de_retrait70", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client71", type=Client_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Point_de_retrait___Syst_me___GPS_API3: BinaryAssociation = BinaryAssociation(
    name="Point_de_retrait___Syst_me___GPS_API3",
    ends={
        Property(name="__Syst_me___GPS_API124", type=_2_external, multiplicity=Multiplicity(0, 1)),
        Property(name="point_de_retrait125", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1))
    }
)
Encaisser_une_commande___Syst_me___Banques3: BinaryAssociation = BinaryAssociation(
    name="Encaisser_une_commande___Syst_me___Banques3",
    ends={
        Property(name="__Syst_me___Banques126", type=_3_external, multiplicity=Multiplicity(0, 1)),
        Property(name="encaisser_une_commande127", type=Encaisser_une_commande_external, multiplicity=Multiplicity(0, 1))
    }
)
Commandes_G_rant1: BinaryAssociation = BinaryAssociation(
    name="Commandes_G_rant1",
    ends={
        Property(name="g_rant128", type=G_rant_Actor4, multiplicity=Multiplicity(0, 1)),
        Property(name="commandes129", type=Analyse_commande_external, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Chiffres_d_affaire2: BinaryAssociation = BinaryAssociation(
    name="G_rant_Chiffres_d_affaire2",
    ends={
        Property(name="chiffres_d_affaire130", type=Chiffre_d_affaires_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant131", type=G_rant_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Co_t_de_fonctionnement2: BinaryAssociation = BinaryAssociation(
    name="G_rant_Co_t_de_fonctionnement2",
    ends={
        Property(name="co_t_de_fonctionnement132", type=Co_t_de_fonctionnement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant133", type=G_rant_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Modification_Lecture_du_catalogue_des_pizzas2: BinaryAssociation = BinaryAssociation(
    name="G_rant_Modification_Lecture_du_catalogue_des_pizzas2",
    ends={
        Property(name="modification_Lecture_du_catalogue_des_pizzas134", type=Modification_Lecture_du_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant135", type=G_rant_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
Comptable_Co_t_de_fonctionnement: BinaryAssociation = BinaryAssociation(
    name="Comptable_Co_t_de_fonctionnement",
    ends={
        Property(name="co_t_de_fonctionnement92", type=Co_t_de_fonctionnement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="comptable93", type=Comptable_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
G_rant_Co_t_de_fonctionnement: BinaryAssociation = BinaryAssociation(
    name="G_rant_Co_t_de_fonctionnement",
    ends={
        Property(name="co_t_de_fonctionnement94", type=Co_t_de_fonctionnement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="g_rant95", type=G_rant_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Effectuer_un_achat___Syst_me___Banques2: BinaryAssociation = BinaryAssociation(
    name="Effectuer_un_achat___Syst_me___Banques2",
    ends={
        Property(name="__Syst_me___Banques96", type=__Syst_me___Banques_Actor4, multiplicity=Multiplicity(0, 1)),
        Property(name="effectuer_un_achat97", type=Effectuer_un_achat_external, multiplicity=Multiplicity(0, 1))
    }
)
Point_de_retrait___Syst_me___GPS_API2: BinaryAssociation = BinaryAssociation(
    name="Point_de_retrait___Syst_me___GPS_API2",
    ends={
        Property(name="__Syst_me___GPS_API98", type=__Syst_me___GPS_API_Actor3, multiplicity=Multiplicity(0, 1)),
        Property(name="point_de_retrait99", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1))
    }
)
Encaisser_une_commande___Syst_me___Banques2: BinaryAssociation = BinaryAssociation(
    name="Encaisser_une_commande___Syst_me___Banques2",
    ends={
        Property(name="__Syst_me___Banques100", type=__Syst_me___Banques_Actor4, multiplicity=Multiplicity(0, 1)),
        Property(name="encaisser_une_commande101", type=R_glement_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
R_glement___Syst_me___Banques: BinaryAssociation = BinaryAssociation(
    name="R_glement___Syst_me___Banques",
    ends={
        Property(name="__Syst_me___Banques102", type=__Syst_me___Banques_Actor4, multiplicity=Multiplicity(0, 1)),
        Property(name="r_glement103", type=R_glement_en_ligne_external, multiplicity=Multiplicity(0, 1))
    }
)
R_glement___Syst_me___Banques2: BinaryAssociation = BinaryAssociation(
    name="R_glement___Syst_me___Banques2",
    ends={
        Property(name="__Syst_me___Banques104", type=__Syst_me___Banques_Actor4, multiplicity=Multiplicity(0, 1)),
        Property(name="r_glement105", type=R_glement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Pizza_olo_Pr_parer_une_commande2: BinaryAssociation = BinaryAssociation(
    name="Pizza_olo_Pr_parer_une_commande2",
    ends={
        Property(name="pr_parer_une_commande106", type=Pr_parer_une_commande_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pizza_olo107", type=Pizza_olo_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Client_Effectuer_un_achat2: BinaryAssociation = BinaryAssociation(
    name="Client_Effectuer_un_achat2",
    ends={
        Property(name="effectuer_un_achat108", type=Effectuer_un_achat_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client109", type=Client_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Client_Point_de_retrait2: BinaryAssociation = BinaryAssociation(
    name="Client_Point_de_retrait2",
    ends={
        Property(name="point_de_retrait110", type=Point_de_retrait_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client111", type=Client_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Livreur_Pr_parer_une_livraison2: BinaryAssociation = BinaryAssociation(
    name="Livreur_Pr_parer_une_livraison2",
    ends={
        Property(name="pr_parer_une_livraison112", type=Pr_parer_une_livraison_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="livreur113", type=Livreur_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
Caissier_Encaisser_une_commande2: BinaryAssociation = BinaryAssociation(
    name="Caissier_Encaisser_une_commande2",
    ends={
        Property(name="encaisser_une_commande114", type=Encaisser_une_commande_external, multiplicity=Multiplicity(0, 1)),
        Property(name="caissier115", type=Caissier_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
Logistique_G_rer_le_stock2: BinaryAssociation = BinaryAssociation(
    name="Logistique_G_rer_le_stock2",
    ends={
        Property(name="g_rer_le_stock116", type=G_rer_le_stock_external, multiplicity=Multiplicity(0, 1)),
        Property(name="logistique117", type=Logistique_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
Client_Consulter_le_catalogue_de_pizza2: BinaryAssociation = BinaryAssociation(
    name="Client_Consulter_le_catalogue_de_pizza2",
    ends={
        Property(name="consulter_le_catalogue_de_pizza118", type=Consulter_le_catalogue_des_pizzas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client119", type=Client_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
__Syst_me___GPS_API_Effectuer_un_achat: BinaryAssociation = BinaryAssociation(
    name="__Syst_me___GPS_API_Effectuer_un_achat",
    ends={
        Property(name="effectuer_un_achat120", type=Information_livraison_external, multiplicity=Multiplicity(0, 1)),
        Property(name="__Syst_me___GPS_API121", type=__Syst_me___GPS_API_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Effectuer_un_achat___Syst_me___Banques3: BinaryAssociation = BinaryAssociation(
    name="Effectuer_un_achat___Syst_me___Banques3",
    ends={
        Property(name="__Syst_me___Banques122", type=_3_external, multiplicity=Multiplicity(0, 1)),
        Property(name="effectuer_un_achat123", type=Chiffre_d_affaires_external, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_VX11MG9GEemzHvNogvRQlA",
    types={G_rant_Actor, Comptable_Actor, Livreur_Actor, Logistique_Actor, __Syst_me___Banques_Actor, __Syst_me___GPS_Actor, System_Component, T, T1, Caissier_Actor, Client_Actor, Pizza_olo_Actor, G_rant_Actor1, Comptable_Actor1, Caissier_Actor1, Livreur_Actor1, Logistique_Actor1, __Syst_me___Banques_Actor1, __Syst_me___GPS_API_Actor, System_Component1, T2, T11, Achats_Gestion_des_achats_Component, Administratif_Gestion_administrative_Component, Client_Actor1, Pizza_olo_Actor1, G_rant_Actor2, Comptable_Actor2, Caissier_Actor2, Livreur_Actor2, Logistique_Actor2, __Syst_me___Banques_Actor2, __Syst_me___GPS_API_Actor1, System_Component2, Pr_parer_une_livraison_UseCase, Logistique_Actor3, Caissier_Actor3, Livreur_Actor3, Pizza_olo_Actor2, Client_Actor2, __Syst_me___Banques_Actor3, __Syst_me___GPS_API_Actor2, System_Component3, Pr_parer_une_livraison_UseCase1, G_rant_Actor3, Comptable_Actor3, System_Component4, Pr_parer_une_livraison_UseCase2, R_glement_UseCase, R_glement_UseCase1, Livreur_Actor4, Logistique_Actor4, Client_Actor3, Caissier_Actor4, __Syst_me___GPS_API_Actor3, __Syst_me___Banques_Actor4, Pizza_olo_Actor3, G_rant_Actor4, System_Component5, Pr_parer_une_livraison_UseCase3, Pr_parer_une_commande_external, _3_external, Chiffre_d_affaires_external, _2_external, Analyse_commande_external, Modification_Lecture_du_catalogue_des_pizzas_external, Co_t_de_fonctionnement_external, Effectuer_un_achat_external, Point_de_retrait_external, Encaisser_une_commande_external, Consulter_le_catalogue_des_pizzas_external, G_rer_le_stock_external, R_glement_en_ligne_external, Information_livraison_external},
    associations={GPS_System, Caissier_System, Client_System, Pizza_olo_System, G_rant_System2, Comptable_System2, Livreur_System2, Caissier_System2, Logistique_System2, System___Syst_me___Banques, __Syst_me___GPS_API_System, G_rant_System22, Caissier_System22, Pizza_olo_System2, G_rant_System, Comptable_System, Livreur_System, Logistique_System, Banques_System, Pizza_olo_Pr_parer_une_commande, Pizza_olo_Consulter_le_catalogue_des_pizzas, Caissier_Encaisser_une_commande, Effectuer_un_achat___Syst_me___Banques1, Point_de_retrait___Syst_me___GPS_API1, Encaisser_une_commande___Syst_me___Banques1, Commandes_G_rant, G_rant_Modification_Lecture_du_catalogue_des_pizzas, G_rant_Chiffres_d_affaire, Comptable_Chiffres_d_affaire, Logistique_System22, Comptable_System22, System___Syst_me___Banques2, Client_System2, __Syst_me___GPS_API_System2, Livreur_System22, Effectuer_un_achat___Syst_me___Banques, Point_de_retrait___Syst_me___GPS_API, Encaisser_une_commande___Syst_me___Banques, Effectuer_un_achat___Syst_me___GPS_API, Pr_parer_une_livraison___Syst_me___Banques, Client_Consulter_le_catalogue_de_pizza, __Syst_me___Banques_Consulter_le_catalogue_de_pizza, Livreur_Pr_parer_une_livraison, Logistique_G_rer_le_stock, Client_Effectuer_un_achat, Client_Point_de_retrait, Point_de_retrait___Syst_me___GPS_API3, Encaisser_une_commande___Syst_me___Banques3, Commandes_G_rant1, G_rant_Chiffres_d_affaire2, G_rant_Co_t_de_fonctionnement2, G_rant_Modification_Lecture_du_catalogue_des_pizzas2, Comptable_Co_t_de_fonctionnement, G_rant_Co_t_de_fonctionnement, Effectuer_un_achat___Syst_me___Banques2, Point_de_retrait___Syst_me___GPS_API2, Encaisser_une_commande___Syst_me___Banques2, R_glement___Syst_me___Banques, R_glement___Syst_me___Banques2, Pizza_olo_Pr_parer_une_commande2, Client_Effectuer_un_achat2, Client_Point_de_retrait2, Livreur_Pr_parer_une_livraison2, Caissier_Encaisser_une_commande2, Logistique_G_rer_le_stock2, Client_Consulter_le_catalogue_de_pizza2, __Syst_me___GPS_API_Effectuer_un_achat, Effectuer_un_achat___Syst_me___Banques3},
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
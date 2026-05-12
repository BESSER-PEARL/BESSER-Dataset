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
Utilisateur_Actor = Class(name="Utilisateur_Actor")
Client_ordinaire_Actor = Class(name="Client_ordinaire_Actor")
Administrateur_Actor = Class(name="Administrateur_Actor")
Concessionnaire_Actor = Class(name="Concessionnaire_Actor")
_Component = Class(name="_Component")
Cr_er_un_compte_Component = Class(name="Cr_er_un_compte_Component")
Utilisateur_Actor1 = Class(name="Utilisateur_Actor1")
Munic_Connect_server_Actor = Class(name="Munic_Connect_server_Actor")
Enregistrer_un_v_hicule_Component = Class(name="Enregistrer_un_v_hicule_Component")
Client_Actor = Class(name="Client_Actor")
Serveur_de_l_application_Actor = Class(name="Serveur_de_l_application_Actor")
Serveur_de_l_application_Actor1 = Class(name="Serveur_de_l_application_Actor1")
Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_Component = Class(name="Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_Component")
Administrateur_Actor1 = Class(name="Administrateur_Actor1")
Serveur_de_l_application_Actor2 = Class(name="Serveur_de_l_application_Actor2")
Concessionnaire_Actor1 = Class(name="Concessionnaire_Actor1")
G_rer_l_avancement_des_ventes_Component = Class(name="G_rer_l_avancement_des_ventes_Component")
serveur_de_l_application_Actor = Class(name="serveur_de_l_application_Actor")
Munic_connect_Actor = Class(name="Munic_connect_Actor")
Utilisateur = Class(name="Utilisateur")
V_hicule = Class(name="V_hicule")
Param_tres = Class(name="Param_tres")
Munic_Connect_Actor = Class(name="Munic_Connect_Actor")
Cr_er_un_compte_external = Class(name="Cr_er_un_compte_external")
g_rer_l_avancement_des_ventes_external = Class(name="g_rer_l_avancement_des_ventes_external")
Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external = Class(name="Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external")
Suivre_l__tat_du_v_hicule_et_de_la_conduite_external = Class(name="Suivre_l__tat_du_v_hicule_et_de_la_conduite_external")
Suivre_l_avancement_des_ventes_external = Class(name="Suivre_l_avancement_des_ventes_external")
S_authentifier_external = Class(name="S_authentifier_external")
Enregistrer_un_v_hicule_sur_l_application_external = Class(name="Enregistrer_un_v_hicule_sur_l_application_external")

# Utilisateur_Actor class attributes and methods

# Client_ordinaire_Actor class attributes and methods

# Administrateur_Actor class attributes and methods

# Concessionnaire_Actor class attributes and methods

# _Component class attributes and methods

# Cr_er_un_compte_Component class attributes and methods

# Utilisateur_Actor1 class attributes and methods

# Munic_Connect_server_Actor class attributes and methods

# Enregistrer_un_v_hicule_Component class attributes and methods

# Client_Actor class attributes and methods

# Serveur_de_l_application_Actor class attributes and methods

# Serveur_de_l_application_Actor1 class attributes and methods

# Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_Component class attributes and methods

# Administrateur_Actor1 class attributes and methods

# Serveur_de_l_application_Actor2 class attributes and methods

# Concessionnaire_Actor1 class attributes and methods

# G_rer_l_avancement_des_ventes_Component class attributes and methods

# serveur_de_l_application_Actor class attributes and methods

# Munic_connect_Actor class attributes and methods

# Utilisateur class attributes and methods

# V_hicule class attributes and methods

# Param_tres class attributes and methods

# Munic_Connect_Actor class attributes and methods

# Cr_er_un_compte_external class attributes and methods

# g_rer_l_avancement_des_ventes_external class attributes and methods

# Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external class attributes and methods

# Suivre_l__tat_du_v_hicule_et_de_la_conduite_external class attributes and methods

# Suivre_l_avancement_des_ventes_external class attributes and methods

# S_authentifier_external class attributes and methods

# Enregistrer_un_v_hicule_sur_l_application_external class attributes and methods

# Relationships
Cr_er_un_compte_Application_server: BinaryAssociation = BinaryAssociation(
    name="Cr_er_un_compte_Application_server",
    ends={
        Property(name="application_server0", type=Serveur_de_l_application_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="cr_er_un_compte1", type=Cr_er_un_compte_external, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Cr_er_un_compte: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Cr_er_un_compte",
    ends={
        Property(name="cr_er_un_compte2", type=Cr_er_un_compte_external, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur3", type=Utilisateur_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Munic_Connect_server_Cr_er_un_compte: BinaryAssociation = BinaryAssociation(
    name="Munic_Connect_server_Cr_er_un_compte",
    ends={
        Property(name="cr_er_un_compte4", type=Cr_er_un_compte_external, multiplicity=Multiplicity(0, 1)),
        Property(name="munic_Connect_server5", type=Munic_Connect_server_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_ordinaire_Enregistrer_un_v_hicule_sur_l_application: BinaryAssociation = BinaryAssociation(
    name="Client_ordinaire_Enregistrer_un_v_hicule_sur_l_application",
    ends={
        Property(name="enregistrer_un_v_hicule_sur_l_application22", type=Enregistrer_un_v_hicule_sur_l_application_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_ordinaire23", type=Client_ordinaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Concessionnaire_Cr_er_un_compte: BinaryAssociation = BinaryAssociation(
    name="Concessionnaire_Cr_er_un_compte",
    ends={
        Property(name="cr_er_un_compte24", type=Cr_er_un_compte_external, multiplicity=Multiplicity(0, 1)),
        Property(name="concessionnaire25", type=Concessionnaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Suivre_les_informations_du_v_hicule_et_de_la_conduite_serveur_de_l_application: BinaryAssociation = BinaryAssociation(
    name="Suivre_les_informations_du_v_hicule_et_de_la_conduite_serveur_de_l_application",
    ends={
        Property(name="serveur_de_l_application26", type=serveur_de_l_application_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="suivre_les_informations_du_v_hicule_et_de_la_conduite27", type=g_rer_l_avancement_des_ventes_external, multiplicity=Multiplicity(0, 1))
    }
)
S_authentifier_Munic_connect: BinaryAssociation = BinaryAssociation(
    name="S_authentifier_Munic_connect",
    ends={
        Property(name="munic_connect28", type=Munic_connect_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="s_authentifier29", type=S_authentifier_external, multiplicity=Multiplicity(0, 1))
    }
)
Client_ordinaire_Suivre_les_informations_du_v_hicule_et_de_la_conduite: BinaryAssociation = BinaryAssociation(
    name="Client_ordinaire_Suivre_les_informations_du_v_hicule_et_de_la_conduite",
    ends={
        Property(name="suivre_les_informations_du_v_hicule_et_de_la_conduite30", type=g_rer_l_avancement_des_ventes_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_ordinaire31", type=Concessionnaire_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Administrateur_Voir_les_informations_sous_leur_forme_brute: BinaryAssociation = BinaryAssociation(
    name="Administrateur_Voir_les_informations_sous_leur_forme_brute",
    ends={
        Property(name="voir_les_informations_sous_leur_forme_brute6", type=Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external, multiplicity=Multiplicity(0, 1)),
        Property(name="administrateur7", type=Administrateur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_ordinaire_Suivre_l__tat_du_v_hicule_et_de_la_conduite: BinaryAssociation = BinaryAssociation(
    name="Client_ordinaire_Suivre_l__tat_du_v_hicule_et_de_la_conduite",
    ends={
        Property(name="suivre_l__tat_du_v_hicule_et_de_la_conduite8", type=Suivre_l__tat_du_v_hicule_et_de_la_conduite_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_ordinaire9", type=Client_ordinaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Concessionnaire_Suivre_l_avancement_des_ventes: BinaryAssociation = BinaryAssociation(
    name="Concessionnaire_Suivre_l_avancement_des_ventes",
    ends={
        Property(name="suivre_l_avancement_des_ventes10", type=Suivre_l_avancement_des_ventes_external, multiplicity=Multiplicity(0, 1)),
        Property(name="concessionnaire11", type=Concessionnaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)
S_authentifier_Munic_Connect: BinaryAssociation = BinaryAssociation(
    name="S_authentifier_Munic_Connect",
    ends={
        Property(name="munic_Connect12", type=Munic_Connect_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="s_authentifier13", type=S_authentifier_external, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Enregistrer_un_v_hicule: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Enregistrer_un_v_hicule",
    ends={
        Property(name="enregistrer_un_v_hicule14", type=Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur15", type=Administrateur_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Serveur_de_l_application_Enregistrer_un_v_hicule: BinaryAssociation = BinaryAssociation(
    name="Serveur_de_l_application_Enregistrer_un_v_hicule",
    ends={
        Property(name="enregistrer_un_v_hicule16", type=Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external, multiplicity=Multiplicity(0, 1)),
        Property(name="serveur_de_l_application17", type=Serveur_de_l_application_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Client_ordinaire_Cr_er_un_compte: BinaryAssociation = BinaryAssociation(
    name="Client_ordinaire_Cr_er_un_compte",
    ends={
        Property(name="cr_er_un_compte18", type=Cr_er_un_compte_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_ordinaire19", type=Client_ordinaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Concessionnaire_Enregistrer_un_v_hicule_sur_l_application: BinaryAssociation = BinaryAssociation(
    name="Concessionnaire_Enregistrer_un_v_hicule_sur_l_application",
    ends={
        Property(name="enregistrer_un_v_hicule_sur_l_application20", type=Enregistrer_un_v_hicule_sur_l_application_external, multiplicity=Multiplicity(0, 1)),
        Property(name="concessionnaire21", type=Concessionnaire_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_mI2YYLbQEem8I_zdXKdSGw",
    types={Utilisateur_Actor, Client_ordinaire_Actor, Administrateur_Actor, Concessionnaire_Actor, _Component, Cr_er_un_compte_Component, Utilisateur_Actor1, Munic_Connect_server_Actor, Enregistrer_un_v_hicule_Component, Client_Actor, Serveur_de_l_application_Actor, Serveur_de_l_application_Actor1, Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_Component, Administrateur_Actor1, Serveur_de_l_application_Actor2, Concessionnaire_Actor1, G_rer_l_avancement_des_ventes_Component, serveur_de_l_application_Actor, Munic_connect_Actor, Utilisateur, V_hicule, Param_tres, Munic_Connect_Actor, Cr_er_un_compte_external, g_rer_l_avancement_des_ventes_external, Voir_les_informations_re_us_par_l_application_sous_leur_forme_brute_external, Suivre_l__tat_du_v_hicule_et_de_la_conduite_external, Suivre_l_avancement_des_ventes_external, S_authentifier_external, Enregistrer_un_v_hicule_sur_l_application_external},
    associations={Cr_er_un_compte_Application_server, Utilisateur_Cr_er_un_compte, Munic_Connect_server_Cr_er_un_compte, Client_ordinaire_Enregistrer_un_v_hicule_sur_l_application, Concessionnaire_Cr_er_un_compte, Suivre_les_informations_du_v_hicule_et_de_la_conduite_serveur_de_l_application, S_authentifier_Munic_connect, Client_ordinaire_Suivre_les_informations_du_v_hicule_et_de_la_conduite, Administrateur_Voir_les_informations_sous_leur_forme_brute, Client_ordinaire_Suivre_l__tat_du_v_hicule_et_de_la_conduite, Concessionnaire_Suivre_l_avancement_des_ventes, S_authentifier_Munic_Connect, Utilisateur_Enregistrer_un_v_hicule, Serveur_de_l_application_Enregistrer_un_v_hicule, Client_ordinaire_Cr_er_un_compte, Concessionnaire_Enregistrer_un_v_hicule_sur_l_application},
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
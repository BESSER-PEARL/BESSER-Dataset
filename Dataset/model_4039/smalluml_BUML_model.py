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
smalluml_Classe = Class(name="smalluml::Classe")
ElementDiagramme = Class(name="ElementDiagramme")
ElementNomme = Class(name="ElementNomme")
smalluml_Attribut = Class(name="smalluml::Attribut")
smalluml_Methode = Class(name="smalluml::Methode")
smalluml_TypeDonnee = Class(name="smalluml::TypeDonnee")
smalluml_Association = Class(name="smalluml::Association")
smalluml_Cardinalite = Class(name="smalluml::Cardinalite")
smalluml_Chaine = Class(name="smalluml::Chaine")
smalluml_Entier = Class(name="smalluml::Entier")
smalluml_Booleen = Class(name="smalluml::Booleen")
smalluml_Diagramme = Class(name="smalluml::Diagramme")
smalluml_ElementDiagramme = Class(name="smalluml::ElementDiagramme", is_abstract=True)
smalluml_Type = Class(name="smalluml::Type", is_abstract=True)
smalluml_Enumeration = Class(name="smalluml::Enumeration")
Type = Class(name="Type")
smalluml_ElementNomme = Class(name="smalluml::ElementNomme", is_abstract=True)

# smalluml_Classe class attributes and methods
smalluml_Classe_abstrait: Property = Property(name="abstrait", type=BooleanType)
smalluml_Classe_classeAbstraite: Property = Property(name="classeAbstraite", type=BooleanType)
smalluml_Classe.attributes={smalluml_Classe_classeAbstraite, smalluml_Classe_abstrait}

# ElementDiagramme class attributes and methods

# ElementNomme class attributes and methods

# smalluml_Attribut class attributes and methods

# smalluml_Methode class attributes and methods
smalluml_Methode_methodeAbstraite: Property = Property(name="methodeAbstraite", type=BooleanType)
smalluml_Methode.attributes={smalluml_Methode_methodeAbstraite}

# smalluml_TypeDonnee class attributes and methods

# smalluml_Association class attributes and methods

# smalluml_Cardinalite class attributes and methods
smalluml_Cardinalite_multipliciteInf: Property = Property(name="multipliciteInf", type=StringType)
smalluml_Cardinalite_multipliciteSup: Property = Property(name="multipliciteSup", type=StringType)
smalluml_Cardinalite.attributes={smalluml_Cardinalite_multipliciteSup, smalluml_Cardinalite_multipliciteInf}

# smalluml_Chaine class attributes and methods

# smalluml_Entier class attributes and methods

# smalluml_Booleen class attributes and methods

# smalluml_Diagramme class attributes and methods

# smalluml_ElementDiagramme class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_Enumeration class attributes and methods
smalluml_Enumeration_elements: Property = Property(name="elements", type=StringType)
smalluml_Enumeration.attributes={smalluml_Enumeration_elements}

# Type class attributes and methods

# smalluml_ElementNomme class attributes and methods
smalluml_ElementNomme_nom: Property = Property(name="nom", type=StringType)
smalluml_ElementNomme.attributes={smalluml_ElementNomme_nom}

# Relationships
attributs0: BinaryAssociation = BinaryAssociation(
    name="attributs0",
    ends={
        Property(name="smalluml_Attribut", type=smalluml_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Classe", type=smalluml_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodes1: BinaryAssociation = BinaryAssociation(
    name="methodes1",
    ends={
        Property(name="smalluml_Methode", type=smalluml_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Classe2", type=smalluml_Methode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sousClasses4: BinaryAssociation = BinaryAssociation(
    name="sousClasses4",
    ends={
        Property(name="smalluml_Classe5", type=smalluml_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Classe3", type=smalluml_Classe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasse7: BinaryAssociation = BinaryAssociation(
    name="superClasse7",
    ends={
        Property(name="smalluml_Classe8", type=smalluml_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Classe6", type=smalluml_Classe, multiplicity=Multiplicity(0, 1))
    }
)
attributs17: BinaryAssociation = BinaryAssociation(
    name="attributs17",
    ends={
        Property(name="smalluml_Attribut18", type=smalluml_TypeDonnee, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_TypeDonnee", type=smalluml_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cardinalites19: BinaryAssociation = BinaryAssociation(
    name="cardinalites19",
    ends={
        Property(name="smalluml_Cardinalite", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association", type=smalluml_Cardinalite, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
classe20: BinaryAssociation = BinaryAssociation(
    name="classe20",
    ends={
        Property(name="smalluml_Classe22", type=smalluml_Cardinalite, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Cardinalite21", type=smalluml_Classe, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementsDiagramme23: BinaryAssociation = BinaryAssociation(
    name="elementsDiagramme23",
    ends={
        Property(name="smalluml_ElementDiagramme", type=smalluml_Diagramme, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Diagramme", type=smalluml_ElementDiagramme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classe24: BinaryAssociation = BinaryAssociation(
    name="classe24",
    ends={
        Property(name="smalluml_Classe26", type=smalluml_ElementDiagramme, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_ElementDiagramme25", type=smalluml_Classe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association27: BinaryAssociation = BinaryAssociation(
    name="association27",
    ends={
        Property(name="smalluml_Association29", type=smalluml_ElementDiagramme, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_ElementDiagramme28", type=smalluml_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="smalluml_Type", type=smalluml_Attribut, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribut10", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDeRetour11: BinaryAssociation = BinaryAssociation(
    name="typeDeRetour11",
    ends={
        Property(name="smalluml_Type13", type=smalluml_Methode, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Methode12", type=smalluml_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametres14: BinaryAssociation = BinaryAssociation(
    name="parametres14",
    ends={
        Property(name="smalluml_Attribut16", type=smalluml_Methode, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Methode15", type=smalluml_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration30: BinaryAssociation = BinaryAssociation(
    name="enumeration30",
    ends={
        Property(name="smalluml_Enumeration", type=smalluml_ElementDiagramme, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_ElementDiagramme31", type=smalluml_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDonnee32: BinaryAssociation = BinaryAssociation(
    name="typeDonnee32",
    ends={
        Property(name="smalluml_TypeDonnee34", type=smalluml_ElementDiagramme, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_ElementDiagramme33", type=smalluml_TypeDonnee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Classe_ElementDiagramme = Generalization(general=ElementDiagramme, specific=smalluml_Classe)
gen_smalluml_Classe_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Classe)
gen_smalluml_TypeDonnee_Type = Generalization(general=Type, specific=smalluml_TypeDonnee)
gen_smalluml_TypeDonnee_ElementDiagramme = Generalization(general=ElementDiagramme, specific=smalluml_TypeDonnee)
gen_smalluml_TypeDonnee_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_TypeDonnee)
gen_smalluml_Association_ElementDiagramme = Generalization(general=ElementDiagramme, specific=smalluml_Association)
gen_smalluml_Association_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Association)
gen_smalluml_Cardinalite_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Cardinalite)
gen_smalluml_Chaine_Type = Generalization(general=Type, specific=smalluml_Chaine)
gen_smalluml_Entier_Type = Generalization(general=Type, specific=smalluml_Entier)
gen_smalluml_Booleen_Type = Generalization(general=Type, specific=smalluml_Booleen)
gen_smalluml_Diagramme_ElementDiagramme = Generalization(general=ElementDiagramme, specific=smalluml_Diagramme)
gen_smalluml_Diagramme_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Diagramme)
gen_smalluml_Attribut_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Attribut)
gen_smalluml_Enumeration_Type = Generalization(general=Type, specific=smalluml_Enumeration)
gen_smalluml_Enumeration_ElementDiagramme = Generalization(general=ElementDiagramme, specific=smalluml_Enumeration)
gen_smalluml_Enumeration_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Enumeration)
gen_smalluml_Methode_ElementNomme = Generalization(general=ElementNomme, specific=smalluml_Methode)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Classe, ElementDiagramme, ElementNomme, smalluml_Attribut, smalluml_Methode, smalluml_TypeDonnee, smalluml_Association, smalluml_Cardinalite, smalluml_Chaine, smalluml_Entier, smalluml_Booleen, smalluml_Diagramme, smalluml_ElementDiagramme, smalluml_Type, smalluml_Enumeration, Type, smalluml_ElementNomme},
    associations={attributs0, methodes1, sousClasses4, superClasse7, attributs17, cardinalites19, classe20, elementsDiagramme23, classe24, association27, type9, typeDeRetour11, parametres14, enumeration30, typeDonnee32},
    generalizations={gen_smalluml_Classe_ElementDiagramme, gen_smalluml_Classe_ElementNomme, gen_smalluml_TypeDonnee_Type, gen_smalluml_TypeDonnee_ElementDiagramme, gen_smalluml_TypeDonnee_ElementNomme, gen_smalluml_Association_ElementDiagramme, gen_smalluml_Association_ElementNomme, gen_smalluml_Cardinalite_ElementNomme, gen_smalluml_Chaine_Type, gen_smalluml_Entier_Type, gen_smalluml_Booleen_Type, gen_smalluml_Diagramme_ElementDiagramme, gen_smalluml_Diagramme_ElementNomme, gen_smalluml_Attribut_ElementNomme, gen_smalluml_Enumeration_Type, gen_smalluml_Enumeration_ElementDiagramme, gen_smalluml_Enumeration_ElementNomme, gen_smalluml_Methode_ElementNomme},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
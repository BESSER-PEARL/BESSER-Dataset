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
ClassG = Class(name="ClassG")
ClassJ = Class(name="ClassJ")
ClassH = Class(name="ClassH")
ClassK = Class(name="ClassK")
ClassL = Class(name="ClassL")
MyClass = Class(name="MyClass")
Quizz = Class(name="Quizz")
Membres = Class(name="Membres")
Cours = Class(name="Cours")
Commentaires = Class(name="Commentaires")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")

# ClassG class attributes and methods

# ClassJ class attributes and methods

# ClassH class attributes and methods

# ClassK class attributes and methods

# ClassL class attributes and methods

# MyClass class attributes and methods

# Quizz class attributes and methods
Quizz_ownerName: Property = Property(name="ownerName", type=StringType)
Quizz_balance: Property = Property(name="balance", type=FloatType)
Quizz.attributes={Quizz_balance, Quizz_ownerName}

# Membres class attributes and methods
Membres_idM: Property = Property(name="idM", type=StringType)
Membres_nom: Property = Property(name="nom", type=StringType)
Membres_prenom: Property = Property(name="prenom", type=StringType)
Membres_email: Property = Property(name="email", type=StringType)
Membres_telephone: Property = Property(name="telephone", type=IntegerType)
Membres_mdp: Property = Property(name="mdp", type=StringType)
Membres.attributes={Membres_telephone, Membres_prenom, Membres_nom, Membres_mdp, Membres_email, Membres_idM}

# Cours class attributes and methods

# Commentaires class attributes and methods
Commentaires_idComm: Property = Property(name="idComm", type=FloatType)
Commentaires_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
Commentaires_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
Commentaires_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
Commentaires.attributes={Commentaires_packageAttribute, Commentaires_protectedAttribute, Commentaires_privateAttribute, Commentaires_idComm}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# Relationships
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=ClassE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=ClassD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopy",
    ends={
        Property(name="classG2", type=ClassG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=ClassF, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopyCopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopyCopy",
    ends={
        Property(name="classG4", type=ClassJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=ClassH, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_569a38d0_ada1_4a2c_9ba3_84bff8b00ef0",
    types={ClassG, ClassJ, ClassH, ClassK, ClassL, MyClass, Quizz, Membres, Cours, Commentaires, ClassD, ClassE, ClassF},
    associations={ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy},
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
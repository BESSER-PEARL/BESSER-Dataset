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
Data_Classe = Class(name="Data::Classe")
Data_Attribut = Class(name="Data::Attribut")
Data_Methode = Class(name="Data::Methode")
Data_Model = Class(name="Data::Model")

# Data_Classe class attributes and methods
Data_Classe_nom: Property = Property(name="nom", type=StringType)
Data_Classe.attributes={Data_Classe_nom}

# Data_Attribut class attributes and methods
Data_Attribut_nom: Property = Property(name="nom", type=StringType)
Data_Attribut_type: Property = Property(name="type", type=StringType)
Data_Attribut.attributes={Data_Attribut_type, Data_Attribut_nom}

# Data_Methode class attributes and methods
Data_Methode_nom: Property = Property(name="nom", type=StringType)
Data_Methode_typeRetour: Property = Property(name="typeRetour", type=StringType)
Data_Methode.attributes={Data_Methode_nom, Data_Methode_typeRetour}

# Data_Model class attributes and methods

# Relationships
attribut0: BinaryAssociation = BinaryAssociation(
    name="attribut0",
    ends={
        Property(name="Data_Attribut", type=Data_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Classe", type=Data_Attribut, multiplicity=Multiplicity(0, 9999))
    }
)
methode1: BinaryAssociation = BinaryAssociation(
    name="methode1",
    ends={
        Property(name="Data_Methode", type=Data_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Classe2", type=Data_Methode, multiplicity=Multiplicity(0, 9999))
    }
)
parametre3: BinaryAssociation = BinaryAssociation(
    name="parametre3",
    ends={
        Property(name="Data_Attribut5", type=Data_Methode, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Methode4", type=Data_Attribut, multiplicity=Multiplicity(0, 9999))
    }
)
classe6: BinaryAssociation = BinaryAssociation(
    name="classe6",
    ends={
        Property(name="Data_Classe7", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Classe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Classe, Data_Attribut, Data_Methode, Data_Model},
    associations={attribut0, methode1, parametre3, classe6},
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
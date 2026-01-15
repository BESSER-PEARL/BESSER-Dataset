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
DeclarationType = Class(name="DeclarationType")
Data_Attribut = Class(name="Data::Attribut")
Data_DeclarationType = Class(name="Data::DeclarationType")
Data_Modele = Class(name="Data::Modele")

# Data_Classe class attributes and methods

# DeclarationType class attributes and methods

# Data_Attribut class attributes and methods
Data_Attribut_estTableau: Property = Property(name="estTableau", type=BooleanType)
Data_Attribut_typeStr: Property = Property(name="typeStr", type=StringType)
Data_Attribut_nom: Property = Property(name="nom", type=StringType)
Data_Attribut.attributes={Data_Attribut_nom, Data_Attribut_estTableau, Data_Attribut_typeStr}

# Data_DeclarationType class attributes and methods
Data_DeclarationType_nom: Property = Property(name="nom", type=StringType)
Data_DeclarationType.attributes={Data_DeclarationType_nom}

# Data_Modele class attributes and methods

# Relationships
attributs0: BinaryAssociation = BinaryAssociation(
    name="attributs0",
    ends={
        Property(name="Data_Attribut", type=Data_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Classe", type=Data_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarationType1: BinaryAssociation = BinaryAssociation(
    name="declarationType1",
    ends={
        Property(name="Data_Attribut2", type=Data_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Classe3", type=Data_Attribut, multiplicity=Multiplicity(1, 1))
    }
)
classes4: BinaryAssociation = BinaryAssociation(
    name="classes4",
    ends={
        Property(name="Data_Classe5", type=Data_Modele, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Modele", type=Data_Classe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Data_Classe_DeclarationType = Generalization(general=DeclarationType, specific=Data_Classe)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Classe, DeclarationType, Data_Attribut, Data_DeclarationType, Data_Modele},
    associations={attributs0, declarationType1, classes4},
    generalizations={gen_Data_Classe_DeclarationType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
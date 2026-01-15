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
Data_Model = Class(name="Data::Model")
Data_Classe = Class(name="Data::Classe")
Data_Attribut = Class(name="Data::Attribut")

# Data_Model class attributes and methods

# Data_Classe class attributes and methods
Data_Classe_name: Property = Property(name="name", type=StringType)
Data_Classe.attributes={Data_Classe_name}

# Data_Attribut class attributes and methods
Data_Attribut_name: Property = Property(name="name", type=StringType)
Data_Attribut_type: Property = Property(name="type", type=StringType)
Data_Attribut.attributes={Data_Attribut_type, Data_Attribut_name}

# Relationships
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="Data_Model", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model0", type=Data_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributs2: BinaryAssociation = BinaryAssociation(
    name="attributs2",
    ends={
        Property(name="Data_Attribut", type=Data_Classe, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Classe", type=Data_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Classe, Data_Attribut},
    associations={classes1, attributs2},
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
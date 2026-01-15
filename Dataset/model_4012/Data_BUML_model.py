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
Data_Class = Class(name="Data::Class")
Data_Attribut = Class(name="Data::Attribut")
Data_Model = Class(name="Data::Model")

# Data_Class class attributes and methods
Data_Class_Name: Property = Property(name="Name", type=StringType)
Data_Class.attributes={Data_Class_Name}

# Data_Attribut class attributes and methods
Data_Attribut_Name: Property = Property(name="Name", type=StringType)
Data_Attribut_Type: Property = Property(name="Type", type=StringType)
Data_Attribut_Visibility: Property = Property(name="Visibility", type=StringType)
Data_Attribut_Static: Property = Property(name="Static", type=BooleanType)
Data_Attribut.attributes={Data_Attribut_Static, Data_Attribut_Name, Data_Attribut_Type, Data_Attribut_Visibility}

# Data_Model class attributes and methods
Data_Model_Name: Property = Property(name="Name", type=StringType)
Data_Model.attributes={Data_Model_Name}

# Relationships
Attributs0: BinaryAssociation = BinaryAssociation(
    name="Attributs0",
    ends={
        Property(name="Data_Attribut", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class", type=Data_Attribut, multiplicity=Multiplicity(0, 9999))
    }
)
Classes1: BinaryAssociation = BinaryAssociation(
    name="Classes1",
    ends={
        Property(name="Data_Class2", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Class, Data_Attribut, Data_Model},
    associations={Attributs0, Classes1},
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
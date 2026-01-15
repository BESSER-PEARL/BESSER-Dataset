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
Data_Class = Class(name="Data::Class")
Data_Attribute = Class(name="Data::Attribute")

# Data_Model class attributes and methods

# Data_Class class attributes and methods
Data_Class_Name: Property = Property(name="Name", type=StringType)
Data_Class.attributes={Data_Class_Name}

# Data_Attribute class attributes and methods
Data_Attribute_Type: Property = Property(name="Type", type=StringType)
Data_Attribute_Name: Property = Property(name="Name", type=StringType)
Data_Attribute.attributes={Data_Attribute_Type, Data_Attribute_Name}

# Relationships
Classes0: BinaryAssociation = BinaryAssociation(
    name="Classes0",
    ends={
        Property(name="Data_Class", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Attributes1: BinaryAssociation = BinaryAssociation(
    name="Attributes1",
    ends={
        Property(name="Data_Attribute", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class2", type=Data_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Class, Data_Attribute},
    associations={Classes0, Attributes1},
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
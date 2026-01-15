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
Data_Type = Class(name="Data::Type")

# Data_Model class attributes and methods

# Data_Class class attributes and methods
Data_Class_name: Property = Property(name="name", type=StringType)
Data_Class.attributes={Data_Class_name}

# Data_Attribute class attributes and methods
Data_Attribute_name: Property = Property(name="name", type=StringType)
Data_Attribute_visibility: Property = Property(name="visibility", type=StringType)
Data_Attribute.attributes={Data_Attribute_visibility, Data_Attribute_name}

# Data_Type class attributes and methods
Data_Type_name: Property = Property(name="name", type=StringType)
Data_Type_isReference: Property = Property(name="isReference", type=BooleanType)
Data_Type.attributes={Data_Type_isReference, Data_Type_name}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="Data_Class", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="Data_Attribute", type=Data_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Class2", type=Data_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="Data_Type", type=Data_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Attribute4", type=Data_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Class, Data_Attribute, Data_Type},
    associations={classes0, attributes1, type3},
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
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
classes_Model = Class(name="classes_Model")
classes_Class = Class(name="classes_Class")
classes_Type = Class(name="classes_Type", is_abstract=True)
classes_DataType = Class(name="classes_DataType")
Type = Class(name="Type")
classes_Attribute = Class(name="classes_Attribute")

# classes_Model class attributes and methods

# classes_Class class attributes and methods

# classes_Type class attributes and methods
classes_Type_name: Property = Property(name="name", type=StringType)
classes_Type.attributes={classes_Type_name}

# classes_DataType class attributes and methods

# Type class attributes and methods

# classes_Attribute class attributes and methods
classes_Attribute_name: Property = Property(name="name", type=StringType)
classes_Attribute_value: Property = Property(name="value", type=StringType)
classes_Attribute.attributes={classes_Attribute_value, classes_Attribute_name}

# Relationships
topClass0: BinaryAssociation = BinaryAssociation(
    name="topClass0",
    ends={
        Property(name="classes_Class", type=classes_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Model", type=classes_Class, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="classes_Attribute", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class2", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="classes_Type", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Attribute4", type=classes_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classes_DataType_Type = Generalization(general=Type, specific=classes_DataType)
gen_classes_Class_Type = Generalization(general=Type, specific=classes_Class)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_Model, classes_Class, classes_Type, classes_DataType, Type, classes_Attribute},
    associations={topClass0, attributes1, type3},
    generalizations={gen_classes_DataType_Type, gen_classes_Class_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
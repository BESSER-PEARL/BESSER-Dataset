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
SimpleClass_PrimitiveDataType = Class(name="SimpleClass_PrimitiveDataType")
SimpleClass_Association = Class(name="SimpleClass_Association")
SimpleClass_Attribute = Class(name="SimpleClass_Attribute")
SimpleClass_Classifier = Class(name="SimpleClass_Classifier")
SimpleClass_Class = Class(name="SimpleClass_Class")
Classifier = Class(name="Classifier")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")

# SimpleClass_PrimitiveDataType class attributes and methods

# SimpleClass_Association class attributes and methods
SimpleClass_Association_name: Property = Property(name="name", type=StringType)
SimpleClass_Association.attributes={SimpleClass_Association_name}

# SimpleClass_Attribute class attributes and methods
SimpleClass_Attribute_name: Property = Property(name="name", type=StringType)
SimpleClass_Attribute_is_primary: Property = Property(name="is_primary", type=StringType)
SimpleClass_Attribute.attributes={SimpleClass_Attribute_name, SimpleClass_Attribute_is_primary}

# SimpleClass_Classifier class attributes and methods
SimpleClass_Classifier_name: Property = Property(name="name", type=StringType)
SimpleClass_Classifier.attributes={SimpleClass_Classifier_name}

# SimpleClass_Class class attributes and methods
SimpleClass_Class_is_persistent: Property = Property(name="is_persistent", type=StringType)
SimpleClass_Class.attributes={SimpleClass_Class_is_persistent}

# Classifier class attributes and methods

# Class class attributes and methods

# Attribute class attributes and methods

# Relationships
src2: BinaryAssociation = BinaryAssociation(
    name="src2",
    ends={
        Property(name="Class3", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
dest4: BinaryAssociation = BinaryAssociation(
    name="dest4",
    ends={
        Property(name="Class6", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association5", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="Classifier", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="Class", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Class", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
attrs1: BinaryAssociation = BinaryAssociation(
    name="attrs1",
    ends={
        Property(name="Attribute", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_8: BinaryAssociation = BinaryAssociation(
    name="class_8",
    ends={
        Property(name="Class9", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attrs", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleClass_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=SimpleClass_PrimitiveDataType)
gen_SimpleClass_Class_Classifier = Generalization(general=Classifier, specific=SimpleClass_Class)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SimpleClass_PrimitiveDataType, SimpleClass_Association, SimpleClass_Attribute, SimpleClass_Classifier, SimpleClass_Class, Classifier, Class_, Attribute},
    associations={src2, dest4, type7, parent0, attrs1, class_8},
    generalizations={gen_SimpleClass_PrimitiveDataType_Classifier, gen_SimpleClass_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
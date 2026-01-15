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
SimpleClass_Classifier = Class(name="SimpleClass::Classifier")
SimpleClass_Class = Class(name="SimpleClass::Class")
Classifier = Class(name="Classifier")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")
SimpleClass_PrimitiveDataType = Class(name="SimpleClass::PrimitiveDataType")
SimpleClass_Association = Class(name="SimpleClass::Association")
SimpleClass_Attribute = Class(name="SimpleClass::Attribute")

# SimpleClass_Classifier class attributes and methods
SimpleClass_Classifier_name: Property = Property(name="name", type=StringType)
SimpleClass_Classifier.attributes={SimpleClass_Classifier_name}

# SimpleClass_Class class attributes and methods
SimpleClass_Class_is_persistent: Property = Property(name="is_persistent", type=StringType)
SimpleClass_Class.attributes={SimpleClass_Class_is_persistent}

# Classifier class attributes and methods

# Class class attributes and methods

# Attribute class attributes and methods

# SimpleClass_PrimitiveDataType class attributes and methods

# SimpleClass_Association class attributes and methods
SimpleClass_Association_name: Property = Property(name="name", type=StringType)
SimpleClass_Association.attributes={SimpleClass_Association_name}

# SimpleClass_Attribute class attributes and methods
SimpleClass_Attribute_is_primary: Property = Property(name="is_primary", type=StringType)
SimpleClass_Attribute_name: Property = Property(name="name", type=StringType)
SimpleClass_Attribute.attributes={SimpleClass_Attribute_is_primary, SimpleClass_Attribute_name}

# Relationships
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="Classifier", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
class9: BinaryAssociation = BinaryAssociation(
    name="class9",
    ends={
        Property(name="Class11", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Attribute10", type=Class_, multiplicity=Multiplicity(1, 1))
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
        Property(name="SimpleClass_Class2", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src3: BinaryAssociation = BinaryAssociation(
    name="src3",
    ends={
        Property(name="Class4", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
dest5: BinaryAssociation = BinaryAssociation(
    name="dest5",
    ends={
        Property(name="Class7", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association6", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleClass_Class_Classifier = Generalization(general=Classifier, specific=SimpleClass_Class)
gen_SimpleClass_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=SimpleClass_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SimpleClass_Classifier, SimpleClass_Class, Classifier, Class_, Attribute, SimpleClass_PrimitiveDataType, SimpleClass_Association, SimpleClass_Attribute},
    associations={type8, class9, parent0, attrs1, src3, dest5},
    generalizations={gen_SimpleClass_Class_Classifier, gen_SimpleClass_PrimitiveDataType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
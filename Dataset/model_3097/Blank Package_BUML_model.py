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
SimpleClass_Class = Class(name="SimpleClass::Class")
Classifier = Class(name="Classifier")
SimpleClass_Attribute = Class(name="SimpleClass::Attribute")
SimpleClass_Classifier = Class(name="SimpleClass::Classifier")
SimpleClass_Association = Class(name="SimpleClass::Association")
SimpleClass_PrimitiveDataType = Class(name="SimpleClass::PrimitiveDataType")

# SimpleClass_Class class attributes and methods
SimpleClass_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
SimpleClass_Class.attributes={SimpleClass_Class_is_persistent}

# Classifier class attributes and methods

# SimpleClass_Attribute class attributes and methods
SimpleClass_Attribute_name: Property = Property(name="name", type=StringType)
SimpleClass_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
SimpleClass_Attribute.attributes={SimpleClass_Attribute_name, SimpleClass_Attribute_is_primary}

# SimpleClass_Classifier class attributes and methods
SimpleClass_Classifier_name: Property = Property(name="name", type=StringType)
SimpleClass_Classifier.attributes={SimpleClass_Classifier_name}

# SimpleClass_Association class attributes and methods
SimpleClass_Association_name: Property = Property(name="name", type=StringType)
SimpleClass_Association.attributes={SimpleClass_Association_name}

# SimpleClass_PrimitiveDataType class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="SimpleClass_Class", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Class0", type=SimpleClass_Class, multiplicity=Multiplicity(0, 1))
    }
)
attrs2: BinaryAssociation = BinaryAssociation(
    name="attrs2",
    ends={
        Property(name="SimpleClass_Attribute", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Class3", type=SimpleClass_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="SimpleClass_Classifier", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Attribute5", type=SimpleClass_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="SimpleClass_Class7", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest8: BinaryAssociation = BinaryAssociation(
    name="dest8",
    ends={
        Property(name="SimpleClass_Class10", type=SimpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Association9", type=SimpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleClass_Class_Classifier = Generalization(general=Classifier, specific=SimpleClass_Class)
gen_SimpleClass_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=SimpleClass_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="SimpleClass",
    types={SimpleClass_Class, Classifier, SimpleClass_Attribute, SimpleClass_Classifier, SimpleClass_Association, SimpleClass_PrimitiveDataType},
    associations={parent1, attrs2, type4, src6, dest8},
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
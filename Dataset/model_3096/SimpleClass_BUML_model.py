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

# Enumerations
Vocabulary: Enumeration = Enumeration(
    name="Vocabulary",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Language"),
			EnumerationLiteral(name="Eurovocs"),
			EnumerationLiteral(name="Decs")
    }
)

Entity: Enumeration = Enumeration(
    name="Entity",
    literals={
            
    }
)

EA: Enumeration = Enumeration(
    name="EA",
    literals={
            EnumerationLiteral(name="Institution"),
			EnumerationLiteral(name="Journal"),
			EnumerationLiteral(name="Author")
    }
)

# Classes
SimpleClass_Class = Class(name="SimpleClass::Class")
Classifier = Class(name="Classifier")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")
SimpleClass_PrimitiveDataType = Class(name="SimpleClass::PrimitiveDataType")
SimpleClass_Association = Class(name="SimpleClass::Association")
SimpleClass_Attribute = Class(name="SimpleClass::Attribute")
SimpleClass_Classifier = Class(name="SimpleClass::Classifier")
SimpleClass_Schema = Class(name="SimpleClass::Schema")
Association = Class(name="Association")
PrimitiveDataType = Class(name="PrimitiveDataType")

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
SimpleClass_Attribute_name: Property = Property(name="name", type=StringType)
SimpleClass_Attribute_is_primary: Property = Property(name="is_primary", type=StringType)
SimpleClass_Attribute.attributes={SimpleClass_Attribute_name, SimpleClass_Attribute_is_primary}

# SimpleClass_Classifier class attributes and methods
SimpleClass_Classifier_name: Property = Property(name="name", type=StringType)
SimpleClass_Classifier.attributes={SimpleClass_Classifier_name}

# SimpleClass_Schema class attributes and methods

# Association class attributes and methods

# PrimitiveDataType class attributes and methods

# Relationships
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
clases9: BinaryAssociation = BinaryAssociation(
    name="clases9",
    ends={
        Property(name="Class10", type=SimpleClass_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Schema", type=Class_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relaciones11: BinaryAssociation = BinaryAssociation(
    name="relaciones11",
    ends={
        Property(name="Association", type=SimpleClass_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Schema12", type=Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datos13: BinaryAssociation = BinaryAssociation(
    name="datos13",
    ends={
        Property(name="PrimitiveDataType", type=SimpleClass_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Schema14", type=PrimitiveDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="Classifier", type=SimpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleClass_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleClass_Class_Classifier = Generalization(general=Classifier, specific=SimpleClass_Class)
gen_SimpleClass_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=SimpleClass_PrimitiveDataType)
gen_SimpleClass_Schema_Classifier = Generalization(general=Classifier, specific=SimpleClass_Schema)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SimpleClass_Class, Classifier, Class_, Attribute, SimpleClass_PrimitiveDataType, SimpleClass_Association, SimpleClass_Attribute, SimpleClass_Classifier, SimpleClass_Schema, Association, PrimitiveDataType, Vocabulary, Entity, EA},
    associations={parent0, attrs1, src3, dest5, clases9, relaciones11, datos13, type8},
    generalizations={gen_SimpleClass_Class_Classifier, gen_SimpleClass_PrimitiveDataType_Classifier, gen_SimpleClass_Schema_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
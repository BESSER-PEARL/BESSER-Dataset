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
ClassM_Class = Class(name="ClassM::Class")
Classifier = Class(name="Classifier")
ClassM_Classifier = Class(name="ClassM::Classifier")
ClassM_TypedElement = Class(name="ClassM::TypedElement")
TypedElement = Class(name="TypedElement")
ClassM_StructuralFeature = Class(name="ClassM::StructuralFeature")
ClassM_PrimitiveType = Class(name="ClassM::PrimitiveType")
ClassM_Operation = Class(name="ClassM::Operation")
StructuralFeature = Class(name="StructuralFeature")
ClassM_Parameter = Class(name="ClassM::Parameter")
ClassM_Attribute = Class(name="ClassM::Attribute")
ClassM_Model = Class(name="ClassM::Model")

# ClassM_Class class attributes and methods

# Classifier class attributes and methods

# ClassM_Classifier class attributes and methods
ClassM_Classifier_name: Property = Property(name="name", type=StringType)
ClassM_Classifier.attributes={ClassM_Classifier_name}

# ClassM_TypedElement class attributes and methods

# TypedElement class attributes and methods

# ClassM_StructuralFeature class attributes and methods
ClassM_StructuralFeature_name: Property = Property(name="name", type=StringType)
ClassM_StructuralFeature_visibility: Property = Property(name="visibility", type=StringType)
ClassM_StructuralFeature.attributes={ClassM_StructuralFeature_name, ClassM_StructuralFeature_visibility}

# ClassM_PrimitiveType class attributes and methods

# ClassM_Operation class attributes and methods

# StructuralFeature class attributes and methods

# ClassM_Parameter class attributes and methods
ClassM_Parameter_name: Property = Property(name="name", type=StringType)
ClassM_Parameter.attributes={ClassM_Parameter_name}

# ClassM_Attribute class attributes and methods
ClassM_Attribute_multivalued: Property = Property(name="multivalued", type=BooleanType)
ClassM_Attribute.attributes={ClassM_Attribute_multivalued}

# ClassM_Model class attributes and methods

# Relationships
typeOf6: BinaryAssociation = BinaryAssociation(
    name="typeOf6",
    ends={
        Property(name="TypedElement", type=ClassM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=ClassM_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Class", type=ClassM_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=ClassM_Class, multiplicity=Multiplicity(1, 1))
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="StructuralFeature", type=ClassM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ClassM_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="Classifier", type=ClassM_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOf", type=ClassM_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
parents2: BinaryAssociation = BinaryAssociation(
    name="parents2",
    ends={
        Property(name="ClassM_Class", type=ClassM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassM_Class1", type=ClassM_Class, multiplicity=Multiplicity(0, 9999))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="ClassM_Class5", type=ClassM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassM_Class3", type=ClassM_Class, multiplicity=Multiplicity(0, 9999))
    }
)
params9: BinaryAssociation = BinaryAssociation(
    name="params9",
    ends={
        Property(name="Parameter", type=ClassM_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="paramOf", type=ClassM_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
paramOf10: BinaryAssociation = BinaryAssociation(
    name="paramOf10",
    ends={
        Property(name="Operation", type=ClassM_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="params", type=ClassM_Operation, multiplicity=Multiplicity(1, 1))
    }
)
classifiers11: BinaryAssociation = BinaryAssociation(
    name="classifiers11",
    ends={
        Property(name="ClassM_Classifier", type=ClassM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassM_Model", type=ClassM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ClassM_Class_Classifier = Generalization(general=Classifier, specific=ClassM_Class)
gen_ClassM_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ClassM_StructuralFeature)
gen_ClassM_Operation_StructuralFeature = Generalization(general=StructuralFeature, specific=ClassM_Operation)
gen_ClassM_Parameter_TypedElement = Generalization(general=TypedElement, specific=ClassM_Parameter)
gen_ClassM_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=ClassM_Attribute)
gen_ClassM_PrimitiveType_Classifier = Generalization(general=Classifier, specific=ClassM_PrimitiveType)

# Domain Model
domain_model = DomainModel(
    name="ClassM",
    types={ClassM_Class, Classifier, ClassM_Classifier, ClassM_TypedElement, TypedElement, ClassM_StructuralFeature, ClassM_PrimitiveType, ClassM_Operation, StructuralFeature, ClassM_Parameter, ClassM_Attribute, ClassM_Model},
    associations={typeOf6, owner7, features0, type8, parents2, children4, params9, paramOf10, classifiers11},
    generalizations={gen_ClassM_Class_Classifier, gen_ClassM_StructuralFeature_TypedElement, gen_ClassM_Operation_StructuralFeature, gen_ClassM_Parameter_TypedElement, gen_ClassM_Attribute_StructuralFeature, gen_ClassM_PrimitiveType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
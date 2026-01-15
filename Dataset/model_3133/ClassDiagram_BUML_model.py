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
ClassDiagram_Model = Class(name="ClassDiagram::Model")
ClassDiagram_Classifier = Class(name="ClassDiagram::Classifier")
ClassDiagram_Class = Class(name="ClassDiagram::Class")
Classifier = Class(name="Classifier")
ClassDiagram_StructuralFeature = Class(name="ClassDiagram::StructuralFeature", is_abstract=True)
ClassDiagram_Parameter = Class(name="ClassDiagram::Parameter")
TypedElement = Class(name="TypedElement")
ClassDiagram_TypedElement = Class(name="ClassDiagram::TypedElement")
ClassDiagram_PrimitiveType = Class(name="ClassDiagram::PrimitiveType")
ClassDiagram_Operation = Class(name="ClassDiagram::Operation")
StructuralFeature = Class(name="StructuralFeature")
ClassDiagram_Attribute = Class(name="ClassDiagram::Attribute")

# ClassDiagram_Model class attributes and methods

# ClassDiagram_Classifier class attributes and methods
ClassDiagram_Classifier_name: Property = Property(name="name", type=StringType)
ClassDiagram_Classifier.attributes={ClassDiagram_Classifier_name}

# ClassDiagram_Class class attributes and methods

# Classifier class attributes and methods

# ClassDiagram_StructuralFeature class attributes and methods
ClassDiagram_StructuralFeature_name: Property = Property(name="name", type=StringType)
ClassDiagram_StructuralFeature_visibility: Property = Property(name="visibility", type=StringType)
ClassDiagram_StructuralFeature.attributes={ClassDiagram_StructuralFeature_visibility, ClassDiagram_StructuralFeature_name}

# ClassDiagram_Parameter class attributes and methods
ClassDiagram_Parameter_name: Property = Property(name="name", type=StringType)
ClassDiagram_Parameter.attributes={ClassDiagram_Parameter_name}

# TypedElement class attributes and methods

# ClassDiagram_TypedElement class attributes and methods

# ClassDiagram_PrimitiveType class attributes and methods

# ClassDiagram_Operation class attributes and methods

# StructuralFeature class attributes and methods

# ClassDiagram_Attribute class attributes and methods
ClassDiagram_Attribute_multivalued: Property = Property(name="multivalued", type=BooleanType)
ClassDiagram_Attribute.attributes={ClassDiagram_Attribute_multivalued}

# Relationships
classifiers0: BinaryAssociation = BinaryAssociation(
    name="classifiers0",
    ends={
        Property(name="ClassDiagram_Classifier", type=ClassDiagram_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Model", type=ClassDiagram_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="StructuralFeature", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ClassDiagram_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents3: BinaryAssociation = BinaryAssociation(
    name="parents3",
    ends={
        Property(name="Class", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=ClassDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
childs5: BinaryAssociation = BinaryAssociation(
    name="childs5",
    ends={
        Property(name="Class6", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=ClassDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Class8", type=ClassDiagram_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="ClassDiagram_Classifier10", type=ClassDiagram_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_TypedElement", type=ClassDiagram_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
params11: BinaryAssociation = BinaryAssociation(
    name="params11",
    ends={
        Property(name="Parameter", type=ClassDiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="paramOf", type=ClassDiagram_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
paramOf12: BinaryAssociation = BinaryAssociation(
    name="paramOf12",
    ends={
        Property(name="Operation", type=ClassDiagram_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="params", type=ClassDiagram_Operation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ClassDiagram_Class_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Class)
gen_ClassDiagram_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ClassDiagram_StructuralFeature)
gen_ClassDiagram_PrimitiveType_Classifier = Generalization(general=Classifier, specific=ClassDiagram_PrimitiveType)
gen_ClassDiagram_Operation_StructuralFeature = Generalization(general=StructuralFeature, specific=ClassDiagram_Operation)
gen_ClassDiagram_Parameter_TypedElement = Generalization(general=TypedElement, specific=ClassDiagram_Parameter)
gen_ClassDiagram_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=ClassDiagram_Attribute)

# Domain Model
domain_model = DomainModel(
    name="ClassDiagram",
    types={ClassDiagram_Model, ClassDiagram_Classifier, ClassDiagram_Class, Classifier, ClassDiagram_StructuralFeature, ClassDiagram_Parameter, TypedElement, ClassDiagram_TypedElement, ClassDiagram_PrimitiveType, ClassDiagram_Operation, StructuralFeature, ClassDiagram_Attribute},
    associations={classifiers0, features1, parents3, childs5, owner7, type9, params11, paramOf12},
    generalizations={gen_ClassDiagram_Class_Classifier, gen_ClassDiagram_StructuralFeature_TypedElement, gen_ClassDiagram_PrimitiveType_Classifier, gen_ClassDiagram_Operation_StructuralFeature, gen_ClassDiagram_Parameter_TypedElement, gen_ClassDiagram_Attribute_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
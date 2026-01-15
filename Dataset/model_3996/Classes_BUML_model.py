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
classes_CModel = Class(name="classes::CModel")
classes_Classifier = Class(name="classes::Classifier", is_abstract=True)
classes_NamedElement = Class(name="classes::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
classes_CClass = Class(name="classes::CClass")
Classifier = Class(name="Classifier")
classes_Attribute = Class(name="classes::Attribute")
classes_Datatype = Class(name="classes::Datatype")

# classes_CModel class attributes and methods

# classes_Classifier class attributes and methods

# classes_NamedElement class attributes and methods
classes_NamedElement_name: Property = Property(name="name", type=StringType)
classes_NamedElement.attributes={classes_NamedElement_name}

# NamedElement class attributes and methods

# classes_CClass class attributes and methods
classes_CClass_abstract: Property = Property(name="abstract", type=BooleanType)
classes_CClass.attributes={classes_CClass_abstract}

# Classifier class attributes and methods

# classes_Attribute class attributes and methods
classes_Attribute_isMany: Property = Property(name="isMany", type=BooleanType)
classes_Attribute.attributes={classes_Attribute_isMany}

# classes_Datatype class attributes and methods

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="classes_Classifier", type=classes_CModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_CModel", type=classes_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="classes_CClass", type=classes_CClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_CClass1", type=classes_CClass, multiplicity=Multiplicity(0, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="classes_Attribute", type=classes_CClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_CClass4", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super6: BinaryAssociation = BinaryAssociation(
    name="super6",
    ends={
        Property(name="classes_CClass7", type=classes_CClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_CClass5", type=classes_CClass, multiplicity=Multiplicity(0, 9999))
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="classes_Classifier10", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Attribute9", type=classes_Classifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classes_Classifier_NamedElement = Generalization(general=NamedElement, specific=classes_Classifier)
gen_classes_CClass_Classifier = Generalization(general=Classifier, specific=classes_CClass)
gen_classes_Attribute_NamedElement = Generalization(general=NamedElement, specific=classes_Attribute)
gen_classes_Datatype_Classifier = Generalization(general=Classifier, specific=classes_Datatype)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_CModel, classes_Classifier, classes_NamedElement, NamedElement, classes_CClass, Classifier, classes_Attribute, classes_Datatype},
    associations={contents0, extends2, attributes3, super6, type8},
    generalizations={gen_classes_Classifier_NamedElement, gen_classes_CClass_Classifier, gen_classes_Attribute_NamedElement, gen_classes_Datatype_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
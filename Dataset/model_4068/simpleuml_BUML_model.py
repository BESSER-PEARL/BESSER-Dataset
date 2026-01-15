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
Ignore: Enumeration = Enumeration(
    name="Ignore",
    literals={
            EnumerationLiteral(name="lit1"),
			EnumerationLiteral(name="anotherlit")
    }
)

# Classes
simpleuml_UMLClass = Class(name="simpleuml::UMLClass")
Classifier = Class(name="Classifier")
simpleuml_PrimitiveDataType = Class(name="simpleuml::PrimitiveDataType")
simpleuml_UMLPackage = Class(name="simpleuml::UMLPackage")
simpleuml_Attribute = Class(name="simpleuml::Attribute")
simpleuml_ModelElement = Class(name="simpleuml::ModelElement", is_abstract=True)
simpleuml_Association = Class(name="simpleuml::Association")
ModelElement = Class(name="ModelElement")
simpleuml_Classifier = Class(name="simpleuml::Classifier", is_abstract=True)

# simpleuml_UMLClass class attributes and methods
simpleuml_UMLClass_kind: Property = Property(name="kind", type=StringType)
simpleuml_UMLClass.attributes={simpleuml_UMLClass_kind}

# Classifier class attributes and methods

# simpleuml_PrimitiveDataType class attributes and methods

# simpleuml_UMLPackage class attributes and methods

# simpleuml_Attribute class attributes and methods

# simpleuml_ModelElement class attributes and methods
simpleuml_ModelElement_name: Property = Property(name="name", type=StringType)
simpleuml_ModelElement.attributes={simpleuml_ModelElement_name}

# simpleuml_Association class attributes and methods

# ModelElement class attributes and methods

# simpleuml_Classifier class attributes and methods

# Relationships
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="simpleuml_Classifier", type=simpleuml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Attribute", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="UMLClass", type=simpleuml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=simpleuml_UMLClass, multiplicity=Multiplicity(1, 1))
    }
)
contents10: BinaryAssociation = BinaryAssociation(
    name="contents10",
    ends={
        Property(name="simpleuml_ModelElement", type=simpleuml_UMLPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_UMLPackage", type=simpleuml_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents1: BinaryAssociation = BinaryAssociation(
    name="parents1",
    ends={
        Property(name="simpleuml_UMLClass", type=simpleuml_UMLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_UMLClass0", type=simpleuml_UMLClass, multiplicity=Multiplicity(0, 9999))
    }
)
attribute2: BinaryAssociation = BinaryAssociation(
    name="attribute2",
    ends={
        Property(name="Attribute", type=simpleuml_UMLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleuml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="simpleuml_UMLClass4", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Association", type=simpleuml_UMLClass, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="simpleuml_UMLClass7", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Association6", type=simpleuml_UMLClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleuml_UMLClass_Classifier = Generalization(general=Classifier, specific=simpleuml_UMLClass)
gen_simpleuml_Attribute_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Attribute)
gen_simpleuml_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=simpleuml_PrimitiveDataType)
gen_simpleuml_Association_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Association)
gen_simpleuml_Classifier_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Classifier)

# Domain Model
domain_model = DomainModel(
    name="simpleuml",
    types={simpleuml_UMLClass, Classifier, simpleuml_PrimitiveDataType, simpleuml_UMLPackage, simpleuml_Attribute, simpleuml_ModelElement, simpleuml_Association, ModelElement, simpleuml_Classifier, Ignore},
    associations={type8, owner9, contents10, parents1, attribute2, source3, target5},
    generalizations={gen_simpleuml_UMLClass_Classifier, gen_simpleuml_Attribute_ModelElement, gen_simpleuml_PrimitiveDataType_Classifier, gen_simpleuml_Association_ModelElement, gen_simpleuml_Classifier_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
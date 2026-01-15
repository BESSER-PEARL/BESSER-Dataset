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
simpleuml_NamedElement = Class(name="simpleuml::NamedElement", is_abstract=True)
simpleuml_Feature = Class(name="simpleuml::Feature", is_abstract=True)
NamedElement = Class(name="NamedElement")
simpleuml_Type = Class(name="simpleuml::Type", is_abstract=True)
simpleuml_Classifier = Class(name="simpleuml::Classifier", is_abstract=True)
Type = Class(name="Type")
simpleuml_Generalization = Class(name="simpleuml::Generalization")
simpleuml_StructuralFeature = Class(name="simpleuml::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
simpleuml_Class = Class(name="simpleuml::Class")
Classifier = Class(name="Classifier")
simpleuml_Property = Class(name="simpleuml::Property")
StructuralFeature = Class(name="StructuralFeature")

# simpleuml_NamedElement class attributes and methods
simpleuml_NamedElement_name: Property = Property(name="name", type=StringType)
simpleuml_NamedElement.attributes={simpleuml_NamedElement_name}

# simpleuml_Feature class attributes and methods

# NamedElement class attributes and methods

# simpleuml_Type class attributes and methods

# simpleuml_Classifier class attributes and methods

# Type class attributes and methods

# simpleuml_Generalization class attributes and methods

# simpleuml_StructuralFeature class attributes and methods

# Feature class attributes and methods

# simpleuml_Class class attributes and methods

# Classifier class attributes and methods

# simpleuml_Property class attributes and methods

# StructuralFeature class attributes and methods

# Relationships
generalization0: BinaryAssociation = BinaryAssociation(
    name="generalization0",
    ends={
        Property(name="Generalization", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=simpleuml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general3: BinaryAssociation = BinaryAssociation(
    name="general3",
    ends={
        Property(name="simpleuml_Classifier", type=simpleuml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Generalization", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute1: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1",
    ends={
        Property(name="simpleuml_Property", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Class", type=simpleuml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specific2: BinaryAssociation = BinaryAssociation(
    name="specific2",
    ends={
        Property(name="Classifier", type=simpleuml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=simpleuml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleuml_Feature_NamedElement = Generalization(general=NamedElement, specific=simpleuml_Feature)
gen_simpleuml_Type_NamedElement = Generalization(general=NamedElement, specific=simpleuml_Type)
gen_simpleuml_Classifier_Type = Generalization(general=Type, specific=simpleuml_Classifier)
gen_simpleuml_StructuralFeature_Feature = Generalization(general=Feature, specific=simpleuml_StructuralFeature)
gen_simpleuml_Class_Classifier = Generalization(general=Classifier, specific=simpleuml_Class)
gen_simpleuml_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=simpleuml_Property)

# Domain Model
domain_model = DomainModel(
    name="simpleuml",
    types={simpleuml_NamedElement, simpleuml_Feature, NamedElement, simpleuml_Type, simpleuml_Classifier, Type, simpleuml_Generalization, simpleuml_StructuralFeature, Feature, simpleuml_Class, Classifier, simpleuml_Property, StructuralFeature},
    associations={generalization0, general3, ownedAttribute1, specific2},
    generalizations={gen_simpleuml_Feature_NamedElement, gen_simpleuml_Type_NamedElement, gen_simpleuml_Classifier_Type, gen_simpleuml_StructuralFeature_Feature, gen_simpleuml_Class_Classifier, gen_simpleuml_Property_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
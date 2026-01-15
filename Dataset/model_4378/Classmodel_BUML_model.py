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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PACKAGE_PRIVATE")
    }
)

# Classes
classmodel_Feature = Class(name="classmodel::Feature")
classmodel_Model = Class(name="classmodel::Model")
classmodel_Import = Class(name="classmodel::Import")
classmodel_Element = Class(name="classmodel::Element")
classmodel_Annotation = Class(name="classmodel::Annotation")
classmodel_Entity = Class(name="classmodel::Entity")
Element = Class(name="Element")
classmodel_Datatype = Class(name="classmodel::Datatype")
Entity = Class(name="Entity")
classmodel_Package = Class(name="classmodel::Package")
classmodel_Classifier = Class(name="classmodel::Classifier")
classmodel_Type = Class(name="classmodel::Type")
classmodel_Enumeration = Class(name="classmodel::Enumeration")
classmodel_Relationship = Class(name="classmodel::Relationship")
classmodel_Association = Class(name="classmodel::Association")
Relationship = Class(name="Relationship")
classmodel_Composition = Class(name="classmodel::Composition")
classmodel_Generalization = Class(name="classmodel::Generalization")
classmodel_Dependency = Class(name="classmodel::Dependency")
classmodel_Realization = Class(name="classmodel::Realization")
classmodel_Constant = Class(name="classmodel::Constant")
Feature = Class(name="Feature")
classmodel_Operation = Class(name="classmodel::Operation")
classmodel_Parameter = Class(name="classmodel::Parameter")
classmodel_Multiplicity = Class(name="classmodel::Multiplicity")
classmodel_Aggregation = Class(name="classmodel::Aggregation")
classmodel_Array = Class(name="classmodel::Array")
classmodel_Reference = Class(name="classmodel::Reference")
classmodel_Attribute = Class(name="classmodel::Attribute")

# classmodel_Feature class attributes and methods
classmodel_Feature_name: Property = Property(name="name", type=StringType)
classmodel_Feature_value: Property = Property(name="value", type=StringType)
classmodel_Feature_constraint: Property = Property(name="constraint", type=StringType)
classmodel_Feature_visibility: Property = Property(name="visibility", type=StringType)
classmodel_Feature.attributes={classmodel_Feature_constraint, classmodel_Feature_visibility, classmodel_Feature_name, classmodel_Feature_value}

# classmodel_Model class attributes and methods

# classmodel_Import class attributes and methods
classmodel_Import_importURI: Property = Property(name="importURI", type=StringType)
classmodel_Import.attributes={classmodel_Import_importURI}

# classmodel_Element class attributes and methods

# classmodel_Annotation class attributes and methods

# classmodel_Entity class attributes and methods
classmodel_Entity_name: Property = Property(name="name", type=StringType)
classmodel_Entity.attributes={classmodel_Entity_name}

# Element class attributes and methods

# classmodel_Datatype class attributes and methods

# Entity class attributes and methods

# classmodel_Package class attributes and methods
classmodel_Package_name: Property = Property(name="name", type=StringType)
classmodel_Package.attributes={classmodel_Package_name}

# classmodel_Classifier class attributes and methods
classmodel_Classifier_constraint: Property = Property(name="constraint", type=StringType)
classmodel_Classifier.attributes={classmodel_Classifier_constraint}

# classmodel_Type class attributes and methods
classmodel_Type_visibility: Property = Property(name="visibility", type=StringType)
classmodel_Type.attributes={classmodel_Type_visibility}

# classmodel_Enumeration class attributes and methods
classmodel_Enumeration_constraint: Property = Property(name="constraint", type=StringType)
classmodel_Enumeration.attributes={classmodel_Enumeration_constraint}

# classmodel_Relationship class attributes and methods
classmodel_Relationship_label: Property = Property(name="label", type=StringType)
classmodel_Relationship.attributes={classmodel_Relationship_label}

# classmodel_Association class attributes and methods
classmodel_Association_headNavigable: Property = Property(name="headNavigable", type=BooleanType)
classmodel_Association_headVisibility: Property = Property(name="headVisibility", type=StringType)
classmodel_Association_headLabel: Property = Property(name="headLabel", type=StringType)
classmodel_Association_tailNavigable: Property = Property(name="tailNavigable", type=BooleanType)
classmodel_Association_tailVisibility: Property = Property(name="tailVisibility", type=StringType)
classmodel_Association_tailLabel: Property = Property(name="tailLabel", type=StringType)
classmodel_Association.attributes={classmodel_Association_tailVisibility, classmodel_Association_tailNavigable, classmodel_Association_headNavigable, classmodel_Association_headVisibility, classmodel_Association_headLabel, classmodel_Association_tailLabel}

# Relationship class attributes and methods

# classmodel_Composition class attributes and methods
classmodel_Composition_headNavigable: Property = Property(name="headNavigable", type=BooleanType)
classmodel_Composition_headVisibility: Property = Property(name="headVisibility", type=StringType)
classmodel_Composition_headLabel: Property = Property(name="headLabel", type=StringType)
classmodel_Composition_tailNavigable: Property = Property(name="tailNavigable", type=BooleanType)
classmodel_Composition_tailVisibility: Property = Property(name="tailVisibility", type=StringType)
classmodel_Composition_tailLabel: Property = Property(name="tailLabel", type=StringType)
classmodel_Composition.attributes={classmodel_Composition_headNavigable, classmodel_Composition_tailLabel, classmodel_Composition_headVisibility, classmodel_Composition_tailVisibility, classmodel_Composition_headLabel, classmodel_Composition_tailNavigable}

# classmodel_Generalization class attributes and methods

# classmodel_Dependency class attributes and methods

# classmodel_Realization class attributes and methods

# classmodel_Constant class attributes and methods

# Feature class attributes and methods

# classmodel_Operation class attributes and methods
classmodel_Operation_static: Property = Property(name="static", type=BooleanType)
classmodel_Operation_body: Property = Property(name="body", type=StringType)
classmodel_Operation.attributes={classmodel_Operation_static, classmodel_Operation_body}

# classmodel_Parameter class attributes and methods
classmodel_Parameter_name: Property = Property(name="name", type=StringType)
classmodel_Parameter_implicit: Property = Property(name="implicit", type=StringType)
classmodel_Parameter.attributes={classmodel_Parameter_name, classmodel_Parameter_implicit}

# classmodel_Multiplicity class attributes and methods
classmodel_Multiplicity_lower: Property = Property(name="lower", type=StringType)
classmodel_Multiplicity_upper: Property = Property(name="upper", type=StringType)
classmodel_Multiplicity.attributes={classmodel_Multiplicity_lower, classmodel_Multiplicity_upper}

# classmodel_Aggregation class attributes and methods
classmodel_Aggregation_headLabel: Property = Property(name="headLabel", type=StringType)
classmodel_Aggregation_tailNavigable: Property = Property(name="tailNavigable", type=BooleanType)
classmodel_Aggregation_tailVisibility: Property = Property(name="tailVisibility", type=StringType)
classmodel_Aggregation_tailLabel: Property = Property(name="tailLabel", type=StringType)
classmodel_Aggregation_headNavigable: Property = Property(name="headNavigable", type=BooleanType)
classmodel_Aggregation_headVisibility: Property = Property(name="headVisibility", type=StringType)
classmodel_Aggregation.attributes={classmodel_Aggregation_headVisibility, classmodel_Aggregation_tailVisibility, classmodel_Aggregation_headLabel, classmodel_Aggregation_headNavigable, classmodel_Aggregation_tailLabel, classmodel_Aggregation_tailNavigable}

# classmodel_Array class attributes and methods

# classmodel_Reference class attributes and methods

# classmodel_Attribute class attributes and methods
classmodel_Attribute_implicit: Property = Property(name="implicit", type=StringType)
classmodel_Attribute_static: Property = Property(name="static", type=BooleanType)
classmodel_Attribute.attributes={classmodel_Attribute_implicit, classmodel_Attribute_static}

# Relationships
upperClass8: BinaryAssociation = BinaryAssociation(
    name="upperClass8",
    ends={
        Property(name="classmodel_Classifier9", type=classmodel_Type, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="classmodel_Type10", type=classmodel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
feature11: BinaryAssociation = BinaryAssociation(
    name="feature11",
    ends={
        Property(name="classmodel_Feature", type=classmodel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Classifier12", type=classmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name13: BinaryAssociation = BinaryAssociation(
    name="name13",
    ends={
        Property(name="classmodel_Entity", type=classmodel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Type14", type=classmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="classmodel_Import", type=classmodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Model", type=classmodel_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="classmodel_Element", type=classmodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Model2", type=classmodel_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation3: BinaryAssociation = BinaryAssociation(
    name="annotation3",
    ends={
        Property(name="classmodel_Annotation", type=classmodel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Element4", type=classmodel_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element5: BinaryAssociation = BinaryAssociation(
    name="element5",
    ends={
        Property(name="classmodel_Element6", type=classmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Package", type=classmodel_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization7: BinaryAssociation = BinaryAssociation(
    name="generalization7",
    ends={
        Property(name="classmodel_Type", type=classmodel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Classifier", type=classmodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperClass15: BinaryAssociation = BinaryAssociation(
    name="upperClass15",
    ends={
        Property(name="classmodel_Type16", type=classmodel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Enumeration", type=classmodel_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator17: BinaryAssociation = BinaryAssociation(
    name="enumerator17",
    ends={
        Property(name="classmodel_Feature19", type=classmodel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Enumeration18", type=classmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
head20: BinaryAssociation = BinaryAssociation(
    name="head20",
    ends={
        Property(name="classmodel_Entity21", type=classmodel_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Relationship", type=classmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
headMultiplicity29: BinaryAssociation = BinaryAssociation(
    name="headMultiplicity29",
    ends={
        Property(name="classmodel_Multiplicity30", type=classmodel_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Aggregation", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail22: BinaryAssociation = BinaryAssociation(
    name="tail22",
    ends={
        Property(name="classmodel_Entity24", type=classmodel_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Relationship23", type=classmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
tailMultiplicity31: BinaryAssociation = BinaryAssociation(
    name="tailMultiplicity31",
    ends={
        Property(name="classmodel_Multiplicity33", type=classmodel_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Aggregation32", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headMultiplicity34: BinaryAssociation = BinaryAssociation(
    name="headMultiplicity34",
    ends={
        Property(name="classmodel_Multiplicity35", type=classmodel_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Composition", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tailMultiplicity36: BinaryAssociation = BinaryAssociation(
    name="tailMultiplicity36",
    ends={
        Property(name="classmodel_Multiplicity38", type=classmodel_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Composition37", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter39: BinaryAssociation = BinaryAssociation(
    name="parameter39",
    ends={
        Property(name="classmodel_Parameter", type=classmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Operation", type=classmodel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headMultiplicity25: BinaryAssociation = BinaryAssociation(
    name="headMultiplicity25",
    ends={
        Property(name="classmodel_Multiplicity", type=classmodel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Association", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tailMultiplicity26: BinaryAssociation = BinaryAssociation(
    name="tailMultiplicity26",
    ends={
        Property(name="classmodel_Multiplicity28", type=classmodel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Association27", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="classmodel_Reference46", type=classmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Attribute", type=classmodel_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="classmodel_Entity49", type=classmodel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Reference48", type=classmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
array50: BinaryAssociation = BinaryAssociation(
    name="array50",
    ends={
        Property(name="classmodel_Array", type=classmodel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Reference51", type=classmodel_Array, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size52: BinaryAssociation = BinaryAssociation(
    name="size52",
    ends={
        Property(name="classmodel_Multiplicity54", type=classmodel_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Array53", type=classmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return40: BinaryAssociation = BinaryAssociation(
    name="return40",
    ends={
        Property(name="classmodel_Reference", type=classmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Operation41", type=classmodel_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="classmodel_Reference44", type=classmodel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="classmodel_Parameter43", type=classmodel_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_classmodel_Entity_Element = Generalization(general=Element, specific=classmodel_Entity)
gen_classmodel_Datatype_Entity = Generalization(general=Entity, specific=classmodel_Datatype)
gen_classmodel_Package_Element = Generalization(general=Element, specific=classmodel_Package)
gen_classmodel_Classifier_Entity = Generalization(general=Entity, specific=classmodel_Classifier)
gen_classmodel_Enumeration_Entity = Generalization(general=Entity, specific=classmodel_Enumeration)
gen_classmodel_Relationship_Element = Generalization(general=Element, specific=classmodel_Relationship)
gen_classmodel_Association_Relationship = Generalization(general=Relationship, specific=classmodel_Association)
gen_classmodel_Composition_Relationship = Generalization(general=Relationship, specific=classmodel_Composition)
gen_classmodel_Generalization_Relationship = Generalization(general=Relationship, specific=classmodel_Generalization)
gen_classmodel_Dependency_Relationship = Generalization(general=Relationship, specific=classmodel_Dependency)
gen_classmodel_Realization_Relationship = Generalization(general=Relationship, specific=classmodel_Realization)
gen_classmodel_Constant_Feature = Generalization(general=Feature, specific=classmodel_Constant)
gen_classmodel_Operation_Feature = Generalization(general=Feature, specific=classmodel_Operation)
gen_classmodel_Aggregation_Relationship = Generalization(general=Relationship, specific=classmodel_Aggregation)
gen_classmodel_Attribute_Feature = Generalization(general=Feature, specific=classmodel_Attribute)

# Domain Model
domain_model = DomainModel(
    name="classmodel",
    types={classmodel_Feature, classmodel_Model, classmodel_Import, classmodel_Element, classmodel_Annotation, classmodel_Entity, Element, classmodel_Datatype, Entity, classmodel_Package, classmodel_Classifier, classmodel_Type, classmodel_Enumeration, classmodel_Relationship, classmodel_Association, Relationship, classmodel_Composition, classmodel_Generalization, classmodel_Dependency, classmodel_Realization, classmodel_Constant, Feature, classmodel_Operation, classmodel_Parameter, classmodel_Multiplicity, classmodel_Aggregation, classmodel_Array, classmodel_Reference, classmodel_Attribute, Visibility},
    associations={upperClass8, feature11, name13, imports0, elements1, annotation3, element5, generalization7, upperClass15, enumerator17, head20, headMultiplicity29, tail22, tailMultiplicity31, headMultiplicity34, tailMultiplicity36, parameter39, headMultiplicity25, tailMultiplicity26, type45, type47, array50, size52, return40, type42},
    generalizations={gen_classmodel_Entity_Element, gen_classmodel_Datatype_Entity, gen_classmodel_Package_Element, gen_classmodel_Classifier_Entity, gen_classmodel_Enumeration_Entity, gen_classmodel_Relationship_Element, gen_classmodel_Association_Relationship, gen_classmodel_Composition_Relationship, gen_classmodel_Generalization_Relationship, gen_classmodel_Dependency_Relationship, gen_classmodel_Realization_Relationship, gen_classmodel_Constant_Feature, gen_classmodel_Operation_Feature, gen_classmodel_Aggregation_Relationship, gen_classmodel_Attribute_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
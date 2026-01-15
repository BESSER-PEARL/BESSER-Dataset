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
simpleuml_Model = Class(name="simpleuml::Model")
Package = Class(name="Package")
simpleuml_Package = Class(name="simpleuml::Package")
Classifier = Class(name="Classifier")
simpleuml_DataType = Class(name="simpleuml::DataType")
simpleuml_Association = Class(name="simpleuml::Association")
simpleuml_PrimitiveType = Class(name="simpleuml::PrimitiveType")
Type = Class(name="Type")
simpleuml_Enumeration = Class(name="simpleuml::Enumeration")
simpleuml_EnumerationLiteral = Class(name="simpleuml::EnumerationLiteral")
simpleuml_Classifier = Class(name="simpleuml::Classifier", is_abstract=True)
simpleuml_ModelElement = Class(name="simpleuml::ModelElement", is_abstract=True)
simpleuml_TaggedValue = Class(name="simpleuml::TaggedValue")
Packageable = Class(name="Packageable")
simpleuml_Packageable = Class(name="simpleuml::Packageable", is_abstract=True)
simpleuml_Class = Class(name="simpleuml::Class")
DataType = Class(name="DataType")
simpleuml_Generalization = Class(name="simpleuml::Generalization")
simpleuml_Property = Class(name="simpleuml::Property")
ModelElement = Class(name="ModelElement")
simpleuml_Type = Class(name="simpleuml::Type", is_abstract=True)

# simpleuml_Model class attributes and methods
simpleuml_Model_m_getCustomProperty: Method = Method(name="getCustomProperty", parameters={Parameter(name='name')}, type=StringType)
simpleuml_Model.methods={simpleuml_Model_m_getCustomProperty}

# Package class attributes and methods

# simpleuml_Package class attributes and methods

# Classifier class attributes and methods

# simpleuml_DataType class attributes and methods

# simpleuml_Association class attributes and methods

# simpleuml_PrimitiveType class attributes and methods

# Type class attributes and methods

# simpleuml_Enumeration class attributes and methods

# simpleuml_EnumerationLiteral class attributes and methods
simpleuml_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
simpleuml_EnumerationLiteral.attributes={simpleuml_EnumerationLiteral_name}

# simpleuml_Classifier class attributes and methods

# simpleuml_ModelElement class attributes and methods
simpleuml_ModelElement_name: Property = Property(name="name", type=StringType)
simpleuml_ModelElement_stereotype: Property = Property(name="stereotype", type=StringType)
simpleuml_ModelElement.attributes={simpleuml_ModelElement_name, simpleuml_ModelElement_stereotype}

# simpleuml_TaggedValue class attributes and methods
simpleuml_TaggedValue_name: Property = Property(name="name", type=StringType)
simpleuml_TaggedValue_value: Property = Property(name="value", type=StringType)
simpleuml_TaggedValue.attributes={simpleuml_TaggedValue_name, simpleuml_TaggedValue_value}

# Packageable class attributes and methods

# simpleuml_Packageable class attributes and methods

# simpleuml_Class class attributes and methods
simpleuml_Class_abstract: Property = Property(name="abstract", type=BooleanType)
simpleuml_Class.attributes={simpleuml_Class_abstract}

# DataType class attributes and methods

# simpleuml_Generalization class attributes and methods
simpleuml_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
simpleuml_Generalization.attributes={simpleuml_Generalization_isSubstitutable}

# simpleuml_Property class attributes and methods

# ModelElement class attributes and methods

# simpleuml_Type class attributes and methods

# Relationships
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="DataType", type=simpleuml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=simpleuml_DataType, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="simpleuml_Class5", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Association", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="simpleuml_Class8", type=simpleuml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Association7", type=simpleuml_Class, multiplicity=Multiplicity(1, 1))
    }
)
attributes9: BinaryAssociation = BinaryAssociation(
    name="attributes9",
    ends={
        Property(name="Property", type=simpleuml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="owner10", type=simpleuml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral11: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral11",
    ends={
        Property(name="simpleuml_EnumerationLiteral", type=simpleuml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Enumeration", type=simpleuml_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taggedValue12: BinaryAssociation = BinaryAssociation(
    name="taggedValue12",
    ends={
        Property(name="simpleuml_TaggedValue", type=simpleuml_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_ModelElement", type=simpleuml_TaggedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general13: BinaryAssociation = BinaryAssociation(
    name="general13",
    ends={
        Property(name="simpleuml_Class15", type=simpleuml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Generalization14", type=simpleuml_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements0: BinaryAssociation = BinaryAssociation(
    name="ownedElements0",
    ends={
        Property(name="Packageable", type=simpleuml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleuml_Packageable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizations1: BinaryAssociation = BinaryAssociation(
    name="generalizations1",
    ends={
        Property(name="simpleuml_Generalization", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Class", type=simpleuml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="simpleuml_Type", type=simpleuml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Property", type=simpleuml_Type, multiplicity=Multiplicity(1, 1))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Package", type=simpleuml_Packageable, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=simpleuml_Package, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleuml_Model_Package = Generalization(general=Package, specific=simpleuml_Model)
gen_simpleuml_Package_Classifier = Generalization(general=Classifier, specific=simpleuml_Package)
gen_simpleuml_Association_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Association)
gen_simpleuml_Association_Packageable = Generalization(general=Packageable, specific=simpleuml_Association)
gen_simpleuml_PrimitiveType_Type = Generalization(general=Type, specific=simpleuml_PrimitiveType)
gen_simpleuml_DataType_Type = Generalization(general=Type, specific=simpleuml_DataType)
gen_simpleuml_Enumeration_Type = Generalization(general=Type, specific=simpleuml_Enumeration)
gen_simpleuml_Classifier_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Classifier)
gen_simpleuml_Package_Packageable = Generalization(general=Packageable, specific=simpleuml_Package)
gen_simpleuml_Class_DataType = Generalization(general=DataType, specific=simpleuml_Class)
gen_simpleuml_Property_ModelElement = Generalization(general=ModelElement, specific=simpleuml_Property)
gen_simpleuml_Type_Classifier = Generalization(general=Classifier, specific=simpleuml_Type)
gen_simpleuml_Type_Packageable = Generalization(general=Packageable, specific=simpleuml_Type)

# Domain Model
domain_model = DomainModel(
    name="simpleuml",
    types={simpleuml_Model, Package, simpleuml_Package, Classifier, simpleuml_DataType, simpleuml_Association, simpleuml_PrimitiveType, Type, simpleuml_Enumeration, simpleuml_EnumerationLiteral, simpleuml_Classifier, simpleuml_ModelElement, simpleuml_TaggedValue, Packageable, simpleuml_Packageable, simpleuml_Class, DataType, simpleuml_Generalization, simpleuml_Property, ModelElement, simpleuml_Type},
    associations={owner3, source4, target6, attributes9, ownedLiteral11, taggedValue12, general13, ownedElements0, generalizations1, type2, owner16},
    generalizations={gen_simpleuml_Model_Package, gen_simpleuml_Package_Classifier, gen_simpleuml_Association_ModelElement, gen_simpleuml_Association_Packageable, gen_simpleuml_PrimitiveType_Type, gen_simpleuml_DataType_Type, gen_simpleuml_Enumeration_Type, gen_simpleuml_Classifier_ModelElement, gen_simpleuml_Package_Packageable, gen_simpleuml_Class_DataType, gen_simpleuml_Property_ModelElement, gen_simpleuml_Type_Classifier, gen_simpleuml_Type_Packageable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
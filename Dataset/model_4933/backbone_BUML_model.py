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
CardinalityKind: Enumeration = Enumeration(
    name="CardinalityKind",
    literals={
            EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="MANY")
    }
)

# Classes
backbone_Collection = Class(name="backbone::Collection")
backbone_Router = Class(name="backbone::Router")
backbone_View = Class(name="backbone::View")
backbone_NamedElement = Class(name="backbone::NamedElement", is_abstract=True)
backbone_Attribute = Class(name="backbone::Attribute")
backbone_Reference = Class(name="backbone::Reference")
backbone_Operation = Class(name="backbone::Operation")
backbone_Parameter = Class(name="backbone::Parameter")
backbone_Application = Class(name="backbone::Application")
NamedElement = Class(name="NamedElement")
backbone_Model = Class(name="backbone::Model")
backbone_RouterMapping = Class(name="backbone::RouterMapping")

# backbone_Collection class attributes and methods

# backbone_Router class attributes and methods

# backbone_View class attributes and methods

# backbone_NamedElement class attributes and methods
backbone_NamedElement_name: Property = Property(name="name", type=StringType)
backbone_NamedElement.attributes={backbone_NamedElement_name}

# backbone_Attribute class attributes and methods
backbone_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
backbone_Attribute_cardinality: Property = Property(name="cardinality", type=StringType)
backbone_Attribute.attributes={backbone_Attribute_cardinality, backbone_Attribute_defaultValue}

# backbone_Reference class attributes and methods
backbone_Reference_cardinality: Property = Property(name="cardinality", type=StringType)
backbone_Reference.attributes={backbone_Reference_cardinality}

# backbone_Operation class attributes and methods

# backbone_Parameter class attributes and methods

# backbone_Application class attributes and methods

# NamedElement class attributes and methods

# backbone_Model class attributes and methods

# backbone_RouterMapping class attributes and methods
backbone_RouterMapping_path: Property = Property(name="path", type=StringType)
backbone_RouterMapping.attributes={backbone_RouterMapping_path}

# Relationships
models0: BinaryAssociation = BinaryAssociation(
    name="models0",
    ends={
        Property(name="application", type=backbone_Model, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Model", type=backbone_Application, multiplicity=Multiplicity(1, 1))
    }
)
collections1: BinaryAssociation = BinaryAssociation(
    name="collections1",
    ends={
        Property(name="Collection", type=backbone_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application2", type=backbone_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
router3: BinaryAssociation = BinaryAssociation(
    name="router3",
    ends={
        Property(name="Router", type=backbone_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application4", type=backbone_Router, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
views5: BinaryAssociation = BinaryAssociation(
    name="views5",
    ends={
        Property(name="View", type=backbone_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application6", type=backbone_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="backbone_Attribute", type=backbone_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Model", type=backbone_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references8: BinaryAssociation = BinaryAssociation(
    name="references8",
    ends={
        Property(name="backbone_Reference", type=backbone_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Model9", type=backbone_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations10: BinaryAssociation = BinaryAssociation(
    name="operations10",
    ends={
        Property(name="backbone_Operation", type=backbone_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Model11", type=backbone_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application12: BinaryAssociation = BinaryAssociation(
    name="application12",
    ends={
        Property(name="Application", type=backbone_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=backbone_Application, multiplicity=Multiplicity(1, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="backbone_Model15", type=backbone_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Reference14", type=backbone_Model, multiplicity=Multiplicity(1, 1))
    }
)
model18: BinaryAssociation = BinaryAssociation(
    name="model18",
    ends={
        Property(name="backbone_Model19", type=backbone_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Collection", type=backbone_Model, multiplicity=Multiplicity(0, 1))
    }
)
application20: BinaryAssociation = BinaryAssociation(
    name="application20",
    ends={
        Property(name="Application21", type=backbone_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="collections", type=backbone_Application, multiplicity=Multiplicity(1, 1))
    }
)
mappings22: BinaryAssociation = BinaryAssociation(
    name="mappings22",
    ends={
        Property(name="backbone_RouterMapping", type=backbone_Router, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Router", type=backbone_RouterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application23: BinaryAssociation = BinaryAssociation(
    name="application23",
    ends={
        Property(name="Application24", type=backbone_Router, multiplicity=Multiplicity(1, 1)),
        Property(name="router", type=backbone_Application, multiplicity=Multiplicity(1, 1))
    }
)
view25: BinaryAssociation = BinaryAssociation(
    name="view25",
    ends={
        Property(name="backbone_View", type=backbone_RouterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_RouterMapping26", type=backbone_View, multiplicity=Multiplicity(1, 1))
    }
)
operations27: BinaryAssociation = BinaryAssociation(
    name="operations27",
    ends={
        Property(name="backbone_Operation29", type=backbone_View, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_View28", type=backbone_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
application30: BinaryAssociation = BinaryAssociation(
    name="application30",
    ends={
        Property(name="Application31", type=backbone_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=backbone_Application, multiplicity=Multiplicity(1, 1))
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="backbone_Parameter", type=backbone_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="backbone_Operation17", type=backbone_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_backbone_Model_NamedElement = Generalization(general=NamedElement, specific=backbone_Model)
gen_backbone_Attribute_NamedElement = Generalization(general=NamedElement, specific=backbone_Attribute)
gen_backbone_Reference_NamedElement = Generalization(general=NamedElement, specific=backbone_Reference)
gen_backbone_Operation_NamedElement = Generalization(general=NamedElement, specific=backbone_Operation)
gen_backbone_Application_NamedElement = Generalization(general=NamedElement, specific=backbone_Application)
gen_backbone_Router_NamedElement = Generalization(general=NamedElement, specific=backbone_Router)
gen_backbone_View_NamedElement = Generalization(general=NamedElement, specific=backbone_View)
gen_backbone_Parameter_NamedElement = Generalization(general=NamedElement, specific=backbone_Parameter)
gen_backbone_Collection_NamedElement = Generalization(general=NamedElement, specific=backbone_Collection)

# Domain Model
domain_model = DomainModel(
    name="backbone",
    types={backbone_Collection, backbone_Router, backbone_View, backbone_NamedElement, backbone_Attribute, backbone_Reference, backbone_Operation, backbone_Parameter, backbone_Application, NamedElement, backbone_Model, backbone_RouterMapping, CardinalityKind},
    associations={models0, collections1, router3, views5, attributes7, references8, operations10, application12, type13, model18, application20, mappings22, application23, view25, operations27, application30, parameters16},
    generalizations={gen_backbone_Model_NamedElement, gen_backbone_Attribute_NamedElement, gen_backbone_Reference_NamedElement, gen_backbone_Operation_NamedElement, gen_backbone_Application_NamedElement, gen_backbone_Router_NamedElement, gen_backbone_View_NamedElement, gen_backbone_Parameter_NamedElement, gen_backbone_Collection_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
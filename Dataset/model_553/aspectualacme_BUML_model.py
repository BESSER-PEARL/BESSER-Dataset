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
GlueType: Enumeration = Enumeration(
    name="GlueType",
    literals={
            EnumerationLiteral(name="before"),
			EnumerationLiteral(name="around"),
			EnumerationLiteral(name="after")
    }
)

ArmaniTypes: Enumeration = Enumeration(
    name="ArmaniTypes",
    literals={
            EnumerationLiteral(name="Component"),
			EnumerationLiteral(name="Connector"),
			EnumerationLiteral(name="Role"),
			EnumerationLiteral(name="Port"),
			EnumerationLiteral(name="Representation"),
			EnumerationLiteral(name="Property")
    }
)

ArmaniSetTypes: Enumeration = Enumeration(
    name="ArmaniSetTypes",
    literals={
            EnumerationLiteral(name="Ports"),
			EnumerationLiteral(name="Representations"),
			EnumerationLiteral(name="Properties"),
			EnumerationLiteral(name="Elements"),
			EnumerationLiteral(name="Components"),
			EnumerationLiteral(name="Connectors"),
			EnumerationLiteral(name="Roles")
    }
)

ArmaniQuantifier: Enumeration = Enumeration(
    name="ArmaniQuantifier",
    literals={
            EnumerationLiteral(name="forall"),
			EnumerationLiteral(name="exists")
    }
)

# Classes
aspectualacme_Root = Class(name="aspectualacme::Root")
aspectualacme_Import = Class(name="aspectualacme::Import")
aspectualacme_attachableElement = Class(name="aspectualacme::attachableElement", is_abstract=True)
Element = Class(name="Element")
aspectualacme_Armani = Class(name="aspectualacme::Armani")
aspectualacme_Family = Class(name="aspectualacme::Family")
aspectualacme_BasicElement = Class(name="aspectualacme::BasicElement", is_abstract=True)
aspectualacme_Element = Class(name="aspectualacme::Element")
aspectualacme_Property = Class(name="aspectualacme::Property")
aspectualacme_Representation = Class(name="aspectualacme::Representation")
aspectualacme_ComponentType = Class(name="aspectualacme::ComponentType")
aspectualacme_PortType = Class(name="aspectualacme::PortType")
aspectualacme_ConnectorType = Class(name="aspectualacme::ConnectorType")
aspectualacme_RoleType = Class(name="aspectualacme::RoleType")
BasicElement = Class(name="BasicElement")
aspectualacme_Connector = Class(name="aspectualacme::Connector")
aspectualacme_Component = Class(name="aspectualacme::Component")
aspectualacme_Attachment = Class(name="aspectualacme::Attachment")
aspectualacme_WildCard = Class(name="aspectualacme::WildCard")
aspectualacme_PropertyType = Class(name="aspectualacme::PropertyType")
TypeDefinition = Class(name="TypeDefinition")
aspectualacme_Port = Class(name="aspectualacme::Port")
aspectualacme_Role = Class(name="aspectualacme::Role")
aspectualacme_Glue = Class(name="aspectualacme::Glue")
aspectualacme_System = Class(name="aspectualacme::System")
aspectualacme_BaseRole = Class(name="aspectualacme::BaseRole")
Role = Class(name="Role")
aspectualacme_CrosscuttingRole = Class(name="aspectualacme::CrosscuttingRole")
attachableElement = Class(name="attachableElement")
BindableElement = Class(name="BindableElement")
aspectualacme_Binding = Class(name="aspectualacme::Binding")
aspectualacme_BindableElement = Class(name="aspectualacme::BindableElement")
aspectualacme_ArmaniPrimitiveExpression = Class(name="aspectualacme::ArmaniPrimitiveExpression")
aspectualacme_ArmaniSetExpression = Class(name="aspectualacme::ArmaniSetExpression")
aspectualacme_ArmaniConstant = Class(name="aspectualacme::ArmaniConstant")
aspectualacme_TypeDefinition = Class(name="aspectualacme::TypeDefinition")
aspectualacme_ArmaniDesignRuleExpression = Class(name="aspectualacme::ArmaniDesignRuleExpression", is_abstract=True)
aspectualacme_ArmaniExpression = Class(name="aspectualacme::ArmaniExpression")
aspectualacme_ArmaniFunctionCall = Class(name="aspectualacme::ArmaniFunctionCall")
ArmaniPrimitiveExpression = Class(name="ArmaniPrimitiveExpression")
aspectualacme_ArmaniMultiplicativeExpression = Class(name="aspectualacme::ArmaniMultiplicativeExpression")
ArmaniUnaryExpression = Class(name="ArmaniUnaryExpression")
aspectualacme_ArmaniUnaryExpression = Class(name="aspectualacme::ArmaniUnaryExpression")
ArmaniExpression = Class(name="ArmaniExpression")
aspectualacme_ArmaniEqualityExpression = Class(name="aspectualacme::ArmaniEqualityExpression")
aspectualacme_ArmaniIffExpression = Class(name="aspectualacme::ArmaniIffExpression")
aspectualacme_ArmaniAdditiveExpression = Class(name="aspectualacme::ArmaniAdditiveExpression")
aspectualacme_ArmaniRelationalExpression = Class(name="aspectualacme::ArmaniRelationalExpression")
aspectualacme_ArmaniBooleanExpression = Class(name="aspectualacme::ArmaniBooleanExpression")
ArmaniDesignRuleExpression = Class(name="ArmaniDesignRuleExpression")
aspectualacme_ArmaniQuantifiedExpression = Class(name="aspectualacme::ArmaniQuantifiedExpression")
aspectualacme_ArmaniImpliesExpression = Class(name="aspectualacme::ArmaniImpliesExpression")
aspectualacme_ArmaniOrExpression = Class(name="aspectualacme::ArmaniOrExpression")
aspectualacme_ArmaniVariable = Class(name="aspectualacme::ArmaniVariable")

# aspectualacme_Root class attributes and methods

# aspectualacme_Import class attributes and methods
aspectualacme_Import_fileName: Property = Property(name="fileName", type=StringType)
aspectualacme_Import.attributes={aspectualacme_Import_fileName}

# aspectualacme_attachableElement class attributes and methods

# Element class attributes and methods

# aspectualacme_Armani class attributes and methods
aspectualacme_Armani_modifiers: Property = Property(name="modifiers", type=StringType)
aspectualacme_Armani.attributes={aspectualacme_Armani_modifiers}

# aspectualacme_Family class attributes and methods

# aspectualacme_BasicElement class attributes and methods

# aspectualacme_Element class attributes and methods
aspectualacme_Element_name: Property = Property(name="name", type=StringType)
aspectualacme_Element.attributes={aspectualacme_Element_name}

# aspectualacme_Property class attributes and methods
aspectualacme_Property_name: Property = Property(name="name", type=StringType)
aspectualacme_Property_value: Property = Property(name="value", type=StringType)
aspectualacme_Property.attributes={aspectualacme_Property_value, aspectualacme_Property_name}

# aspectualacme_Representation class attributes and methods
aspectualacme_Representation_name: Property = Property(name="name", type=StringType)
aspectualacme_Representation.attributes={aspectualacme_Representation_name}

# aspectualacme_ComponentType class attributes and methods

# aspectualacme_PortType class attributes and methods

# aspectualacme_ConnectorType class attributes and methods

# aspectualacme_RoleType class attributes and methods

# BasicElement class attributes and methods

# aspectualacme_Connector class attributes and methods

# aspectualacme_Component class attributes and methods

# aspectualacme_Attachment class attributes and methods

# aspectualacme_WildCard class attributes and methods
aspectualacme_WildCard_expression: Property = Property(name="expression", type=StringType)
aspectualacme_WildCard.attributes={aspectualacme_WildCard_expression}

# aspectualacme_PropertyType class attributes and methods
aspectualacme_PropertyType_type: Property = Property(name="type", type=StringType)
aspectualacme_PropertyType_values: Property = Property(name="values", type=StringType)
aspectualacme_PropertyType.attributes={aspectualacme_PropertyType_type, aspectualacme_PropertyType_values}

# TypeDefinition class attributes and methods

# aspectualacme_Port class attributes and methods

# aspectualacme_Role class attributes and methods

# aspectualacme_Glue class attributes and methods
aspectualacme_Glue_glueType: Property = Property(name="glueType", type=StringType)
aspectualacme_Glue.attributes={aspectualacme_Glue_glueType}

# aspectualacme_System class attributes and methods

# aspectualacme_BaseRole class attributes and methods

# Role class attributes and methods

# aspectualacme_CrosscuttingRole class attributes and methods

# attachableElement class attributes and methods

# BindableElement class attributes and methods

# aspectualacme_Binding class attributes and methods

# aspectualacme_BindableElement class attributes and methods

# aspectualacme_ArmaniPrimitiveExpression class attributes and methods

# aspectualacme_ArmaniSetExpression class attributes and methods
aspectualacme_ArmaniSetExpression_reference: Property = Property(name="reference", type=StringType)
aspectualacme_ArmaniSetExpression_referenceType: Property = Property(name="referenceType", type=StringType)
aspectualacme_ArmaniSetExpression.attributes={aspectualacme_ArmaniSetExpression_referenceType, aspectualacme_ArmaniSetExpression_reference}

# aspectualacme_ArmaniConstant class attributes and methods

# aspectualacme_TypeDefinition class attributes and methods

# aspectualacme_ArmaniDesignRuleExpression class attributes and methods

# aspectualacme_ArmaniExpression class attributes and methods

# aspectualacme_ArmaniFunctionCall class attributes and methods
aspectualacme_ArmaniFunctionCall_functionId: Property = Property(name="functionId", type=StringType)
aspectualacme_ArmaniFunctionCall.attributes={aspectualacme_ArmaniFunctionCall_functionId}

# ArmaniPrimitiveExpression class attributes and methods

# aspectualacme_ArmaniMultiplicativeExpression class attributes and methods
aspectualacme_ArmaniMultiplicativeExpression_operators: Property = Property(name="operators", type=StringType)
aspectualacme_ArmaniMultiplicativeExpression.attributes={aspectualacme_ArmaniMultiplicativeExpression_operators}

# ArmaniUnaryExpression class attributes and methods

# aspectualacme_ArmaniUnaryExpression class attributes and methods
aspectualacme_ArmaniUnaryExpression_operator: Property = Property(name="operator", type=StringType)
aspectualacme_ArmaniUnaryExpression.attributes={aspectualacme_ArmaniUnaryExpression_operator}

# ArmaniExpression class attributes and methods

# aspectualacme_ArmaniEqualityExpression class attributes and methods
aspectualacme_ArmaniEqualityExpression_operators: Property = Property(name="operators", type=StringType)
aspectualacme_ArmaniEqualityExpression.attributes={aspectualacme_ArmaniEqualityExpression_operators}

# aspectualacme_ArmaniIffExpression class attributes and methods

# aspectualacme_ArmaniAdditiveExpression class attributes and methods
aspectualacme_ArmaniAdditiveExpression_operators: Property = Property(name="operators", type=StringType)
aspectualacme_ArmaniAdditiveExpression.attributes={aspectualacme_ArmaniAdditiveExpression_operators}

# aspectualacme_ArmaniRelationalExpression class attributes and methods
aspectualacme_ArmaniRelationalExpression_operators: Property = Property(name="operators", type=StringType)
aspectualacme_ArmaniRelationalExpression.attributes={aspectualacme_ArmaniRelationalExpression_operators}

# aspectualacme_ArmaniBooleanExpression class attributes and methods

# ArmaniDesignRuleExpression class attributes and methods

# aspectualacme_ArmaniQuantifiedExpression class attributes and methods
aspectualacme_ArmaniQuantifiedExpression_quantifier: Property = Property(name="quantifier", type=StringType)
aspectualacme_ArmaniQuantifiedExpression.attributes={aspectualacme_ArmaniQuantifiedExpression_quantifier}

# aspectualacme_ArmaniImpliesExpression class attributes and methods

# aspectualacme_ArmaniOrExpression class attributes and methods
aspectualacme_ArmaniOrExpression_operators: Property = Property(name="operators", type=StringType)
aspectualacme_ArmaniOrExpression.attributes={aspectualacme_ArmaniOrExpression_operators}

# aspectualacme_ArmaniVariable class attributes and methods
aspectualacme_ArmaniVariable_basicType: Property = Property(name="basicType", type=StringType)
aspectualacme_ArmaniVariable_id: Property = Property(name="id", type=StringType)
aspectualacme_ArmaniVariable.attributes={aspectualacme_ArmaniVariable_basicType, aspectualacme_ArmaniVariable_id}

# Relationships
armani5: BinaryAssociation = BinaryAssociation(
    name="armani5",
    ends={
        Property(name="aspectualacme_Armani", type=aspectualacme_BasicElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_BasicElement6", type=aspectualacme_Armani, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentFamily7: BinaryAssociation = BinaryAssociation(
    name="parentFamily7",
    ends={
        Property(name="aspectualacme_Family", type=aspectualacme_BasicElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_BasicElement8", type=aspectualacme_Family, multiplicity=Multiplicity(0, 9999))
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="aspectualacme_Import", type=aspectualacme_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Root", type=aspectualacme_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="aspectualacme_BasicElement", type=aspectualacme_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Root2", type=aspectualacme_BasicElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
property3: BinaryAssociation = BinaryAssociation(
    name="property3",
    ends={
        Property(name="aspectualacme_Property", type=aspectualacme_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Element", type=aspectualacme_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representations4: BinaryAssociation = BinaryAssociation(
    name="representations4",
    ends={
        Property(name="Representation", type=aspectualacme_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=aspectualacme_Representation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctypes16: BinaryAssociation = BinaryAssociation(
    name="ctypes16",
    ends={
        Property(name="ComponentType", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily17", type=aspectualacme_ComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ptypes18: BinaryAssociation = BinaryAssociation(
    name="ptypes18",
    ends={
        Property(name="PortType", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily19", type=aspectualacme_PortType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cntypes20: BinaryAssociation = BinaryAssociation(
    name="cntypes20",
    ends={
        Property(name="ConnectorType", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily21", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors9: BinaryAssociation = BinaryAssociation(
    name="connectors9",
    ends={
        Property(name="Connector", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily", type=aspectualacme_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components10: BinaryAssociation = BinaryAssociation(
    name="components10",
    ends={
        Property(name="Component", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily11", type=aspectualacme_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachments12: BinaryAssociation = BinaryAssociation(
    name="attachments12",
    ends={
        Property(name="Attachment", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily13", type=aspectualacme_Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wildcard14: BinaryAssociation = BinaryAssociation(
    name="wildcard14",
    ends={
        Property(name="aspectualacme_WildCard", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Family15", type=aspectualacme_WildCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentFamily31: BinaryAssociation = BinaryAssociation(
    name="parentFamily31",
    ends={
        Property(name="Family", type=aspectualacme_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="ctypes", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
parentType33: BinaryAssociation = BinaryAssociation(
    name="parentType33",
    ends={
        Property(name="aspectualacme_RoleType", type=aspectualacme_RoleType, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_RoleType32", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999))
    }
)
parentFamily34: BinaryAssociation = BinaryAssociation(
    name="parentFamily34",
    ends={
        Property(name="Family35", type=aspectualacme_RoleType, multiplicity=Multiplicity(1, 1)),
        Property(name="rtypes", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
rtypes22: BinaryAssociation = BinaryAssociation(
    name="rtypes22",
    ends={
        Property(name="RoleType", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily23", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prtypes24: BinaryAssociation = BinaryAssociation(
    name="prtypes24",
    ends={
        Property(name="PropertyType", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily25", type=aspectualacme_PropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties26: BinaryAssociation = BinaryAssociation(
    name="properties26",
    ends={
        Property(name="Property", type=aspectualacme_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFamily27", type=aspectualacme_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port28: BinaryAssociation = BinaryAssociation(
    name="port28",
    ends={
        Property(name="Port", type=aspectualacme_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentT", type=aspectualacme_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentType30: BinaryAssociation = BinaryAssociation(
    name="parentType30",
    ends={
        Property(name="aspectualacme_ComponentType", type=aspectualacme_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ComponentType29", type=aspectualacme_ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
parentType37: BinaryAssociation = BinaryAssociation(
    name="parentType37",
    ends={
        Property(name="aspectualacme_PortType", type=aspectualacme_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_PortType36", type=aspectualacme_PortType, multiplicity=Multiplicity(0, 9999))
    }
)
parentFamily38: BinaryAssociation = BinaryAssociation(
    name="parentFamily38",
    ends={
        Property(name="Family39", type=aspectualacme_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="ptypes", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
parentFamily45: BinaryAssociation = BinaryAssociation(
    name="parentFamily45",
    ends={
        Property(name="Family46", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="cntypes", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
parentFamily47: BinaryAssociation = BinaryAssociation(
    name="parentFamily47",
    ends={
        Property(name="Family48", type=aspectualacme_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="prtypes", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
parentType41: BinaryAssociation = BinaryAssociation(
    name="parentType41",
    ends={
        Property(name="aspectualacme_ConnectorType", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ConnectorType40", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(0, 9999))
    }
)
role42: BinaryAssociation = BinaryAssociation(
    name="role42",
    ends={
        Property(name="Role", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="ConnectorT", type=aspectualacme_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
glue43: BinaryAssociation = BinaryAssociation(
    name="glue43",
    ends={
        Property(name="aspectualacme_Glue", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ConnectorType44", type=aspectualacme_Glue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentRepresentation62: BinaryAssociation = BinaryAssociation(
    name="parentRepresentation62",
    ends={
        Property(name="Representation63", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=aspectualacme_Representation, multiplicity=Multiplicity(0, 1))
    }
)
effective_type64: BinaryAssociation = BinaryAssociation(
    name="effective_type64",
    ends={
        Property(name="aspectualacme_Family66", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_System65", type=aspectualacme_Family, multiplicity=Multiplicity(0, 9999))
    }
)
port67: BinaryAssociation = BinaryAssociation(
    name="port67",
    ends={
        Property(name="Port69", type=aspectualacme_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Component68", type=aspectualacme_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors49: BinaryAssociation = BinaryAssociation(
    name="connectors49",
    ends={
        Property(name="Connector50", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem", type=aspectualacme_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties51: BinaryAssociation = BinaryAssociation(
    name="properties51",
    ends={
        Property(name="Property53", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem52", type=aspectualacme_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachments54: BinaryAssociation = BinaryAssociation(
    name="attachments54",
    ends={
        Property(name="Attachment56", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem55", type=aspectualacme_Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wildCard57: BinaryAssociation = BinaryAssociation(
    name="wildCard57",
    ends={
        Property(name="aspectualacme_WildCard58", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_System", type=aspectualacme_WildCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components59: BinaryAssociation = BinaryAssociation(
    name="components59",
    ends={
        Property(name="Component61", type=aspectualacme_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem60", type=aspectualacme_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role79: BinaryAssociation = BinaryAssociation(
    name="role79",
    ends={
        Property(name="Connector80", type=aspectualacme_Role, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Role81", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1))
    }
)
glue82: BinaryAssociation = BinaryAssociation(
    name="glue82",
    ends={
        Property(name="Glue", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connector", type=aspectualacme_Glue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="aspectualacme_ConnectorType84", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Connector", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(0, 9999))
    }
)
parentSystem85: BinaryAssociation = BinaryAssociation(
    name="parentSystem85",
    ends={
        Property(name="System86", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors", type=aspectualacme_System, multiplicity=Multiplicity(0, 1))
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="aspectualacme_ComponentType71", type=aspectualacme_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Component", type=aspectualacme_ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
parentSystem72: BinaryAssociation = BinaryAssociation(
    name="parentSystem72",
    ends={
        Property(name="System", type=aspectualacme_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=aspectualacme_System, multiplicity=Multiplicity(0, 1))
    }
)
parentFamily73: BinaryAssociation = BinaryAssociation(
    name="parentFamily73",
    ends={
        Property(name="Family75", type=aspectualacme_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="components74", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
effective_type76: BinaryAssociation = BinaryAssociation(
    name="effective_type76",
    ends={
        Property(name="aspectualacme_ComponentType78", type=aspectualacme_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Component77", type=aspectualacme_ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
roleType98: BinaryAssociation = BinaryAssociation(
    name="roleType98",
    ends={
        Property(name="aspectualacme_Role", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999)),
        Property(name="aspectualacme_RoleType99", type=aspectualacme_Role, multiplicity=Multiplicity(1, 1))
    }
)
effective_type100: BinaryAssociation = BinaryAssociation(
    name="effective_type100",
    ends={
        Property(name="aspectualacme_RoleType102", type=aspectualacme_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Role101", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999))
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="aspectualacme_RoleType104", type=aspectualacme_BaseRole, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_BaseRole", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999))
    }
)
parentFamily87: BinaryAssociation = BinaryAssociation(
    name="parentFamily87",
    ends={
        Property(name="Family89", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors88", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
effective_type90: BinaryAssociation = BinaryAssociation(
    name="effective_type90",
    ends={
        Property(name="aspectualacme_ConnectorType92", type=aspectualacme_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Connector91", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(0, 9999))
    }
)
Connector93: BinaryAssociation = BinaryAssociation(
    name="Connector93",
    ends={
        Property(name="Connector94", type=aspectualacme_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=aspectualacme_Connector, multiplicity=Multiplicity(0, 1))
    }
)
ConnectorT95: BinaryAssociation = BinaryAssociation(
    name="ConnectorT95",
    ends={
        Property(name="ConnectorType97", type=aspectualacme_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="role96", type=aspectualacme_ConnectorType, multiplicity=Multiplicity(0, 1))
    }
)
type117: BinaryAssociation = BinaryAssociation(
    name="type117",
    ends={
        Property(name="aspectualacme_PropertyType", type=aspectualacme_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Property118", type=aspectualacme_PropertyType, multiplicity=Multiplicity(0, 9999))
    }
)
parentSystem119: BinaryAssociation = BinaryAssociation(
    name="parentSystem119",
    ends={
        Property(name="System120", type=aspectualacme_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="properties", type=aspectualacme_System, multiplicity=Multiplicity(0, 1))
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="aspectualacme_RoleType106", type=aspectualacme_CrosscuttingRole, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_CrosscuttingRole", type=aspectualacme_RoleType, multiplicity=Multiplicity(0, 9999))
    }
)
portType107: BinaryAssociation = BinaryAssociation(
    name="portType107",
    ends={
        Property(name="aspectualacme_PortType108", type=aspectualacme_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Port", type=aspectualacme_PortType, multiplicity=Multiplicity(0, 9999))
    }
)
Component109: BinaryAssociation = BinaryAssociation(
    name="Component109",
    ends={
        Property(name="Component110", type=aspectualacme_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=aspectualacme_Component, multiplicity=Multiplicity(0, 1))
    }
)
ComponentT111: BinaryAssociation = BinaryAssociation(
    name="ComponentT111",
    ends={
        Property(name="ComponentType113", type=aspectualacme_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port112", type=aspectualacme_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
effective_type114: BinaryAssociation = BinaryAssociation(
    name="effective_type114",
    ends={
        Property(name="aspectualacme_PortType116", type=aspectualacme_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Port115", type=aspectualacme_PortType, multiplicity=Multiplicity(0, 9999))
    }
)
firstElement132: BinaryAssociation = BinaryAssociation(
    name="firstElement132",
    ends={
        Property(name="aspectualacme_attachableElement", type=aspectualacme_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Attachment", type=aspectualacme_attachableElement, multiplicity=Multiplicity(1, 1))
    }
)
secondElement133: BinaryAssociation = BinaryAssociation(
    name="secondElement133",
    ends={
        Property(name="aspectualacme_attachableElement135", type=aspectualacme_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Attachment134", type=aspectualacme_attachableElement, multiplicity=Multiplicity(1, 1))
    }
)
parentSystem136: BinaryAssociation = BinaryAssociation(
    name="parentSystem136",
    ends={
        Property(name="System137", type=aspectualacme_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="attachments", type=aspectualacme_System, multiplicity=Multiplicity(0, 1))
    }
)
parentFamily138: BinaryAssociation = BinaryAssociation(
    name="parentFamily138",
    ends={
        Property(name="Family140", type=aspectualacme_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="attachments139", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
parentFamily121: BinaryAssociation = BinaryAssociation(
    name="parentFamily121",
    ends={
        Property(name="Family123", type=aspectualacme_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="properties122", type=aspectualacme_Family, multiplicity=Multiplicity(0, 1))
    }
)
baseAttach124: BinaryAssociation = BinaryAssociation(
    name="baseAttach124",
    ends={
        Property(name="aspectualacme_BaseRole126", type=aspectualacme_Glue, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Glue125", type=aspectualacme_BaseRole, multiplicity=Multiplicity(0, 1))
    }
)
crosscuttingAttach127: BinaryAssociation = BinaryAssociation(
    name="crosscuttingAttach127",
    ends={
        Property(name="aspectualacme_CrosscuttingRole129", type=aspectualacme_Glue, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Glue128", type=aspectualacme_CrosscuttingRole, multiplicity=Multiplicity(0, 1))
    }
)
connector130: BinaryAssociation = BinaryAssociation(
    name="connector130",
    ends={
        Property(name="Connector131", type=aspectualacme_Glue, multiplicity=Multiplicity(1, 1)),
        Property(name="glue", type=aspectualacme_Connector, multiplicity=Multiplicity(0, 1))
    }
)
system150: BinaryAssociation = BinaryAssociation(
    name="system150",
    ends={
        Property(name="System151", type=aspectualacme_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="parentRepresentation", type=aspectualacme_System, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindings152: BinaryAssociation = BinaryAssociation(
    name="bindings152",
    ends={
        Property(name="Binding", type=aspectualacme_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="representation", type=aspectualacme_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element153: BinaryAssociation = BinaryAssociation(
    name="element153",
    ends={
        Property(name="Element", type=aspectualacme_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="representations", type=aspectualacme_Element, multiplicity=Multiplicity(1, 1))
    }
)
property141: BinaryAssociation = BinaryAssociation(
    name="property141",
    ends={
        Property(name="aspectualacme_Property142", type=aspectualacme_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Binding", type=aspectualacme_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstPort143: BinaryAssociation = BinaryAssociation(
    name="firstPort143",
    ends={
        Property(name="aspectualacme_BindableElement", type=aspectualacme_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Binding144", type=aspectualacme_BindableElement, multiplicity=Multiplicity(1, 1))
    }
)
secondPort145: BinaryAssociation = BinaryAssociation(
    name="secondPort145",
    ends={
        Property(name="aspectualacme_BindableElement147", type=aspectualacme_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Binding146", type=aspectualacme_BindableElement, multiplicity=Multiplicity(1, 1))
    }
)
representation148: BinaryAssociation = BinaryAssociation(
    name="representation148",
    ends={
        Property(name="Representation149", type=aspectualacme_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=aspectualacme_Representation, multiplicity=Multiplicity(0, 1))
    }
)
parameters156: BinaryAssociation = BinaryAssociation(
    name="parameters156",
    ends={
        Property(name="aspectualacme_ArmaniPrimitiveExpression", type=aspectualacme_ArmaniFunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniFunctionCall", type=aspectualacme_ArmaniPrimitiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setValues157: BinaryAssociation = BinaryAssociation(
    name="setValues157",
    ends={
        Property(name="aspectualacme_ArmaniConstant", type=aspectualacme_ArmaniSetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniSetExpression", type=aspectualacme_ArmaniConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
designRule154: BinaryAssociation = BinaryAssociation(
    name="designRule154",
    ends={
        Property(name="aspectualacme_ArmaniDesignRuleExpression", type=aspectualacme_Armani, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_Armani155", type=aspectualacme_ArmaniDesignRuleExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
designRule158: BinaryAssociation = BinaryAssociation(
    name="designRule158",
    ends={
        Property(name="aspectualacme_ArmaniDesignRuleExpression160", type=aspectualacme_ArmaniPrimitiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniPrimitiveExpression159", type=aspectualacme_ArmaniDesignRuleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression162: BinaryAssociation = BinaryAssociation(
    name="unaryExpression162",
    ends={
        Property(name="aspectualacme_ArmaniUnaryExpression", type=aspectualacme_ArmaniUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniUnaryExpression161", type=aspectualacme_ArmaniUnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions169: BinaryAssociation = BinaryAssociation(
    name="expressions169",
    ends={
        Property(name="aspectualacme_ArmaniRelationalExpression170", type=aspectualacme_ArmaniEqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniEqualityExpression", type=aspectualacme_ArmaniRelationalExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions163: BinaryAssociation = BinaryAssociation(
    name="expressions163",
    ends={
        Property(name="aspectualacme_ArmaniUnaryExpression164", type=aspectualacme_ArmaniMultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniMultiplicativeExpression", type=aspectualacme_ArmaniUnaryExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions165: BinaryAssociation = BinaryAssociation(
    name="expressions165",
    ends={
        Property(name="aspectualacme_ArmaniMultiplicativeExpression166", type=aspectualacme_ArmaniAdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniAdditiveExpression", type=aspectualacme_ArmaniMultiplicativeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions167: BinaryAssociation = BinaryAssociation(
    name="expressions167",
    ends={
        Property(name="aspectualacme_ArmaniAdditiveExpression168", type=aspectualacme_ArmaniRelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniRelationalExpression", type=aspectualacme_ArmaniAdditiveExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
userType177: BinaryAssociation = BinaryAssociation(
    name="userType177",
    ends={
        Property(name="aspectualacme_TypeDefinition", type=aspectualacme_ArmaniVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniVariable", type=aspectualacme_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expressions178: BinaryAssociation = BinaryAssociation(
    name="expressions178",
    ends={
        Property(name="aspectualacme_ArmaniOrExpression179", type=aspectualacme_ArmaniBooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniBooleanExpression", type=aspectualacme_ArmaniOrExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions171: BinaryAssociation = BinaryAssociation(
    name="expressions171",
    ends={
        Property(name="aspectualacme_ArmaniEqualityExpression172", type=aspectualacme_ArmaniIffExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniIffExpression", type=aspectualacme_ArmaniEqualityExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions173: BinaryAssociation = BinaryAssociation(
    name="expressions173",
    ends={
        Property(name="aspectualacme_ArmaniIffExpression174", type=aspectualacme_ArmaniImpliesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniImpliesExpression", type=aspectualacme_ArmaniIffExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions175: BinaryAssociation = BinaryAssociation(
    name="expressions175",
    ends={
        Property(name="aspectualacme_ArmaniImpliesExpression176", type=aspectualacme_ArmaniOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniOrExpression", type=aspectualacme_ArmaniImpliesExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable180: BinaryAssociation = BinaryAssociation(
    name="variable180",
    ends={
        Property(name="aspectualacme_ArmaniVariable181", type=aspectualacme_ArmaniQuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniQuantifiedExpression", type=aspectualacme_ArmaniVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setExpression182: BinaryAssociation = BinaryAssociation(
    name="setExpression182",
    ends={
        Property(name="aspectualacme_ArmaniSetExpression184", type=aspectualacme_ArmaniQuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniQuantifiedExpression183", type=aspectualacme_ArmaniSetExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
designRule185: BinaryAssociation = BinaryAssociation(
    name="designRule185",
    ends={
        Property(name="aspectualacme_ArmaniDesignRuleExpression187", type=aspectualacme_ArmaniQuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aspectualacme_ArmaniQuantifiedExpression186", type=aspectualacme_ArmaniDesignRuleExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_aspectualacme_attachableElement_Element = Generalization(general=Element, specific=aspectualacme_attachableElement)
gen_aspectualacme_BasicElement_Element = Generalization(general=Element, specific=aspectualacme_BasicElement)
gen_aspectualacme_Family_BasicElement = Generalization(general=BasicElement, specific=aspectualacme_Family)
gen_aspectualacme_RoleType_TypeDefinition = Generalization(general=TypeDefinition, specific=aspectualacme_RoleType)
gen_aspectualacme_ComponentType_TypeDefinition = Generalization(general=TypeDefinition, specific=aspectualacme_ComponentType)
gen_aspectualacme_PortType_TypeDefinition = Generalization(general=TypeDefinition, specific=aspectualacme_PortType)
gen_aspectualacme_PropertyType_TypeDefinition = Generalization(general=TypeDefinition, specific=aspectualacme_PropertyType)
gen_aspectualacme_ConnectorType_TypeDefinition = Generalization(general=TypeDefinition, specific=aspectualacme_ConnectorType)
gen_aspectualacme_Component_Element = Generalization(general=Element, specific=aspectualacme_Component)
gen_aspectualacme_System_BasicElement = Generalization(general=BasicElement, specific=aspectualacme_System)
gen_aspectualacme_Connector_Element = Generalization(general=Element, specific=aspectualacme_Connector)
gen_aspectualacme_BaseRole_Role = Generalization(general=Role, specific=aspectualacme_BaseRole)
gen_aspectualacme_CrosscuttingRole_Role = Generalization(general=Role, specific=aspectualacme_CrosscuttingRole)
gen_aspectualacme_Role_attachableElement = Generalization(general=attachableElement, specific=aspectualacme_Role)
gen_aspectualacme_Role_BindableElement = Generalization(general=BindableElement, specific=aspectualacme_Role)
gen_aspectualacme_Port_attachableElement = Generalization(general=attachableElement, specific=aspectualacme_Port)
gen_aspectualacme_Port_BindableElement = Generalization(general=BindableElement, specific=aspectualacme_Port)
gen_aspectualacme_WildCard_attachableElement = Generalization(general=attachableElement, specific=aspectualacme_WildCard)
gen_aspectualacme_ArmaniSetExpression_ArmaniPrimitiveExpression = Generalization(general=ArmaniPrimitiveExpression, specific=aspectualacme_ArmaniSetExpression)
gen_aspectualacme_BindableElement_Element = Generalization(general=Element, specific=aspectualacme_BindableElement)
gen_aspectualacme_TypeDefinition_Element = Generalization(general=Element, specific=aspectualacme_TypeDefinition)
gen_aspectualacme_ArmaniFunctionCall_ArmaniPrimitiveExpression = Generalization(general=ArmaniPrimitiveExpression, specific=aspectualacme_ArmaniFunctionCall)
gen_aspectualacme_ArmaniMultiplicativeExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniMultiplicativeExpression)
gen_aspectualacme_ArmaniConstant_ArmaniPrimitiveExpression = Generalization(general=ArmaniPrimitiveExpression, specific=aspectualacme_ArmaniConstant)
gen_aspectualacme_ArmaniPrimitiveExpression_ArmaniUnaryExpression = Generalization(general=ArmaniUnaryExpression, specific=aspectualacme_ArmaniPrimitiveExpression)
gen_aspectualacme_ArmaniUnaryExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniUnaryExpression)
gen_aspectualacme_ArmaniEqualityExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniEqualityExpression)
gen_aspectualacme_ArmaniIffExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniIffExpression)
gen_aspectualacme_ArmaniAdditiveExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniAdditiveExpression)
gen_aspectualacme_ArmaniRelationalExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniRelationalExpression)
gen_aspectualacme_ArmaniBooleanExpression_ArmaniDesignRuleExpression = Generalization(general=ArmaniDesignRuleExpression, specific=aspectualacme_ArmaniBooleanExpression)
gen_aspectualacme_ArmaniQuantifiedExpression_ArmaniDesignRuleExpression = Generalization(general=ArmaniDesignRuleExpression, specific=aspectualacme_ArmaniQuantifiedExpression)
gen_aspectualacme_ArmaniImpliesExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniImpliesExpression)
gen_aspectualacme_ArmaniOrExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniOrExpression)
gen_aspectualacme_ArmaniVariable_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniVariable)
gen_aspectualacme_ArmaniDesignRuleExpression_ArmaniExpression = Generalization(general=ArmaniExpression, specific=aspectualacme_ArmaniDesignRuleExpression)

# Domain Model
domain_model = DomainModel(
    name="aspectualacme",
    types={aspectualacme_Root, aspectualacme_Import, aspectualacme_attachableElement, Element, aspectualacme_Armani, aspectualacme_Family, aspectualacme_BasicElement, aspectualacme_Element, aspectualacme_Property, aspectualacme_Representation, aspectualacme_ComponentType, aspectualacme_PortType, aspectualacme_ConnectorType, aspectualacme_RoleType, BasicElement, aspectualacme_Connector, aspectualacme_Component, aspectualacme_Attachment, aspectualacme_WildCard, aspectualacme_PropertyType, TypeDefinition, aspectualacme_Port, aspectualacme_Role, aspectualacme_Glue, aspectualacme_System, aspectualacme_BaseRole, Role, aspectualacme_CrosscuttingRole, attachableElement, BindableElement, aspectualacme_Binding, aspectualacme_BindableElement, aspectualacme_ArmaniPrimitiveExpression, aspectualacme_ArmaniSetExpression, aspectualacme_ArmaniConstant, aspectualacme_TypeDefinition, aspectualacme_ArmaniDesignRuleExpression, aspectualacme_ArmaniExpression, aspectualacme_ArmaniFunctionCall, ArmaniPrimitiveExpression, aspectualacme_ArmaniMultiplicativeExpression, ArmaniUnaryExpression, aspectualacme_ArmaniUnaryExpression, ArmaniExpression, aspectualacme_ArmaniEqualityExpression, aspectualacme_ArmaniIffExpression, aspectualacme_ArmaniAdditiveExpression, aspectualacme_ArmaniRelationalExpression, aspectualacme_ArmaniBooleanExpression, ArmaniDesignRuleExpression, aspectualacme_ArmaniQuantifiedExpression, aspectualacme_ArmaniImpliesExpression, aspectualacme_ArmaniOrExpression, aspectualacme_ArmaniVariable, GlueType, ArmaniTypes, ArmaniSetTypes, ArmaniQuantifier},
    associations={armani5, parentFamily7, imports0, elements1, property3, representations4, ctypes16, ptypes18, cntypes20, connectors9, components10, attachments12, wildcard14, parentFamily31, parentType33, parentFamily34, rtypes22, prtypes24, properties26, port28, parentType30, parentType37, parentFamily38, parentFamily45, parentFamily47, parentType41, role42, glue43, parentRepresentation62, effective_type64, port67, connectors49, properties51, attachments54, wildCard57, components59, role79, glue82, type83, parentSystem85, type70, parentSystem72, parentFamily73, effective_type76, roleType98, effective_type100, type103, parentFamily87, effective_type90, Connector93, ConnectorT95, type117, parentSystem119, type105, portType107, Component109, ComponentT111, effective_type114, firstElement132, secondElement133, parentSystem136, parentFamily138, parentFamily121, baseAttach124, crosscuttingAttach127, connector130, system150, bindings152, element153, property141, firstPort143, secondPort145, representation148, parameters156, setValues157, designRule154, designRule158, unaryExpression162, expressions169, expressions163, expressions165, expressions167, userType177, expressions178, expressions171, expressions173, expressions175, variable180, setExpression182, designRule185},
    generalizations={gen_aspectualacme_attachableElement_Element, gen_aspectualacme_BasicElement_Element, gen_aspectualacme_Family_BasicElement, gen_aspectualacme_RoleType_TypeDefinition, gen_aspectualacme_ComponentType_TypeDefinition, gen_aspectualacme_PortType_TypeDefinition, gen_aspectualacme_PropertyType_TypeDefinition, gen_aspectualacme_ConnectorType_TypeDefinition, gen_aspectualacme_Component_Element, gen_aspectualacme_System_BasicElement, gen_aspectualacme_Connector_Element, gen_aspectualacme_BaseRole_Role, gen_aspectualacme_CrosscuttingRole_Role, gen_aspectualacme_Role_attachableElement, gen_aspectualacme_Role_BindableElement, gen_aspectualacme_Port_attachableElement, gen_aspectualacme_Port_BindableElement, gen_aspectualacme_WildCard_attachableElement, gen_aspectualacme_ArmaniSetExpression_ArmaniPrimitiveExpression, gen_aspectualacme_BindableElement_Element, gen_aspectualacme_TypeDefinition_Element, gen_aspectualacme_ArmaniFunctionCall_ArmaniPrimitiveExpression, gen_aspectualacme_ArmaniMultiplicativeExpression_ArmaniExpression, gen_aspectualacme_ArmaniConstant_ArmaniPrimitiveExpression, gen_aspectualacme_ArmaniPrimitiveExpression_ArmaniUnaryExpression, gen_aspectualacme_ArmaniUnaryExpression_ArmaniExpression, gen_aspectualacme_ArmaniEqualityExpression_ArmaniExpression, gen_aspectualacme_ArmaniIffExpression_ArmaniExpression, gen_aspectualacme_ArmaniAdditiveExpression_ArmaniExpression, gen_aspectualacme_ArmaniRelationalExpression_ArmaniExpression, gen_aspectualacme_ArmaniBooleanExpression_ArmaniDesignRuleExpression, gen_aspectualacme_ArmaniQuantifiedExpression_ArmaniDesignRuleExpression, gen_aspectualacme_ArmaniImpliesExpression_ArmaniExpression, gen_aspectualacme_ArmaniOrExpression_ArmaniExpression, gen_aspectualacme_ArmaniVariable_ArmaniExpression, gen_aspectualacme_ArmaniDesignRuleExpression_ArmaniExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
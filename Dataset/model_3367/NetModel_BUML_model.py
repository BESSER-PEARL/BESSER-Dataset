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
HttpMethodType: Enumeration = Enumeration(
    name="HttpMethodType",
    literals={
            EnumerationLiteral(name="get"),
			EnumerationLiteral(name="put"),
			EnumerationLiteral(name="post"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="patch")
    }
)

BooleanValue: Enumeration = Enumeration(
    name="BooleanValue",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false")
    }
)

# Classes
netModel_Model = Class(name="netModel_Model")
netModel_Declaration = Class(name="netModel_Declaration")
netModel_Client = Class(name="netModel_Client")
Declaration = Class(name="Declaration")
netModel_SimpleMemberAssignment = Class(name="netModel_SimpleMemberAssignment")
netModel_ParamsBlock = Class(name="netModel_ParamsBlock")
netModel_SimpleMember = Class(name="netModel_SimpleMember")
netModel_Literal = Class(name="netModel_Literal")
netModel_BodyBlock = Class(name="netModel_BodyBlock")
netModel_BlockType = Class(name="netModel_BlockType")
netModel_ResponseBlock = Class(name="netModel_ResponseBlock")
netModel_ComplexTypeDeclaration = Class(name="netModel_ComplexTypeDeclaration")
netModel_ClientBlock = Class(name="netModel_ClientBlock")
netModel_HeaderBlock = Class(name="netModel_HeaderBlock")
ClientBlock = Class(name="ClientBlock")
HttpMethodBlock = Class(name="HttpMethodBlock")
netModel_Header = Class(name="netModel_Header")
netModel_HttpMethod = Class(name="netModel_HttpMethod")
netModel_Path = Class(name="netModel_Path")
netModel_HttpMethodBlock = Class(name="netModel_HttpMethodBlock")
UserTypeDeclaration = Class(name="UserTypeDeclaration")
netModel_EnumTypeDeclaration = Class(name="netModel_EnumTypeDeclaration")
netModel_IntegerType = Class(name="netModel_IntegerType")
netModel_EnumTypeLiteral = Class(name="netModel_EnumTypeLiteral")
netModel_EnumMember = Class(name="netModel_EnumMember")
netModel_Member = Class(name="netModel_Member")
netModel_TypedMember = Class(name="netModel_TypedMember")
Member = Class(name="Member")
netModel_Type = Class(name="netModel_Type")
netModel_SkipMember = Class(name="netModel_SkipMember")
netModel_ComplexTypeLiteral = Class(name="netModel_ComplexTypeLiteral")
netModel_IntrinsicType = Class(name="netModel_IntrinsicType")
BlockType = Class(name="BlockType")
netModel_GenericListType = Class(name="netModel_GenericListType")
Type = Class(name="Type")
netModel_UserType = Class(name="netModel_UserType")
netModel_UserTypeDeclaration = Class(name="netModel_UserTypeDeclaration")
netModel_DoubleType = Class(name="netModel_DoubleType")
netModel_BooleanLiteral = Class(name="netModel_BooleanLiteral")
Literal = Class(name="Literal")
netModel_StringLiteral = Class(name="netModel_StringLiteral")
netModel_NumericLiteral = Class(name="netModel_NumericLiteral")
netModel_StringType = Class(name="netModel_StringType")
IntrinsicType = Class(name="IntrinsicType")
netModel_BooleanType = Class(name="netModel_BooleanType")
netModel_NumericType = Class(name="netModel_NumericType")
NumericType = Class(name="NumericType")
netModel_LongType = Class(name="netModel_LongType")

# netModel_Model class attributes and methods
netModel_Model_packageName: Property = Property(name="packageName", type=StringType)
netModel_Model.attributes={netModel_Model_packageName}

# netModel_Declaration class attributes and methods
netModel_Declaration_name: Property = Property(name="name", type=StringType)
netModel_Declaration.attributes={netModel_Declaration_name}

# netModel_Client class attributes and methods
netModel_Client_baseUrl: Property = Property(name="baseUrl", type=StringType)
netModel_Client.attributes={netModel_Client_baseUrl}

# Declaration class attributes and methods

# netModel_SimpleMemberAssignment class attributes and methods

# netModel_ParamsBlock class attributes and methods

# netModel_SimpleMember class attributes and methods
netModel_SimpleMember_name: Property = Property(name="name", type=StringType)
netModel_SimpleMember.attributes={netModel_SimpleMember_name}

# netModel_Literal class attributes and methods

# netModel_BodyBlock class attributes and methods

# netModel_BlockType class attributes and methods

# netModel_ResponseBlock class attributes and methods

# netModel_ComplexTypeDeclaration class attributes and methods

# netModel_ClientBlock class attributes and methods

# netModel_HeaderBlock class attributes and methods

# ClientBlock class attributes and methods

# HttpMethodBlock class attributes and methods

# netModel_Header class attributes and methods
netModel_Header_name: Property = Property(name="name", type=StringType)
netModel_Header_value: Property = Property(name="value", type=StringType)
netModel_Header.attributes={netModel_Header_name, netModel_Header_value}

# netModel_HttpMethod class attributes and methods
netModel_HttpMethod_type: Property = Property(name="type", type=StringType)
netModel_HttpMethod_name: Property = Property(name="name", type=StringType)
netModel_HttpMethod.attributes={netModel_HttpMethod_type, netModel_HttpMethod_name}

# netModel_Path class attributes and methods
netModel_Path_arb: Property = Property(name="arb", type=StringType)
netModel_Path.attributes={netModel_Path_arb}

# netModel_HttpMethodBlock class attributes and methods

# UserTypeDeclaration class attributes and methods

# netModel_EnumTypeDeclaration class attributes and methods

# netModel_IntegerType class attributes and methods

# netModel_EnumTypeLiteral class attributes and methods

# netModel_EnumMember class attributes and methods
netModel_EnumMember_name: Property = Property(name="name", type=StringType)
netModel_EnumMember_assignment: Property = Property(name="assignment", type=BooleanType)
netModel_EnumMember_value: Property = Property(name="value", type=IntegerType)
netModel_EnumMember.attributes={netModel_EnumMember_value, netModel_EnumMember_name, netModel_EnumMember_assignment}

# netModel_Member class attributes and methods
netModel_Member_name: Property = Property(name="name", type=StringType)
netModel_Member.attributes={netModel_Member_name}

# netModel_TypedMember class attributes and methods

# Member class attributes and methods

# netModel_Type class attributes and methods

# netModel_SkipMember class attributes and methods

# netModel_ComplexTypeLiteral class attributes and methods

# netModel_IntrinsicType class attributes and methods
netModel_IntrinsicType_id: Property = Property(name="id", type=StringType)
netModel_IntrinsicType.attributes={netModel_IntrinsicType_id}

# BlockType class attributes and methods

# netModel_GenericListType class attributes and methods
netModel_GenericListType_id: Property = Property(name="id", type=StringType)
netModel_GenericListType.attributes={netModel_GenericListType_id}

# Type class attributes and methods

# netModel_UserType class attributes and methods

# netModel_UserTypeDeclaration class attributes and methods
netModel_UserTypeDeclaration_keyword: Property = Property(name="keyword", type=StringType)
netModel_UserTypeDeclaration_nogen: Property = Property(name="nogen", type=BooleanType)
netModel_UserTypeDeclaration.attributes={netModel_UserTypeDeclaration_keyword, netModel_UserTypeDeclaration_nogen}

# netModel_DoubleType class attributes and methods

# netModel_BooleanLiteral class attributes and methods
netModel_BooleanLiteral_literal: Property = Property(name="literal", type=StringType)
netModel_BooleanLiteral.attributes={netModel_BooleanLiteral_literal}

# Literal class attributes and methods

# netModel_StringLiteral class attributes and methods
netModel_StringLiteral_literal: Property = Property(name="literal", type=StringType)
netModel_StringLiteral.attributes={netModel_StringLiteral_literal}

# netModel_NumericLiteral class attributes and methods
netModel_NumericLiteral_literal: Property = Property(name="literal", type=StringType)
netModel_NumericLiteral.attributes={netModel_NumericLiteral_literal}

# netModel_StringType class attributes and methods

# IntrinsicType class attributes and methods

# netModel_BooleanType class attributes and methods

# netModel_NumericType class attributes and methods

# NumericType class attributes and methods

# netModel_LongType class attributes and methods

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="netModel_Declaration", type=netModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_Model", type=netModel_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params6: BinaryAssociation = BinaryAssociation(
    name="params6",
    ends={
        Property(name="netModel_SimpleMemberAssignment", type=netModel_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_Path7", type=netModel_SimpleMemberAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params8: BinaryAssociation = BinaryAssociation(
    name="params8",
    ends={
        Property(name="netModel_SimpleMemberAssignment9", type=netModel_ParamsBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_ParamsBlock", type=netModel_SimpleMemberAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member10: BinaryAssociation = BinaryAssociation(
    name="member10",
    ends={
        Property(name="netModel_SimpleMember", type=netModel_SimpleMemberAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_SimpleMemberAssignment11", type=netModel_SimpleMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue12: BinaryAssociation = BinaryAssociation(
    name="defaultValue12",
    ends={
        Property(name="netModel_Literal", type=netModel_SimpleMemberAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_SimpleMemberAssignment13", type=netModel_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="netModel_BlockType", type=netModel_BodyBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_BodyBlock", type=netModel_BlockType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType15: BinaryAssociation = BinaryAssociation(
    name="superType15",
    ends={
        Property(name="netModel_ComplexTypeDeclaration", type=netModel_ResponseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_ResponseBlock", type=netModel_ComplexTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="netModel_BlockType18", type=netModel_ResponseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_ResponseBlock17", type=netModel_BlockType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocks1: BinaryAssociation = BinaryAssociation(
    name="blocks1",
    ends={
        Property(name="netModel_ClientBlock", type=netModel_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_Client", type=netModel_ClientBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headers2: BinaryAssociation = BinaryAssociation(
    name="headers2",
    ends={
        Property(name="netModel_Header", type=netModel_HeaderBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_HeaderBlock", type=netModel_Header, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path3: BinaryAssociation = BinaryAssociation(
    name="path3",
    ends={
        Property(name="netModel_Path", type=netModel_HttpMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_HttpMethod", type=netModel_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocks4: BinaryAssociation = BinaryAssociation(
    name="blocks4",
    ends={
        Property(name="netModel_HttpMethodBlock", type=netModel_HttpMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_HttpMethod5", type=netModel_HttpMethodBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal26: BinaryAssociation = BinaryAssociation(
    name="literal26",
    ends={
        Property(name="netModel_ComplexTypeLiteral28", type=netModel_ComplexTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_ComplexTypeDeclaration27", type=netModel_ComplexTypeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType29: BinaryAssociation = BinaryAssociation(
    name="superType29",
    ends={
        Property(name="netModel_IntegerType", type=netModel_EnumTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_EnumTypeDeclaration", type=netModel_IntegerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal30: BinaryAssociation = BinaryAssociation(
    name="literal30",
    ends={
        Property(name="netModel_EnumTypeLiteral", type=netModel_EnumTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_EnumTypeDeclaration31", type=netModel_EnumTypeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members32: BinaryAssociation = BinaryAssociation(
    name="members32",
    ends={
        Property(name="netModel_EnumMember", type=netModel_EnumTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_EnumTypeLiteral33", type=netModel_EnumMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="netModel_Type", type=netModel_TypedMember, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_TypedMember", type=netModel_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal20: BinaryAssociation = BinaryAssociation(
    name="literal20",
    ends={
        Property(name="netModel_ComplexTypeLiteral", type=netModel_SkipMember, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_SkipMember", type=netModel_ComplexTypeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="netModel_IntrinsicType", type=netModel_SimpleMember, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_SimpleMember22", type=netModel_IntrinsicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType23: BinaryAssociation = BinaryAssociation(
    name="elementType23",
    ends={
        Property(name="netModel_Type24", type=netModel_GenericListType, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_GenericListType", type=netModel_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration25: BinaryAssociation = BinaryAssociation(
    name="declaration25",
    ends={
        Property(name="netModel_UserTypeDeclaration", type=netModel_UserType, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_UserType", type=netModel_UserTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
members34: BinaryAssociation = BinaryAssociation(
    name="members34",
    ends={
        Property(name="netModel_Member", type=netModel_ComplexTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="netModel_ComplexTypeLiteral35", type=netModel_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_netModel_Client_Declaration = Generalization(general=Declaration, specific=netModel_Client)
gen_netModel_ParamsBlock_ClientBlock = Generalization(general=ClientBlock, specific=netModel_ParamsBlock)
gen_netModel_ParamsBlock_HttpMethodBlock = Generalization(general=HttpMethodBlock, specific=netModel_ParamsBlock)
gen_netModel_BodyBlock_HttpMethodBlock = Generalization(general=HttpMethodBlock, specific=netModel_BodyBlock)
gen_netModel_ResponseBlock_HttpMethodBlock = Generalization(general=HttpMethodBlock, specific=netModel_ResponseBlock)
gen_netModel_HeaderBlock_ClientBlock = Generalization(general=ClientBlock, specific=netModel_HeaderBlock)
gen_netModel_HeaderBlock_HttpMethodBlock = Generalization(general=HttpMethodBlock, specific=netModel_HeaderBlock)
gen_netModel_HttpMethod_ClientBlock = Generalization(general=ClientBlock, specific=netModel_HttpMethod)
gen_netModel_UserTypeDeclaration_Declaration = Generalization(general=Declaration, specific=netModel_UserTypeDeclaration)
gen_netModel_ComplexTypeDeclaration_UserTypeDeclaration = Generalization(general=UserTypeDeclaration, specific=netModel_ComplexTypeDeclaration)
gen_netModel_EnumTypeDeclaration_UserTypeDeclaration = Generalization(general=UserTypeDeclaration, specific=netModel_EnumTypeDeclaration)
gen_netModel_TypedMember_Member = Generalization(general=Member, specific=netModel_TypedMember)
gen_netModel_SkipMember_Member = Generalization(general=Member, specific=netModel_SkipMember)
gen_netModel_Type_BlockType = Generalization(general=BlockType, specific=netModel_Type)
gen_netModel_GenericListType_Type = Generalization(general=Type, specific=netModel_GenericListType)
gen_netModel_UserType_Type = Generalization(general=Type, specific=netModel_UserType)
gen_netModel_DoubleType_NumericType = Generalization(general=NumericType, specific=netModel_DoubleType)
gen_netModel_BooleanLiteral_Literal = Generalization(general=Literal, specific=netModel_BooleanLiteral)
gen_netModel_StringLiteral_Literal = Generalization(general=Literal, specific=netModel_StringLiteral)
gen_netModel_NumericLiteral_Literal = Generalization(general=Literal, specific=netModel_NumericLiteral)
gen_netModel_ComplexTypeLiteral_BlockType = Generalization(general=BlockType, specific=netModel_ComplexTypeLiteral)
gen_netModel_IntrinsicType_Type = Generalization(general=Type, specific=netModel_IntrinsicType)
gen_netModel_StringType_IntrinsicType = Generalization(general=IntrinsicType, specific=netModel_StringType)
gen_netModel_BooleanType_IntrinsicType = Generalization(general=IntrinsicType, specific=netModel_BooleanType)
gen_netModel_NumericType_IntrinsicType = Generalization(general=IntrinsicType, specific=netModel_NumericType)
gen_netModel_IntegerType_NumericType = Generalization(general=NumericType, specific=netModel_IntegerType)
gen_netModel_LongType_NumericType = Generalization(general=NumericType, specific=netModel_LongType)

# Domain Model
domain_model = DomainModel(
    name="netModel",
    types={netModel_Model, netModel_Declaration, netModel_Client, Declaration, netModel_SimpleMemberAssignment, netModel_ParamsBlock, netModel_SimpleMember, netModel_Literal, netModel_BodyBlock, netModel_BlockType, netModel_ResponseBlock, netModel_ComplexTypeDeclaration, netModel_ClientBlock, netModel_HeaderBlock, ClientBlock, HttpMethodBlock, netModel_Header, netModel_HttpMethod, netModel_Path, netModel_HttpMethodBlock, UserTypeDeclaration, netModel_EnumTypeDeclaration, netModel_IntegerType, netModel_EnumTypeLiteral, netModel_EnumMember, netModel_Member, netModel_TypedMember, Member, netModel_Type, netModel_SkipMember, netModel_ComplexTypeLiteral, netModel_IntrinsicType, BlockType, netModel_GenericListType, Type, netModel_UserType, netModel_UserTypeDeclaration, netModel_DoubleType, netModel_BooleanLiteral, Literal, netModel_StringLiteral, netModel_NumericLiteral, netModel_StringType, IntrinsicType, netModel_BooleanType, netModel_NumericType, NumericType, netModel_LongType, HttpMethodType, BooleanValue},
    associations={declarations0, params6, params8, member10, defaultValue12, type14, superType15, type16, blocks1, headers2, path3, blocks4, literal26, superType29, literal30, members32, type19, literal20, type21, elementType23, declaration25, members34},
    generalizations={gen_netModel_Client_Declaration, gen_netModel_ParamsBlock_ClientBlock, gen_netModel_ParamsBlock_HttpMethodBlock, gen_netModel_BodyBlock_HttpMethodBlock, gen_netModel_ResponseBlock_HttpMethodBlock, gen_netModel_HeaderBlock_ClientBlock, gen_netModel_HeaderBlock_HttpMethodBlock, gen_netModel_HttpMethod_ClientBlock, gen_netModel_UserTypeDeclaration_Declaration, gen_netModel_ComplexTypeDeclaration_UserTypeDeclaration, gen_netModel_EnumTypeDeclaration_UserTypeDeclaration, gen_netModel_TypedMember_Member, gen_netModel_SkipMember_Member, gen_netModel_Type_BlockType, gen_netModel_GenericListType_Type, gen_netModel_UserType_Type, gen_netModel_DoubleType_NumericType, gen_netModel_BooleanLiteral_Literal, gen_netModel_StringLiteral_Literal, gen_netModel_NumericLiteral_Literal, gen_netModel_ComplexTypeLiteral_BlockType, gen_netModel_IntrinsicType_Type, gen_netModel_StringType_IntrinsicType, gen_netModel_BooleanType_IntrinsicType, gen_netModel_NumericType_IntrinsicType, gen_netModel_IntegerType_NumericType, gen_netModel_LongType_NumericType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
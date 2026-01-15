from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanValue(Enum):
    true = "true"
    false = "false"
class HttpMethodType(Enum):
    get = "get"
    put = "put"
    post = "post"
    delete = "delete"
    patch = "patch"


############################################
# Definition of Classes
############################################

class Literal:

    pass
class netModel_StringLiteral(Literal):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class netModel_NumericLiteral(Literal):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class netModel_BooleanLiteral(Literal):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class NumericType:

    pass
class netModel_DoubleType(NumericType):

    pass
class netModel_LongType(NumericType):

    pass
class IntrinsicType:

    pass
class netModel_BooleanType(IntrinsicType):

    pass
class netModel_NumericType(IntrinsicType):

    pass
class netModel_StringType(IntrinsicType):

    pass
class netModel_EnumMember:

    def __init__(self, name: str, assignment: bool, value: int, netModel_EnumMember: "netModel_EnumTypeLiteral" = None):
        self.name = name
        self.assignment = assignment
        self.value = value
        self.netModel_EnumMember = netModel_EnumMember
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def assignment(self) -> bool:
        return self.__assignment

    @assignment.setter
    def assignment(self, assignment: bool):
        self.__assignment = assignment

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def netModel_EnumMember(self):
        return self.__netModel_EnumMember

    @netModel_EnumMember.setter
    def netModel_EnumMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_EnumMember__netModel_EnumMember", None)
        self.__netModel_EnumMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_EnumTypeLiteral33"):
                opp_val = getattr(old_value, "netModel_EnumTypeLiteral33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_EnumTypeLiteral33"):
                opp_val = getattr(value, "netModel_EnumTypeLiteral33", None)
                if opp_val is None:
                    setattr(value, "netModel_EnumTypeLiteral33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class netModel_EnumTypeLiteral:

    pass
class netModel_IntegerType(NumericType):

    pass
class UserTypeDeclaration:

    pass
class netModel_EnumTypeDeclaration(UserTypeDeclaration):

    pass
class Type:

    pass
class netModel_UserType(Type):

    pass
class netModel_GenericListType(Type):

    def __init__(self, id: str, netModel_GenericListType: "netModel_Type" = None):
        self.id = id
        self.netModel_GenericListType = netModel_GenericListType
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def netModel_GenericListType(self):
        return self.__netModel_GenericListType

    @netModel_GenericListType.setter
    def netModel_GenericListType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_GenericListType__netModel_GenericListType", None)
        self.__netModel_GenericListType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_Type24"):
                opp_val = getattr(old_value, "netModel_Type24", None)
                if opp_val == self:
                    setattr(old_value, "netModel_Type24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_Type24"):
                opp_val = getattr(value, "netModel_Type24", None)
                setattr(value, "netModel_Type24", self)

class BlockType:

    pass
class netModel_IntrinsicType(Type):

    def __init__(self, id: str, netModel_IntrinsicType: "netModel_SimpleMember" = None):
        self.id = id
        self.netModel_IntrinsicType = netModel_IntrinsicType
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def netModel_IntrinsicType(self):
        return self.__netModel_IntrinsicType

    @netModel_IntrinsicType.setter
    def netModel_IntrinsicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_IntrinsicType__netModel_IntrinsicType", None)
        self.__netModel_IntrinsicType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_SimpleMember22"):
                opp_val = getattr(old_value, "netModel_SimpleMember22", None)
                if opp_val == self:
                    setattr(old_value, "netModel_SimpleMember22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_SimpleMember22"):
                opp_val = getattr(value, "netModel_SimpleMember22", None)
                setattr(value, "netModel_SimpleMember22", self)

class netModel_ComplexTypeLiteral(BlockType):

    pass
class netModel_Type(BlockType):

    pass
class Member:

    pass
class netModel_SkipMember(Member):

    pass
class netModel_TypedMember(Member):

    pass
class netModel_Member:

    def __init__(self, name: str, netModel_Member: "netModel_ComplexTypeLiteral" = None):
        self.name = name
        self.netModel_Member = netModel_Member
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def netModel_Member(self):
        return self.__netModel_Member

    @netModel_Member.setter
    def netModel_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Member__netModel_Member", None)
        self.__netModel_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_ComplexTypeLiteral35"):
                opp_val = getattr(old_value, "netModel_ComplexTypeLiteral35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_ComplexTypeLiteral35"):
                opp_val = getattr(value, "netModel_ComplexTypeLiteral35", None)
                if opp_val is None:
                    setattr(value, "netModel_ComplexTypeLiteral35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class netModel_ComplexTypeDeclaration(UserTypeDeclaration):

    pass
class netModel_BlockType:

    pass
class netModel_Literal:

    pass
class netModel_SimpleMember:

    def __init__(self, name: str, netModel_SimpleMember: "netModel_SimpleMemberAssignment" = None, netModel_SimpleMember22: "netModel_IntrinsicType" = None):
        self.name = name
        self.netModel_SimpleMember = netModel_SimpleMember
        self.netModel_SimpleMember22 = netModel_SimpleMember22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def netModel_SimpleMember(self):
        return self.__netModel_SimpleMember

    @netModel_SimpleMember.setter
    def netModel_SimpleMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_SimpleMember__netModel_SimpleMember", None)
        self.__netModel_SimpleMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_SimpleMemberAssignment11"):
                opp_val = getattr(old_value, "netModel_SimpleMemberAssignment11", None)
                if opp_val == self:
                    setattr(old_value, "netModel_SimpleMemberAssignment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_SimpleMemberAssignment11"):
                opp_val = getattr(value, "netModel_SimpleMemberAssignment11", None)
                setattr(value, "netModel_SimpleMemberAssignment11", self)

    @property
    def netModel_SimpleMember22(self):
        return self.__netModel_SimpleMember22

    @netModel_SimpleMember22.setter
    def netModel_SimpleMember22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_SimpleMember__netModel_SimpleMember22", None)
        self.__netModel_SimpleMember22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_IntrinsicType"):
                opp_val = getattr(old_value, "netModel_IntrinsicType", None)
                if opp_val == self:
                    setattr(old_value, "netModel_IntrinsicType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_IntrinsicType"):
                opp_val = getattr(value, "netModel_IntrinsicType", None)
                setattr(value, "netModel_IntrinsicType", self)

class netModel_SimpleMemberAssignment:

    pass
class netModel_HttpMethodBlock:

    pass
class netModel_Path:

    def __init__(self, arb: str, netModel_Path: "netModel_HttpMethod" = None, netModel_Path7: set["netModel_SimpleMemberAssignment"] = None):
        self.arb = arb
        self.netModel_Path = netModel_Path
        self.netModel_Path7 = netModel_Path7 if netModel_Path7 is not None else set()
        
    @property
    def arb(self) -> str:
        return self.__arb

    @arb.setter
    def arb(self, arb: str):
        self.__arb = arb

    @property
    def netModel_Path7(self):
        return self.__netModel_Path7

    @netModel_Path7.setter
    def netModel_Path7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Path__netModel_Path7", None)
        self.__netModel_Path7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netModel_SimpleMemberAssignment"):
                    opp_val = getattr(item, "netModel_SimpleMemberAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "netModel_SimpleMemberAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netModel_SimpleMemberAssignment"):
                    opp_val = getattr(item, "netModel_SimpleMemberAssignment", None)
                    
                    setattr(item, "netModel_SimpleMemberAssignment", self)
                    

    @property
    def netModel_Path(self):
        return self.__netModel_Path

    @netModel_Path.setter
    def netModel_Path(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Path__netModel_Path", None)
        self.__netModel_Path = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_HttpMethod"):
                opp_val = getattr(old_value, "netModel_HttpMethod", None)
                if opp_val == self:
                    setattr(old_value, "netModel_HttpMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_HttpMethod"):
                opp_val = getattr(value, "netModel_HttpMethod", None)
                setattr(value, "netModel_HttpMethod", self)

class netModel_Header:

    def __init__(self, name: str, value: str, netModel_Header: "netModel_HeaderBlock" = None):
        self.name = name
        self.value = value
        self.netModel_Header = netModel_Header
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def netModel_Header(self):
        return self.__netModel_Header

    @netModel_Header.setter
    def netModel_Header(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Header__netModel_Header", None)
        self.__netModel_Header = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_HeaderBlock"):
                opp_val = getattr(old_value, "netModel_HeaderBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_HeaderBlock"):
                opp_val = getattr(value, "netModel_HeaderBlock", None)
                if opp_val is None:
                    setattr(value, "netModel_HeaderBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HttpMethodBlock:

    pass
class netModel_BodyBlock(HttpMethodBlock):

    pass
class netModel_ResponseBlock(HttpMethodBlock):

    pass
class ClientBlock:

    pass
class netModel_HttpMethod(ClientBlock):

    def __init__(self, type: str, name: str, netModel_HttpMethod: "netModel_Path" = None, netModel_HttpMethod5: set["netModel_HttpMethodBlock"] = None):
        self.type = type
        self.name = name
        self.netModel_HttpMethod = netModel_HttpMethod
        self.netModel_HttpMethod5 = netModel_HttpMethod5 if netModel_HttpMethod5 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def netModel_HttpMethod5(self):
        return self.__netModel_HttpMethod5

    @netModel_HttpMethod5.setter
    def netModel_HttpMethod5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_HttpMethod__netModel_HttpMethod5", None)
        self.__netModel_HttpMethod5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netModel_HttpMethodBlock"):
                    opp_val = getattr(item, "netModel_HttpMethodBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "netModel_HttpMethodBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netModel_HttpMethodBlock"):
                    opp_val = getattr(item, "netModel_HttpMethodBlock", None)
                    
                    setattr(item, "netModel_HttpMethodBlock", self)
                    

    @property
    def netModel_HttpMethod(self):
        return self.__netModel_HttpMethod

    @netModel_HttpMethod.setter
    def netModel_HttpMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_HttpMethod__netModel_HttpMethod", None)
        self.__netModel_HttpMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_Path"):
                opp_val = getattr(old_value, "netModel_Path", None)
                if opp_val == self:
                    setattr(old_value, "netModel_Path", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_Path"):
                opp_val = getattr(value, "netModel_Path", None)
                setattr(value, "netModel_Path", self)

class netModel_ParamsBlock(ClientBlock, HttpMethodBlock):

    pass
class netModel_HeaderBlock(ClientBlock, HttpMethodBlock):

    pass
class netModel_ClientBlock:

    pass
class Declaration:

    pass
class netModel_UserTypeDeclaration(Declaration):

    def __init__(self, keyword: str, nogen: bool, netModel_UserTypeDeclaration: "netModel_UserType" = None):
        self.keyword = keyword
        self.nogen = nogen
        self.netModel_UserTypeDeclaration = netModel_UserTypeDeclaration
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def nogen(self) -> bool:
        return self.__nogen

    @nogen.setter
    def nogen(self, nogen: bool):
        self.__nogen = nogen

    @property
    def netModel_UserTypeDeclaration(self):
        return self.__netModel_UserTypeDeclaration

    @netModel_UserTypeDeclaration.setter
    def netModel_UserTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_UserTypeDeclaration__netModel_UserTypeDeclaration", None)
        self.__netModel_UserTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_UserType"):
                opp_val = getattr(old_value, "netModel_UserType", None)
                if opp_val == self:
                    setattr(old_value, "netModel_UserType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_UserType"):
                opp_val = getattr(value, "netModel_UserType", None)
                setattr(value, "netModel_UserType", self)

class netModel_Client(Declaration):

    def __init__(self, baseUrl: str, netModel_Client: set["netModel_ClientBlock"] = None):
        self.baseUrl = baseUrl
        self.netModel_Client = netModel_Client if netModel_Client is not None else set()
        
    @property
    def baseUrl(self) -> str:
        return self.__baseUrl

    @baseUrl.setter
    def baseUrl(self, baseUrl: str):
        self.__baseUrl = baseUrl

    @property
    def netModel_Client(self):
        return self.__netModel_Client

    @netModel_Client.setter
    def netModel_Client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Client__netModel_Client", None)
        self.__netModel_Client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netModel_ClientBlock"):
                    opp_val = getattr(item, "netModel_ClientBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "netModel_ClientBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netModel_ClientBlock"):
                    opp_val = getattr(item, "netModel_ClientBlock", None)
                    
                    setattr(item, "netModel_ClientBlock", self)
                    

class netModel_Declaration:

    def __init__(self, name: str, netModel_Declaration: "netModel_Model" = None):
        self.name = name
        self.netModel_Declaration = netModel_Declaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def netModel_Declaration(self):
        return self.__netModel_Declaration

    @netModel_Declaration.setter
    def netModel_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Declaration__netModel_Declaration", None)
        self.__netModel_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "netModel_Model"):
                opp_val = getattr(old_value, "netModel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "netModel_Model"):
                opp_val = getattr(value, "netModel_Model", None)
                if opp_val is None:
                    setattr(value, "netModel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class netModel_Model:

    def __init__(self, packageName: str, netModel_Model: set["netModel_Declaration"] = None):
        self.packageName = packageName
        self.netModel_Model = netModel_Model if netModel_Model is not None else set()
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def netModel_Model(self):
        return self.__netModel_Model

    @netModel_Model.setter
    def netModel_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_netModel_Model__netModel_Model", None)
        self.__netModel_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "netModel_Declaration"):
                    opp_val = getattr(item, "netModel_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "netModel_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "netModel_Declaration"):
                    opp_val = getattr(item, "netModel_Declaration", None)
                    
                    setattr(item, "netModel_Declaration", self)
                    

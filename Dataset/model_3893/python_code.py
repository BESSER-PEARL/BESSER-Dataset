from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class workflow_EnumLiteral:

    def __init__(self, name: str, workflow_EnumLiteral161: "workflow_EnumFieldValue" = None, workflow_EnumLiteral165: "workflow_EnumLiteralAtom" = None, workflow_EnumLiteral: "workflow_EnumField" = None, workflow_EnumLiteral155: "workflow_EnumField" = None):
        self.name = name
        self.workflow_EnumLiteral161 = workflow_EnumLiteral161
        self.workflow_EnumLiteral165 = workflow_EnumLiteral165
        self.workflow_EnumLiteral = workflow_EnumLiteral
        self.workflow_EnumLiteral155 = workflow_EnumLiteral155
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_EnumLiteral155(self):
        return self.__workflow_EnumLiteral155

    @workflow_EnumLiteral155.setter
    def workflow_EnumLiteral155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumLiteral__workflow_EnumLiteral155", None)
        self.__workflow_EnumLiteral155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumField154"):
                opp_val = getattr(old_value, "workflow_EnumField154", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumField154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumField154"):
                opp_val = getattr(value, "workflow_EnumField154", None)
                setattr(value, "workflow_EnumField154", self)

    @property
    def workflow_EnumLiteral(self):
        return self.__workflow_EnumLiteral

    @workflow_EnumLiteral.setter
    def workflow_EnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumLiteral__workflow_EnumLiteral", None)
        self.__workflow_EnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumField152"):
                opp_val = getattr(old_value, "workflow_EnumField152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumField152"):
                opp_val = getattr(value, "workflow_EnumField152", None)
                if opp_val is None:
                    setattr(value, "workflow_EnumField152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_EnumLiteral165(self):
        return self.__workflow_EnumLiteral165

    @workflow_EnumLiteral165.setter
    def workflow_EnumLiteral165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumLiteral__workflow_EnumLiteral165", None)
        self.__workflow_EnumLiteral165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumLiteralAtom"):
                opp_val = getattr(old_value, "workflow_EnumLiteralAtom", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumLiteralAtom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumLiteralAtom"):
                opp_val = getattr(value, "workflow_EnumLiteralAtom", None)
                setattr(value, "workflow_EnumLiteralAtom", self)

    @property
    def workflow_EnumLiteral161(self):
        return self.__workflow_EnumLiteral161

    @workflow_EnumLiteral161.setter
    def workflow_EnumLiteral161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumLiteral__workflow_EnumLiteral161", None)
        self.__workflow_EnumLiteral161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumFieldValue160"):
                opp_val = getattr(old_value, "workflow_EnumFieldValue160", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumFieldValue160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumFieldValue160"):
                opp_val = getattr(value, "workflow_EnumFieldValue160", None)
                setattr(value, "workflow_EnumFieldValue160", self)

class DocumentCondition:

    pass
class workflow_DefaultDocumentCondition(DocumentCondition):

    pass
class GlobalAspect:

    pass
class workflow_DocumentTypeContainer(GlobalAspect):

    def __init__(self, name: str, workflow_DocumentTypeContainer: set["workflow_DocumentType"] = None):
        self.name = name
        self.workflow_DocumentTypeContainer = workflow_DocumentTypeContainer if workflow_DocumentTypeContainer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_DocumentTypeContainer(self):
        return self.__workflow_DocumentTypeContainer

    @workflow_DocumentTypeContainer.setter
    def workflow_DocumentTypeContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentTypeContainer__workflow_DocumentTypeContainer", None)
        self.__workflow_DocumentTypeContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_DocumentType175"):
                    opp_val = getattr(item, "workflow_DocumentType175", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_DocumentType175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_DocumentType175"):
                    opp_val = getattr(item, "workflow_DocumentType175", None)
                    
                    setattr(item, "workflow_DocumentType175", self)
                    

class workflow_Organisation(GlobalAspect):

    def __init__(self, name: str, workflow_Organisation: set["workflow_Role"] = None):
        self.name = name
        self.workflow_Organisation = workflow_Organisation if workflow_Organisation is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Organisation(self):
        return self.__workflow_Organisation

    @workflow_Organisation.setter
    def workflow_Organisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Organisation__workflow_Organisation", None)
        self.__workflow_Organisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Role169"):
                    opp_val = getattr(item, "workflow_Role169", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Role169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Role169"):
                    opp_val = getattr(item, "workflow_Role169", None)
                    
                    setattr(item, "workflow_Role169", self)
                    

class RuntimeGlobalAspect:

    pass
class workflow_DocumentContainer(RuntimeGlobalAspect):

    def __init__(self, name: str, workflow_DocumentContainer: set["workflow_Document"] = None):
        self.name = name
        self.workflow_DocumentContainer = workflow_DocumentContainer if workflow_DocumentContainer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_DocumentContainer(self):
        return self.__workflow_DocumentContainer

    @workflow_DocumentContainer.setter
    def workflow_DocumentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentContainer__workflow_DocumentContainer", None)
        self.__workflow_DocumentContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Document177"):
                    opp_val = getattr(item, "workflow_Document177", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Document177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Document177"):
                    opp_val = getattr(item, "workflow_Document177", None)
                    
                    setattr(item, "workflow_Document177", self)
                    

class workflow_AgentContainer(RuntimeGlobalAspect):

    def __init__(self, name: str, workflow_AgentContainer: set["workflow_Agent"] = None):
        self.name = name
        self.workflow_AgentContainer = workflow_AgentContainer if workflow_AgentContainer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_AgentContainer(self):
        return self.__workflow_AgentContainer

    @workflow_AgentContainer.setter
    def workflow_AgentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_AgentContainer__workflow_AgentContainer", None)
        self.__workflow_AgentContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Agent167"):
                    opp_val = getattr(item, "workflow_Agent167", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Agent167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Agent167"):
                    opp_val = getattr(item, "workflow_Agent167", None)
                    
                    setattr(item, "workflow_Agent167", self)
                    

class workflow_EnumFieldValue:

    pass
class workflow_FieldValue:

    def __init__(self, value: str, workflow_FieldValue: "workflow_DefaultDocument" = None, workflow_FieldValue134: "workflow_Field" = None):
        self.value = value
        self.workflow_FieldValue = workflow_FieldValue
        self.workflow_FieldValue134 = workflow_FieldValue134
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def workflow_FieldValue134(self):
        return self.__workflow_FieldValue134

    @workflow_FieldValue134.setter
    def workflow_FieldValue134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_FieldValue__workflow_FieldValue134", None)
        self.__workflow_FieldValue134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Field135"):
                opp_val = getattr(old_value, "workflow_Field135", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Field135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Field135"):
                opp_val = getattr(value, "workflow_Field135", None)
                setattr(value, "workflow_Field135", self)

    @property
    def workflow_FieldValue(self):
        return self.__workflow_FieldValue

    @workflow_FieldValue.setter
    def workflow_FieldValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_FieldValue__workflow_FieldValue", None)
        self.__workflow_FieldValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DefaultDocument"):
                opp_val = getattr(old_value, "workflow_DefaultDocument", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DefaultDocument"):
                opp_val = getattr(value, "workflow_DefaultDocument", None)
                if opp_val is None:
                    setattr(value, "workflow_DefaultDocument", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Document:

    pass
class workflow_DefaultDocument(Document):

    def __init__(self, placeholder: bool, workflow_DefaultDocument: set["workflow_FieldValue"] = None, workflow_DefaultDocument132: set["workflow_EnumFieldValue"] = None):
        self.placeholder = placeholder
        self.workflow_DefaultDocument = workflow_DefaultDocument if workflow_DefaultDocument is not None else set()
        self.workflow_DefaultDocument132 = workflow_DefaultDocument132 if workflow_DefaultDocument132 is not None else set()
        
    @property
    def placeholder(self) -> bool:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: bool):
        self.__placeholder = placeholder

    @property
    def workflow_DefaultDocument(self):
        return self.__workflow_DefaultDocument

    @workflow_DefaultDocument.setter
    def workflow_DefaultDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DefaultDocument__workflow_DefaultDocument", None)
        self.__workflow_DefaultDocument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_FieldValue"):
                    opp_val = getattr(item, "workflow_FieldValue", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_FieldValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_FieldValue"):
                    opp_val = getattr(item, "workflow_FieldValue", None)
                    
                    setattr(item, "workflow_FieldValue", self)
                    

    @property
    def workflow_DefaultDocument132(self):
        return self.__workflow_DefaultDocument132

    @workflow_DefaultDocument132.setter
    def workflow_DefaultDocument132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DefaultDocument__workflow_DefaultDocument132", None)
        self.__workflow_DefaultDocument132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_EnumFieldValue"):
                    opp_val = getattr(item, "workflow_EnumFieldValue", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_EnumFieldValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_EnumFieldValue"):
                    opp_val = getattr(item, "workflow_EnumFieldValue", None)
                    
                    setattr(item, "workflow_EnumFieldValue", self)
                    

class Operator:

    pass
class workflow_UnequalToOperator(Operator):

    pass
class workflow_EqualToOperator(Operator):

    pass
class workflow_GreaterThanOperator(Operator):

    pass
class workflow_LessThanOperator(Operator):

    pass
class workflow_DotOperator(Operator):

    pass
class Atom:

    pass
class workflow_FieldAtom(Atom):

    pass
class workflow_EnumFieldAtom(Atom):

    pass
class workflow_EnumLiteralAtom(Atom):

    pass
class workflow_ConstantAtom(Atom):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class workflow_DocumentDescrAtom(Atom):

    pass
class Expression:

    pass
class workflow_Operator(Expression):

    pass
class workflow_Atom(Expression):

    pass
class DocumentDescriptor:

    pass
class workflow_DefaultDocumentDescriptor(DocumentDescriptor):

    pass
class RuntimeModelAspect:

    pass
class workflow_InformationRuntimeAspect(RuntimeModelAspect):

    pass
class workflow_EnumField:

    def __init__(self, name: str, workflow_EnumField: "workflow_DefaultDocumentType" = None, workflow_EnumField158: "workflow_EnumFieldValue" = None, workflow_EnumField163: "workflow_EnumFieldAtom" = None, workflow_EnumField152: set["workflow_EnumLiteral"] = None, workflow_EnumField154: "workflow_EnumLiteral" = None):
        self.name = name
        self.workflow_EnumField = workflow_EnumField
        self.workflow_EnumField158 = workflow_EnumField158
        self.workflow_EnumField163 = workflow_EnumField163
        self.workflow_EnumField152 = workflow_EnumField152 if workflow_EnumField152 is not None else set()
        self.workflow_EnumField154 = workflow_EnumField154
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_EnumField152(self):
        return self.__workflow_EnumField152

    @workflow_EnumField152.setter
    def workflow_EnumField152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumField__workflow_EnumField152", None)
        self.__workflow_EnumField152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_EnumLiteral"):
                    opp_val = getattr(item, "workflow_EnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_EnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_EnumLiteral"):
                    opp_val = getattr(item, "workflow_EnumLiteral", None)
                    
                    setattr(item, "workflow_EnumLiteral", self)
                    

    @property
    def workflow_EnumField154(self):
        return self.__workflow_EnumField154

    @workflow_EnumField154.setter
    def workflow_EnumField154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumField__workflow_EnumField154", None)
        self.__workflow_EnumField154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumLiteral155"):
                opp_val = getattr(old_value, "workflow_EnumLiteral155", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumLiteral155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumLiteral155"):
                opp_val = getattr(value, "workflow_EnumLiteral155", None)
                setattr(value, "workflow_EnumLiteral155", self)

    @property
    def workflow_EnumField158(self):
        return self.__workflow_EnumField158

    @workflow_EnumField158.setter
    def workflow_EnumField158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumField__workflow_EnumField158", None)
        self.__workflow_EnumField158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumFieldValue157"):
                opp_val = getattr(old_value, "workflow_EnumFieldValue157", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumFieldValue157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumFieldValue157"):
                opp_val = getattr(value, "workflow_EnumFieldValue157", None)
                setattr(value, "workflow_EnumFieldValue157", self)

    @property
    def workflow_EnumField163(self):
        return self.__workflow_EnumField163

    @workflow_EnumField163.setter
    def workflow_EnumField163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumField__workflow_EnumField163", None)
        self.__workflow_EnumField163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_EnumFieldAtom"):
                opp_val = getattr(old_value, "workflow_EnumFieldAtom", None)
                if opp_val == self:
                    setattr(old_value, "workflow_EnumFieldAtom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_EnumFieldAtom"):
                opp_val = getattr(value, "workflow_EnumFieldAtom", None)
                setattr(value, "workflow_EnumFieldAtom", self)

    @property
    def workflow_EnumField(self):
        return self.__workflow_EnumField

    @workflow_EnumField.setter
    def workflow_EnumField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_EnumField__workflow_EnumField", None)
        self.__workflow_EnumField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DefaultDocumentType129"):
                opp_val = getattr(old_value, "workflow_DefaultDocumentType129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DefaultDocumentType129"):
                opp_val = getattr(value, "workflow_DefaultDocumentType129", None)
                if opp_val is None:
                    setattr(value, "workflow_DefaultDocumentType129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_Field:

    def __init__(self, name: str, workflow_Field: "workflow_DefaultDocumentType" = None, workflow_Field148: "workflow_FieldAtom" = None, workflow_Field135: "workflow_FieldValue" = None):
        self.name = name
        self.workflow_Field = workflow_Field
        self.workflow_Field148 = workflow_Field148
        self.workflow_Field135 = workflow_Field135
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Field148(self):
        return self.__workflow_Field148

    @workflow_Field148.setter
    def workflow_Field148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Field__workflow_Field148", None)
        self.__workflow_Field148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_FieldAtom"):
                opp_val = getattr(old_value, "workflow_FieldAtom", None)
                if opp_val == self:
                    setattr(old_value, "workflow_FieldAtom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_FieldAtom"):
                opp_val = getattr(value, "workflow_FieldAtom", None)
                setattr(value, "workflow_FieldAtom", self)

    @property
    def workflow_Field135(self):
        return self.__workflow_Field135

    @workflow_Field135.setter
    def workflow_Field135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Field__workflow_Field135", None)
        self.__workflow_Field135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_FieldValue134"):
                opp_val = getattr(old_value, "workflow_FieldValue134", None)
                if opp_val == self:
                    setattr(old_value, "workflow_FieldValue134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_FieldValue134"):
                opp_val = getattr(value, "workflow_FieldValue134", None)
                setattr(value, "workflow_FieldValue134", self)

    @property
    def workflow_Field(self):
        return self.__workflow_Field

    @workflow_Field.setter
    def workflow_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Field__workflow_Field", None)
        self.__workflow_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DefaultDocumentType"):
                opp_val = getattr(old_value, "workflow_DefaultDocumentType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DefaultDocumentType"):
                opp_val = getattr(value, "workflow_DefaultDocumentType", None)
                if opp_val is None:
                    setattr(value, "workflow_DefaultDocumentType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DocumentType:

    pass
class workflow_DefaultDocumentType(DocumentType):

    pass
class workflow_Expression:

    pass
class workflow_RuntimeGlobalAspect(ABC):

    pass
class ModelAspect:

    pass
class workflow_ControlAspect(ModelAspect):

    pass
class workflow_InformationAspect(ModelAspect):

    pass
class workflow_OrganisationAspect(ModelAspect):

    pass
class workflow_Document(ABC):

    def __init__(self, name: str, id: str, workflow_Document: "workflow_ActivityI" = None, workflow_Document79: "workflow_ActivityI" = None, workflow_Document81: "workflow_DocumentType" = None, workflow_Document143: "workflow_String2DocumentMap" = None, workflow_Document177: "workflow_DocumentContainer" = None):
        self.name = name
        self.id = id
        self.workflow_Document = workflow_Document
        self.workflow_Document79 = workflow_Document79
        self.workflow_Document81 = workflow_Document81
        self.workflow_Document143 = workflow_Document143
        self.workflow_Document177 = workflow_Document177
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def workflow_Document143(self):
        return self.__workflow_Document143

    @workflow_Document143.setter
    def workflow_Document143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Document__workflow_Document143", None)
        self.__workflow_Document143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_String2DocumentMap142"):
                opp_val = getattr(old_value, "workflow_String2DocumentMap142", None)
                if opp_val == self:
                    setattr(old_value, "workflow_String2DocumentMap142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_String2DocumentMap142"):
                opp_val = getattr(value, "workflow_String2DocumentMap142", None)
                setattr(value, "workflow_String2DocumentMap142", self)

    @property
    def workflow_Document81(self):
        return self.__workflow_Document81

    @workflow_Document81.setter
    def workflow_Document81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Document__workflow_Document81", None)
        self.__workflow_Document81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentType82"):
                opp_val = getattr(old_value, "workflow_DocumentType82", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentType82"):
                opp_val = getattr(value, "workflow_DocumentType82", None)
                setattr(value, "workflow_DocumentType82", self)

    @property
    def workflow_Document(self):
        return self.__workflow_Document

    @workflow_Document.setter
    def workflow_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Document__workflow_Document", None)
        self.__workflow_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ActivityI"):
                opp_val = getattr(old_value, "workflow_ActivityI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ActivityI"):
                opp_val = getattr(value, "workflow_ActivityI", None)
                if opp_val is None:
                    setattr(value, "workflow_ActivityI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Document79(self):
        return self.__workflow_Document79

    @workflow_Document79.setter
    def workflow_Document79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Document__workflow_Document79", None)
        self.__workflow_Document79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ActivityI78"):
                opp_val = getattr(old_value, "workflow_ActivityI78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ActivityI78"):
                opp_val = getattr(value, "workflow_ActivityI78", None)
                if opp_val is None:
                    setattr(value, "workflow_ActivityI78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Document177(self):
        return self.__workflow_Document177

    @workflow_Document177.setter
    def workflow_Document177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Document__workflow_Document177", None)
        self.__workflow_Document177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentContainer"):
                opp_val = getattr(old_value, "workflow_DocumentContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentContainer"):
                opp_val = getattr(value, "workflow_DocumentContainer", None)
                if opp_val is None:
                    setattr(value, "workflow_DocumentContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_RuntimeModelAspect(ABC):

    pass
class workflow_TaskAspect(ABC):

    pass
class workflow_ProcessAspect(ABC):

    pass
class workflow_ModelAspect(ABC):

    pass
class workflow_String2DocumentMap:

    def __init__(self, key: str, workflow_String2DocumentMap: "workflow_CaseI" = None, workflow_String2DocumentMap142: "workflow_Document" = None):
        self.key = key
        self.workflow_String2DocumentMap = workflow_String2DocumentMap
        self.workflow_String2DocumentMap142 = workflow_String2DocumentMap142
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def workflow_String2DocumentMap142(self):
        return self.__workflow_String2DocumentMap142

    @workflow_String2DocumentMap142.setter
    def workflow_String2DocumentMap142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_String2DocumentMap__workflow_String2DocumentMap142", None)
        self.__workflow_String2DocumentMap142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Document143"):
                opp_val = getattr(old_value, "workflow_Document143", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Document143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Document143"):
                opp_val = getattr(value, "workflow_Document143", None)
                setattr(value, "workflow_Document143", self)

    @property
    def workflow_String2DocumentMap(self):
        return self.__workflow_String2DocumentMap

    @workflow_String2DocumentMap.setter
    def workflow_String2DocumentMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_String2DocumentMap__workflow_String2DocumentMap", None)
        self.__workflow_String2DocumentMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_CaseI"):
                opp_val = getattr(old_value, "workflow_CaseI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_CaseI"):
                opp_val = getattr(value, "workflow_CaseI", None)
                if opp_val is None:
                    setattr(value, "workflow_CaseI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class State:

    pass
class workflow_Marking(State):

    pass
class workflow_DocumentType(ABC):

    def __init__(self, name: str, workflow_DocumentType: "workflow_DocumentDescriptor" = None, workflow_DocumentType82: "workflow_Document" = None, workflow_DocumentType140: "workflow_ProcessDocument" = None, workflow_DocumentType175: "workflow_DocumentTypeContainer" = None):
        self.name = name
        self.workflow_DocumentType = workflow_DocumentType
        self.workflow_DocumentType82 = workflow_DocumentType82
        self.workflow_DocumentType140 = workflow_DocumentType140
        self.workflow_DocumentType175 = workflow_DocumentType175
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_DocumentType82(self):
        return self.__workflow_DocumentType82

    @workflow_DocumentType82.setter
    def workflow_DocumentType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentType__workflow_DocumentType82", None)
        self.__workflow_DocumentType82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Document81"):
                opp_val = getattr(old_value, "workflow_Document81", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Document81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Document81"):
                opp_val = getattr(value, "workflow_Document81", None)
                setattr(value, "workflow_Document81", self)

    @property
    def workflow_DocumentType140(self):
        return self.__workflow_DocumentType140

    @workflow_DocumentType140.setter
    def workflow_DocumentType140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentType__workflow_DocumentType140", None)
        self.__workflow_DocumentType140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ProcessDocument139"):
                opp_val = getattr(old_value, "workflow_ProcessDocument139", None)
                if opp_val == self:
                    setattr(old_value, "workflow_ProcessDocument139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ProcessDocument139"):
                opp_val = getattr(value, "workflow_ProcessDocument139", None)
                setattr(value, "workflow_ProcessDocument139", self)

    @property
    def workflow_DocumentType(self):
        return self.__workflow_DocumentType

    @workflow_DocumentType.setter
    def workflow_DocumentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentType__workflow_DocumentType", None)
        self.__workflow_DocumentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentDescriptor72"):
                opp_val = getattr(old_value, "workflow_DocumentDescriptor72", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentDescriptor72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentDescriptor72"):
                opp_val = getattr(value, "workflow_DocumentDescriptor72", None)
                setattr(value, "workflow_DocumentDescriptor72", self)

    @property
    def workflow_DocumentType175(self):
        return self.__workflow_DocumentType175

    @workflow_DocumentType175.setter
    def workflow_DocumentType175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentType__workflow_DocumentType175", None)
        self.__workflow_DocumentType175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentTypeContainer"):
                opp_val = getattr(old_value, "workflow_DocumentTypeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentTypeContainer"):
                opp_val = getattr(value, "workflow_DocumentTypeContainer", None)
                if opp_val is None:
                    setattr(value, "workflow_DocumentTypeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_DocumentCondition(ABC):

    def __init__(self, name: str, workflow_DocumentCondition: "workflow_TaskI" = None, workflow_DocumentCondition70: "workflow_TaskI" = None):
        self.name = name
        self.workflow_DocumentCondition = workflow_DocumentCondition
        self.workflow_DocumentCondition70 = workflow_DocumentCondition70
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_DocumentCondition(self):
        return self.__workflow_DocumentCondition

    @workflow_DocumentCondition.setter
    def workflow_DocumentCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentCondition__workflow_DocumentCondition", None)
        self.__workflow_DocumentCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskI67"):
                opp_val = getattr(old_value, "workflow_TaskI67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskI67"):
                opp_val = getattr(value, "workflow_TaskI67", None)
                if opp_val is None:
                    setattr(value, "workflow_TaskI67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_DocumentCondition70(self):
        return self.__workflow_DocumentCondition70

    @workflow_DocumentCondition70.setter
    def workflow_DocumentCondition70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentCondition__workflow_DocumentCondition70", None)
        self.__workflow_DocumentCondition70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskI69"):
                opp_val = getattr(old_value, "workflow_TaskI69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskI69"):
                opp_val = getattr(value, "workflow_TaskI69", None)
                if opp_val is None:
                    setattr(value, "workflow_TaskI69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_DocumentDescriptor(ABC):

    def __init__(self, name: str, workflow_DocumentDescriptor: "workflow_TaskI" = None, workflow_DocumentDescriptor65: "workflow_TaskI" = None, workflow_DocumentDescriptor72: "workflow_DocumentType" = None, workflow_DocumentDescriptor74: "workflow_ProcessDocument" = None, workflow_DocumentDescriptor146: "workflow_DocumentDescrAtom" = None):
        self.name = name
        self.workflow_DocumentDescriptor = workflow_DocumentDescriptor
        self.workflow_DocumentDescriptor65 = workflow_DocumentDescriptor65
        self.workflow_DocumentDescriptor72 = workflow_DocumentDescriptor72
        self.workflow_DocumentDescriptor74 = workflow_DocumentDescriptor74
        self.workflow_DocumentDescriptor146 = workflow_DocumentDescriptor146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_DocumentDescriptor72(self):
        return self.__workflow_DocumentDescriptor72

    @workflow_DocumentDescriptor72.setter
    def workflow_DocumentDescriptor72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentDescriptor__workflow_DocumentDescriptor72", None)
        self.__workflow_DocumentDescriptor72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentType"):
                opp_val = getattr(old_value, "workflow_DocumentType", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentType"):
                opp_val = getattr(value, "workflow_DocumentType", None)
                setattr(value, "workflow_DocumentType", self)

    @property
    def workflow_DocumentDescriptor65(self):
        return self.__workflow_DocumentDescriptor65

    @workflow_DocumentDescriptor65.setter
    def workflow_DocumentDescriptor65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentDescriptor__workflow_DocumentDescriptor65", None)
        self.__workflow_DocumentDescriptor65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskI64"):
                opp_val = getattr(old_value, "workflow_TaskI64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskI64"):
                opp_val = getattr(value, "workflow_TaskI64", None)
                if opp_val is None:
                    setattr(value, "workflow_TaskI64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_DocumentDescriptor(self):
        return self.__workflow_DocumentDescriptor

    @workflow_DocumentDescriptor.setter
    def workflow_DocumentDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentDescriptor__workflow_DocumentDescriptor", None)
        self.__workflow_DocumentDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskI"):
                opp_val = getattr(old_value, "workflow_TaskI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskI"):
                opp_val = getattr(value, "workflow_TaskI", None)
                if opp_val is None:
                    setattr(value, "workflow_TaskI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_DocumentDescriptor74(self):
        return self.__workflow_DocumentDescriptor74

    @workflow_DocumentDescriptor74.setter
    def workflow_DocumentDescriptor74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentDescriptor__workflow_DocumentDescriptor74", None)
        self.__workflow_DocumentDescriptor74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ProcessDocument75"):
                opp_val = getattr(old_value, "workflow_ProcessDocument75", None)
                if opp_val == self:
                    setattr(old_value, "workflow_ProcessDocument75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ProcessDocument75"):
                opp_val = getattr(value, "workflow_ProcessDocument75", None)
                setattr(value, "workflow_ProcessDocument75", self)

    @property
    def workflow_DocumentDescriptor146(self):
        return self.__workflow_DocumentDescriptor146

    @workflow_DocumentDescriptor146.setter
    def workflow_DocumentDescriptor146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_DocumentDescriptor__workflow_DocumentDescriptor146", None)
        self.__workflow_DocumentDescriptor146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentDescrAtom"):
                opp_val = getattr(old_value, "workflow_DocumentDescrAtom", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentDescrAtom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentDescrAtom"):
                opp_val = getattr(value, "workflow_DocumentDescrAtom", None)
                setattr(value, "workflow_DocumentDescrAtom", self)

class workflow_ProcessDocument:

    def __init__(self, name: str, workflow_ProcessDocument: "workflow_Information" = None, workflow_ProcessDocument75: "workflow_DocumentDescriptor" = None, workflow_ProcessDocument139: "workflow_DocumentType" = None):
        self.name = name
        self.workflow_ProcessDocument = workflow_ProcessDocument
        self.workflow_ProcessDocument75 = workflow_ProcessDocument75
        self.workflow_ProcessDocument139 = workflow_ProcessDocument139
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_ProcessDocument139(self):
        return self.__workflow_ProcessDocument139

    @workflow_ProcessDocument139.setter
    def workflow_ProcessDocument139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcessDocument__workflow_ProcessDocument139", None)
        self.__workflow_ProcessDocument139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentType140"):
                opp_val = getattr(old_value, "workflow_DocumentType140", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentType140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentType140"):
                opp_val = getattr(value, "workflow_DocumentType140", None)
                setattr(value, "workflow_DocumentType140", self)

    @property
    def workflow_ProcessDocument(self):
        return self.__workflow_ProcessDocument

    @workflow_ProcessDocument.setter
    def workflow_ProcessDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcessDocument__workflow_ProcessDocument", None)
        self.__workflow_ProcessDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Information"):
                opp_val = getattr(old_value, "workflow_Information", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Information"):
                opp_val = getattr(value, "workflow_Information", None)
                if opp_val is None:
                    setattr(value, "workflow_Information", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_ProcessDocument75(self):
        return self.__workflow_ProcessDocument75

    @workflow_ProcessDocument75.setter
    def workflow_ProcessDocument75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcessDocument__workflow_ProcessDocument75", None)
        self.__workflow_ProcessDocument75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_DocumentDescriptor74"):
                opp_val = getattr(old_value, "workflow_DocumentDescriptor74", None)
                if opp_val == self:
                    setattr(old_value, "workflow_DocumentDescriptor74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_DocumentDescriptor74"):
                opp_val = getattr(value, "workflow_DocumentDescriptor74", None)
                setattr(value, "workflow_DocumentDescriptor74", self)

class workflow_GlobalAspect(ABC):

    pass
class workflow_CoreModel:

    def __init__(self, name: str, CoreModel: "workflow_ModelRegistry" = None, workflow_CoreModel: set["workflow_ModelAspect"] = None, coreModel: "workflow_Process" = None, coreModels: "workflow_ModelRegistry" = None, workflow_CoreModel118: "workflow_RuntimeCoreModel" = None, CoreModel108: "workflow_Process" = None):
        self.name = name
        self.CoreModel = CoreModel
        self.workflow_CoreModel = workflow_CoreModel if workflow_CoreModel is not None else set()
        self.coreModel = coreModel
        self.coreModels = coreModels
        self.workflow_CoreModel118 = workflow_CoreModel118
        self.CoreModel108 = CoreModel108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def coreModels(self):
        return self.__coreModels

    @coreModels.setter
    def coreModels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__coreModels", None)
        self.__coreModels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelRegistry"):
                opp_val = getattr(old_value, "ModelRegistry", None)
                if opp_val == self:
                    setattr(old_value, "ModelRegistry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelRegistry"):
                opp_val = getattr(value, "ModelRegistry", None)
                setattr(value, "ModelRegistry", self)

    @property
    def workflow_CoreModel(self):
        return self.__workflow_CoreModel

    @workflow_CoreModel.setter
    def workflow_CoreModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__workflow_CoreModel", None)
        self.__workflow_CoreModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_ModelAspect100"):
                    opp_val = getattr(item, "workflow_ModelAspect100", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_ModelAspect100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_ModelAspect100"):
                    opp_val = getattr(item, "workflow_ModelAspect100", None)
                    
                    setattr(item, "workflow_ModelAspect100", self)
                    

    @property
    def CoreModel(self):
        return self.__CoreModel

    @CoreModel.setter
    def CoreModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__CoreModel", None)
        self.__CoreModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelRegistry58"):
                opp_val = getattr(old_value, "modelRegistry58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelRegistry58"):
                opp_val = getattr(value, "modelRegistry58", None)
                if opp_val is None:
                    setattr(value, "modelRegistry58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coreModel(self):
        return self.__coreModel

    @coreModel.setter
    def coreModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__coreModel", None)
        self.__coreModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process102"):
                opp_val = getattr(old_value, "Process102", None)
                if opp_val == self:
                    setattr(old_value, "Process102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process102"):
                opp_val = getattr(value, "Process102", None)
                setattr(value, "Process102", self)

    @property
    def CoreModel108(self):
        return self.__CoreModel108

    @CoreModel108.setter
    def CoreModel108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__CoreModel108", None)
        self.__CoreModel108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process"):
                opp_val = getattr(old_value, "process", None)
                if opp_val == self:
                    setattr(old_value, "process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process"):
                opp_val = getattr(value, "process", None)
                setattr(value, "process", self)

    @property
    def workflow_CoreModel118(self):
        return self.__workflow_CoreModel118

    @workflow_CoreModel118.setter
    def workflow_CoreModel118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CoreModel__workflow_CoreModel118", None)
        self.__workflow_CoreModel118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_RuntimeCoreModel117"):
                opp_val = getattr(old_value, "workflow_RuntimeCoreModel117", None)
                if opp_val == self:
                    setattr(old_value, "workflow_RuntimeCoreModel117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_RuntimeCoreModel117"):
                opp_val = getattr(value, "workflow_RuntimeCoreModel117", None)
                setattr(value, "workflow_RuntimeCoreModel117", self)

class workflow_WorkflowEngine:

    pass
class workflow_ModelRegistry:

    pass
class workflow_Token:

    pass
class workflow_RuntimeInformation:

    def __init__(self, caseIdCount: str):
        self.caseIdCount = caseIdCount
        
    @property
    def caseIdCount(self) -> str:
        return self.__caseIdCount

    @caseIdCount.setter
    def caseIdCount(self, caseIdCount: str):
        self.__caseIdCount = caseIdCount

class TaskC:

    pass
class workflow_Transition(TaskC):

    pass
class workflow_Place:

    def __init__(self, name: str, workflow_Place: "workflow_PetriNet" = None, workflow_Place30: "workflow_PetriNet" = None, workflow_Place33: "workflow_PetriNet" = None, Place: "workflow_Arc" = None, Place39: "workflow_Arc" = None, workflow_Place55: "workflow_Token" = None, targetPlace: set["workflow_Arc"] = None, sourcePlace: set["workflow_Arc"] = None):
        self.name = name
        self.workflow_Place = workflow_Place
        self.workflow_Place30 = workflow_Place30
        self.workflow_Place33 = workflow_Place33
        self.Place = Place
        self.Place39 = Place39
        self.workflow_Place55 = workflow_Place55
        self.targetPlace = targetPlace if targetPlace is not None else set()
        self.sourcePlace = sourcePlace if sourcePlace is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Place33(self):
        return self.__workflow_Place33

    @workflow_Place33.setter
    def workflow_Place33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__workflow_Place33", None)
        self.__workflow_Place33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_PetriNet32"):
                opp_val = getattr(old_value, "workflow_PetriNet32", None)
                if opp_val == self:
                    setattr(old_value, "workflow_PetriNet32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_PetriNet32"):
                opp_val = getattr(value, "workflow_PetriNet32", None)
                setattr(value, "workflow_PetriNet32", self)

    @property
    def targetPlace(self):
        return self.__targetPlace

    @targetPlace.setter
    def targetPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__targetPlace", None)
        self.__targetPlace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc46"):
                    opp_val = getattr(item, "Arc46", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc46"):
                    opp_val = getattr(item, "Arc46", None)
                    
                    setattr(item, "Arc46", self)
                    

    @property
    def workflow_Place(self):
        return self.__workflow_Place

    @workflow_Place.setter
    def workflow_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__workflow_Place", None)
        self.__workflow_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_PetriNet27"):
                opp_val = getattr(old_value, "workflow_PetriNet27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_PetriNet27"):
                opp_val = getattr(value, "workflow_PetriNet27", None)
                if opp_val is None:
                    setattr(value, "workflow_PetriNet27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place39(self):
        return self.__Place39

    @Place39.setter
    def Place39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__Place39", None)
        self.__Place39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def workflow_Place30(self):
        return self.__workflow_Place30

    @workflow_Place30.setter
    def workflow_Place30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__workflow_Place30", None)
        self.__workflow_Place30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_PetriNet29"):
                opp_val = getattr(old_value, "workflow_PetriNet29", None)
                if opp_val == self:
                    setattr(old_value, "workflow_PetriNet29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_PetriNet29"):
                opp_val = getattr(value, "workflow_PetriNet29", None)
                setattr(value, "workflow_PetriNet29", self)

    @property
    def workflow_Place55(self):
        return self.__workflow_Place55

    @workflow_Place55.setter
    def workflow_Place55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__workflow_Place55", None)
        self.__workflow_Place55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Token54"):
                opp_val = getattr(old_value, "workflow_Token54", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Token54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Token54"):
                opp_val = getattr(value, "workflow_Token54", None)
                setattr(value, "workflow_Token54", self)

    @property
    def sourcePlace(self):
        return self.__sourcePlace

    @sourcePlace.setter
    def sourcePlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__sourcePlace", None)
        self.__sourcePlace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc48"):
                    opp_val = getattr(item, "Arc48", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc48"):
                    opp_val = getattr(item, "Arc48", None)
                    
                    setattr(item, "Arc48", self)
                    

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

class workflow_Arc:

    def __init__(self, name: str, workflow_Arc: "workflow_PetriNet" = None, Arc: "workflow_Transition" = None, Arc36: "workflow_Transition" = None, out: "workflow_Place" = None, in: "workflow_Place" = None, out41: "workflow_Transition" = None, in43: "workflow_Transition" = None, Arc46: "workflow_Place" = None, Arc48: "workflow_Place" = None):
        self.name = name
        self.workflow_Arc = workflow_Arc
        self.Arc = Arc
        self.Arc36 = Arc36
        self.out = out
        self.in = in
        self.out41 = out41
        self.in43 = in43
        self.Arc46 = Arc46
        self.Arc48 = Arc48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arc48(self):
        return self.__Arc48

    @Arc48.setter
    def Arc48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__Arc48", None)
        self.__Arc48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcePlace"):
                opp_val = getattr(old_value, "sourcePlace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcePlace"):
                opp_val = getattr(value, "sourcePlace", None)
                if opp_val is None:
                    setattr(value, "sourcePlace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc36(self):
        return self.__Arc36

    @Arc36.setter
    def Arc36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__Arc36", None)
        self.__Arc36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetTransition"):
                opp_val = getattr(old_value, "targetTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetTransition"):
                opp_val = getattr(value, "targetTransition", None)
                if opp_val is None:
                    setattr(value, "targetTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def in43(self):
        return self.__in43

    @in43.setter
    def in43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__in43", None)
        self.__in43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition44"):
                opp_val = getattr(old_value, "Transition44", None)
                if opp_val == self:
                    setattr(old_value, "Transition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition44"):
                opp_val = getattr(value, "Transition44", None)
                setattr(value, "Transition44", self)

    @property
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Place39"):
                opp_val = getattr(old_value, "Place39", None)
                if opp_val == self:
                    setattr(old_value, "Place39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Place39"):
                opp_val = getattr(value, "Place39", None)
                setattr(value, "Place39", self)

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__out", None)
        self.__out = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Place"):
                opp_val = getattr(old_value, "Place", None)
                if opp_val == self:
                    setattr(old_value, "Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Place"):
                opp_val = getattr(value, "Place", None)
                setattr(value, "Place", self)

    @property
    def workflow_Arc(self):
        return self.__workflow_Arc

    @workflow_Arc.setter
    def workflow_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__workflow_Arc", None)
        self.__workflow_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_PetriNet"):
                opp_val = getattr(old_value, "workflow_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_PetriNet"):
                opp_val = getattr(value, "workflow_PetriNet", None)
                if opp_val is None:
                    setattr(value, "workflow_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceTransition"):
                opp_val = getattr(old_value, "sourceTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceTransition"):
                opp_val = getattr(value, "sourceTransition", None)
                if opp_val is None:
                    setattr(value, "sourceTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc46(self):
        return self.__Arc46

    @Arc46.setter
    def Arc46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__Arc46", None)
        self.__Arc46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetPlace"):
                opp_val = getattr(old_value, "targetPlace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetPlace"):
                opp_val = getattr(value, "targetPlace", None)
                if opp_val is None:
                    setattr(value, "targetPlace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def out41(self):
        return self.__out41

    @out41.setter
    def out41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Arc__out41", None)
        self.__out41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

class Control:

    pass
class workflow_PetriNet(Control):

    pass
class workflow_State(ABC):

    pass
class CaseAspect:

    pass
class workflow_CaseI(CaseAspect):

    pass
class workflow_CaseO(CaseAspect):

    pass
class ProcessAspect:

    pass
class workflow_Information(ProcessAspect):

    pass
class workflow_ProcessO(ProcessAspect):

    pass
class workflow_Control(ProcessAspect):

    pass
class workflow_CaseC(CaseAspect):

    pass
class workflow_Role:

    def __init__(self, name: str, workflow_Role17: "workflow_Agent" = None, workflow_Role: "workflow_TaskO" = None, workflow_Role21: "workflow_Agent" = None, workflow_Role126: "workflow_ProcessO" = None, workflow_Role169: "workflow_Organisation" = None):
        self.name = name
        self.workflow_Role17 = workflow_Role17
        self.workflow_Role = workflow_Role
        self.workflow_Role21 = workflow_Role21
        self.workflow_Role126 = workflow_Role126
        self.workflow_Role169 = workflow_Role169
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Role169(self):
        return self.__workflow_Role169

    @workflow_Role169.setter
    def workflow_Role169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Role__workflow_Role169", None)
        self.__workflow_Role169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Organisation"):
                opp_val = getattr(old_value, "workflow_Organisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Organisation"):
                opp_val = getattr(value, "workflow_Organisation", None)
                if opp_val is None:
                    setattr(value, "workflow_Organisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Role126(self):
        return self.__workflow_Role126

    @workflow_Role126.setter
    def workflow_Role126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Role__workflow_Role126", None)
        self.__workflow_Role126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ProcessO"):
                opp_val = getattr(old_value, "workflow_ProcessO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ProcessO"):
                opp_val = getattr(value, "workflow_ProcessO", None)
                if opp_val is None:
                    setattr(value, "workflow_ProcessO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Role17(self):
        return self.__workflow_Role17

    @workflow_Role17.setter
    def workflow_Role17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Role__workflow_Role17", None)
        self.__workflow_Role17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Agent"):
                opp_val = getattr(old_value, "workflow_Agent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Agent"):
                opp_val = getattr(value, "workflow_Agent", None)
                if opp_val is None:
                    setattr(value, "workflow_Agent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Role(self):
        return self.__workflow_Role

    @workflow_Role.setter
    def workflow_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Role__workflow_Role", None)
        self.__workflow_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskO"):
                opp_val = getattr(old_value, "workflow_TaskO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskO"):
                opp_val = getattr(value, "workflow_TaskO", None)
                if opp_val is None:
                    setattr(value, "workflow_TaskO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Role21(self):
        return self.__workflow_Role21

    @workflow_Role21.setter
    def workflow_Role21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Role__workflow_Role21", None)
        self.__workflow_Role21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Agent20"):
                opp_val = getattr(old_value, "workflow_Agent20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Agent20"):
                opp_val = getattr(value, "workflow_Agent20", None)
                if opp_val is None:
                    setattr(value, "workflow_Agent20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TaskAspect:

    pass
class workflow_TaskI(TaskAspect):

    pass
class workflow_TaskC(TaskAspect):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class workflow_TaskO(TaskAspect):

    def __init__(self, name: str, workflow_TaskO: set["workflow_Role"] = None, workflow_TaskO3: "workflow_TaskO" = None, workflow_TaskO1: "workflow_TaskO" = None):
        self.name = name
        self.workflow_TaskO = workflow_TaskO if workflow_TaskO is not None else set()
        self.workflow_TaskO3 = workflow_TaskO3
        self.workflow_TaskO1 = workflow_TaskO1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_TaskO(self):
        return self.__workflow_TaskO

    @workflow_TaskO.setter
    def workflow_TaskO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_TaskO__workflow_TaskO", None)
        self.__workflow_TaskO = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Role"):
                    opp_val = getattr(item, "workflow_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Role"):
                    opp_val = getattr(item, "workflow_Role", None)
                    
                    setattr(item, "workflow_Role", self)
                    

    @property
    def workflow_TaskO1(self):
        return self.__workflow_TaskO1

    @workflow_TaskO1.setter
    def workflow_TaskO1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_TaskO__workflow_TaskO1", None)
        self.__workflow_TaskO1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskO3"):
                opp_val = getattr(old_value, "workflow_TaskO3", None)
                if opp_val == self:
                    setattr(old_value, "workflow_TaskO3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskO3"):
                opp_val = getattr(value, "workflow_TaskO3", None)
                setattr(value, "workflow_TaskO3", self)

    @property
    def workflow_TaskO3(self):
        return self.__workflow_TaskO3

    @workflow_TaskO3.setter
    def workflow_TaskO3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_TaskO__workflow_TaskO3", None)
        self.__workflow_TaskO3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_TaskO1"):
                opp_val = getattr(old_value, "workflow_TaskO1", None)
                if opp_val == self:
                    setattr(old_value, "workflow_TaskO1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_TaskO1"):
                opp_val = getattr(value, "workflow_TaskO1", None)
                setattr(value, "workflow_TaskO1", self)

class workflow_Task:

    def __init__(self, name: str, workflow_Task: "workflow_Activity" = None, Task: "workflow_TaskAspect" = None, core112: set["workflow_TaskAspect"] = None, workflow_Task106: "workflow_Process" = None):
        self.name = name
        self.workflow_Task = workflow_Task
        self.Task = Task
        self.core112 = core112 if core112 is not None else set()
        self.workflow_Task106 = workflow_Task106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def core112(self):
        return self.__core112

    @core112.setter
    def core112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Task__core112", None)
        self.__core112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskAspect"):
                    opp_val = getattr(item, "TaskAspect", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskAspect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskAspect"):
                    opp_val = getattr(item, "TaskAspect", None)
                    
                    setattr(item, "TaskAspect", self)
                    

    @property
    def workflow_Task106(self):
        return self.__workflow_Task106

    @workflow_Task106.setter
    def workflow_Task106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Task__workflow_Task106", None)
        self.__workflow_Task106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Process105"):
                opp_val = getattr(old_value, "workflow_Process105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Process105"):
                opp_val = getattr(value, "workflow_Process105", None)
                if opp_val is None:
                    setattr(value, "workflow_Process105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Task(self):
        return self.__Task

    @Task.setter
    def Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Task__Task", None)
        self.__Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspects89"):
                opp_val = getattr(old_value, "aspects89", None)
                if opp_val == self:
                    setattr(old_value, "aspects89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspects89"):
                opp_val = getattr(value, "aspects89", None)
                setattr(value, "aspects89", self)

    @property
    def workflow_Task(self):
        return self.__workflow_Task

    @workflow_Task.setter
    def workflow_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Task__workflow_Task", None)
        self.__workflow_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Activity13"):
                opp_val = getattr(old_value, "workflow_Activity13", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Activity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Activity13"):
                opp_val = getattr(value, "workflow_Activity13", None)
                setattr(value, "workflow_Activity13", self)

class workflow_ActivityAspect(ABC):

    pass
class workflow_RuntimeCoreModel:

    pass
class workflow_Process:

    def __init__(self, name: str, workflow_Process: "workflow_Case" = None, Process: "workflow_ProcessAspect" = None, Process102: "workflow_CoreModel" = None, workflow_Process105: set["workflow_Task"] = None, process: "workflow_CoreModel" = None, core110: set["workflow_ProcessAspect"] = None):
        self.name = name
        self.workflow_Process = workflow_Process
        self.Process = Process
        self.Process102 = Process102
        self.workflow_Process105 = workflow_Process105 if workflow_Process105 is not None else set()
        self.process = process
        self.core110 = core110 if core110 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Process(self):
        return self.__workflow_Process

    @workflow_Process.setter
    def workflow_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__workflow_Process", None)
        self.__workflow_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Case8"):
                opp_val = getattr(old_value, "workflow_Case8", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Case8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Case8"):
                opp_val = getattr(value, "workflow_Case8", None)
                setattr(value, "workflow_Case8", self)

    @property
    def Process102(self):
        return self.__Process102

    @Process102.setter
    def Process102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__Process102", None)
        self.__Process102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coreModel"):
                opp_val = getattr(old_value, "coreModel", None)
                if opp_val == self:
                    setattr(old_value, "coreModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coreModel"):
                opp_val = getattr(value, "coreModel", None)
                setattr(value, "coreModel", self)

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__process", None)
        self.__process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoreModel108"):
                opp_val = getattr(old_value, "CoreModel108", None)
                if opp_val == self:
                    setattr(old_value, "CoreModel108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoreModel108"):
                opp_val = getattr(value, "CoreModel108", None)
                setattr(value, "CoreModel108", self)

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspects"):
                opp_val = getattr(old_value, "aspects", None)
                if opp_val == self:
                    setattr(old_value, "aspects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspects"):
                opp_val = getattr(value, "aspects", None)
                setattr(value, "aspects", self)

    @property
    def workflow_Process105(self):
        return self.__workflow_Process105

    @workflow_Process105.setter
    def workflow_Process105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__workflow_Process105", None)
        self.__workflow_Process105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Task106"):
                    opp_val = getattr(item, "workflow_Task106", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Task106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Task106"):
                    opp_val = getattr(item, "workflow_Task106", None)
                    
                    setattr(item, "workflow_Task106", self)
                    

    @property
    def core110(self):
        return self.__core110

    @core110.setter
    def core110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Process__core110", None)
        self.__core110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcessAspect"):
                    opp_val = getattr(item, "ProcessAspect", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessAspect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessAspect"):
                    opp_val = getattr(item, "ProcessAspect", None)
                    
                    setattr(item, "ProcessAspect", self)
                    

class workflow_Activity:

    def __init__(self, started: bool, finished: bool, workflow_Activity: "workflow_Case" = None, core11: set["workflow_ActivityAspect"] = None, workflow_Activity13: "workflow_Task" = None, workflow_Activity15: "workflow_ActivityAspect" = None, Activity: "workflow_ActivityAspect" = None):
        self.started = started
        self.finished = finished
        self.workflow_Activity = workflow_Activity
        self.core11 = core11 if core11 is not None else set()
        self.workflow_Activity13 = workflow_Activity13
        self.workflow_Activity15 = workflow_Activity15
        self.Activity = Activity
        
    @property
    def started(self) -> bool:
        return self.__started

    @started.setter
    def started(self, started: bool):
        self.__started = started

    @property
    def finished(self) -> bool:
        return self.__finished

    @finished.setter
    def finished(self, finished: bool):
        self.__finished = finished

    @property
    def workflow_Activity15(self):
        return self.__workflow_Activity15

    @workflow_Activity15.setter
    def workflow_Activity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Activity__workflow_Activity15", None)
        self.__workflow_Activity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ActivityAspect"):
                opp_val = getattr(old_value, "workflow_ActivityAspect", None)
                if opp_val == self:
                    setattr(old_value, "workflow_ActivityAspect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ActivityAspect"):
                opp_val = getattr(value, "workflow_ActivityAspect", None)
                setattr(value, "workflow_ActivityAspect", self)

    @property
    def workflow_Activity(self):
        return self.__workflow_Activity

    @workflow_Activity.setter
    def workflow_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Activity__workflow_Activity", None)
        self.__workflow_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Case"):
                opp_val = getattr(old_value, "workflow_Case", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Case"):
                opp_val = getattr(value, "workflow_Case", None)
                if opp_val is None:
                    setattr(value, "workflow_Case", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Activity13(self):
        return self.__workflow_Activity13

    @workflow_Activity13.setter
    def workflow_Activity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Activity__workflow_Activity13", None)
        self.__workflow_Activity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Task"):
                opp_val = getattr(old_value, "workflow_Task", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Task", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Task"):
                opp_val = getattr(value, "workflow_Task", None)
                setattr(value, "workflow_Task", self)

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspects98"):
                opp_val = getattr(old_value, "aspects98", None)
                if opp_val == self:
                    setattr(old_value, "aspects98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspects98"):
                opp_val = getattr(value, "aspects98", None)
                setattr(value, "aspects98", self)

    @property
    def core11(self):
        return self.__core11

    @core11.setter
    def core11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Activity__core11", None)
        self.__core11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityAspect"):
                    opp_val = getattr(item, "ActivityAspect", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityAspect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityAspect"):
                    opp_val = getattr(item, "ActivityAspect", None)
                    
                    setattr(item, "ActivityAspect", self)
                    

class workflow_CaseAspect(ABC):

    pass
class workflow_Case:

    def __init__(self, id: str, client: str, started: bool, finished: bool, core: set["workflow_CaseAspect"] = None, workflow_Case: set["workflow_Activity"] = None, workflow_Case8: "workflow_Process" = None, cases: "workflow_RuntimeCoreModel" = None, Case: "workflow_CaseAspect" = None, Case115: "workflow_RuntimeCoreModel" = None):
        self.id = id
        self.client = client
        self.started = started
        self.finished = finished
        self.core = core if core is not None else set()
        self.workflow_Case = workflow_Case if workflow_Case is not None else set()
        self.workflow_Case8 = workflow_Case8
        self.cases = cases
        self.Case = Case
        self.Case115 = Case115
        
    @property
    def client(self) -> str:
        return self.__client

    @client.setter
    def client(self, client: str):
        self.__client = client

    @property
    def finished(self) -> bool:
        return self.__finished

    @finished.setter
    def finished(self, finished: bool):
        self.__finished = finished

    @property
    def started(self) -> bool:
        return self.__started

    @started.setter
    def started(self, started: bool):
        self.__started = started

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def core(self):
        return self.__core

    @core.setter
    def core(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__core", None)
        self.__core = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CaseAspect"):
                    opp_val = getattr(item, "CaseAspect", None)
                    
                    if opp_val == self:
                        setattr(item, "CaseAspect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CaseAspect"):
                    opp_val = getattr(item, "CaseAspect", None)
                    
                    setattr(item, "CaseAspect", self)
                    

    @property
    def Case115(self):
        return self.__Case115

    @Case115.setter
    def Case115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__Case115", None)
        self.__Case115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "runtimeCoreModel"):
                opp_val = getattr(old_value, "runtimeCoreModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "runtimeCoreModel"):
                opp_val = getattr(value, "runtimeCoreModel", None)
                if opp_val is None:
                    setattr(value, "runtimeCoreModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Case8(self):
        return self.__workflow_Case8

    @workflow_Case8.setter
    def workflow_Case8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__workflow_Case8", None)
        self.__workflow_Case8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Process"):
                opp_val = getattr(old_value, "workflow_Process", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Process"):
                opp_val = getattr(value, "workflow_Process", None)
                setattr(value, "workflow_Process", self)

    @property
    def workflow_Case(self):
        return self.__workflow_Case

    @workflow_Case.setter
    def workflow_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__workflow_Case", None)
        self.__workflow_Case = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Activity"):
                    opp_val = getattr(item, "workflow_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Activity"):
                    opp_val = getattr(item, "workflow_Activity", None)
                    
                    setattr(item, "workflow_Activity", self)
                    

    @property
    def Case(self):
        return self.__Case

    @Case.setter
    def Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__Case", None)
        self.__Case = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspects93"):
                opp_val = getattr(old_value, "aspects93", None)
                if opp_val == self:
                    setattr(old_value, "aspects93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspects93"):
                opp_val = getattr(value, "aspects93", None)
                setattr(value, "aspects93", self)

    @property
    def cases(self):
        return self.__cases

    @cases.setter
    def cases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Case__cases", None)
        self.__cases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RuntimeCoreModel"):
                opp_val = getattr(old_value, "RuntimeCoreModel", None)
                if opp_val == self:
                    setattr(old_value, "RuntimeCoreModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RuntimeCoreModel"):
                opp_val = getattr(value, "RuntimeCoreModel", None)
                setattr(value, "RuntimeCoreModel", self)

class workflow_Agent:

    def __init__(self, name: str, username: str, password: str, Agent: "workflow_ActivityO" = None, workflow_Agent: set["workflow_Role"] = None, assignedTo: set["workflow_ActivityO"] = None, workflow_Agent20: set["workflow_Role"] = None, workflow_Agent137: "workflow_CaseO" = None, workflow_Agent167: "workflow_AgentContainer" = None):
        self.name = name
        self.username = username
        self.password = password
        self.Agent = Agent
        self.workflow_Agent = workflow_Agent if workflow_Agent is not None else set()
        self.assignedTo = assignedTo if assignedTo is not None else set()
        self.workflow_Agent20 = workflow_Agent20 if workflow_Agent20 is not None else set()
        self.workflow_Agent137 = workflow_Agent137
        self.workflow_Agent167 = workflow_Agent167
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def assignedTo(self):
        return self.__assignedTo

    @assignedTo.setter
    def assignedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__assignedTo", None)
        self.__assignedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityO"):
                    opp_val = getattr(item, "ActivityO", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityO", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityO"):
                    opp_val = getattr(item, "ActivityO", None)
                    
                    setattr(item, "ActivityO", self)
                    

    @property
    def workflow_Agent(self):
        return self.__workflow_Agent

    @workflow_Agent.setter
    def workflow_Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__workflow_Agent", None)
        self.__workflow_Agent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Role17"):
                    opp_val = getattr(item, "workflow_Role17", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Role17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Role17"):
                    opp_val = getattr(item, "workflow_Role17", None)
                    
                    setattr(item, "workflow_Role17", self)
                    

    @property
    def workflow_Agent167(self):
        return self.__workflow_Agent167

    @workflow_Agent167.setter
    def workflow_Agent167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__workflow_Agent167", None)
        self.__workflow_Agent167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_AgentContainer"):
                opp_val = getattr(old_value, "workflow_AgentContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_AgentContainer"):
                opp_val = getattr(value, "workflow_AgentContainer", None)
                if opp_val is None:
                    setattr(value, "workflow_AgentContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Agent(self):
        return self.__Agent

    @Agent.setter
    def Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__Agent", None)
        self.__Agent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "active"):
                opp_val = getattr(old_value, "active", None)
                if opp_val == self:
                    setattr(old_value, "active", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "active"):
                opp_val = getattr(value, "active", None)
                setattr(value, "active", self)

    @property
    def workflow_Agent137(self):
        return self.__workflow_Agent137

    @workflow_Agent137.setter
    def workflow_Agent137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__workflow_Agent137", None)
        self.__workflow_Agent137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_CaseO"):
                opp_val = getattr(old_value, "workflow_CaseO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_CaseO"):
                opp_val = getattr(value, "workflow_CaseO", None)
                if opp_val is None:
                    setattr(value, "workflow_CaseO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Agent20(self):
        return self.__workflow_Agent20

    @workflow_Agent20.setter
    def workflow_Agent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Agent__workflow_Agent20", None)
        self.__workflow_Agent20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Role21"):
                    opp_val = getattr(item, "workflow_Role21", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Role21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Role21"):
                    opp_val = getattr(item, "workflow_Role21", None)
                    
                    setattr(item, "workflow_Role21", self)
                    

class ActivityAspect:

    pass
class workflow_ActivityI(ActivityAspect):

    pass
class workflow_ActivityC(ActivityAspect):

    pass
class workflow_ActivityO(ActivityAspect):

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UML_ValueSpecification:

    pass
class uml_UML_OpaqueExpression(UML_ValueSpecification):

    def __init__(self, body: str, language: str, uml_UML_OpaqueExpression: "uml_UML_Constraint" = None):
        self.body = body
        self.language = language
        self.uml_UML_OpaqueExpression = uml_UML_OpaqueExpression
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def uml_UML_OpaqueExpression(self):
        return self.__uml_UML_OpaqueExpression

    @uml_UML_OpaqueExpression.setter
    def uml_UML_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_OpaqueExpression__uml_UML_OpaqueExpression", None)
        self.__uml_UML_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML_Constraint40"):
                opp_val = getattr(old_value, "uml_UML_Constraint40", None)
                if opp_val == self:
                    setattr(old_value, "uml_UML_Constraint40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML_Constraint40"):
                opp_val = getattr(value, "uml_UML_Constraint40", None)
                setattr(value, "uml_UML_Constraint40", self)

class uml_UML_ValueSpecification:

    pass
class uml_UML_ActivityNode:

    def __init__(self, name: str, uml_UML_ActivityNode29: "uml_UML_ActivityNode" = None, uml_UML_ActivityNode27: set["uml_UML_ActivityNode"] = None, uml_UML_ActivityNode31: set["uml_UML_ActivityEdge"] = None, uml_UML_ActivityNode35: "uml_UML_ActivityEdge" = None, uml_UML_ActivityNode: "uml_UML_Activity" = None, uml_UML_ActivityNode38: "uml_UML_ActivityEdge" = None):
        self.name = name
        self.uml_UML_ActivityNode29 = uml_UML_ActivityNode29
        self.uml_UML_ActivityNode27 = uml_UML_ActivityNode27 if uml_UML_ActivityNode27 is not None else set()
        self.uml_UML_ActivityNode31 = uml_UML_ActivityNode31 if uml_UML_ActivityNode31 is not None else set()
        self.uml_UML_ActivityNode35 = uml_UML_ActivityNode35
        self.uml_UML_ActivityNode = uml_UML_ActivityNode
        self.uml_UML_ActivityNode38 = uml_UML_ActivityNode38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_UML_ActivityNode35(self):
        return self.__uml_UML_ActivityNode35

    @uml_UML_ActivityNode35.setter
    def uml_UML_ActivityNode35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode35", None)
        self.__uml_UML_ActivityNode35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML_ActivityEdge34"):
                opp_val = getattr(old_value, "uml_UML_ActivityEdge34", None)
                if opp_val == self:
                    setattr(old_value, "uml_UML_ActivityEdge34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML_ActivityEdge34"):
                opp_val = getattr(value, "uml_UML_ActivityEdge34", None)
                setattr(value, "uml_UML_ActivityEdge34", self)

    @property
    def uml_UML_ActivityNode29(self):
        return self.__uml_UML_ActivityNode29

    @uml_UML_ActivityNode29.setter
    def uml_UML_ActivityNode29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode29", None)
        self.__uml_UML_ActivityNode29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML_ActivityNode27"):
                opp_val = getattr(old_value, "uml_UML_ActivityNode27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML_ActivityNode27"):
                opp_val = getattr(value, "uml_UML_ActivityNode27", None)
                if opp_val is None:
                    setattr(value, "uml_UML_ActivityNode27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_UML_ActivityNode(self):
        return self.__uml_UML_ActivityNode

    @uml_UML_ActivityNode.setter
    def uml_UML_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode", None)
        self.__uml_UML_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML_Activity23"):
                opp_val = getattr(old_value, "uml_UML_Activity23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML_Activity23"):
                opp_val = getattr(value, "uml_UML_Activity23", None)
                if opp_val is None:
                    setattr(value, "uml_UML_Activity23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_UML_ActivityNode27(self):
        return self.__uml_UML_ActivityNode27

    @uml_UML_ActivityNode27.setter
    def uml_UML_ActivityNode27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode27", None)
        self.__uml_UML_ActivityNode27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_UML_ActivityNode29"):
                    opp_val = getattr(item, "uml_UML_ActivityNode29", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_UML_ActivityNode29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_UML_ActivityNode29"):
                    opp_val = getattr(item, "uml_UML_ActivityNode29", None)
                    
                    setattr(item, "uml_UML_ActivityNode29", self)
                    

    @property
    def uml_UML_ActivityNode38(self):
        return self.__uml_UML_ActivityNode38

    @uml_UML_ActivityNode38.setter
    def uml_UML_ActivityNode38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode38", None)
        self.__uml_UML_ActivityNode38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML_ActivityEdge37"):
                opp_val = getattr(old_value, "uml_UML_ActivityEdge37", None)
                if opp_val == self:
                    setattr(old_value, "uml_UML_ActivityEdge37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML_ActivityEdge37"):
                opp_val = getattr(value, "uml_UML_ActivityEdge37", None)
                setattr(value, "uml_UML_ActivityEdge37", self)

    @property
    def uml_UML_ActivityNode31(self):
        return self.__uml_UML_ActivityNode31

    @uml_UML_ActivityNode31.setter
    def uml_UML_ActivityNode31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_UML_ActivityNode__uml_UML_ActivityNode31", None)
        self.__uml_UML_ActivityNode31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_UML_ActivityEdge32"):
                    opp_val = getattr(item, "uml_UML_ActivityEdge32", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_UML_ActivityEdge32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_UML_ActivityEdge32"):
                    opp_val = getattr(item, "uml_UML_ActivityEdge32", None)
                    
                    setattr(item, "uml_UML_ActivityEdge32", self)
                    

class uml_UML_ActivityEdge:

    pass
class UML_Behavior:

    pass
class uml_UML_Activity(UML_Behavior):

    pass
class UML_Class:

    pass
class UML_Property:

    pass
class uml_UML_Port(UML_Property):

    pass
class UML_ConnectableElement:

    pass
class UML_StructuralFeature:

    pass
class UML_BehavioredClassifier:

    pass
class uml_UML_Class(UML_BehavioredClassifier):

    pass
class UML_BehavioralFeature:

    pass
class uml_UML_Behavior(UML_Class):

    pass
class UML_ActivityNode:

    pass
class uml_UML_Action(UML_ActivityNode):

    pass
class UML_Action:

    pass
class uml_UML_CallOperationAction(UML_Action):

    pass
class uml_UML_ConnectorEnd:

    pass
class UML_Namespace:

    pass
class uml_UML_Package(UML_Namespace):

    pass
class UML_RedefinableElement:

    pass
class uml_UML_Feature(UML_RedefinableElement):

    pass
class UML_NamedElement:

    pass
class uml_UML_Namespace(UML_NamedElement):

    pass
class uml_UML_PackageableElement(UML_NamedElement):

    pass
class uml_UML_RedefinableElement(UML_NamedElement):

    pass
class uml_UML_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class uml_UML_InterfaceRealization:

    pass
class uml_UML_Property(UML_ConnectableElement, UML_StructuralFeature):

    pass
class uml_UML_Operation(UML_BehavioralFeature):

    pass
class UML_Classifier:

    pass
class uml_UML_BehavioredClassifier(UML_Classifier):

    pass
class uml_UML_Interface(UML_Classifier):

    pass
class UML_Type:

    pass
class uml_UML_Classifier(UML_Namespace, UML_Type):

    pass
class uml_UML_TypedElement(UML_NamedElement):

    pass
class UML_PackageableElement:

    pass
class uml_UML_Constraint(UML_PackageableElement):

    pass
class uml_UML_Type(UML_PackageableElement):

    pass
class UML_TypedElement:

    pass
class uml_UML_ConnectableElement(UML_TypedElement):

    pass
class UML_Feature:

    pass
class uml_UML_Connector(UML_Feature):

    pass
class uml_UML_StructuralFeature(UML_TypedElement, UML_Feature):

    pass
class uml_UML_BehavioralFeature(UML_Namespace, UML_Feature):

    pass
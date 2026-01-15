from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TreeNodeXML_TreeNodeAtom:

    def __init__(self, AttributeLocalName: str, AttributeValue: str, TreeNodeXML_TreeNodeAtom: "TreeNodeXML_XMLTreeNode" = None):
        self.AttributeLocalName = AttributeLocalName
        self.AttributeValue = AttributeValue
        self.TreeNodeXML_TreeNodeAtom = TreeNodeXML_TreeNodeAtom
        
    @property
    def AttributeLocalName(self) -> str:
        return self.__AttributeLocalName

    @AttributeLocalName.setter
    def AttributeLocalName(self, AttributeLocalName: str):
        self.__AttributeLocalName = AttributeLocalName

    @property
    def AttributeValue(self) -> str:
        return self.__AttributeValue

    @AttributeValue.setter
    def AttributeValue(self, AttributeValue: str):
        self.__AttributeValue = AttributeValue

    @property
    def TreeNodeXML_TreeNodeAtom(self):
        return self.__TreeNodeXML_TreeNodeAtom

    @TreeNodeXML_TreeNodeAtom.setter
    def TreeNodeXML_TreeNodeAtom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeNodeXML_TreeNodeAtom__TreeNodeXML_TreeNodeAtom", None)
        self.__TreeNodeXML_TreeNodeAtom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeNodeXML_XMLTreeNode3"):
                opp_val = getattr(old_value, "TreeNodeXML_XMLTreeNode3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeNodeXML_XMLTreeNode3"):
                opp_val = getattr(value, "TreeNodeXML_XMLTreeNode3", None)
                if opp_val is None:
                    setattr(value, "TreeNodeXML_XMLTreeNode3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TreeNodeXML_XMLTreeNode:

    def __init__(self, LocalName: str, ElementText: str, TreeNodeXML_XMLTreeNode: "TreeNodeXML_XMLTreeNode" = None, TreeNodeXML_XMLTreeNode0: set["TreeNodeXML_XMLTreeNode"] = None, TreeNodeXML_XMLTreeNode3: set["TreeNodeXML_TreeNodeAtom"] = None):
        self.LocalName = LocalName
        self.ElementText = ElementText
        self.TreeNodeXML_XMLTreeNode = TreeNodeXML_XMLTreeNode
        self.TreeNodeXML_XMLTreeNode0 = TreeNodeXML_XMLTreeNode0 if TreeNodeXML_XMLTreeNode0 is not None else set()
        self.TreeNodeXML_XMLTreeNode3 = TreeNodeXML_XMLTreeNode3 if TreeNodeXML_XMLTreeNode3 is not None else set()
        
    @property
    def LocalName(self) -> str:
        return self.__LocalName

    @LocalName.setter
    def LocalName(self, LocalName: str):
        self.__LocalName = LocalName

    @property
    def ElementText(self) -> str:
        return self.__ElementText

    @ElementText.setter
    def ElementText(self, ElementText: str):
        self.__ElementText = ElementText

    @property
    def TreeNodeXML_XMLTreeNode3(self):
        return self.__TreeNodeXML_XMLTreeNode3

    @TreeNodeXML_XMLTreeNode3.setter
    def TreeNodeXML_XMLTreeNode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeNodeXML_XMLTreeNode__TreeNodeXML_XMLTreeNode3", None)
        self.__TreeNodeXML_XMLTreeNode3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeNodeXML_TreeNodeAtom"):
                    opp_val = getattr(item, "TreeNodeXML_TreeNodeAtom", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeNodeXML_TreeNodeAtom", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeNodeXML_TreeNodeAtom"):
                    opp_val = getattr(item, "TreeNodeXML_TreeNodeAtom", None)
                    
                    setattr(item, "TreeNodeXML_TreeNodeAtom", self)
                    

    @property
    def TreeNodeXML_XMLTreeNode(self):
        return self.__TreeNodeXML_XMLTreeNode

    @TreeNodeXML_XMLTreeNode.setter
    def TreeNodeXML_XMLTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeNodeXML_XMLTreeNode__TreeNodeXML_XMLTreeNode", None)
        self.__TreeNodeXML_XMLTreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeNodeXML_XMLTreeNode0"):
                opp_val = getattr(old_value, "TreeNodeXML_XMLTreeNode0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeNodeXML_XMLTreeNode0"):
                opp_val = getattr(value, "TreeNodeXML_XMLTreeNode0", None)
                if opp_val is None:
                    setattr(value, "TreeNodeXML_XMLTreeNode0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TreeNodeXML_XMLTreeNode0(self):
        return self.__TreeNodeXML_XMLTreeNode0

    @TreeNodeXML_XMLTreeNode0.setter
    def TreeNodeXML_XMLTreeNode0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeNodeXML_XMLTreeNode__TreeNodeXML_XMLTreeNode0", None)
        self.__TreeNodeXML_XMLTreeNode0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeNodeXML_XMLTreeNode"):
                    opp_val = getattr(item, "TreeNodeXML_XMLTreeNode", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeNodeXML_XMLTreeNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeNodeXML_XMLTreeNode"):
                    opp_val = getattr(item, "TreeNodeXML_XMLTreeNode", None)
                    
                    setattr(item, "TreeNodeXML_XMLTreeNode", self)
                    

    def addChild(self, newChild: str):
        # TODO: Implement addChild method
        pass

    def addTreeNodeAtom(self, nodeAtom: str):
        # TODO: Implement addTreeNodeAtom method
        pass

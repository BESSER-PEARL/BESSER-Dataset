from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class samplemodel_LinkCrossLink:

    pass
class samplemodel_Child2:

    def __init__(self, childLabel: str, samplemodel_Child2: "samplemodel_NodeSrcA" = None):
        self.childLabel = childLabel
        self.samplemodel_Child2 = samplemodel_Child2
        
    @property
    def childLabel(self) -> str:
        return self.__childLabel

    @childLabel.setter
    def childLabel(self, childLabel: str):
        self.__childLabel = childLabel

    @property
    def samplemodel_Child2(self):
        return self.__samplemodel_Child2

    @samplemodel_Child2.setter
    def samplemodel_Child2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_Child2__samplemodel_Child2", None)
        self.__samplemodel_Child2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA22"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA22"):
                opp_val = getattr(value, "samplemodel_NodeSrcA22", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeSrcA22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class samplemodel_Child:

    def __init__(self, childLabel: str, samplemodel_Child: "samplemodel_NodeSrcA" = None, samplemodel_Child25: "samplemodel_NodeTargetB" = None, samplemodel_Child53: "samplemodel_Child" = None, samplemodel_Child51: set["samplemodel_Child"] = None):
        self.childLabel = childLabel
        self.samplemodel_Child = samplemodel_Child
        self.samplemodel_Child25 = samplemodel_Child25
        self.samplemodel_Child53 = samplemodel_Child53
        self.samplemodel_Child51 = samplemodel_Child51 if samplemodel_Child51 is not None else set()
        
    @property
    def childLabel(self) -> str:
        return self.__childLabel

    @childLabel.setter
    def childLabel(self, childLabel: str):
        self.__childLabel = childLabel

    @property
    def samplemodel_Child25(self):
        return self.__samplemodel_Child25

    @samplemodel_Child25.setter
    def samplemodel_Child25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_Child__samplemodel_Child25", None)
        self.__samplemodel_Child25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeTargetB24"):
                opp_val = getattr(old_value, "samplemodel_NodeTargetB24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeTargetB24"):
                opp_val = getattr(value, "samplemodel_NodeTargetB24", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeTargetB24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def samplemodel_Child(self):
        return self.__samplemodel_Child

    @samplemodel_Child.setter
    def samplemodel_Child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_Child__samplemodel_Child", None)
        self.__samplemodel_Child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA20"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA20"):
                opp_val = getattr(value, "samplemodel_NodeSrcA20", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeSrcA20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def samplemodel_Child51(self):
        return self.__samplemodel_Child51

    @samplemodel_Child51.setter
    def samplemodel_Child51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_Child__samplemodel_Child51", None)
        self.__samplemodel_Child51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_Child53"):
                    opp_val = getattr(item, "samplemodel_Child53", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_Child53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_Child53"):
                    opp_val = getattr(item, "samplemodel_Child53", None)
                    
                    setattr(item, "samplemodel_Child53", self)
                    

    @property
    def samplemodel_Child53(self):
        return self.__samplemodel_Child53

    @samplemodel_Child53.setter
    def samplemodel_Child53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_Child__samplemodel_Child53", None)
        self.__samplemodel_Child53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_Child51"):
                opp_val = getattr(old_value, "samplemodel_Child51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_Child51"):
                opp_val = getattr(value, "samplemodel_Child51", None)
                if opp_val is None:
                    setattr(value, "samplemodel_Child51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class samplemodel_LinkFromLink:

    pass
class samplemodel_Link2Link:

    pass
class NodeTargetB:

    pass
class samplemodel_NodeTargetC(NodeTargetB):

    pass
class samplemodel_NodeTargetD(NodeTargetB):

    pass
class CommonBaseClass:

    pass
class samplemodel_NodeTargetB(CommonBaseClass):

    def __init__(self, title: str, samplemodel_NodeTargetB7: "samplemodel_NodeSrcA" = None, samplemodel_NodeTargetB: "samplemodel_NodeSrcA" = None, samplemodel_NodeTargetB4: "samplemodel_NodeSrcA" = None, samplemodel_NodeTargetB24: set["samplemodel_Child"] = None):
        self.title = title
        self.samplemodel_NodeTargetB7 = samplemodel_NodeTargetB7
        self.samplemodel_NodeTargetB = samplemodel_NodeTargetB
        self.samplemodel_NodeTargetB4 = samplemodel_NodeTargetB4
        self.samplemodel_NodeTargetB24 = samplemodel_NodeTargetB24 if samplemodel_NodeTargetB24 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def samplemodel_NodeTargetB(self):
        return self.__samplemodel_NodeTargetB

    @samplemodel_NodeTargetB.setter
    def samplemodel_NodeTargetB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeTargetB__samplemodel_NodeTargetB", None)
        self.__samplemodel_NodeTargetB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA"):
                opp_val = getattr(value, "samplemodel_NodeSrcA", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeSrcA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def samplemodel_NodeTargetB7(self):
        return self.__samplemodel_NodeTargetB7

    @samplemodel_NodeTargetB7.setter
    def samplemodel_NodeTargetB7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeTargetB__samplemodel_NodeTargetB7", None)
        self.__samplemodel_NodeTargetB7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA6"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA6", None)
                if opp_val == self:
                    setattr(old_value, "samplemodel_NodeSrcA6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA6"):
                opp_val = getattr(value, "samplemodel_NodeSrcA6", None)
                setattr(value, "samplemodel_NodeSrcA6", self)

    @property
    def samplemodel_NodeTargetB24(self):
        return self.__samplemodel_NodeTargetB24

    @samplemodel_NodeTargetB24.setter
    def samplemodel_NodeTargetB24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeTargetB__samplemodel_NodeTargetB24", None)
        self.__samplemodel_NodeTargetB24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_Child25"):
                    opp_val = getattr(item, "samplemodel_Child25", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_Child25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_Child25"):
                    opp_val = getattr(item, "samplemodel_Child25", None)
                    
                    setattr(item, "samplemodel_Child25", self)
                    

    @property
    def samplemodel_NodeTargetB4(self):
        return self.__samplemodel_NodeTargetB4

    @samplemodel_NodeTargetB4.setter
    def samplemodel_NodeTargetB4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeTargetB__samplemodel_NodeTargetB4", None)
        self.__samplemodel_NodeTargetB4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA3"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA3"):
                opp_val = getattr(value, "samplemodel_NodeSrcA3", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeSrcA3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class samplemodel_NodeSrcA(CommonBaseClass):

    def __init__(self, label: str, samplemodel_NodeSrcA6: "samplemodel_NodeTargetB" = None, samplemodel_NodeSrcA10: "samplemodel_NodeSrcA" = None, samplemodel_NodeSrcA8: set["samplemodel_NodeSrcA"] = None, samplemodel_NodeSrcA12: set["samplemodel_LinkAtoC"] = None, samplemodel_NodeSrcA14: set["samplemodel_LinkAtoC_Cardinality2"] = None, samplemodel_NodeSrcA16: "samplemodel_LinkAtoC_Cardinality1" = None, samplemodel_NodeSrcA: set["samplemodel_NodeTargetB"] = None, samplemodel_NodeSrcA3: set["samplemodel_NodeTargetB"] = None, samplemodel_NodeSrcA18: set["samplemodel_LinkAtoA"] = None, samplemodel_NodeSrcA20: set["samplemodel_Child"] = None, samplemodel_NodeSrcA22: set["samplemodel_Child2"] = None, samplemodel_NodeSrcA50: "samplemodel_LinkAtoA" = None):
        self.label = label
        self.samplemodel_NodeSrcA6 = samplemodel_NodeSrcA6
        self.samplemodel_NodeSrcA10 = samplemodel_NodeSrcA10
        self.samplemodel_NodeSrcA8 = samplemodel_NodeSrcA8 if samplemodel_NodeSrcA8 is not None else set()
        self.samplemodel_NodeSrcA12 = samplemodel_NodeSrcA12 if samplemodel_NodeSrcA12 is not None else set()
        self.samplemodel_NodeSrcA14 = samplemodel_NodeSrcA14 if samplemodel_NodeSrcA14 is not None else set()
        self.samplemodel_NodeSrcA16 = samplemodel_NodeSrcA16
        self.samplemodel_NodeSrcA = samplemodel_NodeSrcA if samplemodel_NodeSrcA is not None else set()
        self.samplemodel_NodeSrcA3 = samplemodel_NodeSrcA3 if samplemodel_NodeSrcA3 is not None else set()
        self.samplemodel_NodeSrcA18 = samplemodel_NodeSrcA18 if samplemodel_NodeSrcA18 is not None else set()
        self.samplemodel_NodeSrcA20 = samplemodel_NodeSrcA20 if samplemodel_NodeSrcA20 is not None else set()
        self.samplemodel_NodeSrcA22 = samplemodel_NodeSrcA22 if samplemodel_NodeSrcA22 is not None else set()
        self.samplemodel_NodeSrcA50 = samplemodel_NodeSrcA50
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def samplemodel_NodeSrcA18(self):
        return self.__samplemodel_NodeSrcA18

    @samplemodel_NodeSrcA18.setter
    def samplemodel_NodeSrcA18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA18", None)
        self.__samplemodel_NodeSrcA18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_LinkAtoA"):
                    opp_val = getattr(item, "samplemodel_LinkAtoA", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_LinkAtoA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_LinkAtoA"):
                    opp_val = getattr(item, "samplemodel_LinkAtoA", None)
                    
                    setattr(item, "samplemodel_LinkAtoA", self)
                    

    @property
    def samplemodel_NodeSrcA50(self):
        return self.__samplemodel_NodeSrcA50

    @samplemodel_NodeSrcA50.setter
    def samplemodel_NodeSrcA50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA50", None)
        self.__samplemodel_NodeSrcA50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_LinkAtoA49"):
                opp_val = getattr(old_value, "samplemodel_LinkAtoA49", None)
                if opp_val == self:
                    setattr(old_value, "samplemodel_LinkAtoA49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_LinkAtoA49"):
                opp_val = getattr(value, "samplemodel_LinkAtoA49", None)
                setattr(value, "samplemodel_LinkAtoA49", self)

    @property
    def samplemodel_NodeSrcA12(self):
        return self.__samplemodel_NodeSrcA12

    @samplemodel_NodeSrcA12.setter
    def samplemodel_NodeSrcA12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA12", None)
        self.__samplemodel_NodeSrcA12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_LinkAtoC"):
                    opp_val = getattr(item, "samplemodel_LinkAtoC", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_LinkAtoC", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_LinkAtoC"):
                    opp_val = getattr(item, "samplemodel_LinkAtoC", None)
                    
                    setattr(item, "samplemodel_LinkAtoC", self)
                    

    @property
    def samplemodel_NodeSrcA8(self):
        return self.__samplemodel_NodeSrcA8

    @samplemodel_NodeSrcA8.setter
    def samplemodel_NodeSrcA8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA8", None)
        self.__samplemodel_NodeSrcA8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_NodeSrcA10"):
                    opp_val = getattr(item, "samplemodel_NodeSrcA10", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_NodeSrcA10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_NodeSrcA10"):
                    opp_val = getattr(item, "samplemodel_NodeSrcA10", None)
                    
                    setattr(item, "samplemodel_NodeSrcA10", self)
                    

    @property
    def samplemodel_NodeSrcA10(self):
        return self.__samplemodel_NodeSrcA10

    @samplemodel_NodeSrcA10.setter
    def samplemodel_NodeSrcA10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA10", None)
        self.__samplemodel_NodeSrcA10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeSrcA8"):
                opp_val = getattr(old_value, "samplemodel_NodeSrcA8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeSrcA8"):
                opp_val = getattr(value, "samplemodel_NodeSrcA8", None)
                if opp_val is None:
                    setattr(value, "samplemodel_NodeSrcA8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def samplemodel_NodeSrcA20(self):
        return self.__samplemodel_NodeSrcA20

    @samplemodel_NodeSrcA20.setter
    def samplemodel_NodeSrcA20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA20", None)
        self.__samplemodel_NodeSrcA20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_Child"):
                    opp_val = getattr(item, "samplemodel_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_Child"):
                    opp_val = getattr(item, "samplemodel_Child", None)
                    
                    setattr(item, "samplemodel_Child", self)
                    

    @property
    def samplemodel_NodeSrcA16(self):
        return self.__samplemodel_NodeSrcA16

    @samplemodel_NodeSrcA16.setter
    def samplemodel_NodeSrcA16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA16", None)
        self.__samplemodel_NodeSrcA16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_LinkAtoC_Cardinality1"):
                opp_val = getattr(old_value, "samplemodel_LinkAtoC_Cardinality1", None)
                if opp_val == self:
                    setattr(old_value, "samplemodel_LinkAtoC_Cardinality1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_LinkAtoC_Cardinality1"):
                opp_val = getattr(value, "samplemodel_LinkAtoC_Cardinality1", None)
                setattr(value, "samplemodel_LinkAtoC_Cardinality1", self)

    @property
    def samplemodel_NodeSrcA(self):
        return self.__samplemodel_NodeSrcA

    @samplemodel_NodeSrcA.setter
    def samplemodel_NodeSrcA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA", None)
        self.__samplemodel_NodeSrcA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_NodeTargetB"):
                    opp_val = getattr(item, "samplemodel_NodeTargetB", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_NodeTargetB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_NodeTargetB"):
                    opp_val = getattr(item, "samplemodel_NodeTargetB", None)
                    
                    setattr(item, "samplemodel_NodeTargetB", self)
                    

    @property
    def samplemodel_NodeSrcA14(self):
        return self.__samplemodel_NodeSrcA14

    @samplemodel_NodeSrcA14.setter
    def samplemodel_NodeSrcA14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA14", None)
        self.__samplemodel_NodeSrcA14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_LinkAtoC_Cardinality2"):
                    opp_val = getattr(item, "samplemodel_LinkAtoC_Cardinality2", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_LinkAtoC_Cardinality2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_LinkAtoC_Cardinality2"):
                    opp_val = getattr(item, "samplemodel_LinkAtoC_Cardinality2", None)
                    
                    setattr(item, "samplemodel_LinkAtoC_Cardinality2", self)
                    

    @property
    def samplemodel_NodeSrcA3(self):
        return self.__samplemodel_NodeSrcA3

    @samplemodel_NodeSrcA3.setter
    def samplemodel_NodeSrcA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA3", None)
        self.__samplemodel_NodeSrcA3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_NodeTargetB4"):
                    opp_val = getattr(item, "samplemodel_NodeTargetB4", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_NodeTargetB4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_NodeTargetB4"):
                    opp_val = getattr(item, "samplemodel_NodeTargetB4", None)
                    
                    setattr(item, "samplemodel_NodeTargetB4", self)
                    

    @property
    def samplemodel_NodeSrcA22(self):
        return self.__samplemodel_NodeSrcA22

    @samplemodel_NodeSrcA22.setter
    def samplemodel_NodeSrcA22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA22", None)
        self.__samplemodel_NodeSrcA22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_Child2"):
                    opp_val = getattr(item, "samplemodel_Child2", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_Child2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_Child2"):
                    opp_val = getattr(item, "samplemodel_Child2", None)
                    
                    setattr(item, "samplemodel_Child2", self)
                    

    @property
    def samplemodel_NodeSrcA6(self):
        return self.__samplemodel_NodeSrcA6

    @samplemodel_NodeSrcA6.setter
    def samplemodel_NodeSrcA6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_NodeSrcA__samplemodel_NodeSrcA6", None)
        self.__samplemodel_NodeSrcA6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samplemodel_NodeTargetB7"):
                opp_val = getattr(old_value, "samplemodel_NodeTargetB7", None)
                if opp_val == self:
                    setattr(old_value, "samplemodel_NodeTargetB7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samplemodel_NodeTargetB7"):
                opp_val = getattr(value, "samplemodel_NodeTargetB7", None)
                setattr(value, "samplemodel_NodeTargetB7", self)

class samplemodel_UltimateContainer:

    def __init__(self, diagramAttribute: str, samplemodel_UltimateContainer: set["samplemodel_CommonBaseClass"] = None):
        self.diagramAttribute = diagramAttribute
        self.samplemodel_UltimateContainer = samplemodel_UltimateContainer if samplemodel_UltimateContainer is not None else set()
        
    @property
    def diagramAttribute(self) -> str:
        return self.__diagramAttribute

    @diagramAttribute.setter
    def diagramAttribute(self, diagramAttribute: str):
        self.__diagramAttribute = diagramAttribute

    @property
    def samplemodel_UltimateContainer(self):
        return self.__samplemodel_UltimateContainer

    @samplemodel_UltimateContainer.setter
    def samplemodel_UltimateContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samplemodel_UltimateContainer__samplemodel_UltimateContainer", None)
        self.__samplemodel_UltimateContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samplemodel_CommonBaseClass"):
                    opp_val = getattr(item, "samplemodel_CommonBaseClass", None)
                    
                    if opp_val == self:
                        setattr(item, "samplemodel_CommonBaseClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samplemodel_CommonBaseClass"):
                    opp_val = getattr(item, "samplemodel_CommonBaseClass", None)
                    
                    setattr(item, "samplemodel_CommonBaseClass", self)
                    

class samplemodel_LinkAtoA:

    pass
class samplemodel_LinkAtoC_Cardinality1:

    pass
class samplemodel_LinkAtoC_Cardinality2:

    pass
class samplemodel_LinkAtoC:

    pass
class samplemodel_CommonBaseClass(ABC):

    pass
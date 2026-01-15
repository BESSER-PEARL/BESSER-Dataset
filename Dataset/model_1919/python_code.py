from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class jbatch_Property:

    def __init__(self, value: str, name: str, jbatch_Property: "jbatch_Properties" = None):
        self.value = value
        self.name = name
        self.jbatch_Property = jbatch_Property
        
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
    def jbatch_Property(self):
        return self.__jbatch_Property

    @jbatch_Property.setter
    def jbatch_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Property__jbatch_Property", None)
        self.__jbatch_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties116"):
                opp_val = getattr(old_value, "jbatch_Properties116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties116"):
                opp_val = getattr(value, "jbatch_Properties116", None)
                if opp_val is None:
                    setattr(value, "jbatch_Properties116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_PartitionReducer:

    def __init__(self, ref: str, jbatch_PartitionReducer: "jbatch_Partition" = None, jbatch_PartitionReducer113: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_PartitionReducer = jbatch_PartitionReducer
        self.jbatch_PartitionReducer113 = jbatch_PartitionReducer113
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_PartitionReducer113(self):
        return self.__jbatch_PartitionReducer113

    @jbatch_PartitionReducer113.setter
    def jbatch_PartitionReducer113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionReducer__jbatch_PartitionReducer113", None)
        self.__jbatch_PartitionReducer113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties114"):
                opp_val = getattr(old_value, "jbatch_Properties114", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties114"):
                opp_val = getattr(value, "jbatch_Properties114", None)
                setattr(value, "jbatch_Properties114", self)

    @property
    def jbatch_PartitionReducer(self):
        return self.__jbatch_PartitionReducer

    @jbatch_PartitionReducer.setter
    def jbatch_PartitionReducer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionReducer__jbatch_PartitionReducer", None)
        self.__jbatch_PartitionReducer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition105"):
                opp_val = getattr(old_value, "jbatch_Partition105", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition105"):
                opp_val = getattr(value, "jbatch_Partition105", None)
                setattr(value, "jbatch_Partition105", self)

class jbatch_PartitionMapper:

    def __init__(self, ref: str, jbatch_PartitionMapper: "jbatch_Partition" = None, jbatch_PartitionMapper107: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_PartitionMapper = jbatch_PartitionMapper
        self.jbatch_PartitionMapper107 = jbatch_PartitionMapper107
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_PartitionMapper107(self):
        return self.__jbatch_PartitionMapper107

    @jbatch_PartitionMapper107.setter
    def jbatch_PartitionMapper107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionMapper__jbatch_PartitionMapper107", None)
        self.__jbatch_PartitionMapper107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties108"):
                opp_val = getattr(old_value, "jbatch_Properties108", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties108"):
                opp_val = getattr(value, "jbatch_Properties108", None)
                setattr(value, "jbatch_Properties108", self)

    @property
    def jbatch_PartitionMapper(self):
        return self.__jbatch_PartitionMapper

    @jbatch_PartitionMapper.setter
    def jbatch_PartitionMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionMapper__jbatch_PartitionMapper", None)
        self.__jbatch_PartitionMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition"):
                opp_val = getattr(old_value, "jbatch_Partition", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition"):
                opp_val = getattr(value, "jbatch_Partition", None)
                setattr(value, "jbatch_Partition", self)

class jbatch_Partition:

    pass
class jbatch_PartitionPlan:

    def __init__(self, partitions: str, threads: str, jbatch_PartitionPlan: "jbatch_Partition" = None, jbatch_PartitionPlan110: set["jbatch_Properties"] = None):
        self.partitions = partitions
        self.threads = threads
        self.jbatch_PartitionPlan = jbatch_PartitionPlan
        self.jbatch_PartitionPlan110 = jbatch_PartitionPlan110 if jbatch_PartitionPlan110 is not None else set()
        
    @property
    def partitions(self) -> str:
        return self.__partitions

    @partitions.setter
    def partitions(self, partitions: str):
        self.__partitions = partitions

    @property
    def threads(self) -> str:
        return self.__threads

    @threads.setter
    def threads(self, threads: str):
        self.__threads = threads

    @property
    def jbatch_PartitionPlan(self):
        return self.__jbatch_PartitionPlan

    @jbatch_PartitionPlan.setter
    def jbatch_PartitionPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionPlan__jbatch_PartitionPlan", None)
        self.__jbatch_PartitionPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition97"):
                opp_val = getattr(old_value, "jbatch_Partition97", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition97"):
                opp_val = getattr(value, "jbatch_Partition97", None)
                setattr(value, "jbatch_Partition97", self)

    @property
    def jbatch_PartitionPlan110(self):
        return self.__jbatch_PartitionPlan110

    @jbatch_PartitionPlan110.setter
    def jbatch_PartitionPlan110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_PartitionPlan__jbatch_PartitionPlan110", None)
        self.__jbatch_PartitionPlan110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Properties111"):
                    opp_val = getattr(item, "jbatch_Properties111", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Properties111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Properties111"):
                    opp_val = getattr(item, "jbatch_Properties111", None)
                    
                    setattr(item, "jbatch_Properties111", self)
                    

class jbatch_Listener:

    def __init__(self, ref: str, jbatch_Listener94: "jbatch_Listeners" = None, jbatch_Listener: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_Listener94 = jbatch_Listener94
        self.jbatch_Listener = jbatch_Listener
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_Listener94(self):
        return self.__jbatch_Listener94

    @jbatch_Listener94.setter
    def jbatch_Listener94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Listener__jbatch_Listener94", None)
        self.__jbatch_Listener94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Listeners93"):
                opp_val = getattr(old_value, "jbatch_Listeners93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Listeners93"):
                opp_val = getattr(value, "jbatch_Listeners93", None)
                if opp_val is None:
                    setattr(value, "jbatch_Listeners93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Listener(self):
        return self.__jbatch_Listener

    @jbatch_Listener.setter
    def jbatch_Listener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Listener__jbatch_Listener", None)
        self.__jbatch_Listener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties91"):
                opp_val = getattr(old_value, "jbatch_Properties91", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties91"):
                opp_val = getattr(value, "jbatch_Properties91", None)
                setattr(value, "jbatch_Properties91", self)

class jbatch_Listeners:

    pass
class jbatch_Split:

    def __init__(self, next: str, id: str, jbatch_Split: "jbatch_Flow" = None, jbatch_Split86: "jbatch_Job" = None, jbatch_Split118: set["jbatch_Flow"] = None):
        self.next = next
        self.id = id
        self.jbatch_Split = jbatch_Split
        self.jbatch_Split86 = jbatch_Split86
        self.jbatch_Split118 = jbatch_Split118 if jbatch_Split118 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def next(self) -> str:
        return self.__next

    @next.setter
    def next(self, next: str):
        self.__next = next

    @property
    def jbatch_Split118(self):
        return self.__jbatch_Split118

    @jbatch_Split118.setter
    def jbatch_Split118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Split__jbatch_Split118", None)
        self.__jbatch_Split118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Flow119"):
                    opp_val = getattr(item, "jbatch_Flow119", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Flow119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Flow119"):
                    opp_val = getattr(item, "jbatch_Flow119", None)
                    
                    setattr(item, "jbatch_Flow119", self)
                    

    @property
    def jbatch_Split86(self):
        return self.__jbatch_Split86

    @jbatch_Split86.setter
    def jbatch_Split86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Split__jbatch_Split86", None)
        self.__jbatch_Split86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Job85"):
                opp_val = getattr(old_value, "jbatch_Job85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Job85"):
                opp_val = getattr(value, "jbatch_Job85", None)
                if opp_val is None:
                    setattr(value, "jbatch_Job85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Split(self):
        return self.__jbatch_Split

    @jbatch_Split.setter
    def jbatch_Split(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Split__jbatch_Split", None)
        self.__jbatch_Split = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow49"):
                opp_val = getattr(old_value, "jbatch_Flow49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow49"):
                opp_val = getattr(value, "jbatch_Flow49", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_Step:

    def __init__(self, transitionElements: str, allowStartIfComplete: str, id: str, next1: str, startLimit: str, jbatch_Step: "jbatch_Flow" = None, jbatch_Step89: "jbatch_Job" = None, jbatch_Step127: "jbatch_Batchlet" = None, jbatch_Step121: "jbatch_Properties" = None, jbatch_Step124: "jbatch_Listeners" = None, jbatch_Step133: "jbatch_Partition" = None, jbatch_Step130: "jbatch_Chunk" = None, jbatch_Step142: set["jbatch_Next"] = None, jbatch_Step145: set["jbatch_Stop"] = None, jbatch_Step136: set["jbatch_End"] = None, jbatch_Step139: set["jbatch_Fail"] = None):
        self.transitionElements = transitionElements
        self.allowStartIfComplete = allowStartIfComplete
        self.id = id
        self.next1 = next1
        self.startLimit = startLimit
        self.jbatch_Step = jbatch_Step
        self.jbatch_Step89 = jbatch_Step89
        self.jbatch_Step127 = jbatch_Step127
        self.jbatch_Step121 = jbatch_Step121
        self.jbatch_Step124 = jbatch_Step124
        self.jbatch_Step133 = jbatch_Step133
        self.jbatch_Step130 = jbatch_Step130
        self.jbatch_Step142 = jbatch_Step142 if jbatch_Step142 is not None else set()
        self.jbatch_Step145 = jbatch_Step145 if jbatch_Step145 is not None else set()
        self.jbatch_Step136 = jbatch_Step136 if jbatch_Step136 is not None else set()
        self.jbatch_Step139 = jbatch_Step139 if jbatch_Step139 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def startLimit(self) -> str:
        return self.__startLimit

    @startLimit.setter
    def startLimit(self, startLimit: str):
        self.__startLimit = startLimit

    @property
    def allowStartIfComplete(self) -> str:
        return self.__allowStartIfComplete

    @allowStartIfComplete.setter
    def allowStartIfComplete(self, allowStartIfComplete: str):
        self.__allowStartIfComplete = allowStartIfComplete

    @property
    def transitionElements(self) -> str:
        return self.__transitionElements

    @transitionElements.setter
    def transitionElements(self, transitionElements: str):
        self.__transitionElements = transitionElements

    @property
    def next1(self) -> str:
        return self.__next1

    @next1.setter
    def next1(self, next1: str):
        self.__next1 = next1

    @property
    def jbatch_Step(self):
        return self.__jbatch_Step

    @jbatch_Step.setter
    def jbatch_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step", None)
        self.__jbatch_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow51"):
                opp_val = getattr(old_value, "jbatch_Flow51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow51"):
                opp_val = getattr(value, "jbatch_Flow51", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Step130(self):
        return self.__jbatch_Step130

    @jbatch_Step130.setter
    def jbatch_Step130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step130", None)
        self.__jbatch_Step130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Chunk131"):
                opp_val = getattr(old_value, "jbatch_Chunk131", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Chunk131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Chunk131"):
                opp_val = getattr(value, "jbatch_Chunk131", None)
                setattr(value, "jbatch_Chunk131", self)

    @property
    def jbatch_Step89(self):
        return self.__jbatch_Step89

    @jbatch_Step89.setter
    def jbatch_Step89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step89", None)
        self.__jbatch_Step89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Job88"):
                opp_val = getattr(old_value, "jbatch_Job88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Job88"):
                opp_val = getattr(value, "jbatch_Job88", None)
                if opp_val is None:
                    setattr(value, "jbatch_Job88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Step121(self):
        return self.__jbatch_Step121

    @jbatch_Step121.setter
    def jbatch_Step121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step121", None)
        self.__jbatch_Step121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties122"):
                opp_val = getattr(old_value, "jbatch_Properties122", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties122"):
                opp_val = getattr(value, "jbatch_Properties122", None)
                setattr(value, "jbatch_Properties122", self)

    @property
    def jbatch_Step133(self):
        return self.__jbatch_Step133

    @jbatch_Step133.setter
    def jbatch_Step133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step133", None)
        self.__jbatch_Step133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition134"):
                opp_val = getattr(old_value, "jbatch_Partition134", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition134"):
                opp_val = getattr(value, "jbatch_Partition134", None)
                setattr(value, "jbatch_Partition134", self)

    @property
    def jbatch_Step145(self):
        return self.__jbatch_Step145

    @jbatch_Step145.setter
    def jbatch_Step145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step145", None)
        self.__jbatch_Step145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Stop146"):
                    opp_val = getattr(item, "jbatch_Stop146", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Stop146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Stop146"):
                    opp_val = getattr(item, "jbatch_Stop146", None)
                    
                    setattr(item, "jbatch_Stop146", self)
                    

    @property
    def jbatch_Step136(self):
        return self.__jbatch_Step136

    @jbatch_Step136.setter
    def jbatch_Step136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step136", None)
        self.__jbatch_Step136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_End137"):
                    opp_val = getattr(item, "jbatch_End137", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_End137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_End137"):
                    opp_val = getattr(item, "jbatch_End137", None)
                    
                    setattr(item, "jbatch_End137", self)
                    

    @property
    def jbatch_Step142(self):
        return self.__jbatch_Step142

    @jbatch_Step142.setter
    def jbatch_Step142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step142", None)
        self.__jbatch_Step142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Next143"):
                    opp_val = getattr(item, "jbatch_Next143", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Next143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Next143"):
                    opp_val = getattr(item, "jbatch_Next143", None)
                    
                    setattr(item, "jbatch_Next143", self)
                    

    @property
    def jbatch_Step124(self):
        return self.__jbatch_Step124

    @jbatch_Step124.setter
    def jbatch_Step124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step124", None)
        self.__jbatch_Step124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Listeners125"):
                opp_val = getattr(old_value, "jbatch_Listeners125", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Listeners125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Listeners125"):
                opp_val = getattr(value, "jbatch_Listeners125", None)
                setattr(value, "jbatch_Listeners125", self)

    @property
    def jbatch_Step127(self):
        return self.__jbatch_Step127

    @jbatch_Step127.setter
    def jbatch_Step127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step127", None)
        self.__jbatch_Step127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Batchlet128"):
                opp_val = getattr(old_value, "jbatch_Batchlet128", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Batchlet128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Batchlet128"):
                opp_val = getattr(value, "jbatch_Batchlet128", None)
                setattr(value, "jbatch_Batchlet128", self)

    @property
    def jbatch_Step139(self):
        return self.__jbatch_Step139

    @jbatch_Step139.setter
    def jbatch_Step139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Step__jbatch_Step139", None)
        self.__jbatch_Step139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Fail140"):
                    opp_val = getattr(item, "jbatch_Fail140", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Fail140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Fail140"):
                    opp_val = getattr(item, "jbatch_Fail140", None)
                    
                    setattr(item, "jbatch_Fail140", self)
                    

class jbatch_ExcludeType:

    def __init__(self, class: str, jbatch_ExcludeType: "jbatch_ExceptionClassFilter" = None):
        self.class = class
        self.jbatch_ExcludeType = jbatch_ExcludeType
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def jbatch_ExcludeType(self):
        return self.__jbatch_ExcludeType

    @jbatch_ExcludeType.setter
    def jbatch_ExcludeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ExcludeType__jbatch_ExcludeType", None)
        self.__jbatch_ExcludeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ExceptionClassFilter42"):
                opp_val = getattr(old_value, "jbatch_ExceptionClassFilter42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ExceptionClassFilter42"):
                opp_val = getattr(value, "jbatch_ExceptionClassFilter42", None)
                if opp_val is None:
                    setattr(value, "jbatch_ExceptionClassFilter42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_IncludeType:

    def __init__(self, class: str, jbatch_IncludeType: "jbatch_ExceptionClassFilter" = None):
        self.class = class
        self.jbatch_IncludeType = jbatch_IncludeType
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def jbatch_IncludeType(self):
        return self.__jbatch_IncludeType

    @jbatch_IncludeType.setter
    def jbatch_IncludeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_IncludeType__jbatch_IncludeType", None)
        self.__jbatch_IncludeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ExceptionClassFilter40"):
                opp_val = getattr(old_value, "jbatch_ExceptionClassFilter40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ExceptionClassFilter40"):
                opp_val = getattr(value, "jbatch_ExceptionClassFilter40", None)
                if opp_val is None:
                    setattr(value, "jbatch_ExceptionClassFilter40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_Job:

    def __init__(self, group: str, id: str, restartable: str, version: str, jbatch_Job: "jbatch_DocumentRoot" = None, jbatch_Job77: "jbatch_Listeners" = None, jbatch_Job74: "jbatch_Properties" = None, jbatch_Job82: set["jbatch_Flow"] = None, jbatch_Job79: set["jbatch_Decision"] = None, jbatch_Job85: set["jbatch_Split"] = None, jbatch_Job88: set["jbatch_Step"] = None):
        self.group = group
        self.id = id
        self.restartable = restartable
        self.version = version
        self.jbatch_Job = jbatch_Job
        self.jbatch_Job77 = jbatch_Job77
        self.jbatch_Job74 = jbatch_Job74
        self.jbatch_Job82 = jbatch_Job82 if jbatch_Job82 is not None else set()
        self.jbatch_Job79 = jbatch_Job79 if jbatch_Job79 is not None else set()
        self.jbatch_Job85 = jbatch_Job85 if jbatch_Job85 is not None else set()
        self.jbatch_Job88 = jbatch_Job88 if jbatch_Job88 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def restartable(self) -> str:
        return self.__restartable

    @restartable.setter
    def restartable(self, restartable: str):
        self.__restartable = restartable

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jbatch_Job74(self):
        return self.__jbatch_Job74

    @jbatch_Job74.setter
    def jbatch_Job74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job74", None)
        self.__jbatch_Job74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties75"):
                opp_val = getattr(old_value, "jbatch_Properties75", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties75"):
                opp_val = getattr(value, "jbatch_Properties75", None)
                setattr(value, "jbatch_Properties75", self)

    @property
    def jbatch_Job(self):
        return self.__jbatch_Job

    @jbatch_Job.setter
    def jbatch_Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job", None)
        self.__jbatch_Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_DocumentRoot38"):
                opp_val = getattr(old_value, "jbatch_DocumentRoot38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_DocumentRoot38"):
                opp_val = getattr(value, "jbatch_DocumentRoot38", None)
                if opp_val is None:
                    setattr(value, "jbatch_DocumentRoot38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Job77(self):
        return self.__jbatch_Job77

    @jbatch_Job77.setter
    def jbatch_Job77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job77", None)
        self.__jbatch_Job77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Listeners"):
                opp_val = getattr(old_value, "jbatch_Listeners", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Listeners", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Listeners"):
                opp_val = getattr(value, "jbatch_Listeners", None)
                setattr(value, "jbatch_Listeners", self)

    @property
    def jbatch_Job88(self):
        return self.__jbatch_Job88

    @jbatch_Job88.setter
    def jbatch_Job88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job88", None)
        self.__jbatch_Job88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Step89"):
                    opp_val = getattr(item, "jbatch_Step89", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Step89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Step89"):
                    opp_val = getattr(item, "jbatch_Step89", None)
                    
                    setattr(item, "jbatch_Step89", self)
                    

    @property
    def jbatch_Job85(self):
        return self.__jbatch_Job85

    @jbatch_Job85.setter
    def jbatch_Job85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job85", None)
        self.__jbatch_Job85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Split86"):
                    opp_val = getattr(item, "jbatch_Split86", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Split86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Split86"):
                    opp_val = getattr(item, "jbatch_Split86", None)
                    
                    setattr(item, "jbatch_Split86", self)
                    

    @property
    def jbatch_Job82(self):
        return self.__jbatch_Job82

    @jbatch_Job82.setter
    def jbatch_Job82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job82", None)
        self.__jbatch_Job82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Flow83"):
                    opp_val = getattr(item, "jbatch_Flow83", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Flow83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Flow83"):
                    opp_val = getattr(item, "jbatch_Flow83", None)
                    
                    setattr(item, "jbatch_Flow83", self)
                    

    @property
    def jbatch_Job79(self):
        return self.__jbatch_Job79

    @jbatch_Job79.setter
    def jbatch_Job79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Job__jbatch_Job79", None)
        self.__jbatch_Job79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Decision80"):
                    opp_val = getattr(item, "jbatch_Decision80", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Decision80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Decision80"):
                    opp_val = getattr(item, "jbatch_Decision80", None)
                    
                    setattr(item, "jbatch_Decision80", self)
                    

class jbatch_Flow:

    def __init__(self, group: str, transitionElements: str, id: str, next1: str, jbatch_Flow51: set["jbatch_Step"] = None, jbatch_Flow: set["jbatch_Decision"] = None, jbatch_Flow47: "jbatch_Flow" = None, jbatch_Flow45: set["jbatch_Flow"] = None, jbatch_Flow49: set["jbatch_Split"] = None, jbatch_Flow53: set["jbatch_End"] = None, jbatch_Flow56: set["jbatch_Fail"] = None, jbatch_Flow59: set["jbatch_Next"] = None, jbatch_Flow62: set["jbatch_Stop"] = None, jbatch_Flow83: "jbatch_Job" = None, jbatch_Flow119: "jbatch_Split" = None):
        self.group = group
        self.transitionElements = transitionElements
        self.id = id
        self.next1 = next1
        self.jbatch_Flow51 = jbatch_Flow51 if jbatch_Flow51 is not None else set()
        self.jbatch_Flow = jbatch_Flow if jbatch_Flow is not None else set()
        self.jbatch_Flow47 = jbatch_Flow47
        self.jbatch_Flow45 = jbatch_Flow45 if jbatch_Flow45 is not None else set()
        self.jbatch_Flow49 = jbatch_Flow49 if jbatch_Flow49 is not None else set()
        self.jbatch_Flow53 = jbatch_Flow53 if jbatch_Flow53 is not None else set()
        self.jbatch_Flow56 = jbatch_Flow56 if jbatch_Flow56 is not None else set()
        self.jbatch_Flow59 = jbatch_Flow59 if jbatch_Flow59 is not None else set()
        self.jbatch_Flow62 = jbatch_Flow62 if jbatch_Flow62 is not None else set()
        self.jbatch_Flow83 = jbatch_Flow83
        self.jbatch_Flow119 = jbatch_Flow119
        
    @property
    def transitionElements(self) -> str:
        return self.__transitionElements

    @transitionElements.setter
    def transitionElements(self, transitionElements: str):
        self.__transitionElements = transitionElements

    @property
    def next1(self) -> str:
        return self.__next1

    @next1.setter
    def next1(self, next1: str):
        self.__next1 = next1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jbatch_Flow119(self):
        return self.__jbatch_Flow119

    @jbatch_Flow119.setter
    def jbatch_Flow119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow119", None)
        self.__jbatch_Flow119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Split118"):
                opp_val = getattr(old_value, "jbatch_Split118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Split118"):
                opp_val = getattr(value, "jbatch_Split118", None)
                if opp_val is None:
                    setattr(value, "jbatch_Split118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Flow47(self):
        return self.__jbatch_Flow47

    @jbatch_Flow47.setter
    def jbatch_Flow47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow47", None)
        self.__jbatch_Flow47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow45"):
                opp_val = getattr(old_value, "jbatch_Flow45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow45"):
                opp_val = getattr(value, "jbatch_Flow45", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Flow45(self):
        return self.__jbatch_Flow45

    @jbatch_Flow45.setter
    def jbatch_Flow45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow45", None)
        self.__jbatch_Flow45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Flow47"):
                    opp_val = getattr(item, "jbatch_Flow47", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Flow47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Flow47"):
                    opp_val = getattr(item, "jbatch_Flow47", None)
                    
                    setattr(item, "jbatch_Flow47", self)
                    

    @property
    def jbatch_Flow(self):
        return self.__jbatch_Flow

    @jbatch_Flow.setter
    def jbatch_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow", None)
        self.__jbatch_Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Decision44"):
                    opp_val = getattr(item, "jbatch_Decision44", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Decision44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Decision44"):
                    opp_val = getattr(item, "jbatch_Decision44", None)
                    
                    setattr(item, "jbatch_Decision44", self)
                    

    @property
    def jbatch_Flow53(self):
        return self.__jbatch_Flow53

    @jbatch_Flow53.setter
    def jbatch_Flow53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow53", None)
        self.__jbatch_Flow53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_End54"):
                    opp_val = getattr(item, "jbatch_End54", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_End54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_End54"):
                    opp_val = getattr(item, "jbatch_End54", None)
                    
                    setattr(item, "jbatch_End54", self)
                    

    @property
    def jbatch_Flow56(self):
        return self.__jbatch_Flow56

    @jbatch_Flow56.setter
    def jbatch_Flow56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow56", None)
        self.__jbatch_Flow56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Fail57"):
                    opp_val = getattr(item, "jbatch_Fail57", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Fail57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Fail57"):
                    opp_val = getattr(item, "jbatch_Fail57", None)
                    
                    setattr(item, "jbatch_Fail57", self)
                    

    @property
    def jbatch_Flow51(self):
        return self.__jbatch_Flow51

    @jbatch_Flow51.setter
    def jbatch_Flow51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow51", None)
        self.__jbatch_Flow51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Step"):
                    opp_val = getattr(item, "jbatch_Step", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Step"):
                    opp_val = getattr(item, "jbatch_Step", None)
                    
                    setattr(item, "jbatch_Step", self)
                    

    @property
    def jbatch_Flow62(self):
        return self.__jbatch_Flow62

    @jbatch_Flow62.setter
    def jbatch_Flow62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow62", None)
        self.__jbatch_Flow62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Stop63"):
                    opp_val = getattr(item, "jbatch_Stop63", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Stop63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Stop63"):
                    opp_val = getattr(item, "jbatch_Stop63", None)
                    
                    setattr(item, "jbatch_Stop63", self)
                    

    @property
    def jbatch_Flow83(self):
        return self.__jbatch_Flow83

    @jbatch_Flow83.setter
    def jbatch_Flow83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow83", None)
        self.__jbatch_Flow83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Job82"):
                opp_val = getattr(old_value, "jbatch_Job82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Job82"):
                opp_val = getattr(value, "jbatch_Job82", None)
                if opp_val is None:
                    setattr(value, "jbatch_Job82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Flow49(self):
        return self.__jbatch_Flow49

    @jbatch_Flow49.setter
    def jbatch_Flow49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow49", None)
        self.__jbatch_Flow49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Split"):
                    opp_val = getattr(item, "jbatch_Split", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Split", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Split"):
                    opp_val = getattr(item, "jbatch_Split", None)
                    
                    setattr(item, "jbatch_Split", self)
                    

    @property
    def jbatch_Flow59(self):
        return self.__jbatch_Flow59

    @jbatch_Flow59.setter
    def jbatch_Flow59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Flow__jbatch_Flow59", None)
        self.__jbatch_Flow59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Next60"):
                    opp_val = getattr(item, "jbatch_Next60", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Next60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Next60"):
                    opp_val = getattr(item, "jbatch_Next60", None)
                    
                    setattr(item, "jbatch_Next60", self)
                    

class jbatch_EStringToStringMapEntry:

    pass
class jbatch_Stop:

    def __init__(self, on: str, restart: str, exitStatus: str, jbatch_Stop: "jbatch_Decision" = None, jbatch_Stop63: "jbatch_Flow" = None, jbatch_Stop146: "jbatch_Step" = None):
        self.on = on
        self.restart = restart
        self.exitStatus = exitStatus
        self.jbatch_Stop = jbatch_Stop
        self.jbatch_Stop63 = jbatch_Stop63
        self.jbatch_Stop146 = jbatch_Stop146
        
    @property
    def restart(self) -> str:
        return self.__restart

    @restart.setter
    def restart(self, restart: str):
        self.__restart = restart

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def exitStatus(self) -> str:
        return self.__exitStatus

    @exitStatus.setter
    def exitStatus(self, exitStatus: str):
        self.__exitStatus = exitStatus

    @property
    def jbatch_Stop(self):
        return self.__jbatch_Stop

    @jbatch_Stop.setter
    def jbatch_Stop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Stop__jbatch_Stop", None)
        self.__jbatch_Stop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Decision32"):
                opp_val = getattr(old_value, "jbatch_Decision32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Decision32"):
                opp_val = getattr(value, "jbatch_Decision32", None)
                if opp_val is None:
                    setattr(value, "jbatch_Decision32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Stop146(self):
        return self.__jbatch_Stop146

    @jbatch_Stop146.setter
    def jbatch_Stop146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Stop__jbatch_Stop146", None)
        self.__jbatch_Stop146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step145"):
                opp_val = getattr(old_value, "jbatch_Step145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step145"):
                opp_val = getattr(value, "jbatch_Step145", None)
                if opp_val is None:
                    setattr(value, "jbatch_Step145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Stop63(self):
        return self.__jbatch_Stop63

    @jbatch_Stop63.setter
    def jbatch_Stop63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Stop__jbatch_Stop63", None)
        self.__jbatch_Stop63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow62"):
                opp_val = getattr(old_value, "jbatch_Flow62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow62"):
                opp_val = getattr(value, "jbatch_Flow62", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_Next:

    def __init__(self, on: str, to: str, jbatch_Next: "jbatch_Decision" = None, jbatch_Next60: "jbatch_Flow" = None, jbatch_Next143: "jbatch_Step" = None):
        self.on = on
        self.to = to
        self.jbatch_Next = jbatch_Next
        self.jbatch_Next60 = jbatch_Next60
        self.jbatch_Next143 = jbatch_Next143
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def jbatch_Next143(self):
        return self.__jbatch_Next143

    @jbatch_Next143.setter
    def jbatch_Next143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Next__jbatch_Next143", None)
        self.__jbatch_Next143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step142"):
                opp_val = getattr(old_value, "jbatch_Step142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step142"):
                opp_val = getattr(value, "jbatch_Step142", None)
                if opp_val is None:
                    setattr(value, "jbatch_Step142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Next(self):
        return self.__jbatch_Next

    @jbatch_Next.setter
    def jbatch_Next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Next__jbatch_Next", None)
        self.__jbatch_Next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Decision30"):
                opp_val = getattr(old_value, "jbatch_Decision30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Decision30"):
                opp_val = getattr(value, "jbatch_Decision30", None)
                if opp_val is None:
                    setattr(value, "jbatch_Decision30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Next60(self):
        return self.__jbatch_Next60

    @jbatch_Next60.setter
    def jbatch_Next60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Next__jbatch_Next60", None)
        self.__jbatch_Next60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow59"):
                opp_val = getattr(old_value, "jbatch_Flow59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow59"):
                opp_val = getattr(value, "jbatch_Flow59", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_Fail:

    def __init__(self, exitStatus: str, on: str, jbatch_Fail: "jbatch_Decision" = None, jbatch_Fail57: "jbatch_Flow" = None, jbatch_Fail140: "jbatch_Step" = None):
        self.exitStatus = exitStatus
        self.on = on
        self.jbatch_Fail = jbatch_Fail
        self.jbatch_Fail57 = jbatch_Fail57
        self.jbatch_Fail140 = jbatch_Fail140
        
    @property
    def exitStatus(self) -> str:
        return self.__exitStatus

    @exitStatus.setter
    def exitStatus(self, exitStatus: str):
        self.__exitStatus = exitStatus

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def jbatch_Fail(self):
        return self.__jbatch_Fail

    @jbatch_Fail.setter
    def jbatch_Fail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Fail__jbatch_Fail", None)
        self.__jbatch_Fail = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Decision28"):
                opp_val = getattr(old_value, "jbatch_Decision28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Decision28"):
                opp_val = getattr(value, "jbatch_Decision28", None)
                if opp_val is None:
                    setattr(value, "jbatch_Decision28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Fail140(self):
        return self.__jbatch_Fail140

    @jbatch_Fail140.setter
    def jbatch_Fail140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Fail__jbatch_Fail140", None)
        self.__jbatch_Fail140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step139"):
                opp_val = getattr(old_value, "jbatch_Step139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step139"):
                opp_val = getattr(value, "jbatch_Step139", None)
                if opp_val is None:
                    setattr(value, "jbatch_Step139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Fail57(self):
        return self.__jbatch_Fail57

    @jbatch_Fail57.setter
    def jbatch_Fail57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Fail__jbatch_Fail57", None)
        self.__jbatch_Fail57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow56"):
                opp_val = getattr(old_value, "jbatch_Flow56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow56"):
                opp_val = getattr(value, "jbatch_Flow56", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_End:

    def __init__(self, exitStatus: str, on: str, jbatch_End: "jbatch_Decision" = None, jbatch_End54: "jbatch_Flow" = None, jbatch_End137: "jbatch_Step" = None):
        self.exitStatus = exitStatus
        self.on = on
        self.jbatch_End = jbatch_End
        self.jbatch_End54 = jbatch_End54
        self.jbatch_End137 = jbatch_End137
        
    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def exitStatus(self) -> str:
        return self.__exitStatus

    @exitStatus.setter
    def exitStatus(self, exitStatus: str):
        self.__exitStatus = exitStatus

    @property
    def jbatch_End137(self):
        return self.__jbatch_End137

    @jbatch_End137.setter
    def jbatch_End137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_End__jbatch_End137", None)
        self.__jbatch_End137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step136"):
                opp_val = getattr(old_value, "jbatch_Step136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step136"):
                opp_val = getattr(value, "jbatch_Step136", None)
                if opp_val is None:
                    setattr(value, "jbatch_Step136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_End(self):
        return self.__jbatch_End

    @jbatch_End.setter
    def jbatch_End(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_End__jbatch_End", None)
        self.__jbatch_End = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Decision26"):
                opp_val = getattr(old_value, "jbatch_Decision26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Decision26"):
                opp_val = getattr(value, "jbatch_Decision26", None)
                if opp_val is None:
                    setattr(value, "jbatch_Decision26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_End54(self):
        return self.__jbatch_End54

    @jbatch_End54.setter
    def jbatch_End54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_End__jbatch_End54", None)
        self.__jbatch_End54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow53"):
                opp_val = getattr(old_value, "jbatch_Flow53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow53"):
                opp_val = getattr(value, "jbatch_Flow53", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jbatch_DocumentRoot:

    def __init__(self, mixed: str, jbatch_DocumentRoot: set["jbatch_EStringToStringMapEntry"] = None, jbatch_DocumentRoot35: set["jbatch_EStringToStringMapEntry"] = None, jbatch_DocumentRoot38: set["jbatch_Job"] = None):
        self.mixed = mixed
        self.jbatch_DocumentRoot = jbatch_DocumentRoot if jbatch_DocumentRoot is not None else set()
        self.jbatch_DocumentRoot35 = jbatch_DocumentRoot35 if jbatch_DocumentRoot35 is not None else set()
        self.jbatch_DocumentRoot38 = jbatch_DocumentRoot38 if jbatch_DocumentRoot38 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def jbatch_DocumentRoot38(self):
        return self.__jbatch_DocumentRoot38

    @jbatch_DocumentRoot38.setter
    def jbatch_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_DocumentRoot__jbatch_DocumentRoot38", None)
        self.__jbatch_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Job"):
                    opp_val = getattr(item, "jbatch_Job", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Job", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Job"):
                    opp_val = getattr(item, "jbatch_Job", None)
                    
                    setattr(item, "jbatch_Job", self)
                    

    @property
    def jbatch_DocumentRoot(self):
        return self.__jbatch_DocumentRoot

    @jbatch_DocumentRoot.setter
    def jbatch_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_DocumentRoot__jbatch_DocumentRoot", None)
        self.__jbatch_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jbatch_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jbatch_EStringToStringMapEntry", None)
                    
                    setattr(item, "jbatch_EStringToStringMapEntry", self)
                    

    @property
    def jbatch_DocumentRoot35(self):
        return self.__jbatch_DocumentRoot35

    @jbatch_DocumentRoot35.setter
    def jbatch_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_DocumentRoot__jbatch_DocumentRoot35", None)
        self.__jbatch_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_EStringToStringMapEntry36"):
                    opp_val = getattr(item, "jbatch_EStringToStringMapEntry36", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_EStringToStringMapEntry36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_EStringToStringMapEntry36"):
                    opp_val = getattr(item, "jbatch_EStringToStringMapEntry36", None)
                    
                    setattr(item, "jbatch_EStringToStringMapEntry36", self)
                    

class jbatch_Decision:

    def __init__(self, transitionElements: str, ref: str, id: str, jbatch_Decision: "jbatch_Properties" = None, jbatch_Decision26: set["jbatch_End"] = None, jbatch_Decision28: set["jbatch_Fail"] = None, jbatch_Decision30: set["jbatch_Next"] = None, jbatch_Decision32: set["jbatch_Stop"] = None, jbatch_Decision44: "jbatch_Flow" = None, jbatch_Decision80: "jbatch_Job" = None):
        self.transitionElements = transitionElements
        self.ref = ref
        self.id = id
        self.jbatch_Decision = jbatch_Decision
        self.jbatch_Decision26 = jbatch_Decision26 if jbatch_Decision26 is not None else set()
        self.jbatch_Decision28 = jbatch_Decision28 if jbatch_Decision28 is not None else set()
        self.jbatch_Decision30 = jbatch_Decision30 if jbatch_Decision30 is not None else set()
        self.jbatch_Decision32 = jbatch_Decision32 if jbatch_Decision32 is not None else set()
        self.jbatch_Decision44 = jbatch_Decision44
        self.jbatch_Decision80 = jbatch_Decision80
        
    @property
    def transitionElements(self) -> str:
        return self.__transitionElements

    @transitionElements.setter
    def transitionElements(self, transitionElements: str):
        self.__transitionElements = transitionElements

    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jbatch_Decision(self):
        return self.__jbatch_Decision

    @jbatch_Decision.setter
    def jbatch_Decision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision", None)
        self.__jbatch_Decision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties24"):
                opp_val = getattr(old_value, "jbatch_Properties24", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties24"):
                opp_val = getattr(value, "jbatch_Properties24", None)
                setattr(value, "jbatch_Properties24", self)

    @property
    def jbatch_Decision30(self):
        return self.__jbatch_Decision30

    @jbatch_Decision30.setter
    def jbatch_Decision30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision30", None)
        self.__jbatch_Decision30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Next"):
                    opp_val = getattr(item, "jbatch_Next", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Next", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Next"):
                    opp_val = getattr(item, "jbatch_Next", None)
                    
                    setattr(item, "jbatch_Next", self)
                    

    @property
    def jbatch_Decision80(self):
        return self.__jbatch_Decision80

    @jbatch_Decision80.setter
    def jbatch_Decision80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision80", None)
        self.__jbatch_Decision80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Job79"):
                opp_val = getattr(old_value, "jbatch_Job79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Job79"):
                opp_val = getattr(value, "jbatch_Job79", None)
                if opp_val is None:
                    setattr(value, "jbatch_Job79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Decision44(self):
        return self.__jbatch_Decision44

    @jbatch_Decision44.setter
    def jbatch_Decision44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision44", None)
        self.__jbatch_Decision44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Flow"):
                opp_val = getattr(old_value, "jbatch_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Flow"):
                opp_val = getattr(value, "jbatch_Flow", None)
                if opp_val is None:
                    setattr(value, "jbatch_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Decision32(self):
        return self.__jbatch_Decision32

    @jbatch_Decision32.setter
    def jbatch_Decision32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision32", None)
        self.__jbatch_Decision32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Stop"):
                    opp_val = getattr(item, "jbatch_Stop", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Stop", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Stop"):
                    opp_val = getattr(item, "jbatch_Stop", None)
                    
                    setattr(item, "jbatch_Stop", self)
                    

    @property
    def jbatch_Decision26(self):
        return self.__jbatch_Decision26

    @jbatch_Decision26.setter
    def jbatch_Decision26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision26", None)
        self.__jbatch_Decision26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_End"):
                    opp_val = getattr(item, "jbatch_End", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_End", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_End"):
                    opp_val = getattr(item, "jbatch_End", None)
                    
                    setattr(item, "jbatch_End", self)
                    

    @property
    def jbatch_Decision28(self):
        return self.__jbatch_Decision28

    @jbatch_Decision28.setter
    def jbatch_Decision28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Decision__jbatch_Decision28", None)
        self.__jbatch_Decision28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Fail"):
                    opp_val = getattr(item, "jbatch_Fail", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Fail", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Fail"):
                    opp_val = getattr(item, "jbatch_Fail", None)
                    
                    setattr(item, "jbatch_Fail", self)
                    

class jbatch_Collector:

    def __init__(self, ref: str, jbatch_Collector: "jbatch_Properties" = None, jbatch_Collector100: "jbatch_Partition" = None):
        self.ref = ref
        self.jbatch_Collector = jbatch_Collector
        self.jbatch_Collector100 = jbatch_Collector100
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_Collector(self):
        return self.__jbatch_Collector

    @jbatch_Collector.setter
    def jbatch_Collector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Collector__jbatch_Collector", None)
        self.__jbatch_Collector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties22"):
                opp_val = getattr(old_value, "jbatch_Properties22", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties22"):
                opp_val = getattr(value, "jbatch_Properties22", None)
                setattr(value, "jbatch_Properties22", self)

    @property
    def jbatch_Collector100(self):
        return self.__jbatch_Collector100

    @jbatch_Collector100.setter
    def jbatch_Collector100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Collector__jbatch_Collector100", None)
        self.__jbatch_Collector100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition99"):
                opp_val = getattr(old_value, "jbatch_Partition99", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition99"):
                opp_val = getattr(value, "jbatch_Partition99", None)
                setattr(value, "jbatch_Partition99", self)

class jbatch_ExceptionClassFilter:

    pass
class jbatch_ItemWriter:

    def __init__(self, ref: str, jbatch_ItemWriter: "jbatch_Chunk" = None, jbatch_ItemWriter71: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_ItemWriter = jbatch_ItemWriter
        self.jbatch_ItemWriter71 = jbatch_ItemWriter71
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_ItemWriter71(self):
        return self.__jbatch_ItemWriter71

    @jbatch_ItemWriter71.setter
    def jbatch_ItemWriter71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemWriter__jbatch_ItemWriter71", None)
        self.__jbatch_ItemWriter71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties72"):
                opp_val = getattr(old_value, "jbatch_Properties72", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties72"):
                opp_val = getattr(value, "jbatch_Properties72", None)
                setattr(value, "jbatch_Properties72", self)

    @property
    def jbatch_ItemWriter(self):
        return self.__jbatch_ItemWriter

    @jbatch_ItemWriter.setter
    def jbatch_ItemWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemWriter__jbatch_ItemWriter", None)
        self.__jbatch_ItemWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Chunk9"):
                opp_val = getattr(old_value, "jbatch_Chunk9", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Chunk9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Chunk9"):
                opp_val = getattr(value, "jbatch_Chunk9", None)
                setattr(value, "jbatch_Chunk9", self)

class jbatch_ItemReader:

    def __init__(self, ref: str, jbatch_ItemReader: "jbatch_Chunk" = None, jbatch_ItemReader68: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_ItemReader = jbatch_ItemReader
        self.jbatch_ItemReader68 = jbatch_ItemReader68
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_ItemReader(self):
        return self.__jbatch_ItemReader

    @jbatch_ItemReader.setter
    def jbatch_ItemReader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemReader__jbatch_ItemReader", None)
        self.__jbatch_ItemReader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Chunk"):
                opp_val = getattr(old_value, "jbatch_Chunk", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Chunk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Chunk"):
                opp_val = getattr(value, "jbatch_Chunk", None)
                setattr(value, "jbatch_Chunk", self)

    @property
    def jbatch_ItemReader68(self):
        return self.__jbatch_ItemReader68

    @jbatch_ItemReader68.setter
    def jbatch_ItemReader68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemReader__jbatch_ItemReader68", None)
        self.__jbatch_ItemReader68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties69"):
                opp_val = getattr(old_value, "jbatch_Properties69", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties69"):
                opp_val = getattr(value, "jbatch_Properties69", None)
                setattr(value, "jbatch_Properties69", self)

class jbatch_Chunk:

    def __init__(self, timeLimit: str, checkpointPolicy: str, itemCount: str, retryLimit: str, skipLimit: str, jbatch_Chunk7: "jbatch_ItemProcessor" = None, jbatch_Chunk: "jbatch_ItemReader" = None, jbatch_Chunk9: "jbatch_ItemWriter" = None, jbatch_Chunk11: "jbatch_CheckpointAlgorithm" = None, jbatch_Chunk14: "jbatch_ExceptionClassFilter" = None, jbatch_Chunk16: "jbatch_ExceptionClassFilter" = None, jbatch_Chunk19: "jbatch_ExceptionClassFilter" = None, jbatch_Chunk131: "jbatch_Step" = None):
        self.timeLimit = timeLimit
        self.checkpointPolicy = checkpointPolicy
        self.itemCount = itemCount
        self.retryLimit = retryLimit
        self.skipLimit = skipLimit
        self.jbatch_Chunk7 = jbatch_Chunk7
        self.jbatch_Chunk = jbatch_Chunk
        self.jbatch_Chunk9 = jbatch_Chunk9
        self.jbatch_Chunk11 = jbatch_Chunk11
        self.jbatch_Chunk14 = jbatch_Chunk14
        self.jbatch_Chunk16 = jbatch_Chunk16
        self.jbatch_Chunk19 = jbatch_Chunk19
        self.jbatch_Chunk131 = jbatch_Chunk131
        
    @property
    def skipLimit(self) -> str:
        return self.__skipLimit

    @skipLimit.setter
    def skipLimit(self, skipLimit: str):
        self.__skipLimit = skipLimit

    @property
    def retryLimit(self) -> str:
        return self.__retryLimit

    @retryLimit.setter
    def retryLimit(self, retryLimit: str):
        self.__retryLimit = retryLimit

    @property
    def timeLimit(self) -> str:
        return self.__timeLimit

    @timeLimit.setter
    def timeLimit(self, timeLimit: str):
        self.__timeLimit = timeLimit

    @property
    def itemCount(self) -> str:
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

    @property
    def checkpointPolicy(self) -> str:
        return self.__checkpointPolicy

    @checkpointPolicy.setter
    def checkpointPolicy(self, checkpointPolicy: str):
        self.__checkpointPolicy = checkpointPolicy

    @property
    def jbatch_Chunk11(self):
        return self.__jbatch_Chunk11

    @jbatch_Chunk11.setter
    def jbatch_Chunk11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk11", None)
        self.__jbatch_Chunk11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_CheckpointAlgorithm12"):
                opp_val = getattr(old_value, "jbatch_CheckpointAlgorithm12", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_CheckpointAlgorithm12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_CheckpointAlgorithm12"):
                opp_val = getattr(value, "jbatch_CheckpointAlgorithm12", None)
                setattr(value, "jbatch_CheckpointAlgorithm12", self)

    @property
    def jbatch_Chunk14(self):
        return self.__jbatch_Chunk14

    @jbatch_Chunk14.setter
    def jbatch_Chunk14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk14", None)
        self.__jbatch_Chunk14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ExceptionClassFilter"):
                opp_val = getattr(old_value, "jbatch_ExceptionClassFilter", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ExceptionClassFilter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ExceptionClassFilter"):
                opp_val = getattr(value, "jbatch_ExceptionClassFilter", None)
                setattr(value, "jbatch_ExceptionClassFilter", self)

    @property
    def jbatch_Chunk(self):
        return self.__jbatch_Chunk

    @jbatch_Chunk.setter
    def jbatch_Chunk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk", None)
        self.__jbatch_Chunk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemReader"):
                opp_val = getattr(old_value, "jbatch_ItemReader", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemReader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemReader"):
                opp_val = getattr(value, "jbatch_ItemReader", None)
                setattr(value, "jbatch_ItemReader", self)

    @property
    def jbatch_Chunk19(self):
        return self.__jbatch_Chunk19

    @jbatch_Chunk19.setter
    def jbatch_Chunk19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk19", None)
        self.__jbatch_Chunk19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ExceptionClassFilter20"):
                opp_val = getattr(old_value, "jbatch_ExceptionClassFilter20", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ExceptionClassFilter20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ExceptionClassFilter20"):
                opp_val = getattr(value, "jbatch_ExceptionClassFilter20", None)
                setattr(value, "jbatch_ExceptionClassFilter20", self)

    @property
    def jbatch_Chunk7(self):
        return self.__jbatch_Chunk7

    @jbatch_Chunk7.setter
    def jbatch_Chunk7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk7", None)
        self.__jbatch_Chunk7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemProcessor"):
                opp_val = getattr(old_value, "jbatch_ItemProcessor", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemProcessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemProcessor"):
                opp_val = getattr(value, "jbatch_ItemProcessor", None)
                setattr(value, "jbatch_ItemProcessor", self)

    @property
    def jbatch_Chunk9(self):
        return self.__jbatch_Chunk9

    @jbatch_Chunk9.setter
    def jbatch_Chunk9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk9", None)
        self.__jbatch_Chunk9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemWriter"):
                opp_val = getattr(old_value, "jbatch_ItemWriter", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemWriter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemWriter"):
                opp_val = getattr(value, "jbatch_ItemWriter", None)
                setattr(value, "jbatch_ItemWriter", self)

    @property
    def jbatch_Chunk131(self):
        return self.__jbatch_Chunk131

    @jbatch_Chunk131.setter
    def jbatch_Chunk131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk131", None)
        self.__jbatch_Chunk131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step130"):
                opp_val = getattr(old_value, "jbatch_Step130", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Step130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step130"):
                opp_val = getattr(value, "jbatch_Step130", None)
                setattr(value, "jbatch_Step130", self)

    @property
    def jbatch_Chunk16(self):
        return self.__jbatch_Chunk16

    @jbatch_Chunk16.setter
    def jbatch_Chunk16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Chunk__jbatch_Chunk16", None)
        self.__jbatch_Chunk16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ExceptionClassFilter17"):
                opp_val = getattr(old_value, "jbatch_ExceptionClassFilter17", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ExceptionClassFilter17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ExceptionClassFilter17"):
                opp_val = getattr(value, "jbatch_ExceptionClassFilter17", None)
                setattr(value, "jbatch_ExceptionClassFilter17", self)

class jbatch_CheckpointAlgorithm:

    def __init__(self, ref: str, jbatch_CheckpointAlgorithm: "jbatch_Properties" = None, jbatch_CheckpointAlgorithm12: "jbatch_Chunk" = None):
        self.ref = ref
        self.jbatch_CheckpointAlgorithm = jbatch_CheckpointAlgorithm
        self.jbatch_CheckpointAlgorithm12 = jbatch_CheckpointAlgorithm12
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_CheckpointAlgorithm(self):
        return self.__jbatch_CheckpointAlgorithm

    @jbatch_CheckpointAlgorithm.setter
    def jbatch_CheckpointAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_CheckpointAlgorithm__jbatch_CheckpointAlgorithm", None)
        self.__jbatch_CheckpointAlgorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties4"):
                opp_val = getattr(old_value, "jbatch_Properties4", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties4"):
                opp_val = getattr(value, "jbatch_Properties4", None)
                setattr(value, "jbatch_Properties4", self)

    @property
    def jbatch_CheckpointAlgorithm12(self):
        return self.__jbatch_CheckpointAlgorithm12

    @jbatch_CheckpointAlgorithm12.setter
    def jbatch_CheckpointAlgorithm12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_CheckpointAlgorithm__jbatch_CheckpointAlgorithm12", None)
        self.__jbatch_CheckpointAlgorithm12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Chunk11"):
                opp_val = getattr(old_value, "jbatch_Chunk11", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Chunk11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Chunk11"):
                opp_val = getattr(value, "jbatch_Chunk11", None)
                setattr(value, "jbatch_Chunk11", self)

class jbatch_Batchlet:

    def __init__(self, ref: str, jbatch_Batchlet: "jbatch_Properties" = None, jbatch_Batchlet128: "jbatch_Step" = None):
        self.ref = ref
        self.jbatch_Batchlet = jbatch_Batchlet
        self.jbatch_Batchlet128 = jbatch_Batchlet128
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_Batchlet128(self):
        return self.__jbatch_Batchlet128

    @jbatch_Batchlet128.setter
    def jbatch_Batchlet128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Batchlet__jbatch_Batchlet128", None)
        self.__jbatch_Batchlet128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step127"):
                opp_val = getattr(old_value, "jbatch_Step127", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Step127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step127"):
                opp_val = getattr(value, "jbatch_Step127", None)
                setattr(value, "jbatch_Step127", self)

    @property
    def jbatch_Batchlet(self):
        return self.__jbatch_Batchlet

    @jbatch_Batchlet.setter
    def jbatch_Batchlet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Batchlet__jbatch_Batchlet", None)
        self.__jbatch_Batchlet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties2"):
                opp_val = getattr(old_value, "jbatch_Properties2", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties2"):
                opp_val = getattr(value, "jbatch_Properties2", None)
                setattr(value, "jbatch_Properties2", self)

class jbatch_Properties:

    def __init__(self, partition: str, jbatch_Properties: "jbatch_Analyzer" = None, jbatch_Properties2: "jbatch_Batchlet" = None, jbatch_Properties4: "jbatch_CheckpointAlgorithm" = None, jbatch_Properties22: "jbatch_Collector" = None, jbatch_Properties24: "jbatch_Decision" = None, jbatch_Properties66: "jbatch_ItemProcessor" = None, jbatch_Properties69: "jbatch_ItemReader" = None, jbatch_Properties72: "jbatch_ItemWriter" = None, jbatch_Properties75: "jbatch_Job" = None, jbatch_Properties91: "jbatch_Listener" = None, jbatch_Properties111: "jbatch_PartitionPlan" = None, jbatch_Properties108: "jbatch_PartitionMapper" = None, jbatch_Properties116: set["jbatch_Property"] = None, jbatch_Properties114: "jbatch_PartitionReducer" = None, jbatch_Properties122: "jbatch_Step" = None):
        self.partition = partition
        self.jbatch_Properties = jbatch_Properties
        self.jbatch_Properties2 = jbatch_Properties2
        self.jbatch_Properties4 = jbatch_Properties4
        self.jbatch_Properties22 = jbatch_Properties22
        self.jbatch_Properties24 = jbatch_Properties24
        self.jbatch_Properties66 = jbatch_Properties66
        self.jbatch_Properties69 = jbatch_Properties69
        self.jbatch_Properties72 = jbatch_Properties72
        self.jbatch_Properties75 = jbatch_Properties75
        self.jbatch_Properties91 = jbatch_Properties91
        self.jbatch_Properties111 = jbatch_Properties111
        self.jbatch_Properties108 = jbatch_Properties108
        self.jbatch_Properties116 = jbatch_Properties116 if jbatch_Properties116 is not None else set()
        self.jbatch_Properties114 = jbatch_Properties114
        self.jbatch_Properties122 = jbatch_Properties122
        
    @property
    def partition(self) -> str:
        return self.__partition

    @partition.setter
    def partition(self, partition: str):
        self.__partition = partition

    @property
    def jbatch_Properties(self):
        return self.__jbatch_Properties

    @jbatch_Properties.setter
    def jbatch_Properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties", None)
        self.__jbatch_Properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Analyzer"):
                opp_val = getattr(old_value, "jbatch_Analyzer", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Analyzer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Analyzer"):
                opp_val = getattr(value, "jbatch_Analyzer", None)
                setattr(value, "jbatch_Analyzer", self)

    @property
    def jbatch_Properties116(self):
        return self.__jbatch_Properties116

    @jbatch_Properties116.setter
    def jbatch_Properties116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties116", None)
        self.__jbatch_Properties116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jbatch_Property"):
                    opp_val = getattr(item, "jbatch_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "jbatch_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jbatch_Property"):
                    opp_val = getattr(item, "jbatch_Property", None)
                    
                    setattr(item, "jbatch_Property", self)
                    

    @property
    def jbatch_Properties108(self):
        return self.__jbatch_Properties108

    @jbatch_Properties108.setter
    def jbatch_Properties108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties108", None)
        self.__jbatch_Properties108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_PartitionMapper107"):
                opp_val = getattr(old_value, "jbatch_PartitionMapper107", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_PartitionMapper107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_PartitionMapper107"):
                opp_val = getattr(value, "jbatch_PartitionMapper107", None)
                setattr(value, "jbatch_PartitionMapper107", self)

    @property
    def jbatch_Properties75(self):
        return self.__jbatch_Properties75

    @jbatch_Properties75.setter
    def jbatch_Properties75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties75", None)
        self.__jbatch_Properties75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Job74"):
                opp_val = getattr(old_value, "jbatch_Job74", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Job74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Job74"):
                opp_val = getattr(value, "jbatch_Job74", None)
                setattr(value, "jbatch_Job74", self)

    @property
    def jbatch_Properties22(self):
        return self.__jbatch_Properties22

    @jbatch_Properties22.setter
    def jbatch_Properties22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties22", None)
        self.__jbatch_Properties22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Collector"):
                opp_val = getattr(old_value, "jbatch_Collector", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Collector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Collector"):
                opp_val = getattr(value, "jbatch_Collector", None)
                setattr(value, "jbatch_Collector", self)

    @property
    def jbatch_Properties69(self):
        return self.__jbatch_Properties69

    @jbatch_Properties69.setter
    def jbatch_Properties69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties69", None)
        self.__jbatch_Properties69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemReader68"):
                opp_val = getattr(old_value, "jbatch_ItemReader68", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemReader68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemReader68"):
                opp_val = getattr(value, "jbatch_ItemReader68", None)
                setattr(value, "jbatch_ItemReader68", self)

    @property
    def jbatch_Properties66(self):
        return self.__jbatch_Properties66

    @jbatch_Properties66.setter
    def jbatch_Properties66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties66", None)
        self.__jbatch_Properties66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemProcessor65"):
                opp_val = getattr(old_value, "jbatch_ItemProcessor65", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemProcessor65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemProcessor65"):
                opp_val = getattr(value, "jbatch_ItemProcessor65", None)
                setattr(value, "jbatch_ItemProcessor65", self)

    @property
    def jbatch_Properties114(self):
        return self.__jbatch_Properties114

    @jbatch_Properties114.setter
    def jbatch_Properties114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties114", None)
        self.__jbatch_Properties114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_PartitionReducer113"):
                opp_val = getattr(old_value, "jbatch_PartitionReducer113", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_PartitionReducer113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_PartitionReducer113"):
                opp_val = getattr(value, "jbatch_PartitionReducer113", None)
                setattr(value, "jbatch_PartitionReducer113", self)

    @property
    def jbatch_Properties122(self):
        return self.__jbatch_Properties122

    @jbatch_Properties122.setter
    def jbatch_Properties122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties122", None)
        self.__jbatch_Properties122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Step121"):
                opp_val = getattr(old_value, "jbatch_Step121", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Step121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Step121"):
                opp_val = getattr(value, "jbatch_Step121", None)
                setattr(value, "jbatch_Step121", self)

    @property
    def jbatch_Properties24(self):
        return self.__jbatch_Properties24

    @jbatch_Properties24.setter
    def jbatch_Properties24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties24", None)
        self.__jbatch_Properties24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Decision"):
                opp_val = getattr(old_value, "jbatch_Decision", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Decision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Decision"):
                opp_val = getattr(value, "jbatch_Decision", None)
                setattr(value, "jbatch_Decision", self)

    @property
    def jbatch_Properties111(self):
        return self.__jbatch_Properties111

    @jbatch_Properties111.setter
    def jbatch_Properties111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties111", None)
        self.__jbatch_Properties111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_PartitionPlan110"):
                opp_val = getattr(old_value, "jbatch_PartitionPlan110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_PartitionPlan110"):
                opp_val = getattr(value, "jbatch_PartitionPlan110", None)
                if opp_val is None:
                    setattr(value, "jbatch_PartitionPlan110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jbatch_Properties2(self):
        return self.__jbatch_Properties2

    @jbatch_Properties2.setter
    def jbatch_Properties2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties2", None)
        self.__jbatch_Properties2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Batchlet"):
                opp_val = getattr(old_value, "jbatch_Batchlet", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Batchlet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Batchlet"):
                opp_val = getattr(value, "jbatch_Batchlet", None)
                setattr(value, "jbatch_Batchlet", self)

    @property
    def jbatch_Properties91(self):
        return self.__jbatch_Properties91

    @jbatch_Properties91.setter
    def jbatch_Properties91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties91", None)
        self.__jbatch_Properties91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Listener"):
                opp_val = getattr(old_value, "jbatch_Listener", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Listener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Listener"):
                opp_val = getattr(value, "jbatch_Listener", None)
                setattr(value, "jbatch_Listener", self)

    @property
    def jbatch_Properties4(self):
        return self.__jbatch_Properties4

    @jbatch_Properties4.setter
    def jbatch_Properties4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties4", None)
        self.__jbatch_Properties4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_CheckpointAlgorithm"):
                opp_val = getattr(old_value, "jbatch_CheckpointAlgorithm", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_CheckpointAlgorithm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_CheckpointAlgorithm"):
                opp_val = getattr(value, "jbatch_CheckpointAlgorithm", None)
                setattr(value, "jbatch_CheckpointAlgorithm", self)

    @property
    def jbatch_Properties72(self):
        return self.__jbatch_Properties72

    @jbatch_Properties72.setter
    def jbatch_Properties72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Properties__jbatch_Properties72", None)
        self.__jbatch_Properties72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_ItemWriter71"):
                opp_val = getattr(old_value, "jbatch_ItemWriter71", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_ItemWriter71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_ItemWriter71"):
                opp_val = getattr(value, "jbatch_ItemWriter71", None)
                setattr(value, "jbatch_ItemWriter71", self)

class jbatch_ItemProcessor:

    def __init__(self, ref: str, jbatch_ItemProcessor: "jbatch_Chunk" = None, jbatch_ItemProcessor65: "jbatch_Properties" = None):
        self.ref = ref
        self.jbatch_ItemProcessor = jbatch_ItemProcessor
        self.jbatch_ItemProcessor65 = jbatch_ItemProcessor65
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_ItemProcessor65(self):
        return self.__jbatch_ItemProcessor65

    @jbatch_ItemProcessor65.setter
    def jbatch_ItemProcessor65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemProcessor__jbatch_ItemProcessor65", None)
        self.__jbatch_ItemProcessor65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties66"):
                opp_val = getattr(old_value, "jbatch_Properties66", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties66"):
                opp_val = getattr(value, "jbatch_Properties66", None)
                setattr(value, "jbatch_Properties66", self)

    @property
    def jbatch_ItemProcessor(self):
        return self.__jbatch_ItemProcessor

    @jbatch_ItemProcessor.setter
    def jbatch_ItemProcessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_ItemProcessor__jbatch_ItemProcessor", None)
        self.__jbatch_ItemProcessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Chunk7"):
                opp_val = getattr(old_value, "jbatch_Chunk7", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Chunk7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Chunk7"):
                opp_val = getattr(value, "jbatch_Chunk7", None)
                setattr(value, "jbatch_Chunk7", self)

class jbatch_Analyzer:

    def __init__(self, ref: str, jbatch_Analyzer: "jbatch_Properties" = None, jbatch_Analyzer103: "jbatch_Partition" = None):
        self.ref = ref
        self.jbatch_Analyzer = jbatch_Analyzer
        self.jbatch_Analyzer103 = jbatch_Analyzer103
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def jbatch_Analyzer103(self):
        return self.__jbatch_Analyzer103

    @jbatch_Analyzer103.setter
    def jbatch_Analyzer103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Analyzer__jbatch_Analyzer103", None)
        self.__jbatch_Analyzer103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Partition102"):
                opp_val = getattr(old_value, "jbatch_Partition102", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Partition102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Partition102"):
                opp_val = getattr(value, "jbatch_Partition102", None)
                setattr(value, "jbatch_Partition102", self)

    @property
    def jbatch_Analyzer(self):
        return self.__jbatch_Analyzer

    @jbatch_Analyzer.setter
    def jbatch_Analyzer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jbatch_Analyzer__jbatch_Analyzer", None)
        self.__jbatch_Analyzer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jbatch_Properties"):
                opp_val = getattr(old_value, "jbatch_Properties", None)
                if opp_val == self:
                    setattr(old_value, "jbatch_Properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jbatch_Properties"):
                opp_val = getattr(value, "jbatch_Properties", None)
                setattr(value, "jbatch_Properties", self)

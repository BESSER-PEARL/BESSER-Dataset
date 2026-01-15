from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scxml_Finalize:

    pass
class scxml_Content:

    pass
class scxml_Data:

    def __init__(self, id: str, src: str, expr: str, scxml_Data: "scxml_DataModel" = None, scxml_Data149: "scxml_Content" = None):
        self.id = id
        self.src = src
        self.expr = expr
        self.scxml_Data = scxml_Data
        self.scxml_Data149 = scxml_Data149
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def scxml_Data149(self):
        return self.__scxml_Data149

    @scxml_Data149.setter
    def scxml_Data149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Data__scxml_Data149", None)
        self.__scxml_Data149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Content"):
                opp_val = getattr(old_value, "scxml_Content", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Content"):
                opp_val = getattr(value, "scxml_Content", None)
                setattr(value, "scxml_Content", self)

    @property
    def scxml_Data(self):
        return self.__scxml_Data

    @scxml_Data.setter
    def scxml_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Data__scxml_Data", None)
        self.__scxml_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DataModel147"):
                opp_val = getattr(old_value, "scxml_DataModel147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DataModel147"):
                opp_val = getattr(value, "scxml_DataModel147", None)
                if opp_val is None:
                    setattr(value, "scxml_DataModel147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Else:

    pass
class scxml_ElseIf:

    def __init__(self, cond: str, scxml_ElseIf: "scxml_If" = None):
        self.cond = cond
        self.scxml_ElseIf = scxml_ElseIf
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def scxml_ElseIf(self):
        return self.__scxml_ElseIf

    @scxml_ElseIf.setter
    def scxml_ElseIf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ElseIf__scxml_ElseIf", None)
        self.__scxml_ElseIf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If119"):
                opp_val = getattr(old_value, "scxml_If119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If119"):
                opp_val = getattr(value, "scxml_If119", None)
                if opp_val is None:
                    setattr(value, "scxml_If119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Donedata:

    pass
class scxml_Validate:

    def __init__(self, location: str, schema: str, scxml_Validate: "scxml_OnEntry" = None, scxml_Validate91: "scxml_OnExit" = None, scxml_Validate145: "scxml_If" = None, scxml_Validate196: "scxml_Finalize" = None):
        self.location = location
        self.schema = schema
        self.scxml_Validate = scxml_Validate
        self.scxml_Validate91 = scxml_Validate91
        self.scxml_Validate145 = scxml_Validate145
        self.scxml_Validate196 = scxml_Validate196
        
    @property
    def schema(self) -> str:
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def scxml_Validate(self):
        return self.__scxml_Validate

    @scxml_Validate.setter
    def scxml_Validate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Validate__scxml_Validate", None)
        self.__scxml_Validate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry64"):
                opp_val = getattr(old_value, "scxml_OnEntry64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry64"):
                opp_val = getattr(value, "scxml_OnEntry64", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Validate145(self):
        return self.__scxml_Validate145

    @scxml_Validate145.setter
    def scxml_Validate145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Validate__scxml_Validate145", None)
        self.__scxml_Validate145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If144"):
                opp_val = getattr(old_value, "scxml_If144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If144"):
                opp_val = getattr(value, "scxml_If144", None)
                if opp_val is None:
                    setattr(value, "scxml_If144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Validate91(self):
        return self.__scxml_Validate91

    @scxml_Validate91.setter
    def scxml_Validate91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Validate__scxml_Validate91", None)
        self.__scxml_Validate91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit90"):
                opp_val = getattr(old_value, "scxml_OnExit90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit90"):
                opp_val = getattr(value, "scxml_OnExit90", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Validate196(self):
        return self.__scxml_Validate196

    @scxml_Validate196.setter
    def scxml_Validate196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Validate__scxml_Validate196", None)
        self.__scxml_Validate196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize195"):
                opp_val = getattr(old_value, "scxml_Finalize195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize195"):
                opp_val = getattr(value, "scxml_Finalize195", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Send:

    def __init__(self, event: str, eventexpr: str, target: str, targetexpr: str, type: str, typeexpr: str, id: str, idlocation: str, delay: str, delayexpr: str, namelist: str, hints: str, hintsexpr: str, scxml_Send: "scxml_OnEntry" = None, scxml_Send88: "scxml_OnExit" = None, scxml_Send142: "scxml_If" = None, scxml_Send151: set["scxml_Param"] = None, scxml_Send154: "scxml_Content" = None, scxml_Send193: "scxml_Finalize" = None):
        self.event = event
        self.eventexpr = eventexpr
        self.target = target
        self.targetexpr = targetexpr
        self.type = type
        self.typeexpr = typeexpr
        self.id = id
        self.idlocation = idlocation
        self.delay = delay
        self.delayexpr = delayexpr
        self.namelist = namelist
        self.hints = hints
        self.hintsexpr = hintsexpr
        self.scxml_Send = scxml_Send
        self.scxml_Send88 = scxml_Send88
        self.scxml_Send142 = scxml_Send142
        self.scxml_Send151 = scxml_Send151 if scxml_Send151 is not None else set()
        self.scxml_Send154 = scxml_Send154
        self.scxml_Send193 = scxml_Send193
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def eventexpr(self) -> str:
        return self.__eventexpr

    @eventexpr.setter
    def eventexpr(self, eventexpr: str):
        self.__eventexpr = eventexpr

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def typeexpr(self) -> str:
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr

    @property
    def delay(self) -> str:
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay

    @property
    def namelist(self) -> str:
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist

    @property
    def idlocation(self) -> str:
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation

    @property
    def hints(self) -> str:
        return self.__hints

    @hints.setter
    def hints(self, hints: str):
        self.__hints = hints

    @property
    def hintsexpr(self) -> str:
        return self.__hintsexpr

    @hintsexpr.setter
    def hintsexpr(self, hintsexpr: str):
        self.__hintsexpr = hintsexpr

    @property
    def targetexpr(self) -> str:
        return self.__targetexpr

    @targetexpr.setter
    def targetexpr(self, targetexpr: str):
        self.__targetexpr = targetexpr

    @property
    def delayexpr(self) -> str:
        return self.__delayexpr

    @delayexpr.setter
    def delayexpr(self, delayexpr: str):
        self.__delayexpr = delayexpr

    @property
    def scxml_Send142(self):
        return self.__scxml_Send142

    @scxml_Send142.setter
    def scxml_Send142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send142", None)
        self.__scxml_Send142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If141"):
                opp_val = getattr(old_value, "scxml_If141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If141"):
                opp_val = getattr(value, "scxml_If141", None)
                if opp_val is None:
                    setattr(value, "scxml_If141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Send151(self):
        return self.__scxml_Send151

    @scxml_Send151.setter
    def scxml_Send151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send151", None)
        self.__scxml_Send151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Param152"):
                    opp_val = getattr(item, "scxml_Param152", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Param152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Param152"):
                    opp_val = getattr(item, "scxml_Param152", None)
                    
                    setattr(item, "scxml_Param152", self)
                    

    @property
    def scxml_Send(self):
        return self.__scxml_Send

    @scxml_Send.setter
    def scxml_Send(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send", None)
        self.__scxml_Send = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry62"):
                opp_val = getattr(old_value, "scxml_OnEntry62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry62"):
                opp_val = getattr(value, "scxml_OnEntry62", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Send88(self):
        return self.__scxml_Send88

    @scxml_Send88.setter
    def scxml_Send88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send88", None)
        self.__scxml_Send88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit87"):
                opp_val = getattr(old_value, "scxml_OnExit87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit87"):
                opp_val = getattr(value, "scxml_OnExit87", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Send193(self):
        return self.__scxml_Send193

    @scxml_Send193.setter
    def scxml_Send193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send193", None)
        self.__scxml_Send193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize192"):
                opp_val = getattr(old_value, "scxml_Finalize192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize192"):
                opp_val = getattr(value, "scxml_Finalize192", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Send154(self):
        return self.__scxml_Send154

    @scxml_Send154.setter
    def scxml_Send154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send154", None)
        self.__scxml_Send154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Content155"):
                opp_val = getattr(old_value, "scxml_Content155", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Content155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Content155"):
                opp_val = getattr(value, "scxml_Content155", None)
                setattr(value, "scxml_Content155", self)

class scxml_Raise:

    def __init__(self, event: str, scxml_Raise: "scxml_OnEntry" = None, scxml_Raise85: "scxml_OnExit" = None, scxml_Raise139: "scxml_If" = None, scxml_Raise190: "scxml_Finalize" = None):
        self.event = event
        self.scxml_Raise = scxml_Raise
        self.scxml_Raise85 = scxml_Raise85
        self.scxml_Raise139 = scxml_Raise139
        self.scxml_Raise190 = scxml_Raise190
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def scxml_Raise139(self):
        return self.__scxml_Raise139

    @scxml_Raise139.setter
    def scxml_Raise139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Raise__scxml_Raise139", None)
        self.__scxml_Raise139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If138"):
                opp_val = getattr(old_value, "scxml_If138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If138"):
                opp_val = getattr(value, "scxml_If138", None)
                if opp_val is None:
                    setattr(value, "scxml_If138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Raise(self):
        return self.__scxml_Raise

    @scxml_Raise.setter
    def scxml_Raise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Raise__scxml_Raise", None)
        self.__scxml_Raise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry60"):
                opp_val = getattr(old_value, "scxml_OnEntry60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry60"):
                opp_val = getattr(value, "scxml_OnEntry60", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Raise190(self):
        return self.__scxml_Raise190

    @scxml_Raise190.setter
    def scxml_Raise190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Raise__scxml_Raise190", None)
        self.__scxml_Raise190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize189"):
                opp_val = getattr(old_value, "scxml_Finalize189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize189"):
                opp_val = getattr(value, "scxml_Finalize189", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Raise85(self):
        return self.__scxml_Raise85

    @scxml_Raise85.setter
    def scxml_Raise85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Raise__scxml_Raise85", None)
        self.__scxml_Raise85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit84"):
                opp_val = getattr(old_value, "scxml_OnExit84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit84"):
                opp_val = getattr(value, "scxml_OnExit84", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Param:

    def __init__(self, name: str, expr: str, scxml_Param: "scxml_OnEntry" = None, scxml_Param82: "scxml_OnExit" = None, scxml_Param136: "scxml_If" = None, scxml_Param152: "scxml_Send" = None, scxml_Param164: "scxml_Donedata" = None, scxml_Param170: "scxml_Invoke" = None, scxml_Param187: "scxml_Finalize" = None):
        self.name = name
        self.expr = expr
        self.scxml_Param = scxml_Param
        self.scxml_Param82 = scxml_Param82
        self.scxml_Param136 = scxml_Param136
        self.scxml_Param152 = scxml_Param152
        self.scxml_Param164 = scxml_Param164
        self.scxml_Param170 = scxml_Param170
        self.scxml_Param187 = scxml_Param187
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def scxml_Param164(self):
        return self.__scxml_Param164

    @scxml_Param164.setter
    def scxml_Param164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param164", None)
        self.__scxml_Param164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Donedata163"):
                opp_val = getattr(old_value, "scxml_Donedata163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Donedata163"):
                opp_val = getattr(value, "scxml_Donedata163", None)
                if opp_val is None:
                    setattr(value, "scxml_Donedata163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param(self):
        return self.__scxml_Param

    @scxml_Param.setter
    def scxml_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param", None)
        self.__scxml_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry58"):
                opp_val = getattr(old_value, "scxml_OnEntry58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry58"):
                opp_val = getattr(value, "scxml_OnEntry58", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param187(self):
        return self.__scxml_Param187

    @scxml_Param187.setter
    def scxml_Param187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param187", None)
        self.__scxml_Param187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize186"):
                opp_val = getattr(old_value, "scxml_Finalize186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize186"):
                opp_val = getattr(value, "scxml_Finalize186", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param136(self):
        return self.__scxml_Param136

    @scxml_Param136.setter
    def scxml_Param136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param136", None)
        self.__scxml_Param136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If135"):
                opp_val = getattr(old_value, "scxml_If135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If135"):
                opp_val = getattr(value, "scxml_If135", None)
                if opp_val is None:
                    setattr(value, "scxml_If135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param82(self):
        return self.__scxml_Param82

    @scxml_Param82.setter
    def scxml_Param82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param82", None)
        self.__scxml_Param82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit81"):
                opp_val = getattr(old_value, "scxml_OnExit81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit81"):
                opp_val = getattr(value, "scxml_OnExit81", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param152(self):
        return self.__scxml_Param152

    @scxml_Param152.setter
    def scxml_Param152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param152", None)
        self.__scxml_Param152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Send151"):
                opp_val = getattr(old_value, "scxml_Send151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Send151"):
                opp_val = getattr(value, "scxml_Send151", None)
                if opp_val is None:
                    setattr(value, "scxml_Send151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Param170(self):
        return self.__scxml_Param170

    @scxml_Param170.setter
    def scxml_Param170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param170", None)
        self.__scxml_Param170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Invoke169"):
                opp_val = getattr(old_value, "scxml_Invoke169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Invoke169"):
                opp_val = getattr(value, "scxml_Invoke169", None)
                if opp_val is None:
                    setattr(value, "scxml_Invoke169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Log:

    def __init__(self, label: str, expr: str, level: str, scxml_Log: "scxml_OnEntry" = None, scxml_Log79: "scxml_OnExit" = None, scxml_Log133: "scxml_If" = None, scxml_Log184: "scxml_Finalize" = None):
        self.label = label
        self.expr = expr
        self.level = level
        self.scxml_Log = scxml_Log
        self.scxml_Log79 = scxml_Log79
        self.scxml_Log133 = scxml_Log133
        self.scxml_Log184 = scxml_Log184
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def scxml_Log133(self):
        return self.__scxml_Log133

    @scxml_Log133.setter
    def scxml_Log133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Log__scxml_Log133", None)
        self.__scxml_Log133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If132"):
                opp_val = getattr(old_value, "scxml_If132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If132"):
                opp_val = getattr(value, "scxml_If132", None)
                if opp_val is None:
                    setattr(value, "scxml_If132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Log79(self):
        return self.__scxml_Log79

    @scxml_Log79.setter
    def scxml_Log79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Log__scxml_Log79", None)
        self.__scxml_Log79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit78"):
                opp_val = getattr(old_value, "scxml_OnExit78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit78"):
                opp_val = getattr(value, "scxml_OnExit78", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Log184(self):
        return self.__scxml_Log184

    @scxml_Log184.setter
    def scxml_Log184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Log__scxml_Log184", None)
        self.__scxml_Log184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize183"):
                opp_val = getattr(old_value, "scxml_Finalize183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize183"):
                opp_val = getattr(value, "scxml_Finalize183", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Log(self):
        return self.__scxml_Log

    @scxml_Log.setter
    def scxml_Log(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Log__scxml_Log", None)
        self.__scxml_Log = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry56"):
                opp_val = getattr(old_value, "scxml_OnEntry56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry56"):
                opp_val = getattr(value, "scxml_OnEntry56", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_If:

    def __init__(self, cond: str, scxml_If: "scxml_OnEntry" = None, scxml_If76: "scxml_OnExit" = None, scxml_If119: set["scxml_ElseIf"] = None, scxml_If121: "scxml_Else" = None, scxml_If123: set["scxml_Assign"] = None, scxml_If126: set["scxml_Cancel"] = None, scxml_If130: "scxml_If" = None, scxml_If128: set["scxml_If"] = None, scxml_If132: set["scxml_Log"] = None, scxml_If135: set["scxml_Param"] = None, scxml_If138: set["scxml_Raise"] = None, scxml_If141: set["scxml_Send"] = None, scxml_If144: set["scxml_Validate"] = None, scxml_If181: "scxml_Finalize" = None):
        self.cond = cond
        self.scxml_If = scxml_If
        self.scxml_If76 = scxml_If76
        self.scxml_If119 = scxml_If119 if scxml_If119 is not None else set()
        self.scxml_If121 = scxml_If121
        self.scxml_If123 = scxml_If123 if scxml_If123 is not None else set()
        self.scxml_If126 = scxml_If126 if scxml_If126 is not None else set()
        self.scxml_If130 = scxml_If130
        self.scxml_If128 = scxml_If128 if scxml_If128 is not None else set()
        self.scxml_If132 = scxml_If132 if scxml_If132 is not None else set()
        self.scxml_If135 = scxml_If135 if scxml_If135 is not None else set()
        self.scxml_If138 = scxml_If138 if scxml_If138 is not None else set()
        self.scxml_If141 = scxml_If141 if scxml_If141 is not None else set()
        self.scxml_If144 = scxml_If144 if scxml_If144 is not None else set()
        self.scxml_If181 = scxml_If181
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def scxml_If130(self):
        return self.__scxml_If130

    @scxml_If130.setter
    def scxml_If130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If130", None)
        self.__scxml_If130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If128"):
                opp_val = getattr(old_value, "scxml_If128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If128"):
                opp_val = getattr(value, "scxml_If128", None)
                if opp_val is None:
                    setattr(value, "scxml_If128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_If126(self):
        return self.__scxml_If126

    @scxml_If126.setter
    def scxml_If126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If126", None)
        self.__scxml_If126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Cancel127"):
                    opp_val = getattr(item, "scxml_Cancel127", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Cancel127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Cancel127"):
                    opp_val = getattr(item, "scxml_Cancel127", None)
                    
                    setattr(item, "scxml_Cancel127", self)
                    

    @property
    def scxml_If121(self):
        return self.__scxml_If121

    @scxml_If121.setter
    def scxml_If121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If121", None)
        self.__scxml_If121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Else"):
                opp_val = getattr(old_value, "scxml_Else", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Else", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Else"):
                opp_val = getattr(value, "scxml_Else", None)
                setattr(value, "scxml_Else", self)

    @property
    def scxml_If141(self):
        return self.__scxml_If141

    @scxml_If141.setter
    def scxml_If141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If141", None)
        self.__scxml_If141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Send142"):
                    opp_val = getattr(item, "scxml_Send142", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Send142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Send142"):
                    opp_val = getattr(item, "scxml_Send142", None)
                    
                    setattr(item, "scxml_Send142", self)
                    

    @property
    def scxml_If144(self):
        return self.__scxml_If144

    @scxml_If144.setter
    def scxml_If144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If144", None)
        self.__scxml_If144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Validate145"):
                    opp_val = getattr(item, "scxml_Validate145", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Validate145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Validate145"):
                    opp_val = getattr(item, "scxml_Validate145", None)
                    
                    setattr(item, "scxml_Validate145", self)
                    

    @property
    def scxml_If128(self):
        return self.__scxml_If128

    @scxml_If128.setter
    def scxml_If128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If128", None)
        self.__scxml_If128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_If130"):
                    opp_val = getattr(item, "scxml_If130", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_If130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_If130"):
                    opp_val = getattr(item, "scxml_If130", None)
                    
                    setattr(item, "scxml_If130", self)
                    

    @property
    def scxml_If76(self):
        return self.__scxml_If76

    @scxml_If76.setter
    def scxml_If76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If76", None)
        self.__scxml_If76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit75"):
                opp_val = getattr(old_value, "scxml_OnExit75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit75"):
                opp_val = getattr(value, "scxml_OnExit75", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_If123(self):
        return self.__scxml_If123

    @scxml_If123.setter
    def scxml_If123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If123", None)
        self.__scxml_If123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Assign124"):
                    opp_val = getattr(item, "scxml_Assign124", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Assign124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Assign124"):
                    opp_val = getattr(item, "scxml_Assign124", None)
                    
                    setattr(item, "scxml_Assign124", self)
                    

    @property
    def scxml_If181(self):
        return self.__scxml_If181

    @scxml_If181.setter
    def scxml_If181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If181", None)
        self.__scxml_If181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize180"):
                opp_val = getattr(old_value, "scxml_Finalize180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize180"):
                opp_val = getattr(value, "scxml_Finalize180", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_If132(self):
        return self.__scxml_If132

    @scxml_If132.setter
    def scxml_If132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If132", None)
        self.__scxml_If132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Log133"):
                    opp_val = getattr(item, "scxml_Log133", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Log133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Log133"):
                    opp_val = getattr(item, "scxml_Log133", None)
                    
                    setattr(item, "scxml_Log133", self)
                    

    @property
    def scxml_If(self):
        return self.__scxml_If

    @scxml_If.setter
    def scxml_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If", None)
        self.__scxml_If = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry54"):
                opp_val = getattr(old_value, "scxml_OnEntry54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry54"):
                opp_val = getattr(value, "scxml_OnEntry54", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_If135(self):
        return self.__scxml_If135

    @scxml_If135.setter
    def scxml_If135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If135", None)
        self.__scxml_If135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Param136"):
                    opp_val = getattr(item, "scxml_Param136", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Param136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Param136"):
                    opp_val = getattr(item, "scxml_Param136", None)
                    
                    setattr(item, "scxml_Param136", self)
                    

    @property
    def scxml_If119(self):
        return self.__scxml_If119

    @scxml_If119.setter
    def scxml_If119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If119", None)
        self.__scxml_If119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ElseIf"):
                    opp_val = getattr(item, "scxml_ElseIf", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ElseIf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ElseIf"):
                    opp_val = getattr(item, "scxml_ElseIf", None)
                    
                    setattr(item, "scxml_ElseIf", self)
                    

    @property
    def scxml_If138(self):
        return self.__scxml_If138

    @scxml_If138.setter
    def scxml_If138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_If__scxml_If138", None)
        self.__scxml_If138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Raise139"):
                    opp_val = getattr(item, "scxml_Raise139", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Raise139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Raise139"):
                    opp_val = getattr(item, "scxml_Raise139", None)
                    
                    setattr(item, "scxml_Raise139", self)
                    

class scxml_Cancel:

    def __init__(self, sendid: str, sendidexpr: str, scxml_Cancel: "scxml_OnEntry" = None, scxml_Cancel73: "scxml_OnExit" = None, scxml_Cancel127: "scxml_If" = None, scxml_Cancel178: "scxml_Finalize" = None):
        self.sendid = sendid
        self.sendidexpr = sendidexpr
        self.scxml_Cancel = scxml_Cancel
        self.scxml_Cancel73 = scxml_Cancel73
        self.scxml_Cancel127 = scxml_Cancel127
        self.scxml_Cancel178 = scxml_Cancel178
        
    @property
    def sendid(self) -> str:
        return self.__sendid

    @sendid.setter
    def sendid(self, sendid: str):
        self.__sendid = sendid

    @property
    def sendidexpr(self) -> str:
        return self.__sendidexpr

    @sendidexpr.setter
    def sendidexpr(self, sendidexpr: str):
        self.__sendidexpr = sendidexpr

    @property
    def scxml_Cancel127(self):
        return self.__scxml_Cancel127

    @scxml_Cancel127.setter
    def scxml_Cancel127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Cancel__scxml_Cancel127", None)
        self.__scxml_Cancel127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If126"):
                opp_val = getattr(old_value, "scxml_If126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If126"):
                opp_val = getattr(value, "scxml_If126", None)
                if opp_val is None:
                    setattr(value, "scxml_If126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Cancel178(self):
        return self.__scxml_Cancel178

    @scxml_Cancel178.setter
    def scxml_Cancel178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Cancel__scxml_Cancel178", None)
        self.__scxml_Cancel178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize177"):
                opp_val = getattr(old_value, "scxml_Finalize177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize177"):
                opp_val = getattr(value, "scxml_Finalize177", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Cancel(self):
        return self.__scxml_Cancel

    @scxml_Cancel.setter
    def scxml_Cancel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Cancel__scxml_Cancel", None)
        self.__scxml_Cancel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry52"):
                opp_val = getattr(old_value, "scxml_OnEntry52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry52"):
                opp_val = getattr(value, "scxml_OnEntry52", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Cancel73(self):
        return self.__scxml_Cancel73

    @scxml_Cancel73.setter
    def scxml_Cancel73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Cancel__scxml_Cancel73", None)
        self.__scxml_Cancel73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit72"):
                opp_val = getattr(old_value, "scxml_OnExit72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit72"):
                opp_val = getattr(value, "scxml_OnExit72", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Script:

    pass
class scxml_ServiceTemplate:

    def __init__(self, name: str, xmlns: str, version: str, profile: str, exmode: str, scxml_ServiceTemplate: set["scxml_Transition"] = None, scxml_ServiceTemplate30: set["scxml_State"] = None, scxml_ServiceTemplate36: set["scxml_FinalState"] = None, scxml_ServiceTemplate39: set["scxml_Parallel"] = None, scxml_ServiceTemplate42: set["scxml_DataModel"] = None, scxml_ServiceTemplate45: "scxml_Script" = None, scxml_ServiceTemplate33: "scxml_InitialState" = None):
        self.name = name
        self.xmlns = xmlns
        self.version = version
        self.profile = profile
        self.exmode = exmode
        self.scxml_ServiceTemplate = scxml_ServiceTemplate if scxml_ServiceTemplate is not None else set()
        self.scxml_ServiceTemplate30 = scxml_ServiceTemplate30 if scxml_ServiceTemplate30 is not None else set()
        self.scxml_ServiceTemplate36 = scxml_ServiceTemplate36 if scxml_ServiceTemplate36 is not None else set()
        self.scxml_ServiceTemplate39 = scxml_ServiceTemplate39 if scxml_ServiceTemplate39 is not None else set()
        self.scxml_ServiceTemplate42 = scxml_ServiceTemplate42 if scxml_ServiceTemplate42 is not None else set()
        self.scxml_ServiceTemplate45 = scxml_ServiceTemplate45
        self.scxml_ServiceTemplate33 = scxml_ServiceTemplate33
        
    @property
    def exmode(self) -> str:
        return self.__exmode

    @exmode.setter
    def exmode(self, exmode: str):
        self.__exmode = exmode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xmlns(self) -> str:
        return self.__xmlns

    @xmlns.setter
    def xmlns(self, xmlns: str):
        self.__xmlns = xmlns

    @property
    def profile(self) -> str:
        return self.__profile

    @profile.setter
    def profile(self, profile: str):
        self.__profile = profile

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def scxml_ServiceTemplate39(self):
        return self.__scxml_ServiceTemplate39

    @scxml_ServiceTemplate39.setter
    def scxml_ServiceTemplate39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate39", None)
        self.__scxml_ServiceTemplate39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Parallel40"):
                    opp_val = getattr(item, "scxml_Parallel40", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Parallel40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Parallel40"):
                    opp_val = getattr(item, "scxml_Parallel40", None)
                    
                    setattr(item, "scxml_Parallel40", self)
                    

    @property
    def scxml_ServiceTemplate30(self):
        return self.__scxml_ServiceTemplate30

    @scxml_ServiceTemplate30.setter
    def scxml_ServiceTemplate30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate30", None)
        self.__scxml_ServiceTemplate30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_State31"):
                    opp_val = getattr(item, "scxml_State31", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_State31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_State31"):
                    opp_val = getattr(item, "scxml_State31", None)
                    
                    setattr(item, "scxml_State31", self)
                    

    @property
    def scxml_ServiceTemplate36(self):
        return self.__scxml_ServiceTemplate36

    @scxml_ServiceTemplate36.setter
    def scxml_ServiceTemplate36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate36", None)
        self.__scxml_ServiceTemplate36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_FinalState37"):
                    opp_val = getattr(item, "scxml_FinalState37", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_FinalState37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_FinalState37"):
                    opp_val = getattr(item, "scxml_FinalState37", None)
                    
                    setattr(item, "scxml_FinalState37", self)
                    

    @property
    def scxml_ServiceTemplate(self):
        return self.__scxml_ServiceTemplate

    @scxml_ServiceTemplate.setter
    def scxml_ServiceTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate", None)
        self.__scxml_ServiceTemplate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Transition28"):
                    opp_val = getattr(item, "scxml_Transition28", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Transition28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Transition28"):
                    opp_val = getattr(item, "scxml_Transition28", None)
                    
                    setattr(item, "scxml_Transition28", self)
                    

    @property
    def scxml_ServiceTemplate45(self):
        return self.__scxml_ServiceTemplate45

    @scxml_ServiceTemplate45.setter
    def scxml_ServiceTemplate45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate45", None)
        self.__scxml_ServiceTemplate45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Script"):
                opp_val = getattr(old_value, "scxml_Script", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Script", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Script"):
                opp_val = getattr(value, "scxml_Script", None)
                setattr(value, "scxml_Script", self)

    @property
    def scxml_ServiceTemplate33(self):
        return self.__scxml_ServiceTemplate33

    @scxml_ServiceTemplate33.setter
    def scxml_ServiceTemplate33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate33", None)
        self.__scxml_ServiceTemplate33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_InitialState34"):
                opp_val = getattr(old_value, "scxml_InitialState34", None)
                if opp_val == self:
                    setattr(old_value, "scxml_InitialState34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_InitialState34"):
                opp_val = getattr(value, "scxml_InitialState34", None)
                setattr(value, "scxml_InitialState34", self)

    @property
    def scxml_ServiceTemplate42(self):
        return self.__scxml_ServiceTemplate42

    @scxml_ServiceTemplate42.setter
    def scxml_ServiceTemplate42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ServiceTemplate__scxml_ServiceTemplate42", None)
        self.__scxml_ServiceTemplate42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_DataModel43"):
                    opp_val = getattr(item, "scxml_DataModel43", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_DataModel43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_DataModel43"):
                    opp_val = getattr(item, "scxml_DataModel43", None)
                    
                    setattr(item, "scxml_DataModel43", self)
                    

class scxml_Assign:

    def __init__(self, location: str, dataid: str, expr: str, scxml_Assign: "scxml_OnEntry" = None, scxml_Assign70: "scxml_OnExit" = None, scxml_Assign124: "scxml_If" = None, scxml_Assign175: "scxml_Finalize" = None):
        self.location = location
        self.dataid = dataid
        self.expr = expr
        self.scxml_Assign = scxml_Assign
        self.scxml_Assign70 = scxml_Assign70
        self.scxml_Assign124 = scxml_Assign124
        self.scxml_Assign175 = scxml_Assign175
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def dataid(self) -> str:
        return self.__dataid

    @dataid.setter
    def dataid(self, dataid: str):
        self.__dataid = dataid

    @property
    def scxml_Assign(self):
        return self.__scxml_Assign

    @scxml_Assign.setter
    def scxml_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Assign__scxml_Assign", None)
        self.__scxml_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnEntry50"):
                opp_val = getattr(old_value, "scxml_OnEntry50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnEntry50"):
                opp_val = getattr(value, "scxml_OnEntry50", None)
                if opp_val is None:
                    setattr(value, "scxml_OnEntry50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Assign70(self):
        return self.__scxml_Assign70

    @scxml_Assign70.setter
    def scxml_Assign70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Assign__scxml_Assign70", None)
        self.__scxml_Assign70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_OnExit69"):
                opp_val = getattr(old_value, "scxml_OnExit69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_OnExit69"):
                opp_val = getattr(value, "scxml_OnExit69", None)
                if opp_val is None:
                    setattr(value, "scxml_OnExit69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Assign175(self):
        return self.__scxml_Assign175

    @scxml_Assign175.setter
    def scxml_Assign175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Assign__scxml_Assign175", None)
        self.__scxml_Assign175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize174"):
                opp_val = getattr(old_value, "scxml_Finalize174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize174"):
                opp_val = getattr(value, "scxml_Finalize174", None)
                if opp_val is None:
                    setattr(value, "scxml_Finalize174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Assign124(self):
        return self.__scxml_Assign124

    @scxml_Assign124.setter
    def scxml_Assign124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Assign__scxml_Assign124", None)
        self.__scxml_Assign124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_If123"):
                opp_val = getattr(old_value, "scxml_If123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_If123"):
                opp_val = getattr(value, "scxml_If123", None)
                if opp_val is None:
                    setattr(value, "scxml_If123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Invoke:

    def __init__(self, type: str, typeexpr: str, src: str, srcexpr: str, id: str, idlocation: str, namelist: str, autoforward: str, scxml_Invoke: "scxml_State" = None, scxml_Invoke166: "scxml_Content" = None, scxml_Invoke169: set["scxml_Param"] = None, scxml_Invoke172: "scxml_Finalize" = None):
        self.type = type
        self.typeexpr = typeexpr
        self.src = src
        self.srcexpr = srcexpr
        self.id = id
        self.idlocation = idlocation
        self.namelist = namelist
        self.autoforward = autoforward
        self.scxml_Invoke = scxml_Invoke
        self.scxml_Invoke166 = scxml_Invoke166
        self.scxml_Invoke169 = scxml_Invoke169 if scxml_Invoke169 is not None else set()
        self.scxml_Invoke172 = scxml_Invoke172
        
    @property
    def idlocation(self) -> str:
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation

    @property
    def srcexpr(self) -> str:
        return self.__srcexpr

    @srcexpr.setter
    def srcexpr(self, srcexpr: str):
        self.__srcexpr = srcexpr

    @property
    def typeexpr(self) -> str:
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def namelist(self) -> str:
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist

    @property
    def autoforward(self) -> str:
        return self.__autoforward

    @autoforward.setter
    def autoforward(self, autoforward: str):
        self.__autoforward = autoforward

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def scxml_Invoke166(self):
        return self.__scxml_Invoke166

    @scxml_Invoke166.setter
    def scxml_Invoke166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke166", None)
        self.__scxml_Invoke166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Content167"):
                opp_val = getattr(old_value, "scxml_Content167", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Content167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Content167"):
                opp_val = getattr(value, "scxml_Content167", None)
                setattr(value, "scxml_Content167", self)

    @property
    def scxml_Invoke169(self):
        return self.__scxml_Invoke169

    @scxml_Invoke169.setter
    def scxml_Invoke169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke169", None)
        self.__scxml_Invoke169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Param170"):
                    opp_val = getattr(item, "scxml_Param170", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Param170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Param170"):
                    opp_val = getattr(item, "scxml_Param170", None)
                    
                    setattr(item, "scxml_Param170", self)
                    

    @property
    def scxml_Invoke(self):
        return self.__scxml_Invoke

    @scxml_Invoke.setter
    def scxml_Invoke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke", None)
        self.__scxml_Invoke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State20"):
                opp_val = getattr(old_value, "scxml_State20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State20"):
                opp_val = getattr(value, "scxml_State20", None)
                if opp_val is None:
                    setattr(value, "scxml_State20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Invoke172(self):
        return self.__scxml_Invoke172

    @scxml_Invoke172.setter
    def scxml_Invoke172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke172", None)
        self.__scxml_Invoke172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Finalize"):
                opp_val = getattr(old_value, "scxml_Finalize", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Finalize", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Finalize"):
                opp_val = getattr(value, "scxml_Finalize", None)
                setattr(value, "scxml_Finalize", self)

class scxml_Anchor:

    def __init__(self, type: str, snapshot: str, scxml_Anchor: "scxml_State" = None, scxml_Anchor117: "scxml_Parallel" = None):
        self.type = type
        self.snapshot = snapshot
        self.scxml_Anchor = scxml_Anchor
        self.scxml_Anchor117 = scxml_Anchor117
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def snapshot(self) -> str:
        return self.__snapshot

    @snapshot.setter
    def snapshot(self, snapshot: str):
        self.__snapshot = snapshot

    @property
    def scxml_Anchor117(self):
        return self.__scxml_Anchor117

    @scxml_Anchor117.setter
    def scxml_Anchor117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Anchor__scxml_Anchor117", None)
        self.__scxml_Anchor117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Parallel116"):
                opp_val = getattr(old_value, "scxml_Parallel116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Parallel116"):
                opp_val = getattr(value, "scxml_Parallel116", None)
                if opp_val is None:
                    setattr(value, "scxml_Parallel116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Anchor(self):
        return self.__scxml_Anchor

    @scxml_Anchor.setter
    def scxml_Anchor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Anchor__scxml_Anchor", None)
        self.__scxml_Anchor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State18"):
                opp_val = getattr(old_value, "scxml_State18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State18"):
                opp_val = getattr(value, "scxml_State18", None)
                if opp_val is None:
                    setattr(value, "scxml_State18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_OnExit:

    pass
class scxml_OnEntry:

    pass
class NamedElement:

    pass
class scxml_Parallel(NamedElement):

    def __init__(self, id: str, scxml_Parallel: "scxml_State" = None, scxml_Parallel40: "scxml_ServiceTemplate" = None, scxml_Parallel101: set["scxml_OnEntry"] = None, scxml_Parallel104: set["scxml_OnExit"] = None, scxml_Parallel108: "scxml_Parallel" = None, scxml_Parallel106: set["scxml_Parallel"] = None, scxml_Parallel110: set["scxml_State"] = None, scxml_Parallel113: set["scxml_HistoryState"] = None, scxml_Parallel116: set["scxml_Anchor"] = None):
        self.id = id
        self.scxml_Parallel = scxml_Parallel
        self.scxml_Parallel40 = scxml_Parallel40
        self.scxml_Parallel101 = scxml_Parallel101 if scxml_Parallel101 is not None else set()
        self.scxml_Parallel104 = scxml_Parallel104 if scxml_Parallel104 is not None else set()
        self.scxml_Parallel108 = scxml_Parallel108
        self.scxml_Parallel106 = scxml_Parallel106 if scxml_Parallel106 is not None else set()
        self.scxml_Parallel110 = scxml_Parallel110 if scxml_Parallel110 is not None else set()
        self.scxml_Parallel113 = scxml_Parallel113 if scxml_Parallel113 is not None else set()
        self.scxml_Parallel116 = scxml_Parallel116 if scxml_Parallel116 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxml_Parallel116(self):
        return self.__scxml_Parallel116

    @scxml_Parallel116.setter
    def scxml_Parallel116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel116", None)
        self.__scxml_Parallel116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Anchor117"):
                    opp_val = getattr(item, "scxml_Anchor117", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Anchor117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Anchor117"):
                    opp_val = getattr(item, "scxml_Anchor117", None)
                    
                    setattr(item, "scxml_Anchor117", self)
                    

    @property
    def scxml_Parallel101(self):
        return self.__scxml_Parallel101

    @scxml_Parallel101.setter
    def scxml_Parallel101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel101", None)
        self.__scxml_Parallel101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnEntry102"):
                    opp_val = getattr(item, "scxml_OnEntry102", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnEntry102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnEntry102"):
                    opp_val = getattr(item, "scxml_OnEntry102", None)
                    
                    setattr(item, "scxml_OnEntry102", self)
                    

    @property
    def scxml_Parallel(self):
        return self.__scxml_Parallel

    @scxml_Parallel.setter
    def scxml_Parallel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel", None)
        self.__scxml_Parallel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State14"):
                opp_val = getattr(old_value, "scxml_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State14"):
                opp_val = getattr(value, "scxml_State14", None)
                if opp_val is None:
                    setattr(value, "scxml_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Parallel106(self):
        return self.__scxml_Parallel106

    @scxml_Parallel106.setter
    def scxml_Parallel106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel106", None)
        self.__scxml_Parallel106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Parallel108"):
                    opp_val = getattr(item, "scxml_Parallel108", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Parallel108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Parallel108"):
                    opp_val = getattr(item, "scxml_Parallel108", None)
                    
                    setattr(item, "scxml_Parallel108", self)
                    

    @property
    def scxml_Parallel113(self):
        return self.__scxml_Parallel113

    @scxml_Parallel113.setter
    def scxml_Parallel113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel113", None)
        self.__scxml_Parallel113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_HistoryState114"):
                    opp_val = getattr(item, "scxml_HistoryState114", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_HistoryState114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_HistoryState114"):
                    opp_val = getattr(item, "scxml_HistoryState114", None)
                    
                    setattr(item, "scxml_HistoryState114", self)
                    

    @property
    def scxml_Parallel108(self):
        return self.__scxml_Parallel108

    @scxml_Parallel108.setter
    def scxml_Parallel108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel108", None)
        self.__scxml_Parallel108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Parallel106"):
                opp_val = getattr(old_value, "scxml_Parallel106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Parallel106"):
                opp_val = getattr(value, "scxml_Parallel106", None)
                if opp_val is None:
                    setattr(value, "scxml_Parallel106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Parallel40(self):
        return self.__scxml_Parallel40

    @scxml_Parallel40.setter
    def scxml_Parallel40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel40", None)
        self.__scxml_Parallel40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ServiceTemplate39"):
                opp_val = getattr(old_value, "scxml_ServiceTemplate39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ServiceTemplate39"):
                opp_val = getattr(value, "scxml_ServiceTemplate39", None)
                if opp_val is None:
                    setattr(value, "scxml_ServiceTemplate39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Parallel110(self):
        return self.__scxml_Parallel110

    @scxml_Parallel110.setter
    def scxml_Parallel110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel110", None)
        self.__scxml_Parallel110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_State111"):
                    opp_val = getattr(item, "scxml_State111", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_State111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_State111"):
                    opp_val = getattr(item, "scxml_State111", None)
                    
                    setattr(item, "scxml_State111", self)
                    

    @property
    def scxml_Parallel104(self):
        return self.__scxml_Parallel104

    @scxml_Parallel104.setter
    def scxml_Parallel104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Parallel__scxml_Parallel104", None)
        self.__scxml_Parallel104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnExit105"):
                    opp_val = getattr(item, "scxml_OnExit105", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnExit105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnExit105"):
                    opp_val = getattr(item, "scxml_OnExit105", None)
                    
                    setattr(item, "scxml_OnExit105", self)
                    

class scxml_FinalState(NamedElement):

    def __init__(self, id: str, scxml_FinalState: "scxml_State" = None, scxml_FinalState37: "scxml_ServiceTemplate" = None, scxml_FinalState93: set["scxml_OnEntry"] = None, scxml_FinalState96: set["scxml_OnExit"] = None, scxml_FinalState99: "scxml_Donedata" = None):
        self.id = id
        self.scxml_FinalState = scxml_FinalState
        self.scxml_FinalState37 = scxml_FinalState37
        self.scxml_FinalState93 = scxml_FinalState93 if scxml_FinalState93 is not None else set()
        self.scxml_FinalState96 = scxml_FinalState96 if scxml_FinalState96 is not None else set()
        self.scxml_FinalState99 = scxml_FinalState99
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxml_FinalState96(self):
        return self.__scxml_FinalState96

    @scxml_FinalState96.setter
    def scxml_FinalState96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_FinalState__scxml_FinalState96", None)
        self.__scxml_FinalState96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnExit97"):
                    opp_val = getattr(item, "scxml_OnExit97", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnExit97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnExit97"):
                    opp_val = getattr(item, "scxml_OnExit97", None)
                    
                    setattr(item, "scxml_OnExit97", self)
                    

    @property
    def scxml_FinalState93(self):
        return self.__scxml_FinalState93

    @scxml_FinalState93.setter
    def scxml_FinalState93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_FinalState__scxml_FinalState93", None)
        self.__scxml_FinalState93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnEntry94"):
                    opp_val = getattr(item, "scxml_OnEntry94", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnEntry94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnEntry94"):
                    opp_val = getattr(item, "scxml_OnEntry94", None)
                    
                    setattr(item, "scxml_OnEntry94", self)
                    

    @property
    def scxml_FinalState37(self):
        return self.__scxml_FinalState37

    @scxml_FinalState37.setter
    def scxml_FinalState37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_FinalState__scxml_FinalState37", None)
        self.__scxml_FinalState37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ServiceTemplate36"):
                opp_val = getattr(old_value, "scxml_ServiceTemplate36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ServiceTemplate36"):
                opp_val = getattr(value, "scxml_ServiceTemplate36", None)
                if opp_val is None:
                    setattr(value, "scxml_ServiceTemplate36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_FinalState(self):
        return self.__scxml_FinalState

    @scxml_FinalState.setter
    def scxml_FinalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_FinalState__scxml_FinalState", None)
        self.__scxml_FinalState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State12"):
                opp_val = getattr(old_value, "scxml_State12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State12"):
                opp_val = getattr(value, "scxml_State12", None)
                if opp_val is None:
                    setattr(value, "scxml_State12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_FinalState99(self):
        return self.__scxml_FinalState99

    @scxml_FinalState99.setter
    def scxml_FinalState99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_FinalState__scxml_FinalState99", None)
        self.__scxml_FinalState99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Donedata"):
                opp_val = getattr(old_value, "scxml_Donedata", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Donedata", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Donedata"):
                opp_val = getattr(value, "scxml_Donedata", None)
                setattr(value, "scxml_Donedata", self)

class scxml_HistoryState(NamedElement):

    def __init__(self, id: str, type: str, scxml_HistoryState: "scxml_State" = None, scxml_HistoryState114: "scxml_Parallel" = None):
        self.id = id
        self.type = type
        self.scxml_HistoryState = scxml_HistoryState
        self.scxml_HistoryState114 = scxml_HistoryState114
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def scxml_HistoryState114(self):
        return self.__scxml_HistoryState114

    @scxml_HistoryState114.setter
    def scxml_HistoryState114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_HistoryState__scxml_HistoryState114", None)
        self.__scxml_HistoryState114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Parallel113"):
                opp_val = getattr(old_value, "scxml_Parallel113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Parallel113"):
                opp_val = getattr(value, "scxml_Parallel113", None)
                if opp_val is None:
                    setattr(value, "scxml_Parallel113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_HistoryState(self):
        return self.__scxml_HistoryState

    @scxml_HistoryState.setter
    def scxml_HistoryState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_HistoryState__scxml_HistoryState", None)
        self.__scxml_HistoryState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State16"):
                opp_val = getattr(old_value, "scxml_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State16"):
                opp_val = getattr(value, "scxml_State16", None)
                if opp_val is None:
                    setattr(value, "scxml_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_InitialState(NamedElement):

    pass
class scxml_State(NamedElement):

    def __init__(self, id: str, scxml_State: set["scxml_OnEntry"] = None, scxml_State5: set["scxml_OnExit"] = None, scxml_State7: "scxml_InitialState" = None, scxml_State10: "scxml_State" = None, scxml_State8: set["scxml_State"] = None, scxml_State12: set["scxml_FinalState"] = None, scxml_State14: set["scxml_Parallel"] = None, scxml_State16: set["scxml_HistoryState"] = None, scxml_State18: set["scxml_Anchor"] = None, scxml_State20: set["scxml_Invoke"] = None, scxml_State31: "scxml_ServiceTemplate" = None, scxml_State111: "scxml_Parallel" = None):
        self.id = id
        self.scxml_State = scxml_State if scxml_State is not None else set()
        self.scxml_State5 = scxml_State5 if scxml_State5 is not None else set()
        self.scxml_State7 = scxml_State7
        self.scxml_State10 = scxml_State10
        self.scxml_State8 = scxml_State8 if scxml_State8 is not None else set()
        self.scxml_State12 = scxml_State12 if scxml_State12 is not None else set()
        self.scxml_State14 = scxml_State14 if scxml_State14 is not None else set()
        self.scxml_State16 = scxml_State16 if scxml_State16 is not None else set()
        self.scxml_State18 = scxml_State18 if scxml_State18 is not None else set()
        self.scxml_State20 = scxml_State20 if scxml_State20 is not None else set()
        self.scxml_State31 = scxml_State31
        self.scxml_State111 = scxml_State111
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxml_State10(self):
        return self.__scxml_State10

    @scxml_State10.setter
    def scxml_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State10", None)
        self.__scxml_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State8"):
                opp_val = getattr(old_value, "scxml_State8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State8"):
                opp_val = getattr(value, "scxml_State8", None)
                if opp_val is None:
                    setattr(value, "scxml_State8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_State14(self):
        return self.__scxml_State14

    @scxml_State14.setter
    def scxml_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State14", None)
        self.__scxml_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Parallel"):
                    opp_val = getattr(item, "scxml_Parallel", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Parallel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Parallel"):
                    opp_val = getattr(item, "scxml_Parallel", None)
                    
                    setattr(item, "scxml_Parallel", self)
                    

    @property
    def scxml_State8(self):
        return self.__scxml_State8

    @scxml_State8.setter
    def scxml_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State8", None)
        self.__scxml_State8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_State10"):
                    opp_val = getattr(item, "scxml_State10", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_State10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_State10"):
                    opp_val = getattr(item, "scxml_State10", None)
                    
                    setattr(item, "scxml_State10", self)
                    

    @property
    def scxml_State(self):
        return self.__scxml_State

    @scxml_State.setter
    def scxml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State", None)
        self.__scxml_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnEntry"):
                    opp_val = getattr(item, "scxml_OnEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnEntry"):
                    opp_val = getattr(item, "scxml_OnEntry", None)
                    
                    setattr(item, "scxml_OnEntry", self)
                    

    @property
    def scxml_State111(self):
        return self.__scxml_State111

    @scxml_State111.setter
    def scxml_State111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State111", None)
        self.__scxml_State111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Parallel110"):
                opp_val = getattr(old_value, "scxml_Parallel110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Parallel110"):
                opp_val = getattr(value, "scxml_Parallel110", None)
                if opp_val is None:
                    setattr(value, "scxml_Parallel110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_State16(self):
        return self.__scxml_State16

    @scxml_State16.setter
    def scxml_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State16", None)
        self.__scxml_State16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_HistoryState"):
                    opp_val = getattr(item, "scxml_HistoryState", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_HistoryState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_HistoryState"):
                    opp_val = getattr(item, "scxml_HistoryState", None)
                    
                    setattr(item, "scxml_HistoryState", self)
                    

    @property
    def scxml_State20(self):
        return self.__scxml_State20

    @scxml_State20.setter
    def scxml_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State20", None)
        self.__scxml_State20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Invoke"):
                    opp_val = getattr(item, "scxml_Invoke", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Invoke", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Invoke"):
                    opp_val = getattr(item, "scxml_Invoke", None)
                    
                    setattr(item, "scxml_Invoke", self)
                    

    @property
    def scxml_State7(self):
        return self.__scxml_State7

    @scxml_State7.setter
    def scxml_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State7", None)
        self.__scxml_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_InitialState"):
                opp_val = getattr(old_value, "scxml_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "scxml_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_InitialState"):
                opp_val = getattr(value, "scxml_InitialState", None)
                setattr(value, "scxml_InitialState", self)

    @property
    def scxml_State18(self):
        return self.__scxml_State18

    @scxml_State18.setter
    def scxml_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State18", None)
        self.__scxml_State18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Anchor"):
                    opp_val = getattr(item, "scxml_Anchor", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Anchor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Anchor"):
                    opp_val = getattr(item, "scxml_Anchor", None)
                    
                    setattr(item, "scxml_Anchor", self)
                    

    @property
    def scxml_State5(self):
        return self.__scxml_State5

    @scxml_State5.setter
    def scxml_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State5", None)
        self.__scxml_State5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_OnExit"):
                    opp_val = getattr(item, "scxml_OnExit", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_OnExit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_OnExit"):
                    opp_val = getattr(item, "scxml_OnExit", None)
                    
                    setattr(item, "scxml_OnExit", self)
                    

    @property
    def scxml_State12(self):
        return self.__scxml_State12

    @scxml_State12.setter
    def scxml_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State12", None)
        self.__scxml_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_FinalState"):
                    opp_val = getattr(item, "scxml_FinalState", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_FinalState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_FinalState"):
                    opp_val = getattr(item, "scxml_FinalState", None)
                    
                    setattr(item, "scxml_FinalState", self)
                    

    @property
    def scxml_State31(self):
        return self.__scxml_State31

    @scxml_State31.setter
    def scxml_State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_State__scxml_State31", None)
        self.__scxml_State31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ServiceTemplate30"):
                opp_val = getattr(old_value, "scxml_ServiceTemplate30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ServiceTemplate30"):
                opp_val = getattr(value, "scxml_ServiceTemplate30", None)
                if opp_val is None:
                    setattr(value, "scxml_ServiceTemplate30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Transition:

    def __init__(self, event: str, cond: str, anchor: str, scxml_Transition: "scxml_NamedElement" = None, scxml_Transition22: "scxml_NamedElement" = None, scxml_Transition25: "scxml_NamedElement" = None, scxml_Transition28: "scxml_ServiceTemplate" = None):
        self.event = event
        self.cond = cond
        self.anchor = anchor
        self.scxml_Transition = scxml_Transition
        self.scxml_Transition22 = scxml_Transition22
        self.scxml_Transition25 = scxml_Transition25
        self.scxml_Transition28 = scxml_Transition28
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def anchor(self) -> str:
        return self.__anchor

    @anchor.setter
    def anchor(self, anchor: str):
        self.__anchor = anchor

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def scxml_Transition25(self):
        return self.__scxml_Transition25

    @scxml_Transition25.setter
    def scxml_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Transition__scxml_Transition25", None)
        self.__scxml_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_NamedElement26"):
                opp_val = getattr(old_value, "scxml_NamedElement26", None)
                if opp_val == self:
                    setattr(old_value, "scxml_NamedElement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_NamedElement26"):
                opp_val = getattr(value, "scxml_NamedElement26", None)
                setattr(value, "scxml_NamedElement26", self)

    @property
    def scxml_Transition(self):
        return self.__scxml_Transition

    @scxml_Transition.setter
    def scxml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Transition__scxml_Transition", None)
        self.__scxml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_NamedElement2"):
                opp_val = getattr(old_value, "scxml_NamedElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_NamedElement2"):
                opp_val = getattr(value, "scxml_NamedElement2", None)
                if opp_val is None:
                    setattr(value, "scxml_NamedElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Transition22(self):
        return self.__scxml_Transition22

    @scxml_Transition22.setter
    def scxml_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Transition__scxml_Transition22", None)
        self.__scxml_Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_NamedElement23"):
                opp_val = getattr(old_value, "scxml_NamedElement23", None)
                if opp_val == self:
                    setattr(old_value, "scxml_NamedElement23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_NamedElement23"):
                opp_val = getattr(value, "scxml_NamedElement23", None)
                setattr(value, "scxml_NamedElement23", self)

    @property
    def scxml_Transition28(self):
        return self.__scxml_Transition28

    @scxml_Transition28.setter
    def scxml_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Transition__scxml_Transition28", None)
        self.__scxml_Transition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ServiceTemplate"):
                opp_val = getattr(old_value, "scxml_ServiceTemplate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ServiceTemplate"):
                opp_val = getattr(value, "scxml_ServiceTemplate", None)
                if opp_val is None:
                    setattr(value, "scxml_ServiceTemplate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_DataModel:

    def __init__(self, schema: str, scxml_DataModel: "scxml_NamedElement" = None, scxml_DataModel43: "scxml_ServiceTemplate" = None, scxml_DataModel147: set["scxml_Data"] = None):
        self.schema = schema
        self.scxml_DataModel = scxml_DataModel
        self.scxml_DataModel43 = scxml_DataModel43
        self.scxml_DataModel147 = scxml_DataModel147 if scxml_DataModel147 is not None else set()
        
    @property
    def schema(self) -> str:
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema

    @property
    def scxml_DataModel147(self):
        return self.__scxml_DataModel147

    @scxml_DataModel147.setter
    def scxml_DataModel147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DataModel__scxml_DataModel147", None)
        self.__scxml_DataModel147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Data"):
                    opp_val = getattr(item, "scxml_Data", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Data"):
                    opp_val = getattr(item, "scxml_Data", None)
                    
                    setattr(item, "scxml_Data", self)
                    

    @property
    def scxml_DataModel43(self):
        return self.__scxml_DataModel43

    @scxml_DataModel43.setter
    def scxml_DataModel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DataModel__scxml_DataModel43", None)
        self.__scxml_DataModel43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ServiceTemplate42"):
                opp_val = getattr(old_value, "scxml_ServiceTemplate42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ServiceTemplate42"):
                opp_val = getattr(value, "scxml_ServiceTemplate42", None)
                if opp_val is None:
                    setattr(value, "scxml_ServiceTemplate42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_DataModel(self):
        return self.__scxml_DataModel

    @scxml_DataModel.setter
    def scxml_DataModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DataModel__scxml_DataModel", None)
        self.__scxml_DataModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_NamedElement"):
                opp_val = getattr(old_value, "scxml_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_NamedElement"):
                opp_val = getattr(value, "scxml_NamedElement", None)
                if opp_val is None:
                    setattr(value, "scxml_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_NamedElement:

    pass
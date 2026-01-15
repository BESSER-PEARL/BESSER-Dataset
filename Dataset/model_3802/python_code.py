from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ER_Relship:

    def __init__(self, name: str, Relship: "ER_ERSchema" = None, relships: "ER_ERSchema" = None, Relship15: "ER_RelshipEnd" = None, relship: set["ER_ERAttribute"] = None, relship10: set["ER_RelshipEnd"] = None, Relship23: "ER_ERAttribute" = None):
        self.name = name
        self.Relship = Relship
        self.relships = relships
        self.Relship15 = Relship15
        self.relship = relship if relship is not None else set()
        self.relship10 = relship10 if relship10 is not None else set()
        self.Relship23 = Relship23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Relship(self):
        return self.__Relship

    @Relship.setter
    def Relship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__Relship", None)
        self.__Relship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema2"):
                opp_val = getattr(old_value, "schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema2"):
                opp_val = getattr(value, "schema2", None)
                if opp_val is None:
                    setattr(value, "schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relship23(self):
        return self.__Relship23

    @Relship23.setter
    def Relship23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__Relship23", None)
        self.__Relship23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attrs22"):
                opp_val = getattr(old_value, "attrs22", None)
                if opp_val == self:
                    setattr(old_value, "attrs22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attrs22"):
                opp_val = getattr(value, "attrs22", None)
                setattr(value, "attrs22", self)

    @property
    def relship10(self):
        return self.__relship10

    @relship10.setter
    def relship10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__relship10", None)
        self.__relship10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelshipEnd11"):
                    opp_val = getattr(item, "RelshipEnd11", None)
                    
                    if opp_val == self:
                        setattr(item, "RelshipEnd11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelshipEnd11"):
                    opp_val = getattr(item, "RelshipEnd11", None)
                    
                    setattr(item, "RelshipEnd11", self)
                    

    @property
    def relships(self):
        return self.__relships

    @relships.setter
    def relships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__relships", None)
        self.__relships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERSchema13"):
                opp_val = getattr(old_value, "ERSchema13", None)
                if opp_val == self:
                    setattr(old_value, "ERSchema13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERSchema13"):
                opp_val = getattr(value, "ERSchema13", None)
                setattr(value, "ERSchema13", self)

    @property
    def relship(self):
        return self.__relship

    @relship.setter
    def relship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__relship", None)
        self.__relship = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ERAttribute8"):
                    opp_val = getattr(item, "ERAttribute8", None)
                    
                    if opp_val == self:
                        setattr(item, "ERAttribute8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ERAttribute8"):
                    opp_val = getattr(item, "ERAttribute8", None)
                    
                    setattr(item, "ERAttribute8", self)
                    

    @property
    def Relship15(self):
        return self.__Relship15

    @Relship15.setter
    def Relship15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Relship__Relship15", None)
        self.__Relship15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ends"):
                opp_val = getattr(old_value, "ends", None)
                if opp_val == self:
                    setattr(old_value, "ends", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ends"):
                opp_val = getattr(value, "ends", None)
                setattr(value, "ends", self)

class ER_Entity:

    def __init__(self, name: str, entity: set["ER_ERAttribute"] = None, entity5: set["ER_RelshipEnd"] = None, Entity: "ER_ERSchema" = None, entities: "ER_ERSchema" = None, Entity18: "ER_RelshipEnd" = None, Entity20: "ER_ERAttribute" = None):
        self.name = name
        self.entity = entity if entity is not None else set()
        self.entity5 = entity5 if entity5 is not None else set()
        self.Entity = Entity
        self.entities = entities
        self.Entity18 = Entity18
        self.Entity20 = Entity20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Entity18(self):
        return self.__Entity18

    @Entity18.setter
    def Entity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__Entity18", None)
        self.__Entity18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ends17"):
                opp_val = getattr(old_value, "ends17", None)
                if opp_val == self:
                    setattr(old_value, "ends17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ends17"):
                opp_val = getattr(value, "ends17", None)
                setattr(value, "ends17", self)

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__entity", None)
        self.__entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ERAttribute"):
                    opp_val = getattr(item, "ERAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ERAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ERAttribute"):
                    opp_val = getattr(item, "ERAttribute", None)
                    
                    setattr(item, "ERAttribute", self)
                    

    @property
    def entity5(self):
        return self.__entity5

    @entity5.setter
    def entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__entity5", None)
        self.__entity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelshipEnd"):
                    opp_val = getattr(item, "RelshipEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "RelshipEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelshipEnd"):
                    opp_val = getattr(item, "RelshipEnd", None)
                    
                    setattr(item, "RelshipEnd", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                if opp_val is None:
                    setattr(value, "schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Entity20(self):
        return self.__Entity20

    @Entity20.setter
    def Entity20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__Entity20", None)
        self.__Entity20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attrs"):
                opp_val = getattr(old_value, "attrs", None)
                if opp_val == self:
                    setattr(old_value, "attrs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attrs"):
                opp_val = getattr(value, "attrs", None)
                setattr(value, "attrs", self)

    @property
    def entities(self):
        return self.__entities

    @entities.setter
    def entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Entity__entities", None)
        self.__entities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERSchema"):
                opp_val = getattr(old_value, "ERSchema", None)
                if opp_val == self:
                    setattr(old_value, "ERSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERSchema"):
                opp_val = getattr(value, "ERSchema", None)
                setattr(value, "ERSchema", self)

class ER_RelshipEnd:

    def __init__(self, name: str, RelshipEnd: "ER_Entity" = None, ends: "ER_Relship" = None, RelshipEnd11: "ER_Relship" = None, ends17: "ER_Entity" = None):
        self.name = name
        self.RelshipEnd = RelshipEnd
        self.ends = ends
        self.RelshipEnd11 = RelshipEnd11
        self.ends17 = ends17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ends(self):
        return self.__ends

    @ends.setter
    def ends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_RelshipEnd__ends", None)
        self.__ends = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relship15"):
                opp_val = getattr(old_value, "Relship15", None)
                if opp_val == self:
                    setattr(old_value, "Relship15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relship15"):
                opp_val = getattr(value, "Relship15", None)
                setattr(value, "Relship15", self)

    @property
    def RelshipEnd(self):
        return self.__RelshipEnd

    @RelshipEnd.setter
    def RelshipEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_RelshipEnd__RelshipEnd", None)
        self.__RelshipEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity5"):
                opp_val = getattr(old_value, "entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity5"):
                opp_val = getattr(value, "entity5", None)
                if opp_val is None:
                    setattr(value, "entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ends17(self):
        return self.__ends17

    @ends17.setter
    def ends17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_RelshipEnd__ends17", None)
        self.__ends17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity18"):
                opp_val = getattr(old_value, "Entity18", None)
                if opp_val == self:
                    setattr(old_value, "Entity18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity18"):
                opp_val = getattr(value, "Entity18", None)
                setattr(value, "Entity18", self)

    @property
    def RelshipEnd11(self):
        return self.__RelshipEnd11

    @RelshipEnd11.setter
    def RelshipEnd11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_RelshipEnd__RelshipEnd11", None)
        self.__RelshipEnd11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relship10"):
                opp_val = getattr(old_value, "relship10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relship10"):
                opp_val = getattr(value, "relship10", None)
                if opp_val is None:
                    setattr(value, "relship10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ER_ERAttribute:

    def __init__(self, isKey: bool, name: str, ERAttribute: "ER_Entity" = None, ERAttribute8: "ER_Relship" = None, attrs22: "ER_Relship" = None, attrs: "ER_Entity" = None):
        self.isKey = isKey
        self.name = name
        self.ERAttribute = ERAttribute
        self.ERAttribute8 = ERAttribute8
        self.attrs22 = attrs22
        self.attrs = attrs
        
    @property
    def isKey(self) -> bool:
        return self.__isKey

    @isKey.setter
    def isKey(self, isKey: bool):
        self.__isKey = isKey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ERAttribute8(self):
        return self.__ERAttribute8

    @ERAttribute8.setter
    def ERAttribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERAttribute__ERAttribute8", None)
        self.__ERAttribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relship"):
                opp_val = getattr(old_value, "relship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relship"):
                opp_val = getattr(value, "relship", None)
                if opp_val is None:
                    setattr(value, "relship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attrs(self):
        return self.__attrs

    @attrs.setter
    def attrs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERAttribute__attrs", None)
        self.__attrs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity20"):
                opp_val = getattr(old_value, "Entity20", None)
                if opp_val == self:
                    setattr(old_value, "Entity20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity20"):
                opp_val = getattr(value, "Entity20", None)
                setattr(value, "Entity20", self)

    @property
    def attrs22(self):
        return self.__attrs22

    @attrs22.setter
    def attrs22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERAttribute__attrs22", None)
        self.__attrs22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relship23"):
                opp_val = getattr(old_value, "Relship23", None)
                if opp_val == self:
                    setattr(old_value, "Relship23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relship23"):
                opp_val = getattr(value, "Relship23", None)
                setattr(value, "Relship23", self)

    @property
    def ERAttribute(self):
        return self.__ERAttribute

    @ERAttribute.setter
    def ERAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERAttribute__ERAttribute", None)
        self.__ERAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity"):
                opp_val = getattr(old_value, "entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity"):
                opp_val = getattr(value, "entity", None)
                if opp_val is None:
                    setattr(value, "entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ER_ERSchema:

    def __init__(self, name: str, ERSchema: "ER_Entity" = None, schema: set["ER_Entity"] = None, schema2: set["ER_Relship"] = None, ERSchema13: "ER_Relship" = None):
        self.name = name
        self.ERSchema = ERSchema
        self.schema = schema if schema is not None else set()
        self.schema2 = schema2 if schema2 is not None else set()
        self.ERSchema13 = ERSchema13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schema2(self):
        return self.__schema2

    @schema2.setter
    def schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERSchema__schema2", None)
        self.__schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relship"):
                    opp_val = getattr(item, "Relship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relship"):
                    opp_val = getattr(item, "Relship", None)
                    
                    setattr(item, "Relship", self)
                    

    @property
    def ERSchema(self):
        return self.__ERSchema

    @ERSchema.setter
    def ERSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERSchema__ERSchema", None)
        self.__ERSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities"):
                opp_val = getattr(old_value, "entities", None)
                if opp_val == self:
                    setattr(old_value, "entities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities"):
                opp_val = getattr(value, "entities", None)
                setattr(value, "entities", self)

    @property
    def ERSchema13(self):
        return self.__ERSchema13

    @ERSchema13.setter
    def ERSchema13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERSchema__ERSchema13", None)
        self.__ERSchema13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relships"):
                opp_val = getattr(old_value, "relships", None)
                if opp_val == self:
                    setattr(old_value, "relships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relships"):
                opp_val = getattr(value, "relships", None)
                setattr(value, "relships", self)

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ERSchema__schema", None)
        self.__schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    setattr(item, "Entity", self)
                    

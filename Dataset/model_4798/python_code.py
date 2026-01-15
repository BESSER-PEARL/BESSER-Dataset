from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class primitives_Bag:

    def __init__(self, id: str, primitives_Bag: "primitives_Primitive" = None, primitives_Bag3: "primitives_Bag" = None, primitives_Bag1: set["primitives_Bag"] = None):
        self.id = id
        self.primitives_Bag = primitives_Bag
        self.primitives_Bag3 = primitives_Bag3
        self.primitives_Bag1 = primitives_Bag1 if primitives_Bag1 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def primitives_Bag1(self):
        return self.__primitives_Bag1

    @primitives_Bag1.setter
    def primitives_Bag1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_primitives_Bag__primitives_Bag1", None)
        self.__primitives_Bag1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "primitives_Bag3"):
                    opp_val = getattr(item, "primitives_Bag3", None)
                    
                    if opp_val == self:
                        setattr(item, "primitives_Bag3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "primitives_Bag3"):
                    opp_val = getattr(item, "primitives_Bag3", None)
                    
                    setattr(item, "primitives_Bag3", self)
                    

    @property
    def primitives_Bag3(self):
        return self.__primitives_Bag3

    @primitives_Bag3.setter
    def primitives_Bag3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_primitives_Bag__primitives_Bag3", None)
        self.__primitives_Bag3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primitives_Bag1"):
                opp_val = getattr(old_value, "primitives_Bag1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primitives_Bag1"):
                opp_val = getattr(value, "primitives_Bag1", None)
                if opp_val is None:
                    setattr(value, "primitives_Bag1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def primitives_Bag(self):
        return self.__primitives_Bag

    @primitives_Bag.setter
    def primitives_Bag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_primitives_Bag__primitives_Bag", None)
        self.__primitives_Bag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primitives_Primitive"):
                opp_val = getattr(old_value, "primitives_Primitive", None)
                if opp_val == self:
                    setattr(old_value, "primitives_Primitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primitives_Primitive"):
                opp_val = getattr(value, "primitives_Primitive", None)
                setattr(value, "primitives_Primitive", self)

class primitives_Primitive:

    def __init__(self, bigdecimal: str, bigint: str, boolean: bool, booleanObj: str, byte: str, byteArray: str, byteObj: str, char: str, characterObj: str, date: date, double: float, doubleObj: str, float: float, floatObj: str, int: int, integerObj: str, javaClass: str, javaObj: str, long: str, longObj: str, short: str, shortObj: str, string: str, primitives_Primitive: "primitives_Bag" = None):
        self.bigdecimal = bigdecimal
        self.bigint = bigint
        self.boolean = boolean
        self.booleanObj = booleanObj
        self.byte = byte
        self.byteArray = byteArray
        self.byteObj = byteObj
        self.char = char
        self.characterObj = characterObj
        self.date = date
        self.double = double
        self.doubleObj = doubleObj
        self.float = float
        self.floatObj = floatObj
        self.int = int
        self.integerObj = integerObj
        self.javaClass = javaClass
        self.javaObj = javaObj
        self.long = long
        self.longObj = longObj
        self.short = short
        self.shortObj = shortObj
        self.string = string
        self.primitives_Primitive = primitives_Primitive
        
    @property
    def integerObj(self) -> str:
        return self.__integerObj

    @integerObj.setter
    def integerObj(self, integerObj: str):
        self.__integerObj = integerObj

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def booleanObj(self) -> str:
        return self.__booleanObj

    @booleanObj.setter
    def booleanObj(self, booleanObj: str):
        self.__booleanObj = booleanObj

    @property
    def byteArray(self) -> str:
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

    @property
    def double(self) -> float:
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double

    @property
    def boolean(self) -> bool:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: bool):
        self.__boolean = boolean

    @property
    def floatObj(self) -> str:
        return self.__floatObj

    @floatObj.setter
    def floatObj(self, floatObj: str):
        self.__floatObj = floatObj

    @property
    def bigint(self) -> str:
        return self.__bigint

    @bigint.setter
    def bigint(self, bigint: str):
        self.__bigint = bigint

    @property
    def javaObj(self) -> str:
        return self.__javaObj

    @javaObj.setter
    def javaObj(self, javaObj: str):
        self.__javaObj = javaObj

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def byteObj(self) -> str:
        return self.__byteObj

    @byteObj.setter
    def byteObj(self, byteObj: str):
        self.__byteObj = byteObj

    @property
    def bigdecimal(self) -> str:
        return self.__bigdecimal

    @bigdecimal.setter
    def bigdecimal(self, bigdecimal: str):
        self.__bigdecimal = bigdecimal

    @property
    def doubleObj(self) -> str:
        return self.__doubleObj

    @doubleObj.setter
    def doubleObj(self, doubleObj: str):
        self.__doubleObj = doubleObj

    @property
    def short(self) -> str:
        return self.__short

    @short.setter
    def short(self, short: str):
        self.__short = short

    @property
    def float(self) -> float:
        return self.__float

    @float.setter
    def float(self, float: float):
        self.__float = float

    @property
    def longObj(self) -> str:
        return self.__longObj

    @longObj.setter
    def longObj(self, longObj: str):
        self.__longObj = longObj

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def characterObj(self) -> str:
        return self.__characterObj

    @characterObj.setter
    def characterObj(self, characterObj: str):
        self.__characterObj = characterObj

    @property
    def javaClass(self) -> str:
        return self.__javaClass

    @javaClass.setter
    def javaClass(self, javaClass: str):
        self.__javaClass = javaClass

    @property
    def byte(self) -> str:
        return self.__byte

    @byte.setter
    def byte(self, byte: str):
        self.__byte = byte

    @property
    def shortObj(self) -> str:
        return self.__shortObj

    @shortObj.setter
    def shortObj(self, shortObj: str):
        self.__shortObj = shortObj

    @property
    def primitives_Primitive(self):
        return self.__primitives_Primitive

    @primitives_Primitive.setter
    def primitives_Primitive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_primitives_Primitive__primitives_Primitive", None)
        self.__primitives_Primitive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primitives_Bag"):
                opp_val = getattr(old_value, "primitives_Bag", None)
                if opp_val == self:
                    setattr(old_value, "primitives_Bag", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primitives_Bag"):
                opp_val = getattr(value, "primitives_Bag", None)
                setattr(value, "primitives_Bag", self)

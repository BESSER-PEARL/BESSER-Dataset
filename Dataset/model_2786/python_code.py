from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test1_StringToIntegerMapEntry:

    def __init__(self, value: str, key: str, test1_StringToIntegerMapEntry: "test1_ConceptA" = None):
        self.value = value
        self.key = key
        self.test1_StringToIntegerMapEntry = test1_StringToIntegerMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test1_StringToIntegerMapEntry(self):
        return self.__test1_StringToIntegerMapEntry

    @test1_StringToIntegerMapEntry.setter
    def test1_StringToIntegerMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test1_StringToIntegerMapEntry__test1_StringToIntegerMapEntry", None)
        self.__test1_StringToIntegerMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test1_ConceptA"):
                opp_val = getattr(old_value, "test1_ConceptA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test1_ConceptA"):
                opp_val = getattr(value, "test1_ConceptA", None)
                if opp_val is None:
                    setattr(value, "test1_ConceptA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test1_ConceptA:

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ocltestmodel_MyClass:

    def __init__(self, static_sequence: str, collection_literals: str, boolean_unequal: bool, boolean_equal: bool, boolean_and: bool, integer_addition: int, integer_subtraction: int, integer_lessthan: bool, integer_greaterthan: bool, integer_greaterequals: bool, integer_lessequals: bool, integer_division: float, integer_absolute: int, integer_maximum: int, integer_minimum: int, integer_modulo: int, integer_toString: str, boolean_implies: bool, boolean_not: bool, boolean_or: bool, boolean_xor: bool, boolean_toString: str, integer_multiplication: int, real_lessequals: bool, real_division: str, real_absolute: str, real_maximum: str, real_minimum: str, real_floor: str, real_toString: str, string_addition: str, string_lessthan: bool, string_lessequals: bool, string_unequal: bool, string_equal: bool, string_greaterthan: bool, real_multiplication: str, real_addition: str, real_subtraction: str, real_lessthan: bool, real_greaterthan: bool, real_greaterequals: bool, string_replaceAll: str, string_size: str, let2: bool, let3: int, unEmployed: bool, let: bool, integer_sequence: int, sequence_selectByKind: str, string_greaterequals: bool, string_at: str, string_compareTo: str, string_concat: str, string_equalsIgnoreCase: bool, string_indexOf: str, string_lastIndexOf: str, _IntegerLiteralExp: str, _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER: str, _StringLiteralExp: str, _BooleanLiteralExp: bool, _RealLiteralExp: str, _NumberLiteralExp: str, _IfExp: str, _IfExp2: str, sequence_selectByType: str, tuple_literal: bool, orderedset_size: str, sequence_count: str, ocltestmodel_MyClass: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass0: set["ocltestmodel_MyClass"] = None, ocltestmodel_MyClass4: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass2: set["ocltestmodel_MyClass"] = None, ocltestmodel_MyClass7: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass5: set["ocltestmodel_MyClass"] = None, ocltestmodel_MyClass10: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass8: set["ocltestmodel_MyClass"] = None, ocltestmodel_MyClass16: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass14: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass19: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass17: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass22: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass20: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass13: "ocltestmodel_MyClass" = None, ocltestmodel_MyClass11: set["ocltestmodel_MyClass"] = None):
        self.static_sequence = static_sequence
        self.collection_literals = collection_literals
        self.boolean_unequal = boolean_unequal
        self.boolean_equal = boolean_equal
        self.boolean_and = boolean_and
        self.integer_addition = integer_addition
        self.integer_subtraction = integer_subtraction
        self.integer_lessthan = integer_lessthan
        self.integer_greaterthan = integer_greaterthan
        self.integer_greaterequals = integer_greaterequals
        self.integer_lessequals = integer_lessequals
        self.integer_division = integer_division
        self.integer_absolute = integer_absolute
        self.integer_maximum = integer_maximum
        self.integer_minimum = integer_minimum
        self.integer_modulo = integer_modulo
        self.integer_toString = integer_toString
        self.boolean_implies = boolean_implies
        self.boolean_not = boolean_not
        self.boolean_or = boolean_or
        self.boolean_xor = boolean_xor
        self.boolean_toString = boolean_toString
        self.integer_multiplication = integer_multiplication
        self.real_lessequals = real_lessequals
        self.real_division = real_division
        self.real_absolute = real_absolute
        self.real_maximum = real_maximum
        self.real_minimum = real_minimum
        self.real_floor = real_floor
        self.real_toString = real_toString
        self.string_addition = string_addition
        self.string_lessthan = string_lessthan
        self.string_lessequals = string_lessequals
        self.string_unequal = string_unequal
        self.string_equal = string_equal
        self.string_greaterthan = string_greaterthan
        self.real_multiplication = real_multiplication
        self.real_addition = real_addition
        self.real_subtraction = real_subtraction
        self.real_lessthan = real_lessthan
        self.real_greaterthan = real_greaterthan
        self.real_greaterequals = real_greaterequals
        self.string_replaceAll = string_replaceAll
        self.string_size = string_size
        self.let2 = let2
        self.let3 = let3
        self.unEmployed = unEmployed
        self.let = let
        self.integer_sequence = integer_sequence
        self.sequence_selectByKind = sequence_selectByKind
        self.string_greaterequals = string_greaterequals
        self.string_at = string_at
        self.string_compareTo = string_compareTo
        self.string_concat = string_concat
        self.string_equalsIgnoreCase = string_equalsIgnoreCase
        self.string_indexOf = string_indexOf
        self.string_lastIndexOf = string_lastIndexOf
        self._IntegerLiteralExp = _IntegerLiteralExp
        self._InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER = _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER
        self._StringLiteralExp = _StringLiteralExp
        self._BooleanLiteralExp = _BooleanLiteralExp
        self._RealLiteralExp = _RealLiteralExp
        self._NumberLiteralExp = _NumberLiteralExp
        self._IfExp = _IfExp
        self._IfExp2 = _IfExp2
        self.sequence_selectByType = sequence_selectByType
        self.tuple_literal = tuple_literal
        self.orderedset_size = orderedset_size
        self.sequence_count = sequence_count
        self.ocltestmodel_MyClass = ocltestmodel_MyClass
        self.ocltestmodel_MyClass0 = ocltestmodel_MyClass0 if ocltestmodel_MyClass0 is not None else set()
        self.ocltestmodel_MyClass4 = ocltestmodel_MyClass4
        self.ocltestmodel_MyClass2 = ocltestmodel_MyClass2 if ocltestmodel_MyClass2 is not None else set()
        self.ocltestmodel_MyClass7 = ocltestmodel_MyClass7
        self.ocltestmodel_MyClass5 = ocltestmodel_MyClass5 if ocltestmodel_MyClass5 is not None else set()
        self.ocltestmodel_MyClass10 = ocltestmodel_MyClass10
        self.ocltestmodel_MyClass8 = ocltestmodel_MyClass8 if ocltestmodel_MyClass8 is not None else set()
        self.ocltestmodel_MyClass16 = ocltestmodel_MyClass16
        self.ocltestmodel_MyClass14 = ocltestmodel_MyClass14
        self.ocltestmodel_MyClass19 = ocltestmodel_MyClass19
        self.ocltestmodel_MyClass17 = ocltestmodel_MyClass17
        self.ocltestmodel_MyClass22 = ocltestmodel_MyClass22
        self.ocltestmodel_MyClass20 = ocltestmodel_MyClass20
        self.ocltestmodel_MyClass13 = ocltestmodel_MyClass13
        self.ocltestmodel_MyClass11 = ocltestmodel_MyClass11 if ocltestmodel_MyClass11 is not None else set()
        
    @property
    def _BooleanLiteralExp(self) -> bool:
        return self.___BooleanLiteralExp

    @_BooleanLiteralExp.setter
    def _BooleanLiteralExp(self, _BooleanLiteralExp: bool):
        self.___BooleanLiteralExp = _BooleanLiteralExp

    @property
    def string_greaterequals(self) -> bool:
        return self.__string_greaterequals

    @string_greaterequals.setter
    def string_greaterequals(self, string_greaterequals: bool):
        self.__string_greaterequals = string_greaterequals

    @property
    def integer_sequence(self) -> int:
        return self.__integer_sequence

    @integer_sequence.setter
    def integer_sequence(self, integer_sequence: int):
        self.__integer_sequence = integer_sequence

    @property
    def real_lessequals(self) -> bool:
        return self.__real_lessequals

    @real_lessequals.setter
    def real_lessequals(self, real_lessequals: bool):
        self.__real_lessequals = real_lessequals

    @property
    def _IfExp2(self) -> str:
        return self.___IfExp2

    @_IfExp2.setter
    def _IfExp2(self, _IfExp2: str):
        self.___IfExp2 = _IfExp2

    @property
    def collection_literals(self) -> str:
        return self.__collection_literals

    @collection_literals.setter
    def collection_literals(self, collection_literals: str):
        self.__collection_literals = collection_literals

    @property
    def integer_lessthan(self) -> bool:
        return self.__integer_lessthan

    @integer_lessthan.setter
    def integer_lessthan(self, integer_lessthan: bool):
        self.__integer_lessthan = integer_lessthan

    @property
    def string_replaceAll(self) -> str:
        return self.__string_replaceAll

    @string_replaceAll.setter
    def string_replaceAll(self, string_replaceAll: str):
        self.__string_replaceAll = string_replaceAll

    @property
    def integer_lessequals(self) -> bool:
        return self.__integer_lessequals

    @integer_lessequals.setter
    def integer_lessequals(self, integer_lessequals: bool):
        self.__integer_lessequals = integer_lessequals

    @property
    def integer_greaterequals(self) -> bool:
        return self.__integer_greaterequals

    @integer_greaterequals.setter
    def integer_greaterequals(self, integer_greaterequals: bool):
        self.__integer_greaterequals = integer_greaterequals

    @property
    def integer_multiplication(self) -> int:
        return self.__integer_multiplication

    @integer_multiplication.setter
    def integer_multiplication(self, integer_multiplication: int):
        self.__integer_multiplication = integer_multiplication

    @property
    def boolean_unequal(self) -> bool:
        return self.__boolean_unequal

    @boolean_unequal.setter
    def boolean_unequal(self, boolean_unequal: bool):
        self.__boolean_unequal = boolean_unequal

    @property
    def real_lessthan(self) -> bool:
        return self.__real_lessthan

    @real_lessthan.setter
    def real_lessthan(self, real_lessthan: bool):
        self.__real_lessthan = real_lessthan

    @property
    def boolean_and(self) -> bool:
        return self.__boolean_and

    @boolean_and.setter
    def boolean_and(self, boolean_and: bool):
        self.__boolean_and = boolean_and

    @property
    def string_addition(self) -> str:
        return self.__string_addition

    @string_addition.setter
    def string_addition(self, string_addition: str):
        self.__string_addition = string_addition

    @property
    def string_concat(self) -> str:
        return self.__string_concat

    @string_concat.setter
    def string_concat(self, string_concat: str):
        self.__string_concat = string_concat

    @property
    def string_indexOf(self) -> str:
        return self.__string_indexOf

    @string_indexOf.setter
    def string_indexOf(self, string_indexOf: str):
        self.__string_indexOf = string_indexOf

    @property
    def real_greaterequals(self) -> bool:
        return self.__real_greaterequals

    @real_greaterequals.setter
    def real_greaterequals(self, real_greaterequals: bool):
        self.__real_greaterequals = real_greaterequals

    @property
    def real_absolute(self) -> str:
        return self.__real_absolute

    @real_absolute.setter
    def real_absolute(self, real_absolute: str):
        self.__real_absolute = real_absolute

    @property
    def boolean_toString(self) -> str:
        return self.__boolean_toString

    @boolean_toString.setter
    def boolean_toString(self, boolean_toString: str):
        self.__boolean_toString = boolean_toString

    @property
    def let3(self) -> int:
        return self.__let3

    @let3.setter
    def let3(self, let3: int):
        self.__let3 = let3

    @property
    def string_lessequals(self) -> bool:
        return self.__string_lessequals

    @string_lessequals.setter
    def string_lessequals(self, string_lessequals: bool):
        self.__string_lessequals = string_lessequals

    @property
    def _RealLiteralExp(self) -> str:
        return self.___RealLiteralExp

    @_RealLiteralExp.setter
    def _RealLiteralExp(self, _RealLiteralExp: str):
        self.___RealLiteralExp = _RealLiteralExp

    @property
    def integer_division(self) -> float:
        return self.__integer_division

    @integer_division.setter
    def integer_division(self, integer_division: float):
        self.__integer_division = integer_division

    @property
    def real_greaterthan(self) -> bool:
        return self.__real_greaterthan

    @real_greaterthan.setter
    def real_greaterthan(self, real_greaterthan: bool):
        self.__real_greaterthan = real_greaterthan

    @property
    def string_equalsIgnoreCase(self) -> bool:
        return self.__string_equalsIgnoreCase

    @string_equalsIgnoreCase.setter
    def string_equalsIgnoreCase(self, string_equalsIgnoreCase: bool):
        self.__string_equalsIgnoreCase = string_equalsIgnoreCase

    @property
    def _IfExp(self) -> str:
        return self.___IfExp

    @_IfExp.setter
    def _IfExp(self, _IfExp: str):
        self.___IfExp = _IfExp

    @property
    def real_toString(self) -> str:
        return self.__real_toString

    @real_toString.setter
    def real_toString(self, real_toString: str):
        self.__real_toString = real_toString

    @property
    def string_lessthan(self) -> bool:
        return self.__string_lessthan

    @string_lessthan.setter
    def string_lessthan(self, string_lessthan: bool):
        self.__string_lessthan = string_lessthan

    @property
    def _IntegerLiteralExp(self) -> str:
        return self.___IntegerLiteralExp

    @_IntegerLiteralExp.setter
    def _IntegerLiteralExp(self, _IntegerLiteralExp: str):
        self.___IntegerLiteralExp = _IntegerLiteralExp

    @property
    def boolean_xor(self) -> bool:
        return self.__boolean_xor

    @boolean_xor.setter
    def boolean_xor(self, boolean_xor: bool):
        self.__boolean_xor = boolean_xor

    @property
    def boolean_not(self) -> bool:
        return self.__boolean_not

    @boolean_not.setter
    def boolean_not(self, boolean_not: bool):
        self.__boolean_not = boolean_not

    @property
    def string_compareTo(self) -> str:
        return self.__string_compareTo

    @string_compareTo.setter
    def string_compareTo(self, string_compareTo: str):
        self.__string_compareTo = string_compareTo

    @property
    def boolean_or(self) -> bool:
        return self.__boolean_or

    @boolean_or.setter
    def boolean_or(self, boolean_or: bool):
        self.__boolean_or = boolean_or

    @property
    def sequence_selectByType(self) -> str:
        return self.__sequence_selectByType

    @sequence_selectByType.setter
    def sequence_selectByType(self, sequence_selectByType: str):
        self.__sequence_selectByType = sequence_selectByType

    @property
    def tuple_literal(self) -> bool:
        return self.__tuple_literal

    @tuple_literal.setter
    def tuple_literal(self, tuple_literal: bool):
        self.__tuple_literal = tuple_literal

    @property
    def sequence_count(self) -> str:
        return self.__sequence_count

    @sequence_count.setter
    def sequence_count(self, sequence_count: str):
        self.__sequence_count = sequence_count

    @property
    def _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER(self) -> str:
        return self.___InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER

    @_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER.setter
    def _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER(self, _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER: str):
        self.___InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER = _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER

    @property
    def real_floor(self) -> str:
        return self.__real_floor

    @real_floor.setter
    def real_floor(self, real_floor: str):
        self.__real_floor = real_floor

    @property
    def let(self) -> bool:
        return self.__let

    @let.setter
    def let(self, let: bool):
        self.__let = let

    @property
    def string_at(self) -> str:
        return self.__string_at

    @string_at.setter
    def string_at(self, string_at: str):
        self.__string_at = string_at

    @property
    def string_equal(self) -> bool:
        return self.__string_equal

    @string_equal.setter
    def string_equal(self, string_equal: bool):
        self.__string_equal = string_equal

    @property
    def boolean_implies(self) -> bool:
        return self.__boolean_implies

    @boolean_implies.setter
    def boolean_implies(self, boolean_implies: bool):
        self.__boolean_implies = boolean_implies

    @property
    def static_sequence(self) -> str:
        return self.__static_sequence

    @static_sequence.setter
    def static_sequence(self, static_sequence: str):
        self.__static_sequence = static_sequence

    @property
    def string_size(self) -> str:
        return self.__string_size

    @string_size.setter
    def string_size(self, string_size: str):
        self.__string_size = string_size

    @property
    def boolean_equal(self) -> bool:
        return self.__boolean_equal

    @boolean_equal.setter
    def boolean_equal(self, boolean_equal: bool):
        self.__boolean_equal = boolean_equal

    @property
    def string_lastIndexOf(self) -> str:
        return self.__string_lastIndexOf

    @string_lastIndexOf.setter
    def string_lastIndexOf(self, string_lastIndexOf: str):
        self.__string_lastIndexOf = string_lastIndexOf

    @property
    def integer_toString(self) -> str:
        return self.__integer_toString

    @integer_toString.setter
    def integer_toString(self, integer_toString: str):
        self.__integer_toString = integer_toString

    @property
    def unEmployed(self) -> bool:
        return self.__unEmployed

    @unEmployed.setter
    def unEmployed(self, unEmployed: bool):
        self.__unEmployed = unEmployed

    @property
    def _NumberLiteralExp(self) -> str:
        return self.___NumberLiteralExp

    @_NumberLiteralExp.setter
    def _NumberLiteralExp(self, _NumberLiteralExp: str):
        self.___NumberLiteralExp = _NumberLiteralExp

    @property
    def _StringLiteralExp(self) -> str:
        return self.___StringLiteralExp

    @_StringLiteralExp.setter
    def _StringLiteralExp(self, _StringLiteralExp: str):
        self.___StringLiteralExp = _StringLiteralExp

    @property
    def integer_maximum(self) -> int:
        return self.__integer_maximum

    @integer_maximum.setter
    def integer_maximum(self, integer_maximum: int):
        self.__integer_maximum = integer_maximum

    @property
    def integer_subtraction(self) -> int:
        return self.__integer_subtraction

    @integer_subtraction.setter
    def integer_subtraction(self, integer_subtraction: int):
        self.__integer_subtraction = integer_subtraction

    @property
    def real_multiplication(self) -> str:
        return self.__real_multiplication

    @real_multiplication.setter
    def real_multiplication(self, real_multiplication: str):
        self.__real_multiplication = real_multiplication

    @property
    def integer_greaterthan(self) -> bool:
        return self.__integer_greaterthan

    @integer_greaterthan.setter
    def integer_greaterthan(self, integer_greaterthan: bool):
        self.__integer_greaterthan = integer_greaterthan

    @property
    def string_unequal(self) -> bool:
        return self.__string_unequal

    @string_unequal.setter
    def string_unequal(self, string_unequal: bool):
        self.__string_unequal = string_unequal

    @property
    def orderedset_size(self) -> str:
        return self.__orderedset_size

    @orderedset_size.setter
    def orderedset_size(self, orderedset_size: str):
        self.__orderedset_size = orderedset_size

    @property
    def integer_addition(self) -> int:
        return self.__integer_addition

    @integer_addition.setter
    def integer_addition(self, integer_addition: int):
        self.__integer_addition = integer_addition

    @property
    def integer_modulo(self) -> int:
        return self.__integer_modulo

    @integer_modulo.setter
    def integer_modulo(self, integer_modulo: int):
        self.__integer_modulo = integer_modulo

    @property
    def real_subtraction(self) -> str:
        return self.__real_subtraction

    @real_subtraction.setter
    def real_subtraction(self, real_subtraction: str):
        self.__real_subtraction = real_subtraction

    @property
    def real_minimum(self) -> str:
        return self.__real_minimum

    @real_minimum.setter
    def real_minimum(self, real_minimum: str):
        self.__real_minimum = real_minimum

    @property
    def sequence_selectByKind(self) -> str:
        return self.__sequence_selectByKind

    @sequence_selectByKind.setter
    def sequence_selectByKind(self, sequence_selectByKind: str):
        self.__sequence_selectByKind = sequence_selectByKind

    @property
    def integer_absolute(self) -> int:
        return self.__integer_absolute

    @integer_absolute.setter
    def integer_absolute(self, integer_absolute: int):
        self.__integer_absolute = integer_absolute

    @property
    def real_maximum(self) -> str:
        return self.__real_maximum

    @real_maximum.setter
    def real_maximum(self, real_maximum: str):
        self.__real_maximum = real_maximum

    @property
    def let2(self) -> bool:
        return self.__let2

    @let2.setter
    def let2(self, let2: bool):
        self.__let2 = let2

    @property
    def real_division(self) -> str:
        return self.__real_division

    @real_division.setter
    def real_division(self, real_division: str):
        self.__real_division = real_division

    @property
    def string_greaterthan(self) -> bool:
        return self.__string_greaterthan

    @string_greaterthan.setter
    def string_greaterthan(self, string_greaterthan: bool):
        self.__string_greaterthan = string_greaterthan

    @property
    def integer_minimum(self) -> int:
        return self.__integer_minimum

    @integer_minimum.setter
    def integer_minimum(self, integer_minimum: int):
        self.__integer_minimum = integer_minimum

    @property
    def real_addition(self) -> str:
        return self.__real_addition

    @real_addition.setter
    def real_addition(self, real_addition: str):
        self.__real_addition = real_addition

    @property
    def ocltestmodel_MyClass17(self):
        return self.__ocltestmodel_MyClass17

    @ocltestmodel_MyClass17.setter
    def ocltestmodel_MyClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass17", None)
        self.__ocltestmodel_MyClass17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass19"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass19", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass19"):
                opp_val = getattr(value, "ocltestmodel_MyClass19", None)
                setattr(value, "ocltestmodel_MyClass19", self)

    @property
    def ocltestmodel_MyClass20(self):
        return self.__ocltestmodel_MyClass20

    @ocltestmodel_MyClass20.setter
    def ocltestmodel_MyClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass20", None)
        self.__ocltestmodel_MyClass20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass22"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass22", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass22"):
                opp_val = getattr(value, "ocltestmodel_MyClass22", None)
                setattr(value, "ocltestmodel_MyClass22", self)

    @property
    def ocltestmodel_MyClass16(self):
        return self.__ocltestmodel_MyClass16

    @ocltestmodel_MyClass16.setter
    def ocltestmodel_MyClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass16", None)
        self.__ocltestmodel_MyClass16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass14"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass14", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass14"):
                opp_val = getattr(value, "ocltestmodel_MyClass14", None)
                setattr(value, "ocltestmodel_MyClass14", self)

    @property
    def ocltestmodel_MyClass0(self):
        return self.__ocltestmodel_MyClass0

    @ocltestmodel_MyClass0.setter
    def ocltestmodel_MyClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass0", None)
        self.__ocltestmodel_MyClass0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ocltestmodel_MyClass"):
                    opp_val = getattr(item, "ocltestmodel_MyClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ocltestmodel_MyClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ocltestmodel_MyClass"):
                    opp_val = getattr(item, "ocltestmodel_MyClass", None)
                    
                    setattr(item, "ocltestmodel_MyClass", self)
                    

    @property
    def ocltestmodel_MyClass11(self):
        return self.__ocltestmodel_MyClass11

    @ocltestmodel_MyClass11.setter
    def ocltestmodel_MyClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass11", None)
        self.__ocltestmodel_MyClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ocltestmodel_MyClass13"):
                    opp_val = getattr(item, "ocltestmodel_MyClass13", None)
                    
                    if opp_val == self:
                        setattr(item, "ocltestmodel_MyClass13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ocltestmodel_MyClass13"):
                    opp_val = getattr(item, "ocltestmodel_MyClass13", None)
                    
                    setattr(item, "ocltestmodel_MyClass13", self)
                    

    @property
    def ocltestmodel_MyClass14(self):
        return self.__ocltestmodel_MyClass14

    @ocltestmodel_MyClass14.setter
    def ocltestmodel_MyClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass14", None)
        self.__ocltestmodel_MyClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass16"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass16", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass16"):
                opp_val = getattr(value, "ocltestmodel_MyClass16", None)
                setattr(value, "ocltestmodel_MyClass16", self)

    @property
    def ocltestmodel_MyClass19(self):
        return self.__ocltestmodel_MyClass19

    @ocltestmodel_MyClass19.setter
    def ocltestmodel_MyClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass19", None)
        self.__ocltestmodel_MyClass19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass17"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass17", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass17"):
                opp_val = getattr(value, "ocltestmodel_MyClass17", None)
                setattr(value, "ocltestmodel_MyClass17", self)

    @property
    def ocltestmodel_MyClass5(self):
        return self.__ocltestmodel_MyClass5

    @ocltestmodel_MyClass5.setter
    def ocltestmodel_MyClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass5", None)
        self.__ocltestmodel_MyClass5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ocltestmodel_MyClass7"):
                    opp_val = getattr(item, "ocltestmodel_MyClass7", None)
                    
                    if opp_val == self:
                        setattr(item, "ocltestmodel_MyClass7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ocltestmodel_MyClass7"):
                    opp_val = getattr(item, "ocltestmodel_MyClass7", None)
                    
                    setattr(item, "ocltestmodel_MyClass7", self)
                    

    @property
    def ocltestmodel_MyClass8(self):
        return self.__ocltestmodel_MyClass8

    @ocltestmodel_MyClass8.setter
    def ocltestmodel_MyClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass8", None)
        self.__ocltestmodel_MyClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ocltestmodel_MyClass10"):
                    opp_val = getattr(item, "ocltestmodel_MyClass10", None)
                    
                    if opp_val == self:
                        setattr(item, "ocltestmodel_MyClass10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ocltestmodel_MyClass10"):
                    opp_val = getattr(item, "ocltestmodel_MyClass10", None)
                    
                    setattr(item, "ocltestmodel_MyClass10", self)
                    

    @property
    def ocltestmodel_MyClass22(self):
        return self.__ocltestmodel_MyClass22

    @ocltestmodel_MyClass22.setter
    def ocltestmodel_MyClass22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass22", None)
        self.__ocltestmodel_MyClass22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass20"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass20", None)
                if opp_val == self:
                    setattr(old_value, "ocltestmodel_MyClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass20"):
                opp_val = getattr(value, "ocltestmodel_MyClass20", None)
                setattr(value, "ocltestmodel_MyClass20", self)

    @property
    def ocltestmodel_MyClass10(self):
        return self.__ocltestmodel_MyClass10

    @ocltestmodel_MyClass10.setter
    def ocltestmodel_MyClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass10", None)
        self.__ocltestmodel_MyClass10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass8"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass8"):
                opp_val = getattr(value, "ocltestmodel_MyClass8", None)
                if opp_val is None:
                    setattr(value, "ocltestmodel_MyClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltestmodel_MyClass(self):
        return self.__ocltestmodel_MyClass

    @ocltestmodel_MyClass.setter
    def ocltestmodel_MyClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass", None)
        self.__ocltestmodel_MyClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass0"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass0"):
                opp_val = getattr(value, "ocltestmodel_MyClass0", None)
                if opp_val is None:
                    setattr(value, "ocltestmodel_MyClass0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltestmodel_MyClass13(self):
        return self.__ocltestmodel_MyClass13

    @ocltestmodel_MyClass13.setter
    def ocltestmodel_MyClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass13", None)
        self.__ocltestmodel_MyClass13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass11"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass11"):
                opp_val = getattr(value, "ocltestmodel_MyClass11", None)
                if opp_val is None:
                    setattr(value, "ocltestmodel_MyClass11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltestmodel_MyClass7(self):
        return self.__ocltestmodel_MyClass7

    @ocltestmodel_MyClass7.setter
    def ocltestmodel_MyClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass7", None)
        self.__ocltestmodel_MyClass7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass5"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass5"):
                opp_val = getattr(value, "ocltestmodel_MyClass5", None)
                if opp_val is None:
                    setattr(value, "ocltestmodel_MyClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltestmodel_MyClass4(self):
        return self.__ocltestmodel_MyClass4

    @ocltestmodel_MyClass4.setter
    def ocltestmodel_MyClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass4", None)
        self.__ocltestmodel_MyClass4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltestmodel_MyClass2"):
                opp_val = getattr(old_value, "ocltestmodel_MyClass2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltestmodel_MyClass2"):
                opp_val = getattr(value, "ocltestmodel_MyClass2", None)
                if opp_val is None:
                    setattr(value, "ocltestmodel_MyClass2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltestmodel_MyClass2(self):
        return self.__ocltestmodel_MyClass2

    @ocltestmodel_MyClass2.setter
    def ocltestmodel_MyClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltestmodel_MyClass__ocltestmodel_MyClass2", None)
        self.__ocltestmodel_MyClass2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ocltestmodel_MyClass4"):
                    opp_val = getattr(item, "ocltestmodel_MyClass4", None)
                    
                    if opp_val == self:
                        setattr(item, "ocltestmodel_MyClass4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ocltestmodel_MyClass4"):
                    opp_val = getattr(item, "ocltestmodel_MyClass4", None)
                    
                    setattr(item, "ocltestmodel_MyClass4", self)
                    

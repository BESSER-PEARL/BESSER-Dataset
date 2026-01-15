from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MyEnumeration(Enum):


############################################
# Definition of Classes
############################################

class typetranslation_AbstractClass(ABC):

    pass
class typetranslation_MyClass:

    def __init__(self, ocl_string_single: str, ocl_string_multi: str, ocl_integer_single: str, ocl_integer_multi: str, ocl_real_single: str, ocl_real_multi: str, ocl_boolean_single: str, ocl_boolean_multi: str, ecore_ebigdecimal_single: str, ecore_ebigdecimal_multi: str, ecore_ebiginteger_single: str, ecore_ebiginteger_multi: str, ecore_eboolean_single: bool, ecore_eboolean_multi: bool, ecore_ebooleanobject_single: str, ecore_ebooleanobject_multi: str, ecore_ebyte_single: str, ecore_ebyte_multi: str, ecore_ebytearray_single: str, ecore_ebytearray_multi: str, ecore_ebyteobject_single: str, ecore_ebyteobject_multi: str, ecore_echar_single: str, ecore_echar_multi: str, ecore_echaracterobject_single: str, ecore_echaracterobject_multi: str, ecore_edate_single: date, ecore_edate_multi: date, ecore_ediagnosticchain_single: str, ecore_ediagnosticchain_multi: str, ecore_edouble_single: float, ecore_edouble_multi: float, ecore_edoubleobject_single: str, ecore_edoubleobject_multi: str, ecore_eelist_multi: str, ecore_eenumerator_single: str, ecore_eenumerator_multi: str, ecore_efeaturemap_single: str, ecore_efeaturemap_multi: str, ecore_efeaturemapentry_single: str, ecore_efeaturemapentry_multi: str, ecore_efloat_single: float, ecore_efloat_multi: float, ecore_efloatobject_single: str, ecore_efloatobject_multi: str, ecore_eint_single: int, ecore_eint_multi: int, ecore_eintegerobject_single: str, ecore_eintegerobject_multi: str, ecore_ejavaclass_single: str, ecore_ejavaclass_multi: str, ecore_ejavaobject_single: str, ecore_ejavaobject_multi: str, ecore_elong_single: str, ecore_elong_multi: str, ecore_elongobject_single: str, ecore_elongobject_multi: str, ecore_emap_single: str, ecore_emap_multi: str, ecore_eresource_single: str, ecore_eresource_multi: str, ecore_eelist_single: str, ecore_eresourceset_single: str, ecore_eresourceset_multi: str, ecore_eshort_single: str, ecore_eshort_multi: str, ecore_eshortobject_single: str, ecore_eshortobject_multi: str, ecore_estring_single: str, ecore_estring_multi: str, ecore_etreeiterator_single: str, ecore_etreeiterator_multi: str, ecore_einvocationtargetexception_single: str, ecore_einvocationtargetexception_multi: str):
        self.ocl_string_single = ocl_string_single
        self.ocl_string_multi = ocl_string_multi
        self.ocl_integer_single = ocl_integer_single
        self.ocl_integer_multi = ocl_integer_multi
        self.ocl_real_single = ocl_real_single
        self.ocl_real_multi = ocl_real_multi
        self.ocl_boolean_single = ocl_boolean_single
        self.ocl_boolean_multi = ocl_boolean_multi
        self.ecore_ebigdecimal_single = ecore_ebigdecimal_single
        self.ecore_ebigdecimal_multi = ecore_ebigdecimal_multi
        self.ecore_ebiginteger_single = ecore_ebiginteger_single
        self.ecore_ebiginteger_multi = ecore_ebiginteger_multi
        self.ecore_eboolean_single = ecore_eboolean_single
        self.ecore_eboolean_multi = ecore_eboolean_multi
        self.ecore_ebooleanobject_single = ecore_ebooleanobject_single
        self.ecore_ebooleanobject_multi = ecore_ebooleanobject_multi
        self.ecore_ebyte_single = ecore_ebyte_single
        self.ecore_ebyte_multi = ecore_ebyte_multi
        self.ecore_ebytearray_single = ecore_ebytearray_single
        self.ecore_ebytearray_multi = ecore_ebytearray_multi
        self.ecore_ebyteobject_single = ecore_ebyteobject_single
        self.ecore_ebyteobject_multi = ecore_ebyteobject_multi
        self.ecore_echar_single = ecore_echar_single
        self.ecore_echar_multi = ecore_echar_multi
        self.ecore_echaracterobject_single = ecore_echaracterobject_single
        self.ecore_echaracterobject_multi = ecore_echaracterobject_multi
        self.ecore_edate_single = ecore_edate_single
        self.ecore_edate_multi = ecore_edate_multi
        self.ecore_ediagnosticchain_single = ecore_ediagnosticchain_single
        self.ecore_ediagnosticchain_multi = ecore_ediagnosticchain_multi
        self.ecore_edouble_single = ecore_edouble_single
        self.ecore_edouble_multi = ecore_edouble_multi
        self.ecore_edoubleobject_single = ecore_edoubleobject_single
        self.ecore_edoubleobject_multi = ecore_edoubleobject_multi
        self.ecore_eelist_multi = ecore_eelist_multi
        self.ecore_eenumerator_single = ecore_eenumerator_single
        self.ecore_eenumerator_multi = ecore_eenumerator_multi
        self.ecore_efeaturemap_single = ecore_efeaturemap_single
        self.ecore_efeaturemap_multi = ecore_efeaturemap_multi
        self.ecore_efeaturemapentry_single = ecore_efeaturemapentry_single
        self.ecore_efeaturemapentry_multi = ecore_efeaturemapentry_multi
        self.ecore_efloat_single = ecore_efloat_single
        self.ecore_efloat_multi = ecore_efloat_multi
        self.ecore_efloatobject_single = ecore_efloatobject_single
        self.ecore_efloatobject_multi = ecore_efloatobject_multi
        self.ecore_eint_single = ecore_eint_single
        self.ecore_eint_multi = ecore_eint_multi
        self.ecore_eintegerobject_single = ecore_eintegerobject_single
        self.ecore_eintegerobject_multi = ecore_eintegerobject_multi
        self.ecore_ejavaclass_single = ecore_ejavaclass_single
        self.ecore_ejavaclass_multi = ecore_ejavaclass_multi
        self.ecore_ejavaobject_single = ecore_ejavaobject_single
        self.ecore_ejavaobject_multi = ecore_ejavaobject_multi
        self.ecore_elong_single = ecore_elong_single
        self.ecore_elong_multi = ecore_elong_multi
        self.ecore_elongobject_single = ecore_elongobject_single
        self.ecore_elongobject_multi = ecore_elongobject_multi
        self.ecore_emap_single = ecore_emap_single
        self.ecore_emap_multi = ecore_emap_multi
        self.ecore_eresource_single = ecore_eresource_single
        self.ecore_eresource_multi = ecore_eresource_multi
        self.ecore_eelist_single = ecore_eelist_single
        self.ecore_eresourceset_single = ecore_eresourceset_single
        self.ecore_eresourceset_multi = ecore_eresourceset_multi
        self.ecore_eshort_single = ecore_eshort_single
        self.ecore_eshort_multi = ecore_eshort_multi
        self.ecore_eshortobject_single = ecore_eshortobject_single
        self.ecore_eshortobject_multi = ecore_eshortobject_multi
        self.ecore_estring_single = ecore_estring_single
        self.ecore_estring_multi = ecore_estring_multi
        self.ecore_etreeiterator_single = ecore_etreeiterator_single
        self.ecore_etreeiterator_multi = ecore_etreeiterator_multi
        self.ecore_einvocationtargetexception_single = ecore_einvocationtargetexception_single
        self.ecore_einvocationtargetexception_multi = ecore_einvocationtargetexception_multi
        
    @property
    def ecore_efloatobject_multi(self) -> str:
        return self.__ecore_efloatobject_multi

    @ecore_efloatobject_multi.setter
    def ecore_efloatobject_multi(self, ecore_efloatobject_multi: str):
        self.__ecore_efloatobject_multi = ecore_efloatobject_multi

    @property
    def ecore_eshortobject_multi(self) -> str:
        return self.__ecore_eshortobject_multi

    @ecore_eshortobject_multi.setter
    def ecore_eshortobject_multi(self, ecore_eshortobject_multi: str):
        self.__ecore_eshortobject_multi = ecore_eshortobject_multi

    @property
    def ecore_ediagnosticchain_multi(self) -> str:
        return self.__ecore_ediagnosticchain_multi

    @ecore_ediagnosticchain_multi.setter
    def ecore_ediagnosticchain_multi(self, ecore_ediagnosticchain_multi: str):
        self.__ecore_ediagnosticchain_multi = ecore_ediagnosticchain_multi

    @property
    def ocl_string_single(self) -> str:
        return self.__ocl_string_single

    @ocl_string_single.setter
    def ocl_string_single(self, ocl_string_single: str):
        self.__ocl_string_single = ocl_string_single

    @property
    def ecore_edoubleobject_single(self) -> str:
        return self.__ecore_edoubleobject_single

    @ecore_edoubleobject_single.setter
    def ecore_edoubleobject_single(self, ecore_edoubleobject_single: str):
        self.__ecore_edoubleobject_single = ecore_edoubleobject_single

    @property
    def ecore_elongobject_multi(self) -> str:
        return self.__ecore_elongobject_multi

    @ecore_elongobject_multi.setter
    def ecore_elongobject_multi(self, ecore_elongobject_multi: str):
        self.__ecore_elongobject_multi = ecore_elongobject_multi

    @property
    def ecore_eshortobject_single(self) -> str:
        return self.__ecore_eshortobject_single

    @ecore_eshortobject_single.setter
    def ecore_eshortobject_single(self, ecore_eshortobject_single: str):
        self.__ecore_eshortobject_single = ecore_eshortobject_single

    @property
    def ecore_ebiginteger_multi(self) -> str:
        return self.__ecore_ebiginteger_multi

    @ecore_ebiginteger_multi.setter
    def ecore_ebiginteger_multi(self, ecore_ebiginteger_multi: str):
        self.__ecore_ebiginteger_multi = ecore_ebiginteger_multi

    @property
    def ecore_eint_multi(self) -> int:
        return self.__ecore_eint_multi

    @ecore_eint_multi.setter
    def ecore_eint_multi(self, ecore_eint_multi: int):
        self.__ecore_eint_multi = ecore_eint_multi

    @property
    def ecore_etreeiterator_multi(self) -> str:
        return self.__ecore_etreeiterator_multi

    @ecore_etreeiterator_multi.setter
    def ecore_etreeiterator_multi(self, ecore_etreeiterator_multi: str):
        self.__ecore_etreeiterator_multi = ecore_etreeiterator_multi

    @property
    def ecore_eintegerobject_multi(self) -> str:
        return self.__ecore_eintegerobject_multi

    @ecore_eintegerobject_multi.setter
    def ecore_eintegerobject_multi(self, ecore_eintegerobject_multi: str):
        self.__ecore_eintegerobject_multi = ecore_eintegerobject_multi

    @property
    def ecore_eenumerator_multi(self) -> str:
        return self.__ecore_eenumerator_multi

    @ecore_eenumerator_multi.setter
    def ecore_eenumerator_multi(self, ecore_eenumerator_multi: str):
        self.__ecore_eenumerator_multi = ecore_eenumerator_multi

    @property
    def ecore_eint_single(self) -> int:
        return self.__ecore_eint_single

    @ecore_eint_single.setter
    def ecore_eint_single(self, ecore_eint_single: int):
        self.__ecore_eint_single = ecore_eint_single

    @property
    def ocl_integer_multi(self) -> str:
        return self.__ocl_integer_multi

    @ocl_integer_multi.setter
    def ocl_integer_multi(self, ocl_integer_multi: str):
        self.__ocl_integer_multi = ocl_integer_multi

    @property
    def ecore_eboolean_single(self) -> bool:
        return self.__ecore_eboolean_single

    @ecore_eboolean_single.setter
    def ecore_eboolean_single(self, ecore_eboolean_single: bool):
        self.__ecore_eboolean_single = ecore_eboolean_single

    @property
    def ecore_ebooleanobject_multi(self) -> str:
        return self.__ecore_ebooleanobject_multi

    @ecore_ebooleanobject_multi.setter
    def ecore_ebooleanobject_multi(self, ecore_ebooleanobject_multi: str):
        self.__ecore_ebooleanobject_multi = ecore_ebooleanobject_multi

    @property
    def ecore_eresourceset_multi(self) -> str:
        return self.__ecore_eresourceset_multi

    @ecore_eresourceset_multi.setter
    def ecore_eresourceset_multi(self, ecore_eresourceset_multi: str):
        self.__ecore_eresourceset_multi = ecore_eresourceset_multi

    @property
    def ecore_ejavaobject_single(self) -> str:
        return self.__ecore_ejavaobject_single

    @ecore_ejavaobject_single.setter
    def ecore_ejavaobject_single(self, ecore_ejavaobject_single: str):
        self.__ecore_ejavaobject_single = ecore_ejavaobject_single

    @property
    def ecore_eresource_single(self) -> str:
        return self.__ecore_eresource_single

    @ecore_eresource_single.setter
    def ecore_eresource_single(self, ecore_eresource_single: str):
        self.__ecore_eresource_single = ecore_eresource_single

    @property
    def ecore_ejavaobject_multi(self) -> str:
        return self.__ecore_ejavaobject_multi

    @ecore_ejavaobject_multi.setter
    def ecore_ejavaobject_multi(self, ecore_ejavaobject_multi: str):
        self.__ecore_ejavaobject_multi = ecore_ejavaobject_multi

    @property
    def ecore_emap_single(self) -> str:
        return self.__ecore_emap_single

    @ecore_emap_single.setter
    def ecore_emap_single(self, ecore_emap_single: str):
        self.__ecore_emap_single = ecore_emap_single

    @property
    def ecore_edate_single(self) -> date:
        return self.__ecore_edate_single

    @ecore_edate_single.setter
    def ecore_edate_single(self, ecore_edate_single: date):
        self.__ecore_edate_single = ecore_edate_single

    @property
    def ecore_eshort_multi(self) -> str:
        return self.__ecore_eshort_multi

    @ecore_eshort_multi.setter
    def ecore_eshort_multi(self, ecore_eshort_multi: str):
        self.__ecore_eshort_multi = ecore_eshort_multi

    @property
    def ecore_edoubleobject_multi(self) -> str:
        return self.__ecore_edoubleobject_multi

    @ecore_edoubleobject_multi.setter
    def ecore_edoubleobject_multi(self, ecore_edoubleobject_multi: str):
        self.__ecore_edoubleobject_multi = ecore_edoubleobject_multi

    @property
    def ecore_ebyteobject_single(self) -> str:
        return self.__ecore_ebyteobject_single

    @ecore_ebyteobject_single.setter
    def ecore_ebyteobject_single(self, ecore_ebyteobject_single: str):
        self.__ecore_ebyteobject_single = ecore_ebyteobject_single

    @property
    def ecore_ebooleanobject_single(self) -> str:
        return self.__ecore_ebooleanobject_single

    @ecore_ebooleanobject_single.setter
    def ecore_ebooleanobject_single(self, ecore_ebooleanobject_single: str):
        self.__ecore_ebooleanobject_single = ecore_ebooleanobject_single

    @property
    def ecore_echaracterobject_multi(self) -> str:
        return self.__ecore_echaracterobject_multi

    @ecore_echaracterobject_multi.setter
    def ecore_echaracterobject_multi(self, ecore_echaracterobject_multi: str):
        self.__ecore_echaracterobject_multi = ecore_echaracterobject_multi

    @property
    def ecore_efloat_single(self) -> float:
        return self.__ecore_efloat_single

    @ecore_efloat_single.setter
    def ecore_efloat_single(self, ecore_efloat_single: float):
        self.__ecore_efloat_single = ecore_efloat_single

    @property
    def ecore_etreeiterator_single(self) -> str:
        return self.__ecore_etreeiterator_single

    @ecore_etreeiterator_single.setter
    def ecore_etreeiterator_single(self, ecore_etreeiterator_single: str):
        self.__ecore_etreeiterator_single = ecore_etreeiterator_single

    @property
    def ecore_ejavaclass_single(self) -> str:
        return self.__ecore_ejavaclass_single

    @ecore_ejavaclass_single.setter
    def ecore_ejavaclass_single(self, ecore_ejavaclass_single: str):
        self.__ecore_ejavaclass_single = ecore_ejavaclass_single

    @property
    def ecore_eresource_multi(self) -> str:
        return self.__ecore_eresource_multi

    @ecore_eresource_multi.setter
    def ecore_eresource_multi(self, ecore_eresource_multi: str):
        self.__ecore_eresource_multi = ecore_eresource_multi

    @property
    def ocl_boolean_single(self) -> str:
        return self.__ocl_boolean_single

    @ocl_boolean_single.setter
    def ocl_boolean_single(self, ocl_boolean_single: str):
        self.__ocl_boolean_single = ocl_boolean_single

    @property
    def ocl_real_single(self) -> str:
        return self.__ocl_real_single

    @ocl_real_single.setter
    def ocl_real_single(self, ocl_real_single: str):
        self.__ocl_real_single = ocl_real_single

    @property
    def ecore_edouble_multi(self) -> float:
        return self.__ecore_edouble_multi

    @ecore_edouble_multi.setter
    def ecore_edouble_multi(self, ecore_edouble_multi: float):
        self.__ecore_edouble_multi = ecore_edouble_multi

    @property
    def ecore_emap_multi(self) -> str:
        return self.__ecore_emap_multi

    @ecore_emap_multi.setter
    def ecore_emap_multi(self, ecore_emap_multi: str):
        self.__ecore_emap_multi = ecore_emap_multi

    @property
    def ecore_ebiginteger_single(self) -> str:
        return self.__ecore_ebiginteger_single

    @ecore_ebiginteger_single.setter
    def ecore_ebiginteger_single(self, ecore_ebiginteger_single: str):
        self.__ecore_ebiginteger_single = ecore_ebiginteger_single

    @property
    def ecore_efeaturemap_single(self) -> str:
        return self.__ecore_efeaturemap_single

    @ecore_efeaturemap_single.setter
    def ecore_efeaturemap_single(self, ecore_efeaturemap_single: str):
        self.__ecore_efeaturemap_single = ecore_efeaturemap_single

    @property
    def ecore_eboolean_multi(self) -> bool:
        return self.__ecore_eboolean_multi

    @ecore_eboolean_multi.setter
    def ecore_eboolean_multi(self, ecore_eboolean_multi: bool):
        self.__ecore_eboolean_multi = ecore_eboolean_multi

    @property
    def ecore_ebytearray_multi(self) -> str:
        return self.__ecore_ebytearray_multi

    @ecore_ebytearray_multi.setter
    def ecore_ebytearray_multi(self, ecore_ebytearray_multi: str):
        self.__ecore_ebytearray_multi = ecore_ebytearray_multi

    @property
    def ecore_eelist_multi(self) -> str:
        return self.__ecore_eelist_multi

    @ecore_eelist_multi.setter
    def ecore_eelist_multi(self, ecore_eelist_multi: str):
        self.__ecore_eelist_multi = ecore_eelist_multi

    @property
    def ecore_elong_single(self) -> str:
        return self.__ecore_elong_single

    @ecore_elong_single.setter
    def ecore_elong_single(self, ecore_elong_single: str):
        self.__ecore_elong_single = ecore_elong_single

    @property
    def ecore_elong_multi(self) -> str:
        return self.__ecore_elong_multi

    @ecore_elong_multi.setter
    def ecore_elong_multi(self, ecore_elong_multi: str):
        self.__ecore_elong_multi = ecore_elong_multi

    @property
    def ecore_efloat_multi(self) -> float:
        return self.__ecore_efloat_multi

    @ecore_efloat_multi.setter
    def ecore_efloat_multi(self, ecore_efloat_multi: float):
        self.__ecore_efloat_multi = ecore_efloat_multi

    @property
    def ecore_ebyteobject_multi(self) -> str:
        return self.__ecore_ebyteobject_multi

    @ecore_ebyteobject_multi.setter
    def ecore_ebyteobject_multi(self, ecore_ebyteobject_multi: str):
        self.__ecore_ebyteobject_multi = ecore_ebyteobject_multi

    @property
    def ecore_ediagnosticchain_single(self) -> str:
        return self.__ecore_ediagnosticchain_single

    @ecore_ediagnosticchain_single.setter
    def ecore_ediagnosticchain_single(self, ecore_ediagnosticchain_single: str):
        self.__ecore_ediagnosticchain_single = ecore_ediagnosticchain_single

    @property
    def ocl_boolean_multi(self) -> str:
        return self.__ocl_boolean_multi

    @ocl_boolean_multi.setter
    def ocl_boolean_multi(self, ocl_boolean_multi: str):
        self.__ocl_boolean_multi = ocl_boolean_multi

    @property
    def ecore_efloatobject_single(self) -> str:
        return self.__ecore_efloatobject_single

    @ecore_efloatobject_single.setter
    def ecore_efloatobject_single(self, ecore_efloatobject_single: str):
        self.__ecore_efloatobject_single = ecore_efloatobject_single

    @property
    def ecore_efeaturemapentry_single(self) -> str:
        return self.__ecore_efeaturemapentry_single

    @ecore_efeaturemapentry_single.setter
    def ecore_efeaturemapentry_single(self, ecore_efeaturemapentry_single: str):
        self.__ecore_efeaturemapentry_single = ecore_efeaturemapentry_single

    @property
    def ecore_einvocationtargetexception_multi(self) -> str:
        return self.__ecore_einvocationtargetexception_multi

    @ecore_einvocationtargetexception_multi.setter
    def ecore_einvocationtargetexception_multi(self, ecore_einvocationtargetexception_multi: str):
        self.__ecore_einvocationtargetexception_multi = ecore_einvocationtargetexception_multi

    @property
    def ecore_edouble_single(self) -> float:
        return self.__ecore_edouble_single

    @ecore_edouble_single.setter
    def ecore_edouble_single(self, ecore_edouble_single: float):
        self.__ecore_edouble_single = ecore_edouble_single

    @property
    def ocl_integer_single(self) -> str:
        return self.__ocl_integer_single

    @ocl_integer_single.setter
    def ocl_integer_single(self, ocl_integer_single: str):
        self.__ocl_integer_single = ocl_integer_single

    @property
    def ecore_efeaturemapentry_multi(self) -> str:
        return self.__ecore_efeaturemapentry_multi

    @ecore_efeaturemapentry_multi.setter
    def ecore_efeaturemapentry_multi(self, ecore_efeaturemapentry_multi: str):
        self.__ecore_efeaturemapentry_multi = ecore_efeaturemapentry_multi

    @property
    def ecore_eintegerobject_single(self) -> str:
        return self.__ecore_eintegerobject_single

    @ecore_eintegerobject_single.setter
    def ecore_eintegerobject_single(self, ecore_eintegerobject_single: str):
        self.__ecore_eintegerobject_single = ecore_eintegerobject_single

    @property
    def ecore_eenumerator_single(self) -> str:
        return self.__ecore_eenumerator_single

    @ecore_eenumerator_single.setter
    def ecore_eenumerator_single(self, ecore_eenumerator_single: str):
        self.__ecore_eenumerator_single = ecore_eenumerator_single

    @property
    def ecore_eresourceset_single(self) -> str:
        return self.__ecore_eresourceset_single

    @ecore_eresourceset_single.setter
    def ecore_eresourceset_single(self, ecore_eresourceset_single: str):
        self.__ecore_eresourceset_single = ecore_eresourceset_single

    @property
    def ecore_ebytearray_single(self) -> str:
        return self.__ecore_ebytearray_single

    @ecore_ebytearray_single.setter
    def ecore_ebytearray_single(self, ecore_ebytearray_single: str):
        self.__ecore_ebytearray_single = ecore_ebytearray_single

    @property
    def ecore_eshort_single(self) -> str:
        return self.__ecore_eshort_single

    @ecore_eshort_single.setter
    def ecore_eshort_single(self, ecore_eshort_single: str):
        self.__ecore_eshort_single = ecore_eshort_single

    @property
    def ocl_string_multi(self) -> str:
        return self.__ocl_string_multi

    @ocl_string_multi.setter
    def ocl_string_multi(self, ocl_string_multi: str):
        self.__ocl_string_multi = ocl_string_multi

    @property
    def ecore_ebyte_single(self) -> str:
        return self.__ecore_ebyte_single

    @ecore_ebyte_single.setter
    def ecore_ebyte_single(self, ecore_ebyte_single: str):
        self.__ecore_ebyte_single = ecore_ebyte_single

    @property
    def ecore_efeaturemap_multi(self) -> str:
        return self.__ecore_efeaturemap_multi

    @ecore_efeaturemap_multi.setter
    def ecore_efeaturemap_multi(self, ecore_efeaturemap_multi: str):
        self.__ecore_efeaturemap_multi = ecore_efeaturemap_multi

    @property
    def ecore_ebigdecimal_multi(self) -> str:
        return self.__ecore_ebigdecimal_multi

    @ecore_ebigdecimal_multi.setter
    def ecore_ebigdecimal_multi(self, ecore_ebigdecimal_multi: str):
        self.__ecore_ebigdecimal_multi = ecore_ebigdecimal_multi

    @property
    def ecore_ejavaclass_multi(self) -> str:
        return self.__ecore_ejavaclass_multi

    @ecore_ejavaclass_multi.setter
    def ecore_ejavaclass_multi(self, ecore_ejavaclass_multi: str):
        self.__ecore_ejavaclass_multi = ecore_ejavaclass_multi

    @property
    def ecore_estring_single(self) -> str:
        return self.__ecore_estring_single

    @ecore_estring_single.setter
    def ecore_estring_single(self, ecore_estring_single: str):
        self.__ecore_estring_single = ecore_estring_single

    @property
    def ecore_edate_multi(self) -> date:
        return self.__ecore_edate_multi

    @ecore_edate_multi.setter
    def ecore_edate_multi(self, ecore_edate_multi: date):
        self.__ecore_edate_multi = ecore_edate_multi

    @property
    def ocl_real_multi(self) -> str:
        return self.__ocl_real_multi

    @ocl_real_multi.setter
    def ocl_real_multi(self, ocl_real_multi: str):
        self.__ocl_real_multi = ocl_real_multi

    @property
    def ecore_echar_single(self) -> str:
        return self.__ecore_echar_single

    @ecore_echar_single.setter
    def ecore_echar_single(self, ecore_echar_single: str):
        self.__ecore_echar_single = ecore_echar_single

    @property
    def ecore_echar_multi(self) -> str:
        return self.__ecore_echar_multi

    @ecore_echar_multi.setter
    def ecore_echar_multi(self, ecore_echar_multi: str):
        self.__ecore_echar_multi = ecore_echar_multi

    @property
    def ecore_estring_multi(self) -> str:
        return self.__ecore_estring_multi

    @ecore_estring_multi.setter
    def ecore_estring_multi(self, ecore_estring_multi: str):
        self.__ecore_estring_multi = ecore_estring_multi

    @property
    def ecore_elongobject_single(self) -> str:
        return self.__ecore_elongobject_single

    @ecore_elongobject_single.setter
    def ecore_elongobject_single(self, ecore_elongobject_single: str):
        self.__ecore_elongobject_single = ecore_elongobject_single

    @property
    def ecore_einvocationtargetexception_single(self) -> str:
        return self.__ecore_einvocationtargetexception_single

    @ecore_einvocationtargetexception_single.setter
    def ecore_einvocationtargetexception_single(self, ecore_einvocationtargetexception_single: str):
        self.__ecore_einvocationtargetexception_single = ecore_einvocationtargetexception_single

    @property
    def ecore_ebyte_multi(self) -> str:
        return self.__ecore_ebyte_multi

    @ecore_ebyte_multi.setter
    def ecore_ebyte_multi(self, ecore_ebyte_multi: str):
        self.__ecore_ebyte_multi = ecore_ebyte_multi

    @property
    def ecore_eelist_single(self) -> str:
        return self.__ecore_eelist_single

    @ecore_eelist_single.setter
    def ecore_eelist_single(self, ecore_eelist_single: str):
        self.__ecore_eelist_single = ecore_eelist_single

    @property
    def ecore_ebigdecimal_single(self) -> str:
        return self.__ecore_ebigdecimal_single

    @ecore_ebigdecimal_single.setter
    def ecore_ebigdecimal_single(self, ecore_ebigdecimal_single: str):
        self.__ecore_ebigdecimal_single = ecore_ebigdecimal_single

    @property
    def ecore_echaracterobject_single(self) -> str:
        return self.__ecore_echaracterobject_single

    @ecore_echaracterobject_single.setter
    def ecore_echaracterobject_single(self, ecore_echaracterobject_single: str):
        self.__ecore_echaracterobject_single = ecore_echaracterobject_single

    def operation_efloatobject(self) -> str:
        # TODO: Implement operation_efloatobject method
        pass

    def operation_eintegerobject(self) -> str:
        # TODO: Implement operation_eintegerobject method
        pass

    def operation_etreeiterator(self) -> str:
        # TODO: Implement operation_etreeiterator method
        pass

    def operation_edoubleobject(self) -> str:
        # TODO: Implement operation_edoubleobject method
        pass

    def operation_ejavaclass(self) -> str:
        # TODO: Implement operation_ejavaclass method
        pass

    def operation_estring(self) -> str:
        # TODO: Implement operation_estring method
        pass

    def operation_eelist(self) -> str:
        # TODO: Implement operation_eelist method
        pass

    def operation_eenumerator(self) -> str:
        # TODO: Implement operation_eenumerator method
        pass

    def operation_echaracterobject(self) -> str:
        # TODO: Implement operation_echaracterobject method
        pass

    def operation_ediagnosticchain(self) -> str:
        # TODO: Implement operation_ediagnosticchain method
        pass

    def operation_ebyteobject(self) -> str:
        # TODO: Implement operation_ebyteobject method
        pass

    def operation_eresourceset(self) -> str:
        # TODO: Implement operation_eresourceset method
        pass

    def operation_ebigdecimal(self) -> str:
        # TODO: Implement operation_ebigdecimal method
        pass

    def operation_ebiginteger(self) -> str:
        # TODO: Implement operation_ebiginteger method
        pass

    def operation_efeaturemap(self) -> str:
        # TODO: Implement operation_efeaturemap method
        pass

    def operation_efeaturemapentry(self) -> str:
        # TODO: Implement operation_efeaturemapentry method
        pass

    def operation_ejavaobject(self) -> str:
        # TODO: Implement operation_ejavaobject method
        pass

    def operation_edouble(self) -> float:
        # TODO: Implement operation_edouble method
        pass

    def operation_einvocationtargetexception(self) -> str:
        # TODO: Implement operation_einvocationtargetexception method
        pass

    def operation_void(self):
        # TODO: Implement operation_void method
        pass

    def operation_eint(self) -> int:
        # TODO: Implement operation_eint method
        pass

    def operation_elongobject(self) -> str:
        # TODO: Implement operation_elongobject method
        pass

    def operation_eshort(self) -> str:
        # TODO: Implement operation_eshort method
        pass

    def operation_emap(self) -> str:
        # TODO: Implement operation_emap method
        pass

    def operation_eshortobject(self) -> str:
        # TODO: Implement operation_eshortobject method
        pass

    def operation_elong(self) -> str:
        # TODO: Implement operation_elong method
        pass

    def operation_efloat(self) -> float:
        # TODO: Implement operation_efloat method
        pass

    def operation_ebyte(self) -> str:
        # TODO: Implement operation_ebyte method
        pass

    def operation_ebytearray(self) -> str:
        # TODO: Implement operation_ebytearray method
        pass

    def operation_edate(self) -> date:
        # TODO: Implement operation_edate method
        pass

    def operation_eboolean(self) -> bool:
        # TODO: Implement operation_eboolean method
        pass

    def operation_echar(self) -> str:
        # TODO: Implement operation_echar method
        pass

    def operation_ebooleanobject(self) -> str:
        # TODO: Implement operation_ebooleanobject method
        pass

    def operation_eresource(self) -> str:
        # TODO: Implement operation_eresource method
        pass

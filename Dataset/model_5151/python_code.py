from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tests_C:

    pass
class ObjectUnionOf_A_B:

    pass
class tests_A(ObjectUnionOf_A_B):

    pass
class C:

    pass
class A:

    pass
class tests_ObjectIntersectionOf_A_C(C, A):

    pass
class tests_ObjectUnionOf_A_B(ABC):

    pass
class ObjectIntersectionOf_A_C:

    pass
class tests_B(ObjectIntersectionOf_A_C, ObjectUnionOf_A_B):

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TreeCS:

    pass
class kwcs_LeafCS(TreeCS):

    def __init__(self, val: int):
        self.val = val
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val


class kwcs_BinCS(TreeCS):

    pass
class kwcs_TreeCS(ABC):

    pass
class kwcs_TopCS:

    pass
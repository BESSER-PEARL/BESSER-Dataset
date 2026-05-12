from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Data_Basse:

    pass


class RestServices:

    def __init__(self, base_url: str):
        self.base_url = base_url
        
        pass
    @property
    def base_url(self):
        return self.__base_url
    @base_url.setter
    def base_url(self, base_url: str):
        self.__base_url = base_url



class Case_Index:

    def __init__(self, _scope_cases: str):
        self._scope_cases = _scope_cases
        
        pass
    @property
    def _scope_cases(self):
        return self.___scope_cases
    @_scope_cases.setter
    def _scope_cases(self, _scope_cases: str):
        self.___scope_cases = _scope_cases



class User:

    def __init__(self, _scope_user___PA_SA: str):
        self._scope_user___PA_SA = _scope_user___PA_SA
        
        pass
    @property
    def _scope_user___PA_SA(self):
        return self.___scope_user___PA_SA
    @_scope_user___PA_SA.setter
    def _scope_user___PA_SA(self, _scope_user___PA_SA: str):
        self.___scope_user___PA_SA = _scope_user___PA_SA



class Case_Edit_Component:

    pass


class Case_Details_Component:

    pass


class Case_Create_Component:

    pass


class Case_index_Component:

    pass


class Home__Component:

    pass

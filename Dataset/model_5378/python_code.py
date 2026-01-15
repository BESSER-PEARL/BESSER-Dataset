from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class types(Enum):
    text = "text"
    number = "number"
    button = "button"


############################################
# Definition of Classes
############################################

class html5_container(ABC):

    def __init__(self, class: str, html5_container: "html5_html" = None, html5_container8: set["html5_htmlElement"] = None, html5_container12: "html5_container" = None, html5_container10: set["html5_container"] = None):
        self.class = class
        self.html5_container = html5_container
        self.html5_container8 = html5_container8 if html5_container8 is not None else set()
        self.html5_container12 = html5_container12
        self.html5_container10 = html5_container10 if html5_container10 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def html5_container10(self):
        return self.__html5_container10

    @html5_container10.setter
    def html5_container10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container10", None)
        self.__html5_container10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html5_container12"):
                    opp_val = getattr(item, "html5_container12", None)
                    
                    if opp_val == self:
                        setattr(item, "html5_container12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html5_container12"):
                    opp_val = getattr(item, "html5_container12", None)
                    
                    setattr(item, "html5_container12", self)
                    

    @property
    def html5_container(self):
        return self.__html5_container

    @html5_container.setter
    def html5_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container", None)
        self.__html5_container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_html"):
                opp_val = getattr(old_value, "html5_html", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_html"):
                opp_val = getattr(value, "html5_html", None)
                if opp_val is None:
                    setattr(value, "html5_html", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html5_container12(self):
        return self.__html5_container12

    @html5_container12.setter
    def html5_container12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container12", None)
        self.__html5_container12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_container10"):
                opp_val = getattr(old_value, "html5_container10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_container10"):
                opp_val = getattr(value, "html5_container10", None)
                if opp_val is None:
                    setattr(value, "html5_container10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html5_container8(self):
        return self.__html5_container8

    @html5_container8.setter
    def html5_container8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container8", None)
        self.__html5_container8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html5_htmlElement9"):
                    opp_val = getattr(item, "html5_htmlElement9", None)
                    
                    if opp_val == self:
                        setattr(item, "html5_htmlElement9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html5_htmlElement9"):
                    opp_val = getattr(item, "html5_htmlElement9", None)
                    
                    setattr(item, "html5_htmlElement9", self)
                    

class html5_html:

    pass
class html5_legend:

    def __init__(self, class: str, valor: str, html5_legend: "html5_fieldset" = None):
        self.class = class
        self.valor = valor
        self.html5_legend = html5_legend
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def html5_legend(self):
        return self.__html5_legend

    @html5_legend.setter
    def html5_legend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_legend__html5_legend", None)
        self.__html5_legend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_fieldset"):
                opp_val = getattr(old_value, "html5_fieldset", None)
                if opp_val == self:
                    setattr(old_value, "html5_fieldset", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_fieldset"):
                opp_val = getattr(value, "html5_fieldset", None)
                setattr(value, "html5_fieldset", self)

class html5_option:

    pass
class html5_htmlElement(ABC):

    def __init__(self, class: str, html5_htmlElement: "html5_td" = None, html5_htmlElement9: "html5_container" = None):
        self.class = class
        self.html5_htmlElement = html5_htmlElement
        self.html5_htmlElement9 = html5_htmlElement9
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def html5_htmlElement(self):
        return self.__html5_htmlElement

    @html5_htmlElement.setter
    def html5_htmlElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_htmlElement__html5_htmlElement", None)
        self.__html5_htmlElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_td4"):
                opp_val = getattr(old_value, "html5_td4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_td4"):
                opp_val = getattr(value, "html5_td4", None)
                if opp_val is None:
                    setattr(value, "html5_td4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html5_htmlElement9(self):
        return self.__html5_htmlElement9

    @html5_htmlElement9.setter
    def html5_htmlElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_htmlElement__html5_htmlElement9", None)
        self.__html5_htmlElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_container8"):
                opp_val = getattr(old_value, "html5_container8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_container8"):
                opp_val = getattr(value, "html5_container8", None)
                if opp_val is None:
                    setattr(value, "html5_container8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html5_td:

    pass
class html5_tr:

    pass
class htmlElement:

    pass
class html5_select_multiple(htmlElement):

    def __init__(self, multiple: str, html5_select_multiple: "html5_option" = None):
        self.multiple = multiple
        self.html5_select_multiple = html5_select_multiple
        
    @property
    def multiple(self) -> str:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple

    @property
    def html5_select_multiple(self):
        return self.__html5_select_multiple

    @html5_select_multiple.setter
    def html5_select_multiple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_select_multiple__html5_select_multiple", None)
        self.__html5_select_multiple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_option"):
                opp_val = getattr(old_value, "html5_option", None)
                if opp_val == self:
                    setattr(old_value, "html5_option", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_option"):
                opp_val = getattr(value, "html5_option", None)
                setattr(value, "html5_option", self)

class html5_dialog(htmlElement):

    pass
class html5_button(htmlElement):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class html5_input(htmlElement):

    def __init__(self, value: str, disable: str, type: str):
        self.value = value
        self.disable = disable
        self.type = type
        
    @property
    def disable(self) -> str:
        return self.__disable

    @disable.setter
    def disable(self, disable: str):
        self.__disable = disable

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class html5_img(htmlElement):

    def __init__(self, src: str):
        self.src = src
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class html5_label(htmlElement):

    def __init__(self, valor: str):
        self.valor = valor
        
    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

class html5_table(htmlElement):

    pass
class container:

    pass
class html5_fieldset(container):

    pass
class html5_div(container):

    pass
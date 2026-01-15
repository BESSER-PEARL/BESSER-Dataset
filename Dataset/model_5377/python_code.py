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

class html5_htmlElement(ABC):

    def __init__(self, class: str, html5_htmlElement10: "html5_container" = None, html5_htmlElement: "html5_td" = None):
        self.class = class
        self.html5_htmlElement10 = html5_htmlElement10
        self.html5_htmlElement = html5_htmlElement
        
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
            if hasattr(old_value, "html5_td5"):
                opp_val = getattr(old_value, "html5_td5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_td5"):
                opp_val = getattr(value, "html5_td5", None)
                if opp_val is None:
                    setattr(value, "html5_td5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html5_htmlElement10(self):
        return self.__html5_htmlElement10

    @html5_htmlElement10.setter
    def html5_htmlElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_htmlElement__html5_htmlElement10", None)
        self.__html5_htmlElement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_container9"):
                opp_val = getattr(old_value, "html5_container9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_container9"):
                opp_val = getattr(value, "html5_container9", None)
                if opp_val is None:
                    setattr(value, "html5_container9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html5_container(ABC):

    def __init__(self, class: str, html5_container: "html5_html" = None, html5_container9: set["html5_htmlElement"] = None, html5_container13: "html5_container" = None, html5_container11: set["html5_container"] = None):
        self.class = class
        self.html5_container = html5_container
        self.html5_container9 = html5_container9 if html5_container9 is not None else set()
        self.html5_container13 = html5_container13
        self.html5_container11 = html5_container11 if html5_container11 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def html5_container11(self):
        return self.__html5_container11

    @html5_container11.setter
    def html5_container11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container11", None)
        self.__html5_container11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html5_container13"):
                    opp_val = getattr(item, "html5_container13", None)
                    
                    if opp_val == self:
                        setattr(item, "html5_container13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html5_container13"):
                    opp_val = getattr(item, "html5_container13", None)
                    
                    setattr(item, "html5_container13", self)
                    

    @property
    def html5_container9(self):
        return self.__html5_container9

    @html5_container9.setter
    def html5_container9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container9", None)
        self.__html5_container9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html5_htmlElement10"):
                    opp_val = getattr(item, "html5_htmlElement10", None)
                    
                    if opp_val == self:
                        setattr(item, "html5_htmlElement10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html5_htmlElement10"):
                    opp_val = getattr(item, "html5_htmlElement10", None)
                    
                    setattr(item, "html5_htmlElement10", self)
                    

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
    def html5_container13(self):
        return self.__html5_container13

    @html5_container13.setter
    def html5_container13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_container__html5_container13", None)
        self.__html5_container13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_container11"):
                opp_val = getattr(old_value, "html5_container11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_container11"):
                opp_val = getattr(value, "html5_container11", None)
                if opp_val is None:
                    setattr(value, "html5_container11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html5_html:

    pass
class html5_legend:

    def __init__(self, class: str, valor: str, html5_legend: "html5_fieldset" = None):
        self.class = class
        self.valor = valor
        self.html5_legend = html5_legend
        
    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

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
class html5_td:

    pass
class html5_tr:

    pass
class htmlElement:

    pass
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

    def __init__(self, valor: str, value: str):
        self.valor = valor
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

class html5_input(htmlElement):

    def __init__(self, type: str, value: str, disable: str):
        self.type = type
        self.value = value
        self.disable = disable
        
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

    @property
    def disable(self) -> str:
        return self.__disable

    @disable.setter
    def disable(self, disable: str):
        self.__disable = disable

class html5_dialog(htmlElement):

    pass
class html5_select(htmlElement):

    def __init__(self, multiple: str, size: str, html5_select: "html5_option" = None):
        self.multiple = multiple
        self.size = size
        self.html5_select = html5_select
        
    @property
    def multiple(self) -> str:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def html5_select(self):
        return self.__html5_select

    @html5_select.setter
    def html5_select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_select__html5_select", None)
        self.__html5_select = value
        
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

class html5_button(htmlElement):

    def __init__(self, type: str, value: str, action: str):
        self.type = type
        self.value = value
        self.action = action
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class html5_table(htmlElement):

    pass
class html5_Action:

    def __init__(self, codigo: str, html5_Action: "html5_div" = None):
        self.codigo = codigo
        self.html5_Action = html5_Action
        
    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def html5_Action(self):
        return self.__html5_Action

    @html5_Action.setter
    def html5_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_Action__html5_Action", None)
        self.__html5_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html5_div"):
                opp_val = getattr(old_value, "html5_div", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html5_div"):
                opp_val = getattr(value, "html5_div", None)
                if opp_val is None:
                    setattr(value, "html5_div", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class container:

    pass
class html5_fieldset(container):

    pass
class html5_div(container):

    def __init__(self, id: str, html5_div: set["html5_Action"] = None):
        self.id = id
        self.html5_div = html5_div if html5_div is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def html5_div(self):
        return self.__html5_div

    @html5_div.setter
    def html5_div(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html5_div__html5_div", None)
        self.__html5_div = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html5_Action"):
                    opp_val = getattr(item, "html5_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "html5_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html5_Action"):
                    opp_val = getattr(item, "html5_Action", None)
                    
                    setattr(item, "html5_Action", self)
                    

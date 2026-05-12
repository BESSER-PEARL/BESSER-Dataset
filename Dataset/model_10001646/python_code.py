from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class _UserType:

    def __init__(self, _userrole: str, _has12: set["_User"] = None):
        self._userrole = _userrole
        self._has12 = _has12 if _has12 is not None else set()
        
        pass
    @property
    def _userrole(self):
        return self.___userrole
    @_userrole.setter
    def _userrole(self, _userrole: str):
        self.___userrole = _userrole

    @property
    def _has12(self):
        return self.___has12
    @_has12.setter
    def _has12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__UserType___has12", None)
        self.___has12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_belongs_to13"):
                    opp_val = getattr(item, "_belongs_to13", None)
                    
                    if opp_val == self:
                        setattr(item, "_belongs_to13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_belongs_to13"):
                    opp_val = getattr(item, "_belongs_to13", None)
                    
                    setattr(item, "_belongs_to13", self)
                    



class _PaymentInfo:

    def __init__(self, _cardno: int, _cvv: int, _expirydate: date, _cardname: str, _userid: int, _belongs_to7: "_User" = None):
        self._cardno = _cardno
        self._cvv = _cvv
        self._expirydate = _expirydate
        self._cardname = _cardname
        self._userid = _userid
        self._belongs_to7 = _belongs_to7
        
        pass
    @property
    def _userid(self):
        return self.___userid
    @_userid.setter
    def _userid(self, _userid: int):
        self.___userid = _userid

    @property
    def _cardname(self):
        return self.___cardname
    @_cardname.setter
    def _cardname(self, _cardname: str):
        self.___cardname = _cardname

    @property
    def _expirydate(self):
        return self.___expirydate
    @_expirydate.setter
    def _expirydate(self, _expirydate: date):
        self.___expirydate = _expirydate

    @property
    def _cvv(self):
        return self.___cvv
    @_cvv.setter
    def _cvv(self, _cvv: int):
        self.___cvv = _cvv

    @property
    def _cardno(self):
        return self.___cardno
    @_cardno.setter
    def _cardno(self, _cardno: int):
        self.___cardno = _cardno

    @property
    def _belongs_to7(self):
        return self.___belongs_to7
    @_belongs_to7.setter
    def _belongs_to7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__PaymentInfo___belongs_to7", None)
        self.___belongs_to7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_has6"):
                opp_val = getattr(old_value, "_has6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_has6"):
                opp_val = getattr(value, "_has6", None)
                if opp_val is None:
                    setattr(value, "_has6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _OrderDetail:

    def __init__(self, _productid: int, _quantity: int, _orderdate: date, _totalamount: int, _userid: int, _contains9: set["_Product"] = None, _ordered_by11: "_User" = None):
        self._productid = _productid
        self._quantity = _quantity
        self._orderdate = _orderdate
        self._totalamount = _totalamount
        self._userid = _userid
        self._contains9 = _contains9 if _contains9 is not None else set()
        self._ordered_by11 = _ordered_by11
        
        pass
    @property
    def _productid(self):
        return self.___productid
    @_productid.setter
    def _productid(self, _productid: int):
        self.___productid = _productid

    @property
    def _orderdate(self):
        return self.___orderdate
    @_orderdate.setter
    def _orderdate(self, _orderdate: date):
        self.___orderdate = _orderdate

    @property
    def _userid(self):
        return self.___userid
    @_userid.setter
    def _userid(self, _userid: int):
        self.___userid = _userid

    @property
    def _totalamount(self):
        return self.___totalamount
    @_totalamount.setter
    def _totalamount(self, _totalamount: int):
        self.___totalamount = _totalamount

    @property
    def _quantity(self):
        return self.___quantity
    @_quantity.setter
    def _quantity(self, _quantity: int):
        self.___quantity = _quantity

    @property
    def _ordered_by11(self):
        return self.___ordered_by11
    @_ordered_by11.setter
    def _ordered_by11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__OrderDetail___ordered_by11", None)
        self.___ordered_by11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_orders10"):
                opp_val = getattr(old_value, "_orders10", None)
                if opp_val == self:
                    setattr(old_value, "_orders10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_orders10"):
                opp_val = getattr(value, "_orders10", None)
                setattr(value, "_orders10", self)

    @property
    def _contains9(self):
        return self.___contains9
    @_contains9.setter
    def _contains9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__OrderDetail___contains9", None)
        self.___contains9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_is_in8"):
                    opp_val = getattr(item, "_is_in8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_is_in8"):
                    opp_val = getattr(item, "_is_in8", None)
                    
                    if opp_val is None:
                        setattr(item, "_is_in8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _ProductType:

    def __init__(self, _type: str, _has_products4: set["_Product"] = None):
        self._type = _type
        self._has_products4 = _has_products4 if _has_products4 is not None else set()
        
        pass
    @property
    def _type(self):
        return self.___type
    @_type.setter
    def _type(self, _type: str):
        self.___type = _type

    @property
    def _has_products4(self):
        return self.___has_products4
    @_has_products4.setter
    def _has_products4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__ProductType___has_products4", None)
        self.___has_products4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_type_of5"):
                    opp_val = getattr(item, "_type_of5", None)
                    
                    if opp_val == self:
                        setattr(item, "_type_of5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_type_of5"):
                    opp_val = getattr(item, "_type_of5", None)
                    
                    setattr(item, "_type_of5", self)
                    



class _Product:

    def __init__(self, _name: str, _modelno: str, _description: str, _stock: int, _price: int, _producttypeid: int, _type_of5: "_ProductType" = None, _is_in8: set["_OrderDetail"] = None, _has_rating15: set["_ProductRating"] = None):
        self._name = _name
        self._modelno = _modelno
        self._description = _description
        self._stock = _stock
        self._price = _price
        self._producttypeid = _producttypeid
        self._type_of5 = _type_of5
        self._is_in8 = _is_in8 if _is_in8 is not None else set()
        self._has_rating15 = _has_rating15 if _has_rating15 is not None else set()
        
        pass
    @property
    def _producttypeid(self):
        return self.___producttypeid
    @_producttypeid.setter
    def _producttypeid(self, _producttypeid: int):
        self.___producttypeid = _producttypeid

    @property
    def _price(self):
        return self.___price
    @_price.setter
    def _price(self, _price: int):
        self.___price = _price

    @property
    def _name(self):
        return self.___name
    @_name.setter
    def _name(self, _name: str):
        self.___name = _name

    @property
    def _modelno(self):
        return self.___modelno
    @_modelno.setter
    def _modelno(self, _modelno: str):
        self.___modelno = _modelno

    @property
    def _description(self):
        return self.___description
    @_description.setter
    def _description(self, _description: str):
        self.___description = _description

    @property
    def _stock(self):
        return self.___stock
    @_stock.setter
    def _stock(self, _stock: int):
        self.___stock = _stock

    @property
    def _has_rating15(self):
        return self.___has_rating15
    @_has_rating15.setter
    def _has_rating15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__Product___has_rating15", None)
        self.___has_rating15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_is_for14"):
                    opp_val = getattr(item, "_is_for14", None)
                    
                    if opp_val == self:
                        setattr(item, "_is_for14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_is_for14"):
                    opp_val = getattr(item, "_is_for14", None)
                    
                    setattr(item, "_is_for14", self)
                    

    @property
    def _type_of5(self):
        return self.___type_of5
    @_type_of5.setter
    def _type_of5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__Product___type_of5", None)
        self.___type_of5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_has_products4"):
                opp_val = getattr(old_value, "_has_products4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_has_products4"):
                opp_val = getattr(value, "_has_products4", None)
                if opp_val is None:
                    setattr(value, "_has_products4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _is_in8(self):
        return self.___is_in8
    @_is_in8.setter
    def _is_in8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__Product___is_in8", None)
        self.___is_in8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_contains9"):
                    opp_val = getattr(item, "_contains9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_contains9"):
                    opp_val = getattr(item, "_contains9", None)
                    
                    if opp_val is None:
                        setattr(item, "_contains9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _ProductRating:

    def __init__(self, _rating: int, _userid: int, _productid: int, _rated_by2: set["_User"] = None, _is_for14: "_Product" = None):
        self._rating = _rating
        self._userid = _userid
        self._productid = _productid
        self._rated_by2 = _rated_by2 if _rated_by2 is not None else set()
        self._is_for14 = _is_for14
        
        pass
    @property
    def _userid(self):
        return self.___userid
    @_userid.setter
    def _userid(self, _userid: int):
        self.___userid = _userid

    @property
    def _rating(self):
        return self.___rating
    @_rating.setter
    def _rating(self, _rating: int):
        self.___rating = _rating

    @property
    def _productid(self):
        return self.___productid
    @_productid.setter
    def _productid(self, _productid: int):
        self.___productid = _productid

    @property
    def _rated_by2(self):
        return self.___rated_by2
    @_rated_by2.setter
    def _rated_by2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__ProductRating___rated_by2", None)
        self.___rated_by2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_rates3"):
                    opp_val = getattr(item, "_rates3", None)
                    
                    if opp_val == self:
                        setattr(item, "_rates3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_rates3"):
                    opp_val = getattr(item, "_rates3", None)
                    
                    setattr(item, "_rates3", self)
                    

    @property
    def _is_for14(self):
        return self.___is_for14
    @_is_for14.setter
    def _is_for14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__ProductRating___is_for14", None)
        self.___is_for14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_has_rating15"):
                opp_val = getattr(old_value, "_has_rating15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_has_rating15"):
                opp_val = getattr(value, "_has_rating15", None)
                if opp_val is None:
                    setattr(value, "_has_rating15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _User:

    def __init__(self, _username: str, _address: str, _phone: int, _email: str, _usertypeid: int, _logincredentialsid: int, _rates3: "_ProductRating" = None, _has6: set["_PaymentInfo"] = None, _orders10: "_OrderDetail" = None, _belongs_to13: "_UserType" = None, _logs_in_with1: "_LoginCredential" = None):
        self._username = _username
        self._address = _address
        self._phone = _phone
        self._email = _email
        self._usertypeid = _usertypeid
        self._logincredentialsid = _logincredentialsid
        self._rates3 = _rates3
        self._has6 = _has6 if _has6 is not None else set()
        self._orders10 = _orders10
        self._belongs_to13 = _belongs_to13
        self._logs_in_with1 = _logs_in_with1
        
        pass
    @property
    def _usertypeid(self):
        return self.___usertypeid
    @_usertypeid.setter
    def _usertypeid(self, _usertypeid: int):
        self.___usertypeid = _usertypeid

    @property
    def _phone(self):
        return self.___phone
    @_phone.setter
    def _phone(self, _phone: int):
        self.___phone = _phone

    @property
    def _logincredentialsid(self):
        return self.___logincredentialsid
    @_logincredentialsid.setter
    def _logincredentialsid(self, _logincredentialsid: int):
        self.___logincredentialsid = _logincredentialsid

    @property
    def _email(self):
        return self.___email
    @_email.setter
    def _email(self, _email: str):
        self.___email = _email

    @property
    def _username(self):
        return self.___username
    @_username.setter
    def _username(self, _username: str):
        self.___username = _username

    @property
    def _address(self):
        return self.___address
    @_address.setter
    def _address(self, _address: str):
        self.___address = _address

    @property
    def _belongs_to13(self):
        return self.___belongs_to13
    @_belongs_to13.setter
    def _belongs_to13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__User___belongs_to13", None)
        self.___belongs_to13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_has12"):
                opp_val = getattr(old_value, "_has12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_has12"):
                opp_val = getattr(value, "_has12", None)
                if opp_val is None:
                    setattr(value, "_has12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _orders10(self):
        return self.___orders10
    @_orders10.setter
    def _orders10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__User___orders10", None)
        self.___orders10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_ordered_by11"):
                opp_val = getattr(old_value, "_ordered_by11", None)
                if opp_val == self:
                    setattr(old_value, "_ordered_by11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_ordered_by11"):
                opp_val = getattr(value, "_ordered_by11", None)
                setattr(value, "_ordered_by11", self)

    @property
    def _logs_in_with1(self):
        return self.___logs_in_with1
    @_logs_in_with1.setter
    def _logs_in_with1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__User___logs_in_with1", None)
        self.___logs_in_with1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_for0"):
                opp_val = getattr(old_value, "_for0", None)
                if opp_val == self:
                    setattr(old_value, "_for0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_for0"):
                opp_val = getattr(value, "_for0", None)
                setattr(value, "_for0", self)

    @property
    def _has6(self):
        return self.___has6
    @_has6.setter
    def _has6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__User___has6", None)
        self.___has6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_belongs_to7"):
                    opp_val = getattr(item, "_belongs_to7", None)
                    
                    if opp_val == self:
                        setattr(item, "_belongs_to7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_belongs_to7"):
                    opp_val = getattr(item, "_belongs_to7", None)
                    
                    setattr(item, "_belongs_to7", self)
                    

    @property
    def _rates3(self):
        return self.___rates3
    @_rates3.setter
    def _rates3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__User___rates3", None)
        self.___rates3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_rated_by2"):
                opp_val = getattr(old_value, "_rated_by2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_rated_by2"):
                opp_val = getattr(value, "_rated_by2", None)
                if opp_val is None:
                    setattr(value, "_rated_by2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _LoginCredential:

    def __init__(self, _loginid: str, _password: str, _for0: "_User" = None):
        self._loginid = _loginid
        self._password = _password
        self._for0 = _for0
        
        pass
    @property
    def _loginid(self):
        return self.___loginid
    @_loginid.setter
    def _loginid(self, _loginid: str):
        self.___loginid = _loginid

    @property
    def _password(self):
        return self.___password
    @_password.setter
    def _password(self, _password: str):
        self.___password = _password

    @property
    def _for0(self):
        return self.___for0
    @_for0.setter
    def _for0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__LoginCredential___for0", None)
        self.___for0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_logs_in_with1"):
                opp_val = getattr(old_value, "_logs_in_with1", None)
                if opp_val == self:
                    setattr(old_value, "_logs_in_with1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_logs_in_with1"):
                opp_val = getattr(value, "_logs_in_with1", None)
                setattr(value, "_logs_in_with1", self)


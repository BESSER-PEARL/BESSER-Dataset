from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class _PaymentInfo:

    def __init__(self, _cardno: int, _cvv: int, _expirydate: date, _cardname: str, _userid: int, paymentId: int, _OrderDetail10: "_OrderDetail" = None):
        self._cardno = _cardno
        self._cvv = _cvv
        self._expirydate = _expirydate
        self._cardname = _cardname
        self._userid = _userid
        self.paymentId = paymentId
        self._OrderDetail10 = _OrderDetail10
        
        pass
    @property
    def _cardno(self):
        return self.___cardno
    @_cardno.setter
    def _cardno(self, _cardno: int):
        self.___cardno = _cardno

    @property
    def _cardname(self):
        return self.___cardname
    @_cardname.setter
    def _cardname(self, _cardname: str):
        self.___cardname = _cardname

    @property
    def _userid(self):
        return self.___userid
    @_userid.setter
    def _userid(self, _userid: int):
        self.___userid = _userid

    @property
    def paymentId(self):
        return self.__paymentId
    @paymentId.setter
    def paymentId(self, paymentId: int):
        self.__paymentId = paymentId

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
    def _OrderDetail10(self):
        return self.___OrderDetail10
    @_OrderDetail10.setter
    def _OrderDetail10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__PaymentInfo___OrderDetail10", None)
        self.___OrderDetail10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_PaymentInfo11"):
                opp_val = getattr(old_value, "_PaymentInfo11", None)
                if opp_val == self:
                    setattr(old_value, "_PaymentInfo11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_PaymentInfo11"):
                opp_val = getattr(value, "_PaymentInfo11", None)
                setattr(value, "_PaymentInfo11", self)



class _OrderDetail:

    def __init__(self, OrderId: int, paymentInfoId: int, _productid: int, _quantity: int, _orderdate: date, _totalamount: int, _userid: int, _contains7: set["_Fee"] = None, receives9: "Card" = None, _PaymentInfo11: "_PaymentInfo" = None):
        self.OrderId = OrderId
        self.paymentInfoId = paymentInfoId
        self._productid = _productid
        self._quantity = _quantity
        self._orderdate = _orderdate
        self._totalamount = _totalamount
        self._userid = _userid
        self._contains7 = _contains7 if _contains7 is not None else set()
        self.receives9 = receives9
        self._PaymentInfo11 = _PaymentInfo11
        
        pass
    @property
    def paymentInfoId(self):
        return self.__paymentInfoId
    @paymentInfoId.setter
    def paymentInfoId(self, paymentInfoId: int):
        self.__paymentInfoId = paymentInfoId

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: int):
        self.__OrderId = OrderId

    @property
    def _quantity(self):
        return self.___quantity
    @_quantity.setter
    def _quantity(self, _quantity: int):
        self.___quantity = _quantity

    @property
    def _totalamount(self):
        return self.___totalamount
    @_totalamount.setter
    def _totalamount(self, _totalamount: int):
        self.___totalamount = _totalamount

    @property
    def _productid(self):
        return self.___productid
    @_productid.setter
    def _productid(self, _productid: int):
        self.___productid = _productid

    @property
    def _userid(self):
        return self.___userid
    @_userid.setter
    def _userid(self, _userid: int):
        self.___userid = _userid

    @property
    def _orderdate(self):
        return self.___orderdate
    @_orderdate.setter
    def _orderdate(self, _orderdate: date):
        self.___orderdate = _orderdate

    @property
    def _PaymentInfo11(self):
        return self.___PaymentInfo11
    @_PaymentInfo11.setter
    def _PaymentInfo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__OrderDetail___PaymentInfo11", None)
        self.___PaymentInfo11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_OrderDetail10"):
                opp_val = getattr(old_value, "_OrderDetail10", None)
                if opp_val == self:
                    setattr(old_value, "_OrderDetail10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_OrderDetail10"):
                opp_val = getattr(value, "_OrderDetail10", None)
                setattr(value, "_OrderDetail10", self)

    @property
    def _contains7(self):
        return self.___contains7
    @_contains7.setter
    def _contains7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__OrderDetail___contains7", None)
        self.___contains7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_is_in6"):
                    opp_val = getattr(item, "_is_in6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_is_in6"):
                    opp_val = getattr(item, "_is_in6", None)
                    
                    if opp_val is None:
                        setattr(item, "_is_in6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def receives9(self):
        return self.__receives9
    @receives9.setter
    def receives9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__OrderDetail__receives9", None)
        self.__receives9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_orders8"):
                opp_val = getattr(old_value, "_orders8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_orders8"):
                opp_val = getattr(value, "_orders8", None)
                if opp_val is None:
                    setattr(value, "_orders8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _TransactionType:

    def __init__(self, _type: str, _has_products4: set["_Fee"] = None, farmer13: "Card" = None):
        self._type = _type
        self._has_products4 = _has_products4 if _has_products4 is not None else set()
        self.farmer13 = farmer13
        
        pass
    @property
    def _type(self):
        return self.___type
    @_type.setter
    def _type(self, _type: str):
        self.___type = _type

    @property
    def farmer13(self):
        return self.__farmer13
    @farmer13.setter
    def farmer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__TransactionType__farmer13", None)
        self.__farmer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_Add_Product_Type12"):
                opp_val = getattr(old_value, "_Add_Product_Type12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_Add_Product_Type12"):
                opp_val = getattr(value, "_Add_Product_Type12", None)
                if opp_val is None:
                    setattr(value, "_Add_Product_Type12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _has_products4(self):
        return self.___has_products4
    @_has_products4.setter
    def _has_products4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__TransactionType___has_products4", None)
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
                    



class _Fee:

    def __init__(self, _name: str, _description: str, _stock: int, _price: int, _producttypeid: int, _type_of5: "_TransactionType" = None, _is_in6: set["_OrderDetail"] = None):
        self._name = _name
        self._description = _description
        self._stock = _stock
        self._price = _price
        self._producttypeid = _producttypeid
        self._type_of5 = _type_of5
        self._is_in6 = _is_in6 if _is_in6 is not None else set()
        
        pass
    @property
    def _description(self):
        return self.___description
    @_description.setter
    def _description(self, _description: str):
        self.___description = _description

    @property
    def _name(self):
        return self.___name
    @_name.setter
    def _name(self, _name: str):
        self.___name = _name

    @property
    def _stock(self):
        return self.___stock
    @_stock.setter
    def _stock(self, _stock: int):
        self.___stock = _stock

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
    def _is_in6(self):
        return self.___is_in6
    @_is_in6.setter
    def _is_in6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__Fee___is_in6", None)
        self.___is_in6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_contains7"):
                    opp_val = getattr(item, "_contains7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_contains7"):
                    opp_val = getattr(item, "_contains7", None)
                    
                    if opp_val is None:
                        setattr(item, "_contains7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def _type_of5(self):
        return self.___type_of5
    @_type_of5.setter
    def _type_of5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__Fee___type_of5", None)
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



class Transaction:

    def __init__(self, shipmentNumber: int, orderId: int, _Delivers2: "Card" = None):
        self.shipmentNumber = shipmentNumber
        self.orderId = orderId
        self._Delivers2 = _Delivers2
        
        pass
    @property
    def shipmentNumber(self):
        return self.__shipmentNumber
    @shipmentNumber.setter
    def shipmentNumber(self, shipmentNumber: int):
        self.__shipmentNumber = shipmentNumber

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def _Delivers2(self):
        return self.___Delivers2
    @_Delivers2.setter
    def _Delivers2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transaction___Delivers2", None)
        self.___Delivers2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_ships3"):
                opp_val = getattr(old_value, "_ships3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_ships3"):
                opp_val = getattr(value, "_ships3", None)
                if opp_val is None:
                    setattr(value, "_ships3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Card:

    def __init__(self, _username: str, _address: str, _phone: int, _email: str, _usertypeid: int, _logincredentialsid: int, _logs_in_with1: "_LoginCredential" = None, _ships3: set["Transaction"] = None, _orders8: set["_OrderDetail"] = None, _Add_Product_Type12: set["_TransactionType"] = None):
        self._username = _username
        self._address = _address
        self._phone = _phone
        self._email = _email
        self._usertypeid = _usertypeid
        self._logincredentialsid = _logincredentialsid
        self._logs_in_with1 = _logs_in_with1
        self._ships3 = _ships3 if _ships3 is not None else set()
        self._orders8 = _orders8 if _orders8 is not None else set()
        self._Add_Product_Type12 = _Add_Product_Type12 if _Add_Product_Type12 is not None else set()
        
        pass
    @property
    def _usertypeid(self):
        return self.___usertypeid
    @_usertypeid.setter
    def _usertypeid(self, _usertypeid: int):
        self.___usertypeid = _usertypeid

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
    def _phone(self):
        return self.___phone
    @_phone.setter
    def _phone(self, _phone: int):
        self.___phone = _phone

    @property
    def _orders8(self):
        return self.___orders8
    @_orders8.setter
    def _orders8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card___orders8", None)
        self.___orders8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receives9"):
                    opp_val = getattr(item, "receives9", None)
                    
                    if opp_val == self:
                        setattr(item, "receives9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receives9"):
                    opp_val = getattr(item, "receives9", None)
                    
                    setattr(item, "receives9", self)
                    

    @property
    def _Add_Product_Type12(self):
        return self.___Add_Product_Type12
    @_Add_Product_Type12.setter
    def _Add_Product_Type12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card___Add_Product_Type12", None)
        self.___Add_Product_Type12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farmer13"):
                    opp_val = getattr(item, "farmer13", None)
                    
                    if opp_val == self:
                        setattr(item, "farmer13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farmer13"):
                    opp_val = getattr(item, "farmer13", None)
                    
                    setattr(item, "farmer13", self)
                    

    @property
    def _ships3(self):
        return self.___ships3
    @_ships3.setter
    def _ships3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card___ships3", None)
        self.___ships3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_Delivers2"):
                    opp_val = getattr(item, "_Delivers2", None)
                    
                    if opp_val == self:
                        setattr(item, "_Delivers2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_Delivers2"):
                    opp_val = getattr(item, "_Delivers2", None)
                    
                    setattr(item, "_Delivers2", self)
                    

    @property
    def _logs_in_with1(self):
        return self.___logs_in_with1
    @_logs_in_with1.setter
    def _logs_in_with1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card___logs_in_with1", None)
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



class _LoginCredential:

    def __init__(self, _loginid: str, _password: str, _for0: "Card" = None):
        self._loginid = _loginid
        self._password = _password
        self._for0 = _for0
        
        pass
    @property
    def _password(self):
        return self.___password
    @_password.setter
    def _password(self, _password: str):
        self.___password = _password

    @property
    def _loginid(self):
        return self.___loginid
    @_loginid.setter
    def _loginid(self, _loginid: str):
        self.___loginid = _loginid

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


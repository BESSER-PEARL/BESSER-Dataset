from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Khoa:

    def __init__(self, makhoa: str, tenkhoa: str, co8: set["BoMon"] = None):
        self.makhoa = makhoa
        self.tenkhoa = tenkhoa
        self.co8 = co8 if co8 is not None else set()
        
        pass
    @property
    def makhoa(self):
        return self.__makhoa
    @makhoa.setter
    def makhoa(self, makhoa: str):
        self.__makhoa = makhoa

    @property
    def tenkhoa(self):
        return self.__tenkhoa
    @tenkhoa.setter
    def tenkhoa(self, tenkhoa: str):
        self.__tenkhoa = tenkhoa

    @property
    def co8(self):
        return self.__co8
    @co8.setter
    def co8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Khoa__co8", None)
        self.__co8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thus9"):
                    opp_val = getattr(item, "thus9", None)
                    
                    if opp_val == self:
                        setattr(item, "thus9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thus9"):
                    opp_val = getattr(item, "thus9", None)
                    
                    setattr(item, "thus9", self)
                    



class BoMon:

    def __init__(self, mabomon: str, tenbomon: str, thus9: "Khoa" = None):
        self.mabomon = mabomon
        self.tenbomon = tenbomon
        self.thus9 = thus9
        
        pass
    @property
    def mabomon(self):
        return self.__mabomon
    @mabomon.setter
    def mabomon(self, mabomon: str):
        self.__mabomon = mabomon

    @property
    def tenbomon(self):
        return self.__tenbomon
    @tenbomon.setter
    def tenbomon(self, tenbomon: str):
        self.__tenbomon = tenbomon

    @property
    def thus9(self):
        return self.__thus9
    @thus9.setter
    def thus9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoMon__thus9", None)
        self.__thus9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co8"):
                opp_val = getattr(old_value, "co8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co8"):
                opp_val = getattr(value, "co8", None)
                if opp_val is None:
                    setattr(value, "co8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, account11: "Account" = None, payment13: "Payment" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.account11 = account11
        self.payment13 = payment13
        
        pass
    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def account11(self):
        return self.__account11
    @account11.setter
    def account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account11", None)
        self.__account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                if opp_val is None:
                    setattr(value, "order10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment13(self):
        return self.__payment13
    @payment13.setter
    def payment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment13", None)
        self.__payment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order12"):
                opp_val = getattr(old_value, "order12", None)
                if opp_val == self:
                    setattr(old_value, "order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order12"):
                opp_val = getattr(value, "order12", None)
                setattr(value, "order12", self)



class SinhVien:

    def __init__(self, MSSV: str, lop: str, nganhhoc: str, bomon: str, customer2: "Customer" = None):
        self.MSSV = MSSV
        self.lop = lop
        self.nganhhoc = nganhhoc
        self.bomon = bomon
        self.customer2 = customer2
        
        pass
    @property
    def lop(self):
        return self.__lop
    @lop.setter
    def lop(self, lop: str):
        self.__lop = lop

    @property
    def nganhhoc(self):
        return self.__nganhhoc
    @nganhhoc.setter
    def nganhhoc(self, nganhhoc: str):
        self.__nganhhoc = nganhhoc

    @property
    def bomon(self):
        return self.__bomon
    @bomon.setter
    def bomon(self, bomon: str):
        self.__bomon = bomon

    @property
    def MSSV(self):
        return self.__MSSV
    @MSSV.setter
    def MSSV(self, MSSV: str):
        self.__MSSV = MSSV

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SinhVien__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser3"):
                opp_val = getattr(old_value, "webUser3", None)
                if opp_val == self:
                    setattr(old_value, "webUser3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser3"):
                opp_val = getattr(value, "webUser3", None)
                setattr(value, "webUser3", self)



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, p0: set["Payment"] = None, customer5: "Customer" = None, cart6: "ConNguoi" = None, order10: set["Order"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.p0 = p0 if p0 is not None else set()
        self.customer5 = customer5
        self.cart6 = cart6
        self.order10 = order10 if order10 is not None else set()
        
        pass
    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order10", None)
        self.__order10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    if opp_val == self:
                        setattr(item, "account11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    setattr(item, "account11", self)
                    

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__p0", None)
        self.__p0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    if opp_val == self:
                        setattr(item, "acc1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    setattr(item, "acc1", self)
                    

    @property
    def cart6(self):
        return self.__cart6
    @cart6.setter
    def cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart6", None)
        self.__cart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)



class ConNguoi:

    def __init__(self, CMND: str, hoten: str, ngaysinh: date, gioitinh: bool, diachi: str, account7: "Account" = None):
        self.CMND = CMND
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.diachi = diachi
        self.account7 = account7
        
        pass
    @property
    def ngaysinh(self):
        return self.__ngaysinh
    @ngaysinh.setter
    def ngaysinh(self, ngaysinh: date):
        self.__ngaysinh = ngaysinh

    @property
    def diachi(self):
        return self.__diachi
    @diachi.setter
    def diachi(self, diachi: str):
        self.__diachi = diachi

    @property
    def hoten(self):
        return self.__hoten
    @hoten.setter
    def hoten(self, hoten: str):
        self.__hoten = hoten

    @property
    def CMND(self):
        return self.__CMND
    @CMND.setter
    def CMND(self, CMND: str):
        self.__CMND = CMND

    @property
    def gioitinh(self):
        return self.__gioitinh
    @gioitinh.setter
    def gioitinh(self, gioitinh: bool):
        self.__gioitinh = gioitinh

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConNguoi__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart6"):
                opp_val = getattr(old_value, "cart6", None)
                if opp_val == self:
                    setattr(old_value, "cart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart6"):
                opp_val = getattr(value, "cart6", None)
                setattr(value, "cart6", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, acc1: "Account" = None, order12: "Order" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.acc1 = acc1
        self.order12 = order12
        
        pass
    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment13"):
                opp_val = getattr(old_value, "payment13", None)
                if opp_val == self:
                    setattr(old_value, "payment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment13"):
                opp_val = getattr(value, "payment13", None)
                setattr(value, "payment13", self)

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc1", None)
        self.__acc1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p0"):
                opp_val = getattr(old_value, "p0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p0"):
                opp_val = getattr(value, "p0", None)
                if opp_val is None:
                    setattr(value, "p0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer:

    def __init__(self, phone: str, email: str, address: str, webUser3: "SinhVien" = None, account4: "Account" = None):
        self.phone = phone
        self.email = email
        self.address = address
        self.webUser3 = webUser3
        self.account4 = account4
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)


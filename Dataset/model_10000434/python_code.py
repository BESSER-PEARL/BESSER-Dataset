from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class admin:

    def __init__(self, id: int, username: str, password: str, user14: "user" = None):
        self.id = id
        self.username = username
        self.password = password
        self.user14 = user14
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def user14(self):
        return self.__user14
    @user14.setter
    def user14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__user14", None)
        self.__user14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin15"):
                opp_val = getattr(old_value, "admin15", None)
                if opp_val == self:
                    setattr(old_value, "admin15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin15"):
                opp_val = getattr(value, "admin15", None)
                setattr(value, "admin15", self)



class orderdetail:

    def __init__(self, order_id: int, barang_id: int, total: str, order23: "order" = None, barang26: set["barang"] = None):
        self.order_id = order_id
        self.barang_id = barang_id
        self.total = total
        self.order23 = order23
        self.barang26 = barang26 if barang26 is not None else set()
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: int):
        self.__order_id = order_id

    @property
    def barang_id(self):
        return self.__barang_id
    @barang_id.setter
    def barang_id(self, barang_id: int):
        self.__barang_id = barang_id

    @property
    def barang26(self):
        return self.__barang26
    @barang26.setter
    def barang26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_orderdetail__barang26", None)
        self.__barang26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderdetail27"):
                    opp_val = getattr(item, "orderdetail27", None)
                    
                    if opp_val == self:
                        setattr(item, "orderdetail27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderdetail27"):
                    opp_val = getattr(item, "orderdetail27", None)
                    
                    setattr(item, "orderdetail27", self)
                    

    @property
    def order23(self):
        return self.__order23
    @order23.setter
    def order23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_orderdetail__order23", None)
        self.__order23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderdetail22"):
                opp_val = getattr(old_value, "orderdetail22", None)
                if opp_val == self:
                    setattr(old_value, "orderdetail22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderdetail22"):
                opp_val = getattr(value, "orderdetail22", None)
                setattr(value, "orderdetail22", self)



class order:

    def __init__(self, order_id: int, id_user: int, dateorder: str, status: str, user20: "user" = None, orderdetail22: "orderdetail" = None):
        self.order_id = order_id
        self.id_user = id_user
        self.dateorder = dateorder
        self.status = status
        self.user20 = user20
        self.orderdetail22 = orderdetail22
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def dateorder(self):
        return self.__dateorder
    @dateorder.setter
    def dateorder(self, dateorder: str):
        self.__dateorder = dateorder

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: int):
        self.__order_id = order_id

    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def user20(self):
        return self.__user20
    @user20.setter
    def user20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__user20", None)
        self.__user20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order21"):
                opp_val = getattr(old_value, "order21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order21"):
                opp_val = getattr(value, "order21", None)
                if opp_val is None:
                    setattr(value, "order21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderdetail22(self):
        return self.__orderdetail22
    @orderdetail22.setter
    def orderdetail22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__orderdetail22", None)
        self.__orderdetail22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order23"):
                opp_val = getattr(old_value, "order23", None)
                if opp_val == self:
                    setattr(old_value, "order23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order23"):
                opp_val = getattr(value, "order23", None)
                setattr(value, "order23", self)



class role:

    def __init__(self, id: int, nama_role: str, deskripsi_role: str, user12: "user" = None):
        self.id = id
        self.nama_role = nama_role
        self.deskripsi_role = deskripsi_role
        self.user12 = user12
        
        pass
    @property
    def deskripsi_role(self):
        return self.__deskripsi_role
    @deskripsi_role.setter
    def deskripsi_role(self, deskripsi_role: str):
        self.__deskripsi_role = deskripsi_role

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nama_role(self):
        return self.__nama_role
    @nama_role.setter
    def nama_role(self, nama_role: str):
        self.__nama_role = nama_role

    @property
    def user12(self):
        return self.__user12
    @user12.setter
    def user12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_role__user12", None)
        self.__user12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role13"):
                opp_val = getattr(old_value, "role13", None)
                if opp_val == self:
                    setattr(old_value, "role13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role13"):
                opp_val = getattr(value, "role13", None)
                setattr(value, "role13", self)



class pembeli1:

    def __init__(self, id: int, id_role: int, name: str, address: str, mail: str, username: str, password: str, user16: "user" = None):
        self.id = id
        self.id_role = id_role
        self.name = name
        self.address = address
        self.mail = mail
        self.username = username
        self.password = password
        self.user16 = user16
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id_role(self):
        return self.__id_role
    @id_role.setter
    def id_role(self, id_role: int):
        self.__id_role = id_role

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def user16(self):
        return self.__user16
    @user16.setter
    def user16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pembeli1__user16", None)
        self.__user16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pembeli17"):
                opp_val = getattr(old_value, "pembeli17", None)
                if opp_val == self:
                    setattr(old_value, "pembeli17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pembeli17"):
                opp_val = getattr(value, "pembeli17", None)
                setattr(value, "pembeli17", self)



class vendor:

    def __init__(self, id: int, id_role: int, name: str, address: str, mail: str, username: str, password: str, shippinginfo: str, bussinessname: str, bank: str, user18: "user" = None):
        self.id = id
        self.id_role = id_role
        self.name = name
        self.address = address
        self.mail = mail
        self.username = username
        self.password = password
        self.shippinginfo = shippinginfo
        self.bussinessname = bussinessname
        self.bank = bank
        self.user18 = user18
        
        pass
    @property
    def bank(self):
        return self.__bank
    @bank.setter
    def bank(self, bank: str):
        self.__bank = bank

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id_role(self):
        return self.__id_role
    @id_role.setter
    def id_role(self, id_role: int):
        self.__id_role = id_role

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def bussinessname(self):
        return self.__bussinessname
    @bussinessname.setter
    def bussinessname(self, bussinessname: str):
        self.__bussinessname = bussinessname

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def user18(self):
        return self.__user18
    @user18.setter
    def user18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vendor__user18", None)
        self.__user18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vendor19"):
                opp_val = getattr(old_value, "vendor19", None)
                if opp_val == self:
                    setattr(old_value, "vendor19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vendor19"):
                opp_val = getattr(value, "vendor19", None)
                setattr(value, "vendor19", self)



class user:

    def __init__(self, id_user: int, id_role: int, id_order: int, role13: "role" = None, admin15: "admin" = None, pembeli17: "pembeli1" = None, vendor19: "vendor" = None, order21: set["order"] = None):
        self.id_user = id_user
        self.id_role = id_role
        self.id_order = id_order
        self.role13 = role13
        self.admin15 = admin15
        self.pembeli17 = pembeli17
        self.vendor19 = vendor19
        self.order21 = order21 if order21 is not None else set()
        
        pass
    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def id_role(self):
        return self.__id_role
    @id_role.setter
    def id_role(self, id_role: int):
        self.__id_role = id_role

    @property
    def id_order(self):
        return self.__id_order
    @id_order.setter
    def id_order(self, id_order: int):
        self.__id_order = id_order

    @property
    def role13(self):
        return self.__role13
    @role13.setter
    def role13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__role13", None)
        self.__role13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user12"):
                opp_val = getattr(old_value, "user12", None)
                if opp_val == self:
                    setattr(old_value, "user12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user12"):
                opp_val = getattr(value, "user12", None)
                setattr(value, "user12", self)

    @property
    def pembeli17(self):
        return self.__pembeli17
    @pembeli17.setter
    def pembeli17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__pembeli17", None)
        self.__pembeli17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user16"):
                opp_val = getattr(old_value, "user16", None)
                if opp_val == self:
                    setattr(old_value, "user16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user16"):
                opp_val = getattr(value, "user16", None)
                setattr(value, "user16", self)

    @property
    def admin15(self):
        return self.__admin15
    @admin15.setter
    def admin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__admin15", None)
        self.__admin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user14"):
                opp_val = getattr(old_value, "user14", None)
                if opp_val == self:
                    setattr(old_value, "user14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user14"):
                opp_val = getattr(value, "user14", None)
                setattr(value, "user14", self)

    @property
    def vendor19(self):
        return self.__vendor19
    @vendor19.setter
    def vendor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__vendor19", None)
        self.__vendor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user18"):
                opp_val = getattr(old_value, "user18", None)
                if opp_val == self:
                    setattr(old_value, "user18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user18"):
                opp_val = getattr(value, "user18", None)
                setattr(value, "user18", self)

    @property
    def order21(self):
        return self.__order21
    @order21.setter
    def order21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__order21", None)
        self.__order21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user20"):
                    opp_val = getattr(item, "user20", None)
                    
                    if opp_val == self:
                        setattr(item, "user20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user20"):
                    opp_val = getattr(item, "user20", None)
                    
                    setattr(item, "user20", self)
                    



class kategori:

    def __init__(self, id: int, nama_kategori: str, deskripsi_kategori: str, barang25: "barang" = None):
        self.id = id
        self.nama_kategori = nama_kategori
        self.deskripsi_kategori = deskripsi_kategori
        self.barang25 = barang25
        
        pass
    @property
    def deskripsi_kategori(self):
        return self.__deskripsi_kategori
    @deskripsi_kategori.setter
    def deskripsi_kategori(self, deskripsi_kategori: str):
        self.__deskripsi_kategori = deskripsi_kategori

    @property
    def nama_kategori(self):
        return self.__nama_kategori
    @nama_kategori.setter
    def nama_kategori(self, nama_kategori: str):
        self.__nama_kategori = nama_kategori

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def barang25(self):
        return self.__barang25
    @barang25.setter
    def barang25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kategori__barang25", None)
        self.__barang25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kategori24"):
                opp_val = getattr(old_value, "kategori24", None)
                if opp_val == self:
                    setattr(old_value, "kategori24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kategori24"):
                opp_val = getattr(value, "kategori24", None)
                setattr(value, "kategori24", self)



class barang:

    def __init__(self, id: int, id_kategori: int, nama_barang: str, deskripsi_barang: str, harga_barang: int, kategori24: "kategori" = None, orderdetail27: "orderdetail" = None):
        self.id = id
        self.id_kategori = id_kategori
        self.nama_barang = nama_barang
        self.deskripsi_barang = deskripsi_barang
        self.harga_barang = harga_barang
        self.kategori24 = kategori24
        self.orderdetail27 = orderdetail27
        
        pass
    @property
    def id_kategori(self):
        return self.__id_kategori
    @id_kategori.setter
    def id_kategori(self, id_kategori: int):
        self.__id_kategori = id_kategori

    @property
    def deskripsi_barang(self):
        return self.__deskripsi_barang
    @deskripsi_barang.setter
    def deskripsi_barang(self, deskripsi_barang: str):
        self.__deskripsi_barang = deskripsi_barang

    @property
    def nama_barang(self):
        return self.__nama_barang
    @nama_barang.setter
    def nama_barang(self, nama_barang: str):
        self.__nama_barang = nama_barang

    @property
    def harga_barang(self):
        return self.__harga_barang
    @harga_barang.setter
    def harga_barang(self, harga_barang: int):
        self.__harga_barang = harga_barang

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def kategori24(self):
        return self.__kategori24
    @kategori24.setter
    def kategori24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_barang__kategori24", None)
        self.__kategori24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "barang25"):
                opp_val = getattr(old_value, "barang25", None)
                if opp_val == self:
                    setattr(old_value, "barang25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "barang25"):
                opp_val = getattr(value, "barang25", None)
                setattr(value, "barang25", self)

    @property
    def orderdetail27(self):
        return self.__orderdetail27
    @orderdetail27.setter
    def orderdetail27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_barang__orderdetail27", None)
        self.__orderdetail27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "barang26"):
                opp_val = getattr(old_value, "barang26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "barang26"):
                opp_val = getattr(value, "barang26", None)
                if opp_val is None:
                    setattr(value, "barang26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class penjual:

    def __init__(self, id: str, name: str, address: str, mail: str, username: str, password: str, shippinginfo: str, bussinessname: str, bank: str, user6: "User" = None):
        self.id = id
        self.name = name
        self.address = address
        self.mail = mail
        self.username = username
        self.password = password
        self.shippinginfo = shippinginfo
        self.bussinessname = bussinessname
        self.bank = bank
        self.user6 = user6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bussinessname(self):
        return self.__bussinessname
    @bussinessname.setter
    def bussinessname(self, bussinessname: str):
        self.__bussinessname = bussinessname

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bank(self):
        return self.__bank
    @bank.setter
    def bank(self, bank: str):
        self.__bank = bank

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_penjual__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "penjual7"):
                opp_val = getattr(old_value, "penjual7", None)
                if opp_val == self:
                    setattr(old_value, "penjual7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "penjual7"):
                opp_val = getattr(value, "penjual7", None)
                setattr(value, "penjual7", self)



class Kategori:

    def __init__(self, idkategori: str, productid: str, name: str, desc: str, produk11: "Produk" = None):
        self.idkategori = idkategori
        self.productid = productid
        self.name = name
        self.desc = desc
        self.produk11 = produk11
        
        pass
    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: str):
        self.__productid = productid

    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idkategori(self):
        return self.__idkategori
    @idkategori.setter
    def idkategori(self, idkategori: str):
        self.__idkategori = idkategori

    @property
    def produk11(self):
        return self.__produk11
    @produk11.setter
    def produk11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kategori__produk11", None)
        self.__produk11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kategori10"):
                opp_val = getattr(old_value, "kategori10", None)
                if opp_val == self:
                    setattr(old_value, "kategori10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kategori10"):
                opp_val = getattr(value, "kategori10", None)
                setattr(value, "kategori10", self)



class Produk:

    def __init__(self, productid: str, idkategori: str, name: str, desc: str, price: str, orderdetail8: "Orderdetail" = None, kategori10: "Kategori" = None):
        self.productid = productid
        self.idkategori = idkategori
        self.name = name
        self.desc = desc
        self.price = price
        self.orderdetail8 = orderdetail8
        self.kategori10 = kategori10
        
        pass
    @property
    def idkategori(self):
        return self.__idkategori
    @idkategori.setter
    def idkategori(self, idkategori: str):
        self.__idkategori = idkategori

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: str):
        self.__productid = productid

    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def orderdetail8(self):
        return self.__orderdetail8
    @orderdetail8.setter
    def orderdetail8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produk__orderdetail8", None)
        self.__orderdetail8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "produk9"):
                opp_val = getattr(old_value, "produk9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "produk9"):
                opp_val = getattr(value, "produk9", None)
                if opp_val is None:
                    setattr(value, "produk9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kategori10(self):
        return self.__kategori10
    @kategori10.setter
    def kategori10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produk__kategori10", None)
        self.__kategori10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "produk11"):
                opp_val = getattr(old_value, "produk11", None)
                if opp_val == self:
                    setattr(old_value, "produk11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "produk11"):
                opp_val = getattr(value, "produk11", None)
                setattr(value, "produk11", self)



class Shippinginfo:

    def __init__(self, region: str, total: str, shippingid: str, type: str, cost: str, order0: "Order" = None):
        self.region = region
        self.total = total
        self.shippingid = shippingid
        self.type = type
        self.cost = cost
        self.order0 = order0
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: str):
        self.__shippingid = shippingid

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shippinginfo__order0", None)
        self.__order0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shippinginfo1"):
                opp_val = getattr(old_value, "shippinginfo1", None)
                if opp_val == self:
                    setattr(old_value, "shippinginfo1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shippinginfo1"):
                opp_val = getattr(value, "shippinginfo1", None)
                setattr(value, "shippinginfo1", self)



class Orderdetail:

    def __init__(self, orderid: str, productid: str, quantity: str, cost: str, total: str, order2: "Order" = None, produk9: set["Produk"] = None):
        self.orderid = orderid
        self.productid = productid
        self.quantity = quantity
        self.cost = cost
        self.total = total
        self.order2 = order2
        self.produk9 = produk9 if produk9 is not None else set()
        
        pass
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: str):
        self.__productid = productid

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def orderid(self):
        return self.__orderid
    @orderid.setter
    def orderid(self, orderid: str):
        self.__orderid = orderid

    @property
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orderdetail__order2", None)
        self.__order2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderdetail3"):
                opp_val = getattr(old_value, "orderdetail3", None)
                if opp_val == self:
                    setattr(old_value, "orderdetail3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderdetail3"):
                opp_val = getattr(value, "orderdetail3", None)
                setattr(value, "orderdetail3", self)

    @property
    def produk9(self):
        return self.__produk9
    @produk9.setter
    def produk9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orderdetail__produk9", None)
        self.__produk9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderdetail8"):
                    opp_val = getattr(item, "orderdetail8", None)
                    
                    if opp_val == self:
                        setattr(item, "orderdetail8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderdetail8"):
                    opp_val = getattr(item, "orderdetail8", None)
                    
                    setattr(item, "orderdetail8", self)
                    



class Order:

    def __init__(self, orderid: str, shippingid: str, customerid: str, dateorder: str, datedeliver: str, status: str, shippinginfo1: "Shippinginfo" = None, orderdetail3: "Orderdetail" = None):
        self.orderid = orderid
        self.shippingid = shippingid
        self.customerid = customerid
        self.dateorder = dateorder
        self.datedeliver = datedeliver
        self.status = status
        self.shippinginfo1 = shippinginfo1
        self.orderdetail3 = orderdetail3
        
        pass
    @property
    def orderid(self):
        return self.__orderid
    @orderid.setter
    def orderid(self, orderid: str):
        self.__orderid = orderid

    @property
    def datedeliver(self):
        return self.__datedeliver
    @datedeliver.setter
    def datedeliver(self, datedeliver: str):
        self.__datedeliver = datedeliver

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def customerid(self):
        return self.__customerid
    @customerid.setter
    def customerid(self, customerid: str):
        self.__customerid = customerid

    @property
    def shippingid(self):
        return self.__shippingid
    @shippingid.setter
    def shippingid(self, shippingid: str):
        self.__shippingid = shippingid

    @property
    def dateorder(self):
        return self.__dateorder
    @dateorder.setter
    def dateorder(self, dateorder: str):
        self.__dateorder = dateorder

    @property
    def shippinginfo1(self):
        return self.__shippinginfo1
    @shippinginfo1.setter
    def shippinginfo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shippinginfo1", None)
        self.__shippinginfo1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order0"):
                opp_val = getattr(old_value, "order0", None)
                if opp_val == self:
                    setattr(old_value, "order0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order0"):
                opp_val = getattr(value, "order0", None)
                setattr(value, "order0", self)

    @property
    def orderdetail3(self):
        return self.__orderdetail3
    @orderdetail3.setter
    def orderdetail3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderdetail3", None)
        self.__orderdetail3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if opp_val == self:
                    setattr(old_value, "order2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                setattr(value, "order2", self)



class Cart:

    def __init__(self, cartid: str, productid: str, quantity: str, date: str, customer4: "pembeli" = None):
        self.cartid = cartid
        self.productid = productid
        self.quantity = quantity
        self.date = date
        self.customer4 = customer4
        
        pass
    @property
    def productid(self):
        return self.__productid
    @productid.setter
    def productid(self, productid: str):
        self.__productid = productid

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def cartid(self):
        return self.__cartid
    @cartid.setter
    def cartid(self, cartid: str):
        self.__cartid = cartid

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__customer4", None)
        self.__customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart5"):
                opp_val = getattr(old_value, "cart5", None)
                if opp_val == self:
                    setattr(old_value, "cart5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart5"):
                opp_val = getattr(value, "cart5", None)
                setattr(value, "cart5", self)



class pembeli:

    def __init__(self, id: str, name: str, address: str, mail: str, username: str, password: str, shippinginfo: str, cart5: "Cart" = None):
        self.id = id
        self.name = name
        self.address = address
        self.mail = mail
        self.username = username
        self.password = password
        self.shippinginfo = shippinginfo
        self.cart5 = cart5
        
        pass
    @property
    def shippinginfo(self):
        return self.__shippinginfo
    @shippinginfo.setter
    def shippinginfo(self, shippinginfo: str):
        self.__shippinginfo = shippinginfo

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def cart5(self):
        return self.__cart5
    @cart5.setter
    def cart5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pembeli__cart5", None)
        self.__cart5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)



class Admin:

    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail



class User:

    def __init__(self, id: str, password: str, penjual7: "penjual" = None):
        self.id = id
        self.password = password
        self.penjual7 = penjual7
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def penjual7(self):
        return self.__penjual7
    @penjual7.setter
    def penjual7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__penjual7", None)
        self.__penjual7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user6"):
                opp_val = getattr(old_value, "user6", None)
                if opp_val == self:
                    setattr(old_value, "user6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user6"):
                opp_val = getattr(value, "user6", None)
                setattr(value, "user6", self)


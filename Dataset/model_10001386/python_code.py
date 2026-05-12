from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Laporan_data_sortir_UseCase:

    pass


class Laporan_data_barang_keluar_UseCase:

    pass


class Laporan_data_barang_masuk_UseCase:

    pass


class Laporan_data_Pembelian_UseCase:

    pass


class Laporan_data_supplier_UseCase:

    pass


class Laporan_ready_stock_UseCase:

    pass


class Direktur_utama_Actor:

    pass


class Direktur_pemasaran_Actor:

    pass


class Work_order_UseCase:

    pass


class Cek_ketersediaan_barang_UseCase:

    pass


class Input_data_sortir_UseCase:

    pass


class Input_data_pembeli_UseCase:

    pass


class Input_data_supplier_UseCase:

    pass


class Input_data_barang_keluar_UseCase:

    pass


class Input_data_barang_masuk_UseCase:

    pass


class Admin_Gudang_Actor:

    pass


class Laporan_work_order_UseCase:

    pass





class Barang:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2


from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Mengedit_Data_Tumbuh_Tumbuhan_Herbal_UseCase:

    pass


class Menghapus_Data_Tumbuh_Tumbuhan_Herbal_UseCase:

    pass


class Menambah_Data_Tumbuh_Tumbuhan_Herbal_UseCase:

    pass


class Mengedit_Profil_Dan_Data_Website_UseCase:

    pass


class Obat__Produk_Jadinya__UseCase:

    pass


class Gambar_Tumbuhan_Herbalnya_UseCase:

    pass


class Kelas_Ordo_Tumbuhan_Herbal_UseCase:

    pass


class Cara_Pengolahannya_UseCase:

    pass


class Khasiat_tumbuhan_Herbalnya_UseCase:

    pass


class Asal_Tumbuhan_Herbalnya_UseCase:

    pass


class Jenis_Tumbuhan_Herbalnya_UseCase:

    pass


class Nama_Latinnya_UseCase:

    pass


class Nama_Tumbuhannya_UseCase:

    pass


class Fitur_Data_Informasi_Tumbuh_Tumbuhan_Herbal_UseCase:

    pass


class Fitur_Galeri_Foto_Tumbuhan_Herbal_UseCase:

    pass


class Fitur_Pencarian_Tumbuhan_Herbal_UseCase:

    pass


class Fitur_Sosial_Media_Sharing_UseCase:

    pass


class Fitur_Kolom_Diskusi_UseCase:

    pass


class Fitur_Pencarian_Berdasarkan_Kategori_Penyakit_UseCase:

    pass


class Fitur_Fitur_Pada_Website_UseCase:

    pass


class Halaman_Utama_Website_UseCase:

    pass


class Website_Informasi_Tumbuhan_Herbal_UseCase:

    pass


class Admin_Website_Actor:

    pass


class User__Pengunjung__Actor:

    pass


class Forum_diskusi_UseCase:

    pass


class Fitur_Pencarian_berdsarkan_penyakit_UseCase:

    pass


class Obat__Produk_jadi__UseCase:

    pass


class Gambar_tumbuhan_herbalnya_UseCase:

    pass


class Cara_pengolahannya_UseCase:

    pass


class Dosisnya_UseCase:

    pass


class Khasiatnya_apa_UseCase:

    pass


class Kelas_Ordo_tumbuhan_herbal_UseCase:

    pass


class Asal_daerah_tumbuhan_herbal_UseCase:

    pass


class Jenis_tumbuhan_herbal_UseCase:

    pass


class Nama_latinnya_UseCase:

    pass


class Nama_Tumbuh_Tumbuhan_Herbal_UseCase:

    pass


class Menu_Halaman_Utama_WebsiteTumbuhan_Herbal_UseCase:

    pass


class Browsing_Situs_UseCase:

    pass


class Mengedit_data_website_UseCase:

    pass


class Menghapus_data_website_UseCase:

    pass


class Menambah_membuat_data_website_UseCase:

    pass


class Kelola_data_website_UseCase:

    pass


class Admin_Actor:

    pass


class Situs_Browsing_UseCase:

    pass


class Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase:

    pass


class Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase:

    pass





class Dosisnya_UseCase1:

    pass


class Nama_Tumbuh_Tumbuhan_Herbal:

    def __init__(self, attribute: Nama_latinnya_UseCase, attribute2: Jenis_tumbuhan_herbal_UseCase, attribute3: Asal_daerah_tumbuhan_herbal_UseCase, attribute4: Kelas_Ordo_tumbuhan_herbal_UseCase, attribute5: Khasiatnya_apa_UseCase, attribute6: Dosisnya_UseCase, attribute7: Cara_pengolahannya_UseCase, attribute8: Gambar_tumbuhan_herbalnya_UseCase, attribute9: Obat__Produk_jadi__UseCase):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.attribute5 = attribute5
        self.attribute6 = attribute6
        self.attribute7 = attribute7
        self.attribute8 = attribute8
        self.attribute9 = attribute9
        
        pass
    @property
    def attribute8(self):
        return self.__attribute8
    @attribute8.setter
    def attribute8(self, attribute8: Gambar_tumbuhan_herbalnya_UseCase):
        self.__attribute8 = attribute8

    @property
    def attribute7(self):
        return self.__attribute7
    @attribute7.setter
    def attribute7(self, attribute7: Cara_pengolahannya_UseCase):
        self.__attribute7 = attribute7

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: Nama_latinnya_UseCase):
        self.__attribute = attribute

    @property
    def attribute4(self):
        return self.__attribute4
    @attribute4.setter
    def attribute4(self, attribute4: Kelas_Ordo_tumbuhan_herbal_UseCase):
        self.__attribute4 = attribute4

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: Jenis_tumbuhan_herbal_UseCase):
        self.__attribute2 = attribute2

    @property
    def attribute6(self):
        return self.__attribute6
    @attribute6.setter
    def attribute6(self, attribute6: Dosisnya_UseCase):
        self.__attribute6 = attribute6

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: Asal_daerah_tumbuhan_herbal_UseCase):
        self.__attribute3 = attribute3

    @property
    def attribute5(self):
        return self.__attribute5
    @attribute5.setter
    def attribute5(self, attribute5: Khasiatnya_apa_UseCase):
        self.__attribute5 = attribute5

    @property
    def attribute9(self):
        return self.__attribute9
    @attribute9.setter
    def attribute9(self, attribute9: Obat__Produk_jadi__UseCase):
        self.__attribute9 = attribute9



class Menu_Halaman_Website:

    def __init__(self, attribute: Forum_diskusi_UseCase, attribute2: Fitur_Pencarian_berdsarkan_penyakit_UseCase):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: Fitur_Pencarian_berdsarkan_penyakit_UseCase):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: Forum_diskusi_UseCase):
        self.__attribute = attribute



class Pengelola_Website:

    def __init__(self, attribute: Kelola_data_website_UseCase, attribute2: Menambah_membuat_data_website_UseCase, attribute3: Menghapus_data_website_UseCase, attribute4: Mengedit_data_website_UseCase):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: Menambah_membuat_data_website_UseCase):
        self.__attribute2 = attribute2

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: Menghapus_data_website_UseCase):
        self.__attribute3 = attribute3

    @property
    def attribute4(self):
        return self.__attribute4
    @attribute4.setter
    def attribute4(self, attribute4: Mengedit_data_website_UseCase):
        self.__attribute4 = attribute4

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: Kelola_data_website_UseCase):
        self.__attribute = attribute



class Browsing_Website:

    def __init__(self, attribute: User__Pengunjung__Actor):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: User__Pengunjung__Actor):
        self.__attribute = attribute



class Login_Website:

    def __init__(self, attribute: Admin_Actor):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: Admin_Actor):
        self.__attribute = attribute



class User__Pengunjung__Actor1:

    pass

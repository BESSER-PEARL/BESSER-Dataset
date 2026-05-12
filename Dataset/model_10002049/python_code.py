from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Dosen_Actor:

    pass





class Menghapus_Nilai_external:

    pass


class Menghapus_Mahasiswa_external:

    pass


class Mengubah_Data_Nilai_external:

    pass


class Mengubah_Data_Mahasiswa_external:

    pass


class Menambah_Data_Nilai_external:

    pass


class Menambah_Data_Mahasiswa_external:

    pass


class Melihat_Data_Nilai_external:

    pass


class Melihat_Data_Mahasiswa_external:

    pass


class Activity_Input_Mahasiswa:

    pass


class Activity_Data_Nilai:

    pass


class Activity_Data_Mahasiswa:

    pass


class view_control_Nilai:

    pass


class view_control_Mahasiswa:

    pass


class DAO_Nilai:

    def __init__(self, uts: str, uas: str, tugas: str, namaMk: str, nilai20: "view_control_Nilai" = None, nilai25: "Nilai" = None):
        self.uts = uts
        self.uas = uas
        self.tugas = tugas
        self.namaMk = namaMk
        self.nilai20 = nilai20
        self.nilai25 = nilai25
        
        pass
    @property
    def uas(self):
        return self.__uas
    @uas.setter
    def uas(self, uas: str):
        self.__uas = uas

    @property
    def tugas(self):
        return self.__tugas
    @tugas.setter
    def tugas(self, tugas: str):
        self.__tugas = tugas

    @property
    def uts(self):
        return self.__uts
    @uts.setter
    def uts(self, uts: str):
        self.__uts = uts

    @property
    def namaMk(self):
        return self.__namaMk
    @namaMk.setter
    def namaMk(self, namaMk: str):
        self.__namaMk = namaMk

    @property
    def nilai20(self):
        return self.__nilai20
    @nilai20.setter
    def nilai20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAO_Nilai__nilai20", None)
        self.__nilai20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nilai21"):
                opp_val = getattr(old_value, "nilai21", None)
                if opp_val == self:
                    setattr(old_value, "nilai21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nilai21"):
                opp_val = getattr(value, "nilai21", None)
                setattr(value, "nilai21", self)

    @property
    def nilai25(self):
        return self.__nilai25
    @nilai25.setter
    def nilai25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAO_Nilai__nilai25", None)
        self.__nilai25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nilai24"):
                opp_val = getattr(old_value, "nilai24", None)
                if opp_val == self:
                    setattr(old_value, "nilai24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nilai24"):
                opp_val = getattr(value, "nilai24", None)
                setattr(value, "nilai24", self)



class DAO_Mahasiswa:

    def __init__(self, nim: str, nama: str, tahun: str, mahasiswa18: "view_control_Mahasiswa" = None, mahasiswa23: "Mahasiswa" = None):
        self.nim = nim
        self.nama = nama
        self.tahun = tahun
        self.mahasiswa18 = mahasiswa18
        self.mahasiswa23 = mahasiswa23
        
        pass
    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def nim(self):
        return self.__nim
    @nim.setter
    def nim(self, nim: str):
        self.__nim = nim

    @property
    def tahun(self):
        return self.__tahun
    @tahun.setter
    def tahun(self, tahun: str):
        self.__tahun = tahun

    @property
    def mahasiswa18(self):
        return self.__mahasiswa18
    @mahasiswa18.setter
    def mahasiswa18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAO_Mahasiswa__mahasiswa18", None)
        self.__mahasiswa18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mahasiswa19"):
                opp_val = getattr(old_value, "mahasiswa19", None)
                if opp_val == self:
                    setattr(old_value, "mahasiswa19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mahasiswa19"):
                opp_val = getattr(value, "mahasiswa19", None)
                setattr(value, "mahasiswa19", self)

    @property
    def mahasiswa23(self):
        return self.__mahasiswa23
    @mahasiswa23.setter
    def mahasiswa23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAO_Mahasiswa__mahasiswa23", None)
        self.__mahasiswa23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mahasiswa22"):
                opp_val = getattr(old_value, "mahasiswa22", None)
                if opp_val == self:
                    setattr(old_value, "mahasiswa22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mahasiswa22"):
                opp_val = getattr(value, "mahasiswa22", None)
                setattr(value, "mahasiswa22", self)



class Aplikasi_Input_Nilai_Matakuliah_Component:

    pass


class Nilai:

    def __init__(self, uts: int, uas: int, tugas: int, namaMK: str, mahasiswa1: "Mahasiswa" = None, nilai24: "DAO_Nilai" = None):
        self.uts = uts
        self.uas = uas
        self.tugas = tugas
        self.namaMK = namaMK
        self.mahasiswa1 = mahasiswa1
        self.nilai24 = nilai24
        
        pass
    @property
    def namaMK(self):
        return self.__namaMK
    @namaMK.setter
    def namaMK(self, namaMK: str):
        self.__namaMK = namaMK

    @property
    def uts(self):
        return self.__uts
    @uts.setter
    def uts(self, uts: int):
        self.__uts = uts

    @property
    def tugas(self):
        return self.__tugas
    @tugas.setter
    def tugas(self, tugas: int):
        self.__tugas = tugas

    @property
    def uas(self):
        return self.__uas
    @uas.setter
    def uas(self, uas: int):
        self.__uas = uas

    @property
    def nilai24(self):
        return self.__nilai24
    @nilai24.setter
    def nilai24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nilai__nilai24", None)
        self.__nilai24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nilai25"):
                opp_val = getattr(old_value, "nilai25", None)
                if opp_val == self:
                    setattr(old_value, "nilai25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nilai25"):
                opp_val = getattr(value, "nilai25", None)
                setattr(value, "nilai25", self)

    @property
    def mahasiswa1(self):
        return self.__mahasiswa1
    @mahasiswa1.setter
    def mahasiswa1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nilai__mahasiswa1", None)
        self.__mahasiswa1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nilai0"):
                opp_val = getattr(old_value, "nilai0", None)
                if opp_val == self:
                    setattr(old_value, "nilai0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nilai0"):
                opp_val = getattr(value, "nilai0", None)
                setattr(value, "nilai0", self)



class Mahasiswa:

    def __init__(self, nim: str, nama: str, tahun: str, nilai0: "Nilai" = None, mahasiswa22: "DAO_Mahasiswa" = None):
        self.nim = nim
        self.nama = nama
        self.tahun = tahun
        self.nilai0 = nilai0
        self.mahasiswa22 = mahasiswa22
        
        pass
    @property
    def nim(self):
        return self.__nim
    @nim.setter
    def nim(self, nim: str):
        self.__nim = nim

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def tahun(self):
        return self.__tahun
    @tahun.setter
    def tahun(self, tahun: str):
        self.__tahun = tahun

    @property
    def nilai0(self):
        return self.__nilai0
    @nilai0.setter
    def nilai0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mahasiswa__nilai0", None)
        self.__nilai0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mahasiswa1"):
                opp_val = getattr(old_value, "mahasiswa1", None)
                if opp_val == self:
                    setattr(old_value, "mahasiswa1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mahasiswa1"):
                opp_val = getattr(value, "mahasiswa1", None)
                setattr(value, "mahasiswa1", self)

    @property
    def mahasiswa22(self):
        return self.__mahasiswa22
    @mahasiswa22.setter
    def mahasiswa22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mahasiswa__mahasiswa22", None)
        self.__mahasiswa22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mahasiswa23"):
                opp_val = getattr(old_value, "mahasiswa23", None)
                if opp_val == self:
                    setattr(old_value, "mahasiswa23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mahasiswa23"):
                opp_val = getattr(value, "mahasiswa23", None)
                setattr(value, "mahasiswa23", self)


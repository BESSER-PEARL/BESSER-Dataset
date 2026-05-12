





import java.util.List;
import java.util.ArrayList;

public class Tata_Usaha_Actor  {






    private Sistem_Pembayaran_Jurusan_UseCase sistem_pembayaran_jurusan_usecase;




    private Sistem_Pembayaran_Prodi_UseCase sistem_pembayaran_prodi_usecase;




    private Sistem_Pembayaran_Pembayaran_UseCase sistem_pembayaran_pembayaran_usecase;




    private Sistem_Pembayaran_Kategori_Biaya_UseCase sistem_pembayaran_kategori_biaya_usecase;




    private Sistem_Pembayaran_Biaya_Kuliah_UseCase sistem_pembayaran_biaya_kuliah_usecase;




    private Sistem_Pembayaran_Login_UseCase sistem_pembayaran_login_usecase;


    public Tata_Usaha_Actor(
    ) {
    }



    public Sistem_Pembayaran_Jurusan_UseCase getSistem_pembayaran_jurusan_usecase() {
        return sistem_pembayaran_jurusan_usecase;
    }

    public void setSistem_pembayaran_jurusan_usecase(Sistem_Pembayaran_Jurusan_UseCase sistem_pembayaran_jurusan_usecase) {
        this.sistem_pembayaran_jurusan_usecase = sistem_pembayaran_jurusan_usecase;
    }
    public Sistem_Pembayaran_Prodi_UseCase getSistem_pembayaran_prodi_usecase() {
        return sistem_pembayaran_prodi_usecase;
    }

    public void setSistem_pembayaran_prodi_usecase(Sistem_Pembayaran_Prodi_UseCase sistem_pembayaran_prodi_usecase) {
        this.sistem_pembayaran_prodi_usecase = sistem_pembayaran_prodi_usecase;
    }
    public Sistem_Pembayaran_Pembayaran_UseCase getSistem_pembayaran_pembayaran_usecase() {
        return sistem_pembayaran_pembayaran_usecase;
    }

    public void setSistem_pembayaran_pembayaran_usecase(Sistem_Pembayaran_Pembayaran_UseCase sistem_pembayaran_pembayaran_usecase) {
        this.sistem_pembayaran_pembayaran_usecase = sistem_pembayaran_pembayaran_usecase;
    }
    public Sistem_Pembayaran_Kategori_Biaya_UseCase getSistem_pembayaran_kategori_biaya_usecase() {
        return sistem_pembayaran_kategori_biaya_usecase;
    }

    public void setSistem_pembayaran_kategori_biaya_usecase(Sistem_Pembayaran_Kategori_Biaya_UseCase sistem_pembayaran_kategori_biaya_usecase) {
        this.sistem_pembayaran_kategori_biaya_usecase = sistem_pembayaran_kategori_biaya_usecase;
    }
    public Sistem_Pembayaran_Biaya_Kuliah_UseCase getSistem_pembayaran_biaya_kuliah_usecase() {
        return sistem_pembayaran_biaya_kuliah_usecase;
    }

    public void setSistem_pembayaran_biaya_kuliah_usecase(Sistem_Pembayaran_Biaya_Kuliah_UseCase sistem_pembayaran_biaya_kuliah_usecase) {
        this.sistem_pembayaran_biaya_kuliah_usecase = sistem_pembayaran_biaya_kuliah_usecase;
    }
    public Sistem_Pembayaran_Login_UseCase getSistem_pembayaran_login_usecase() {
        return sistem_pembayaran_login_usecase;
    }

    public void setSistem_pembayaran_login_usecase(Sistem_Pembayaran_Login_UseCase sistem_pembayaran_login_usecase) {
        this.sistem_pembayaran_login_usecase = sistem_pembayaran_login_usecase;
    }

}
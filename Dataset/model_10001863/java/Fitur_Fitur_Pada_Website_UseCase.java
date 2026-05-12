





import java.util.List;
import java.util.ArrayList;

public class Fitur_Fitur_Pada_Website_UseCase  {






    private Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase fitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase;




    private Halaman_Utama_Website_UseCase halaman_utama_website_usecase;




    private Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase fitur_website_yang_dapat_diakses_oleh_pengunjung_usecase;


    public Fitur_Fitur_Pada_Website_UseCase(
    ) {
    }



    public Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase getFitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase() {
        return fitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase;
    }

    public void setFitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase(Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase fitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase) {
        this.fitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase = fitur_website_yang_dapat_diakses_dan_edit_oleh_admin_usecase;
    }
    public Halaman_Utama_Website_UseCase getHalaman_utama_website_usecase() {
        return halaman_utama_website_usecase;
    }

    public void setHalaman_utama_website_usecase(Halaman_Utama_Website_UseCase halaman_utama_website_usecase) {
        this.halaman_utama_website_usecase = halaman_utama_website_usecase;
    }
    public Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase getFitur_website_yang_dapat_diakses_oleh_pengunjung_usecase() {
        return fitur_website_yang_dapat_diakses_oleh_pengunjung_usecase;
    }

    public void setFitur_website_yang_dapat_diakses_oleh_pengunjung_usecase(Fitur_Website_Yang_Dapat_Diakses_Oleh_Pengunjung_UseCase fitur_website_yang_dapat_diakses_oleh_pengunjung_usecase) {
        this.fitur_website_yang_dapat_diakses_oleh_pengunjung_usecase = fitur_website_yang_dapat_diakses_oleh_pengunjung_usecase;
    }

}
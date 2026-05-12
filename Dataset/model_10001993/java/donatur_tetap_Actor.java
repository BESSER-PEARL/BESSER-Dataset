





import java.util.List;
import java.util.ArrayList;

public class donatur_tetap_Actor  {






    private edit_profil_donatur_UseCase edit_profil_donatur_usecase;




    private meilhat_riwayat_donasi_UseCase meilhat_riwayat_donasi_usecase;


    public donatur_tetap_Actor(
    ) {
    }



    public edit_profil_donatur_UseCase getEdit_profil_donatur_usecase() {
        return edit_profil_donatur_usecase;
    }

    public void setEdit_profil_donatur_usecase(edit_profil_donatur_UseCase edit_profil_donatur_usecase) {
        this.edit_profil_donatur_usecase = edit_profil_donatur_usecase;
    }
    public meilhat_riwayat_donasi_UseCase getMeilhat_riwayat_donasi_usecase() {
        return meilhat_riwayat_donasi_usecase;
    }

    public void setMeilhat_riwayat_donasi_usecase(meilhat_riwayat_donasi_UseCase meilhat_riwayat_donasi_usecase) {
        this.meilhat_riwayat_donasi_usecase = meilhat_riwayat_donasi_usecase;
    }

}
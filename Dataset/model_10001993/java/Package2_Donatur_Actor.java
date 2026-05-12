





import java.util.List;
import java.util.ArrayList;

public class Package2_Donatur_Actor  {






    private Package2_mengubah_profil_UseCase package2_mengubah_profil_usecase;




    private Package2_melihat_riwayat_donasi_UseCase package2_melihat_riwayat_donasi_usecase;


    public Package2_Donatur_Actor(
    ) {
    }



    public Package2_mengubah_profil_UseCase getPackage2_mengubah_profil_usecase() {
        return package2_mengubah_profil_usecase;
    }

    public void setPackage2_mengubah_profil_usecase(Package2_mengubah_profil_UseCase package2_mengubah_profil_usecase) {
        this.package2_mengubah_profil_usecase = package2_mengubah_profil_usecase;
    }
    public Package2_melihat_riwayat_donasi_UseCase getPackage2_melihat_riwayat_donasi_usecase() {
        return package2_melihat_riwayat_donasi_usecase;
    }

    public void setPackage2_melihat_riwayat_donasi_usecase(Package2_melihat_riwayat_donasi_UseCase package2_melihat_riwayat_donasi_usecase) {
        this.package2_melihat_riwayat_donasi_usecase = package2_melihat_riwayat_donasi_usecase;
    }

}
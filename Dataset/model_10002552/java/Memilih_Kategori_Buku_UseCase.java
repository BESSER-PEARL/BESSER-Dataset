





import java.util.List;
import java.util.ArrayList;

public class Memilih_Kategori_Buku_UseCase  {






    private User_Actor user_actor;




    private Melihat_Tampilan_Awal_Aplikasi_UseCase melihat_tampilan_awal_aplikasi_usecase;


    public Memilih_Kategori_Buku_UseCase(
    ) {
    }



    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }
    public Melihat_Tampilan_Awal_Aplikasi_UseCase getMelihat_tampilan_awal_aplikasi_usecase() {
        return melihat_tampilan_awal_aplikasi_usecase;
    }

    public void setMelihat_tampilan_awal_aplikasi_usecase(Melihat_Tampilan_Awal_Aplikasi_UseCase melihat_tampilan_awal_aplikasi_usecase) {
        this.melihat_tampilan_awal_aplikasi_usecase = melihat_tampilan_awal_aplikasi_usecase;
    }

}
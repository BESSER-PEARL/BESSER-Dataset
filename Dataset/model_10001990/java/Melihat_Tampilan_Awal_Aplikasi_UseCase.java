





import java.util.List;
import java.util.ArrayList;

public class Melihat_Tampilan_Awal_Aplikasi_UseCase  {






    private User_Actor user_actor;




    private Masuk_dari_Aplikasi_UseCase masuk_dari_aplikasi_usecase;


    public Melihat_Tampilan_Awal_Aplikasi_UseCase(
    ) {
    }



    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }
    public Masuk_dari_Aplikasi_UseCase getMasuk_dari_aplikasi_usecase() {
        return masuk_dari_aplikasi_usecase;
    }

    public void setMasuk_dari_aplikasi_usecase(Masuk_dari_Aplikasi_UseCase masuk_dari_aplikasi_usecase) {
        this.masuk_dari_aplikasi_usecase = masuk_dari_aplikasi_usecase;
    }

}
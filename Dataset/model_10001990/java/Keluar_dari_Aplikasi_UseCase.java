





import java.util.List;
import java.util.ArrayList;

public class Keluar_dari_Aplikasi_UseCase  {






    private Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase;




    private User_Actor user_actor;


    public Keluar_dari_Aplikasi_UseCase(
    ) {
    }



    public Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase getOtomatis_menginterupsi_notifikasi_akun_media_sosial_usecase() {
        return otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase;
    }

    public void setOtomatis_menginterupsi_notifikasi_akun_media_sosial_usecase(Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase) {
        this.otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase = otomatis_menginterupsi_notifikasi_akun_media_sosial_usecase;
    }
    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }

}
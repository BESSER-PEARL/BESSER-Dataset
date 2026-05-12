





import java.util.List;
import java.util.ArrayList;

public class Melihat_Tampilan_Awal_Aplikasi_UseCase  {






    private Melakukan_Login_UseCase melakukan_login_usecase;




    private User_Actor user_actor;


    public Melihat_Tampilan_Awal_Aplikasi_UseCase(
    ) {
    }



    public Melakukan_Login_UseCase getMelakukan_login_usecase() {
        return melakukan_login_usecase;
    }

    public void setMelakukan_login_usecase(Melakukan_Login_UseCase melakukan_login_usecase) {
        this.melakukan_login_usecase = melakukan_login_usecase;
    }
    public User_Actor getUser_actor() {
        return user_actor;
    }

    public void setUser_actor(User_Actor user_actor) {
        this.user_actor = user_actor;
    }

}
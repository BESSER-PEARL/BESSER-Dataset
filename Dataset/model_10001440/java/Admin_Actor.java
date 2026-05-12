





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Melakukan_Login_UseCase melakukan_login_usecase;




    private Melakukan_Registrasi_UseCase melakukan_registrasi_usecase;


    public Admin_Actor(
    ) {
    }



    public Melakukan_Login_UseCase getMelakukan_login_usecase() {
        return melakukan_login_usecase;
    }

    public void setMelakukan_login_usecase(Melakukan_Login_UseCase melakukan_login_usecase) {
        this.melakukan_login_usecase = melakukan_login_usecase;
    }
    public Melakukan_Registrasi_UseCase getMelakukan_registrasi_usecase() {
        return melakukan_registrasi_usecase;
    }

    public void setMelakukan_registrasi_usecase(Melakukan_Registrasi_UseCase melakukan_registrasi_usecase) {
        this.melakukan_registrasi_usecase = melakukan_registrasi_usecase;
    }

}
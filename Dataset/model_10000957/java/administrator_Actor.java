





import java.util.List;
import java.util.ArrayList;

public class administrator_Actor  {






    private login_UseCase login_usecase;




    private logout_UseCase logout_usecase;


    public administrator_Actor(
    ) {
    }



    public login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }
    public logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }

}
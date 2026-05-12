





import java.util.List;
import java.util.ArrayList;

public class HAL_Connexion  {

    private String password;
    private String login;



    public HAL_Connexion(
        String password,        String login    ) {
        this.password = password;
        this.login = login;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }


}
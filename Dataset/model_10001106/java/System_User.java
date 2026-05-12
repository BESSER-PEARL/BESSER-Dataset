





import java.util.List;
import java.util.ArrayList;

public class System_User  {

    private String password;
    private String login;



    public System_User(
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
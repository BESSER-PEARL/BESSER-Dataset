





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private None state;
    private String password;



    public WebUser(
        String login,        None state,        String password    ) {
        this.login = login;
        this.state = state;
        this.password = password;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
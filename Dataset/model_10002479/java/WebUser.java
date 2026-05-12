





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private String state;
    private String password;



    public WebUser(
        String login,        String state,        String password    ) {
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
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
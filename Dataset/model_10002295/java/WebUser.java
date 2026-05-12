





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private String password;
    private String state;



    public WebUser(
        String login,        String password,        String state    ) {
        this.login = login;
        this.password = password;
        this.state = state;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}
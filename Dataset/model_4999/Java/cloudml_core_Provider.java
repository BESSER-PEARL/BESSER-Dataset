





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Provider extends WithProperties {

    private String password;
    private String login;



    public cloudml_core_Provider(
        String password,        String login    ) {
        super(
        );
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






import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Provider extends CloudMLElementWithProperties {

    private String credentials;
    private String login;
    private String password;



    public cloudml_core_Provider(
        String credentials,        String login,        String password    ) {
        super(
        );
        this.credentials = credentials;
        this.login = login;
        this.password = password;
    }


    public String getCredentials() {
        return credentials;
    }

    public void setCredentials(String credentials) {
        this.credentials = credentials;
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


}
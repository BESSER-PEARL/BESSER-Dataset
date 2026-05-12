





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private None state;
    private String password;





    private client client;




    private Cosul_de_cumparaturi cosul_de_cumparaturi;


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

    public client getClient() {
        return client;
    }

    public void setClient(client client) {
        this.client = client;
    }
    public Cosul_de_cumparaturi getCosul_de_cumparaturi() {
        return cosul_de_cumparaturi;
    }

    public void setCosul_de_cumparaturi(Cosul_de_cumparaturi cosul_de_cumparaturi) {
        this.cosul_de_cumparaturi = cosul_de_cumparaturi;
    }

}
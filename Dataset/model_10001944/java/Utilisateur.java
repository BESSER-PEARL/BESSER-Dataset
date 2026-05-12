





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private String login;
    private String mdp;



    public Utilisateur(
        String login,        String mdp    ) {
        this.login = login;
        this.mdp = mdp;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getMdp() {
        return mdp;
    }

    public void setMdp(String mdp) {
        this.mdp = mdp;
    }


}
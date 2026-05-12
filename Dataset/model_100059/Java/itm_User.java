





import java.util.List;
import java.util.ArrayList;

public class itm_User  {

    private String language;
    private String login;



    public itm_User(
        String language,        String login    ) {
        this.language = language;
        this.login = login;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }


}
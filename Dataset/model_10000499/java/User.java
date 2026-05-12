





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String attribute;





    private Login login;


    public User(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}
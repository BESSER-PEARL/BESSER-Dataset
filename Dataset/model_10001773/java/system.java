





import java.util.List;
import java.util.ArrayList;

public class system  {

    private boolean status;





    private Login login;


    public system(
        boolean status    ) {
        this.status = status;
    }


    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}
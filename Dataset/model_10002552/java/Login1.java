





import java.util.List;
import java.util.ArrayList;

public class Login1  {

    private String password;
    private String usernam;



    public Login1(
        String password,        String usernam    ) {
        this.password = password;
        this.usernam = usernam;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsernam() {
        return usernam;
    }

    public void setUsernam(String usernam) {
        this.usernam = usernam;
    }


}
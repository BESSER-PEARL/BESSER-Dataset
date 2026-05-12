





import java.util.List;
import java.util.ArrayList;

public class Login1  {

    private String Password;
    private String Username;



    public Login1(
        String Password,        String Username    ) {
        this.Password = Password;
        this.Username = Username;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }


}
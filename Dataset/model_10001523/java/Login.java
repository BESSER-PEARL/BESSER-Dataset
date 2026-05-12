





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Username;
    private String Password;



    public Login(
        String Username,        String Password    ) {
        this.Username = Username;
        this.Password = Password;
    }


    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}
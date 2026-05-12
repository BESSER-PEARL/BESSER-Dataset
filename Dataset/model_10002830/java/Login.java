





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String UserName;
    private String Password;



    public Login(
        String UserName,        String Password    ) {
        this.UserName = UserName;
        this.Password = Password;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}
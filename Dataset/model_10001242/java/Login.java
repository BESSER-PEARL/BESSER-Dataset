





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Password1;
    private String UserName;
    private String Password;



    public Login(
        String Password1,        String UserName,        String Password    ) {
        this.Password1 = Password1;
        this.UserName = UserName;
        this.Password = Password;
    }


    public String getPassword1() {
        return Password1;
    }

    public void setPassword1(String Password1) {
        this.Password1 = Password1;
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
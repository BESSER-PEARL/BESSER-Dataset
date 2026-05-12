





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String Password;
    private String UserName;



    public Users(
        String Password,        String UserName    ) {
        this.Password = Password;
        this.UserName = UserName;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}
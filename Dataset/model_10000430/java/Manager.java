





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String password;
    private String UserName;



    public Manager(
        String password,        String UserName    ) {
        this.password = password;
        this.UserName = UserName;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}
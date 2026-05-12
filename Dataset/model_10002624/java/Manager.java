





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String UserName;
    private String password;



    public Manager(
        String UserName,        String password    ) {
        this.UserName = UserName;
        this.password = password;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
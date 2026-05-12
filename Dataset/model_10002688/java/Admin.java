





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String attribute;
    private String UserName;
    private String Password;



    public Admin(
        String attribute,        String UserName,        String Password    ) {
        this.attribute = attribute;
        this.UserName = UserName;
        this.Password = Password;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
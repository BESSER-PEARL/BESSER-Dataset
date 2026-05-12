





import java.util.List;
import java.util.ArrayList;

public class Login_Admin  {

    private String attribute;
    private String User_name;



    public Login_Admin(
        String attribute,        String User_name    ) {
        this.attribute = attribute;
        this.User_name = User_name;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getUser_name() {
        return User_name;
    }

    public void setUser_name(String User_name) {
        this.User_name = User_name;
    }


}
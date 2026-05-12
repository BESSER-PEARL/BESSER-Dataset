





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String user_Name;
    private String Name;
    private String password;



    public Profile(
        String user_Name,        String Name,        String password    ) {
        this.user_Name = user_Name;
        this.Name = Name;
        this.password = password;
    }


    public String getUser_name() {
        return user_Name;
    }

    public void setUser_name(String user_Name) {
        this.user_Name = user_Name;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
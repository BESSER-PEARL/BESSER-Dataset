





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String User_Type;
    private String User_Name;
    private int User_ID;
    private String User_Password;



    public User(
        String User_Type,        String User_Name,        int User_ID,        String User_Password    ) {
        this.User_Type = User_Type;
        this.User_Name = User_Name;
        this.User_ID = User_ID;
        this.User_Password = User_Password;
    }


    public String getUser_type() {
        return User_Type;
    }

    public void setUser_type(String User_Type) {
        this.User_Type = User_Type;
    }
    public String getUser_name() {
        return User_Name;
    }

    public void setUser_name(String User_Name) {
        this.User_Name = User_Name;
    }
    public int getUser_id() {
        return User_ID;
    }

    public void setUser_id(int User_ID) {
        this.User_ID = User_ID;
    }
    public String getUser_password() {
        return User_Password;
    }

    public void setUser_password(String User_Password) {
        this.User_Password = User_Password;
    }


}
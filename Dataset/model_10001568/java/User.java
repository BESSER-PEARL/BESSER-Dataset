





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String UserName;
    private String Password;
    private int UserID;



    public User(
        String UserName,        String Password,        int UserID    ) {
        this.UserName = UserName;
        this.Password = Password;
        this.UserID = UserID;
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
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }


}
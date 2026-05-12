





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String UserID;
    private String Password;



    public User(
        String UserID,        String Password    ) {
        this.UserID = UserID;
        this.Password = Password;
    }


    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}






import java.util.List;
import java.util.ArrayList;

public class SuperAdmin  {

    private int userID;
    private String password;
    private String userName;



    public SuperAdmin(
        int userID,        String password,        String userName    ) {
        this.userID = userID;
        this.password = password;
        this.userName = userName;
    }


    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }


}
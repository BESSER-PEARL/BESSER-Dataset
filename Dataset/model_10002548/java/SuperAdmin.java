





import java.util.List;
import java.util.ArrayList;

public class SuperAdmin  {

    private String password;
    private int userID;
    private String userName;



    public SuperAdmin(
        String password,        int userID,        String userName    ) {
        this.password = password;
        this.userID = userID;
        this.userName = userName;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }


}
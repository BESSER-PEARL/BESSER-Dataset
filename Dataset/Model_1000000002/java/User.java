





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int userId;
    private String userName;
    private String emailId;



    public User(
        int userId,        String userName,        String emailId    ) {
        this.userId = userId;
        this.userName = userName;
        this.emailId = emailId;
    }


    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getEmailid() {
        return emailId;
    }

    public void setEmailid(String emailId) {
        this.emailId = emailId;
    }


}
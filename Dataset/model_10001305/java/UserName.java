





import java.util.List;
import java.util.ArrayList;

public class UserName  {

    private String FirstName;
    private String LastName;





    private User_Account user_account;


    public UserName(
        String FirstName,        String LastName    ) {
        this.FirstName = FirstName;
        this.LastName = LastName;
    }


    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }

    public User_Account getUser_account() {
        return user_account;
    }

    public void setUser_account(User_Account user_account) {
        this.user_account = user_account;
    }

}
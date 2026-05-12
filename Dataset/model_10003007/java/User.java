





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Password;
    private int UserId;



    public User(
        String Password,        int UserId    ) {
        this.Password = Password;
        this.UserId = UserId;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }


}
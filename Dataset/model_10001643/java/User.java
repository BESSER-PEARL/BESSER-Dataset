





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int Password;
    private int User_Id;
    private String Login_Status;



    public User(
        int Password,        int User_Id,        String Login_Status    ) {
        this.Password = Password;
        this.User_Id = User_Id;
        this.Login_Status = Login_Status;
    }


    public int getPassword() {
        return Password;
    }

    public void setPassword(int Password) {
        this.Password = Password;
    }
    public int getUser_id() {
        return User_Id;
    }

    public void setUser_id(int User_Id) {
        this.User_Id = User_Id;
    }
    public String getLogin_status() {
        return Login_Status;
    }

    public void setLogin_status(String Login_Status) {
        this.Login_Status = Login_Status;
    }


}
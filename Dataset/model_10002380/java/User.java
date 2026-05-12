





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int User_Id;
    private int Password;
    private String Login_Status;



    public User(
        int User_Id,        int Password,        String Login_Status    ) {
        this.User_Id = User_Id;
        this.Password = Password;
        this.Login_Status = Login_Status;
    }


    public int getUser_id() {
        return User_Id;
    }

    public void setUser_id(int User_Id) {
        this.User_Id = User_Id;
    }
    public int getPassword() {
        return Password;
    }

    public void setPassword(int Password) {
        this.Password = Password;
    }
    public String getLogin_status() {
        return Login_Status;
    }

    public void setLogin_status(String Login_Status) {
        this.Login_Status = Login_Status;
    }


}
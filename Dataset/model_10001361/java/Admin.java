





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String User_name;
    private int Password;
    private int ID;



    public Admin(
        String User_name,        int Password,        int ID    ) {
        this.User_name = User_name;
        this.Password = Password;
        this.ID = ID;
    }


    public String getUser_name() {
        return User_name;
    }

    public void setUser_name(String User_name) {
        this.User_name = User_name;
    }
    public int getPassword() {
        return Password;
    }

    public void setPassword(int Password) {
        this.Password = Password;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}
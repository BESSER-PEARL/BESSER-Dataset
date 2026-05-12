





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Passowrd;
    private String User_Name;



    public User(
        String Passowrd,        String User_Name    ) {
        this.Passowrd = Passowrd;
        this.User_Name = User_Name;
    }


    public String getPassowrd() {
        return Passowrd;
    }

    public void setPassowrd(String Passowrd) {
        this.Passowrd = Passowrd;
    }
    public String getUser_name() {
        return User_Name;
    }

    public void setUser_name(String User_Name) {
        this.User_Name = User_Name;
    }


}
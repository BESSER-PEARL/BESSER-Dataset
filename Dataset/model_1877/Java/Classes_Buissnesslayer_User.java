





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_User  {

    private String Name;
    private String Email;





    private UserHandler userhandler;


    public Classes_Buissnesslayer_User(
        String Name,        String Email    ) {
        this.Name = Name;
        this.Email = Email;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public UserHandler getUserhandler() {
        return userhandler;
    }

    public void setUserhandler(UserHandler userhandler) {
        this.userhandler = userhandler;
    }

}
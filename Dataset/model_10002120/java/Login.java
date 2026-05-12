





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Name;
    private String Password;





    private User user;


    public Login(
        String Name,        String Password    ) {
        this.Name = Name;
        this.Password = Password;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}
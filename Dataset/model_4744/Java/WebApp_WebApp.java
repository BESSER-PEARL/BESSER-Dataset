





import java.util.List;
import java.util.ArrayList;

public class WebApp_WebApp  {

    private String Password;
    private String User;
    private String name;



    public WebApp_WebApp(
        String Password,        String User,        String name    ) {
        this.Password = Password;
        this.User = User;
        this.name = name;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUser() {
        return User;
    }

    public void setUser(String User) {
        this.User = User;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
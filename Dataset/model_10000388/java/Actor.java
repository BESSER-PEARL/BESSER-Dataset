





import java.util.List;
import java.util.ArrayList;

public class Actor  {

    private String username;
    private String name;
    private String password;



    public Actor(
        String username,        String name,        String password    ) {
        this.username = username;
        this.name = name;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
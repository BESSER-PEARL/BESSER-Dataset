





import java.util.List;
import java.util.ArrayList;

public class User_abstract_  {

    private String name;
    private String email;
    private String password;
    private String userId;



    public User_abstract_(
        String name,        String email,        String password,        String userId    ) {
        this.name = name;
        this.email = email;
        this.password = password;
        this.userId = userId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }


}
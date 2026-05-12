





import java.util.List;
import java.util.ArrayList;

public class person  {

    private String name;
    private String phone;
    private String password;
    private String username;



    public person(
        String name,        String phone,        String password,        String username    ) {
        this.name = name;
        this.phone = phone;
        this.password = password;
        this.username = username;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}
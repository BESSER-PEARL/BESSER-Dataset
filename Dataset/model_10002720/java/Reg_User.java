





import java.util.List;
import java.util.ArrayList;

public class Reg_User  {

    private String username;
    private String Address;
    private String password;



    public Reg_User(
        String username,        String Address,        String password    ) {
        this.username = username;
        this.Address = Address;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
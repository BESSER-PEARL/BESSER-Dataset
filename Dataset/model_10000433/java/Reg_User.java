





import java.util.List;
import java.util.ArrayList;

public class Reg_User  {

    private String Address;
    private String username;
    private String password;



    public Reg_User(
        String Address,        String username,        String password    ) {
        this.Address = Address;
        this.username = username;
        this.password = password;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
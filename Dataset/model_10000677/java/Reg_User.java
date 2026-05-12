





import java.util.List;
import java.util.ArrayList;

public class Reg_User  {

    private String Address;
    private String password;
    private String username;



    public Reg_User(
        String Address,        String password,        String username    ) {
        this.Address = Address;
        this.password = password;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}
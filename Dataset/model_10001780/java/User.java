





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int phoneno;
    private String address;
    private String gender;
    private String password;
    private String username;



    public User(
        int phoneno,        String address,        String gender,        String password,        String username    ) {
        this.phoneno = phoneno;
        this.address = address;
        this.gender = gender;
        this.password = password;
        this.username = username;
    }


    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
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
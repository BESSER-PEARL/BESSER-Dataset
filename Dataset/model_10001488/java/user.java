





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String password;
    private String name;
    private int phone_number;
    private String email;
    private String address;



    public user(
        String password,        String name,        int phone_number,        String email,        String address    ) {
        this.password = password;
        this.name = name;
        this.phone_number = phone_number;
        this.email = email;
        this.address = address;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(int phone_number) {
        this.phone_number = phone_number;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}
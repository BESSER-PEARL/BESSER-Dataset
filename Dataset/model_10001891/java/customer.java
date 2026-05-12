





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private int password;
    private None address;
    private None name;
    private int phone;
    private None email;



    public customer(
        int password,        None address,        None name,        int phone,        None email    ) {
        this.password = password;
        this.address = address;
        this.name = name;
        this.phone = phone;
        this.email = email;
    }


    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public None getEmail() {
        return email;
    }

    public void setEmail(None email) {
        this.email = email;
    }


}
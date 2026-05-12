





import java.util.List;
import java.util.ArrayList;

public class Empleado  {

    private String phone;
    private String email;
    private String address;



    public Empleado(
        String phone,        String email,        String address    ) {
        this.phone = phone;
        this.email = email;
        this.address = address;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
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